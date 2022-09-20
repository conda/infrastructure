## Writing a Spike at `conda`

### Summary

In this document, we go over the procedure to follow when performing research for a
particular project, also known as a "spike". The steps outlined here should be used
for all projects falling underneath the [conda](github.com/conda) organization.

### What is a Spike?

A spike is a term that is borrowed from extreme programming and agile development. At conda,
we use spikes to analyze a bug report more thoroughly or while planning our future epics.
These spike issues help us determine exactly what needs to be done to implement the bug fix or
epic and many times result in the creation of one or more issues to carry out this work.
Below, we will cover some common scenarios for how spikes are created.

### When do I create a spike?

#### For bug reports

In the case of bug reports, these issues may only contain the symptoms of a greater problem. Therefore,
it is important for us to first investigate the actual root cause of the issue in case it is
already related to other known issues. Much of this is already done during [issue sorting](./ISSUE_SORTING.md),
but if it is determined that this bug is either not related to other existing issues or if the
optimal solution is not yet known, we would convert the incoming bug report to a spike issue.

#### As a part of epic planning

Another common way that we create spikes is during the planning and discovery phase of an epic.
Epics represent larger chunks of work that need to be spread out over multiple issues. Spikes are
often needed to figure out the exact details for how a particular feature is to be implemented
because this may not be known when we first begin work on the epic.

### How do I create a spike?

#### When converting an existing issue

- Preface the issue title with, "SPIKE 🔍" (or add a label???)
- Ensure there is enough background information on the issue for a would-be assignee
- Ensure that the issue has clear deliverables. These should state exactly what needs to be done.
  For example, if we expect to create another issue as result of this spike, that should be stated.

#### When planning an epic

- Preface the issue title with, "SPIKE 🔍" (or add a label???)
- Ensure there is enough background information on the issue for a would-be assignee
- State exactly what is unknown that we need to determine so that we can convert this
  knowledge into deliverables for other issues.
- Ensure that the deliverables have been clearly defined and whether other issues
  need to be created as a result of this spike.

### How do I complete a spike?

Being able to determine whether a spike is complete should be an easy task provided
that the deliverables have been clearly defined. When this is not the case, you should
not work on the issue and instead attempt to clarify the deliverables with those also
working on the project.
