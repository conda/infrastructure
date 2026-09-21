#!/usr/bin/env python3
"""Remove conda-canary packages that were uploaded more than N days ago."""

from __future__ import annotations

import logging
import sys
from argparse import ArgumentParser
from datetime import datetime, timedelta, timezone
from typing import TYPE_CHECKING

from binstar_client import errors
from binstar_client.utils import get_server_api

if TYPE_CHECKING:
    from typing import Sequence


ORG = "conda-canary"
DAYS = 30

logger = logging.getLogger("clean_conda_canary")


def main(argv: Sequence[str] | None = None) -> int:
    """Remove conda-canary packages that were uploaded more than N days ago."""
    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="report what would be removed without removing anything",
    )
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.INFO, format="%(message)s")

    cutoff = datetime.now(timezone.utc) - timedelta(days=DAYS)
    logger.info("Cleaning up %s: removing packages uploaded before %s", ORG, cutoff)

    api = get_server_api()

    failures = 0
    removed_releases = 0

    for package in api.user_packages(ORG):
        package_name = package["name"]
        for version in package["versions"]:
            try:
                release = api.release(ORG, package_name, version)
            except errors.NotFound:
                continue

            distributions = release["distributions"]
            # Only remove a release when every distribution in it is stale.
            # A mixed release (some old, some new) is left alone entirely;
            # a release is only ever removed all at once.
            if not distributions or any(
                # Parse an anaconda.org `upload_time` string into an aware datetime.
                # e.g. "2026-09-21 16:58:05.639000+00:00"
                datetime.fromisoformat(dist["upload_time"]) >= cutoff
                for dist in distributions
            ):
                continue

            spec = f"{ORG}/{package_name}/{version}"
            if args.dry_run:
                logger.info("Would remove release %s", spec)
                removed_releases += 1
                continue

            logger.info("Removing release %s", spec)
            try:
                api.remove_release(ORG, package_name, version)
            except errors.BinstarError:
                logger.exception("Failed to remove release %s", spec)
                failures += 1
            else:
                removed_releases += 1

    logger.info(
        "%s %d release(s)",
        "Would remove" if args.dry_run else "Removed",
        removed_releases,
    )

    if failures:
        logger.error("%d removal(s) failed", failures)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
