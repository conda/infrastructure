## 👋 Welcome!

Welcome to the conda infrastructure repo!

### Content

This repo contains a number of things, both to automate and simplify the management of the conda GitHub org as well as to create a place for community members to communicate in an asynchronous manner.

### Discussions

We’re using [GitHub discussions in this repo](https://github.com/conda/infra/discussions) as a place to provide a place for [Conda core members and maintainers](https://github.com/conda-incubator/governance#teams--roles) to raise issues about the Conda community infrastructure such as:
  * Package hosting (e.g. conda-forge channel on anaconda.org)
  * GitHub organization admin questions and issues
  * Test suite and development setup issues
  * Anything that does not fall into any other project specific buckets (e.g. the [conda issues](https://github.com/conda/conda/issues) or [conda-build issues](https://github.com/conda/conda-build/issues))
  * etc.

**NOTE: This is not a forum for end user questions!**

Feel also free to:
  * Share ideas about new features and changes you'd like to see
  * Engage with other community members

Please start by creating a discussion first before you open an issue directly.

Welcome others and be open-minded. Remember that this is a community we build together 💪.

### Team management

This repo contains a Terraform based provisioning setup that allows adding, updating and removing of members and teams of the conda GitHub organization.

Changes to the files (and in effect application of the changes) are required to pass peer-review by at least two admins of the GitHub organization.

Here are the default files maintained in the ``admin`` directory:

- ``members.csv`` - comma-separated list of members

- ``teams.csv`` - comma-separated list of teams

- ``team-members/*.csv`` - comma-separated lists of team memberships, named with the slug of the team name

- ``repos-team/*.csv`` - comma-separated lists of repo<->team permissions, named with the repo name
