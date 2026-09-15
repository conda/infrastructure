# How We Use PyPI

The [conda organization on PyPI](https://pypi.org/org/conda/) holds Python
distributions maintained by projects in the conda Organization. It is separate
from conda package channels.

## Responsibilities

The [infrastructure team](https://github.com/conda/governance/blob/main/teams/infrastructure.yml)
administers organization-level access, teams, and projects. The
governance-backed [Project Team](https://github.com/conda/governance#project-teams)
responsible for a project controls its distributions. If no responsible team
is recorded, identify the existing project owners and establish responsibility
before granting new access.

## Access

Access follows conda governance membership:

- Infrastructure administrators hold the PyPI organization Owner or Manager
  roles needed to administer the organization.
- Members of the responsible governance team join the PyPI organization as
  Members and are added to the corresponding PyPI team.
- PyPI teams receive the Owner role for their projects by default. Use the
  Maintainer role only when upload-only access is deliberately sufficient.
- Do not grant direct project access to individuals when a corresponding team
  exists. Reserve direct access for documented migration or recovery work.

PyPI organization access does not grant conda Project Team membership. If a
person is not already a member of the responsible Project Team, establish that
membership through the governance process first.

Organization membership alone does not grant access to every project.

[PyPI requires two-factor authentication](https://pypi.org/help/#twofa) for all
users. Users should configure more than one authentication method and store
recovery codes securely.

See PyPI's documentation for the current definitions and procedures:

- [Organization roles](https://docs.pypi.org/organization-accounts/roles-entities/)
- [Organization actions](https://docs.pypi.org/organization-accounts/actions/org-actions/)
- [Team actions](https://docs.pypi.org/organization-accounts/actions/team-actions/)
- [Project actions](https://docs.pypi.org/organization-accounts/actions/project-actions/)

## Publishing

Use [Trusted Publishing](https://docs.pypi.org/trusted-publishers/) for automated
releases whenever the release platform supports it. Do not share user API
tokens. If Trusted Publishing cannot be used, limit the token to the project
and document the exception with the responsible governance team.

Review PyPI's [Trusted Publishing security model](https://docs.pypi.org/trusted-publishers/security-model/)
before changing a repository, workflow filename, environment, or release
permission.

Project-specific build and release instructions belong in the project's own
release documentation.

## Request a change

[Open a PyPI organization request](https://github.com/conda/infrastructure/issues/new?template=5_pypi.yml)
when infrastructure team action is needed for any of the following:

- adding or transferring a project
- adding or removing an organization or team member
- creating or changing a team
- changing a team's project role
- adding, changing, or removing a Trusted Publisher

Requests must identify the responsible governance team. If none is recorded,
identify the existing project owners and request assignment of responsibility.
Include team approval or a governance record when requesting a project transfer,
new membership, or additional access. Project transfers must also include
consent from an existing project owner.

Never include passwords, API tokens, recovery codes, or other credentials in a
GitHub issue.

## Offboarding

When a person leaves a Project Team, remove them from the corresponding PyPI
team. Remove them from the PyPI organization if they no longer need access for
another Project Team. Remove their direct project roles and review all Trusted
Publishers for the affected projects. When a project moves or becomes inactive,
review its team permissions, direct collaborators, API tokens, and Trusted
Publishers.

Retiring a project does not authorize deleting it or its releases. Record its
successor team or obtain an explicit governance decision.
