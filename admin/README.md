# Conda GitHub Org Terraform Configuration

> ⚠ **Nothing is currently deployed from here**: Settings are only imported to make them transparent

This is composed by the many `.tf` files in this folder together with:
* an import workflow [tf-import.yml](../.github/workflows/tf-import.yml), that imports resources and creates update PRs (to reconcile with changes done outside terraform).
* a deploy workflow [tf-deploy.yml](../.github/workflows/tf-deploy.yml): TBD
* a [Makefile](Makefile) containing various tasks with or around the code for local usage and also used by the workflows, see `make help`.
