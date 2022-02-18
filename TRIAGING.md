## The Triaging Process at `conda`

"Triaging" refers to the process of assessing the priority of incoming issues.

In order to explain how various `conda` issues are evaluated, the following document will provide information about our triaging process in the form of an FAQ.


### Why triage?

At the most basic "bird's eye view" level, triaged issues will fall into the category of three main priority levels:

- Do now
- Do sometime
- Never do (_i.e._, close)

At its core, triaging enables new issues to be sorted into these three categories, which enables them to be processed at a velocity similar to or exceeding the rate at which new issues are coming in. One of the benefits of actively triaging issues is to avoid burnout and make necessary work sustainable; this is done by eliminating a never-ending backlog that has not been reviewed by any maintainers.

There will always be broad-scope design and architecture implementations that the `conda` team will be interested in pursuing; by actively triaging issues, the `conda` engineers will be able to more easily track and tackle both specific and big-picture goals.


### How do items show up in triaging?

New issues that are opened in any of the repositories in the [`conda` GitHub project](https://github.com/conda) will show up in the `New` column of the [Triaging board](https://github.com/orgs/conda/projects/4).


### What is done about the issues in "triaging" mode?

Issues in the "Triaging" column of the board have been reviewed by the triage rotation engineer and are considered ready for the following procedures:

- Mitigation via short-term workarounds and fixes
- Redirection to the correct project
- Determining if support can be provided for errors and questions
- Closing out of any duplicate issues

The `conda` engineer who is assigned to the triaging rotation is not seeking to _resolve_ issues that arise. Instead, the goal is to understand the issue and to understand whether it is an issue in the first place and to then collect as much relevant information as possible so that the maintainers of `conda` can make an informed decision on the appropriate resolution schedule necessary.

Issues will remain in "Triaging" as long as the issue is in an investigatory phase (_e.g._, querying the user for more details, asking the user to attempt other workarounds, other debugging efforts, etc.) and are likely to remain in this state the longest but should still be progressing over the course of 1-2 weeks.


### When do items move out of triaging?

All triaged issues will be reviewed by `conda` engineers during a weekly Refinement meeting in order to understand how the triaged issues fit into the short- and long-term roadmap of `conda`. Though the Refinement meeting is not open to the public, the prioritization of issues is made publicly available via GitHub Milestones. It will also be during Refinement where decisions are made to earmark feature requests for specific future releases (versus a more open-ended backlog), tag issues as ideal for first-time contributors, as well as making decisions to close/reject specific feature requests.

The additional columns in the triaging board that the issues can be moved to include the following:

- **"Support"** - Any issue moved into this column is a request for support and is not a feature request or a bug report.
- **"Ready"** - The issue has revealed a bug or feature request. We have collected enough details to understand the problem/request and to reproduce it on our own. These issues are ready to be moved into the Backlog at the end of the triage rotation during Refinement.
- **"Closed"** - The issue was closed due to being a duplicate, being redirected to a different project, was a user error, a question that has been resolved, etc.


### Where do items go after being triaged?

Once issues are deemed ready to be worked on, they will be moved to the [`conda` Backlog project board](https://github.com/orgs/conda/projects/5) on GitHub. Once there, the timeline of when/how to work on each issue is decided by members of the `conda` team. When actively in-progress, the issues will be moved to the [Sprint project board](https://github.com/orgs/conda/projects/8) and then closed out once the work is complete.


### What is the purpose of having a "backlog"?

Issues are "backlogged" when they have been triaged but not yet earmarked for an upcoming release. Weekly Refinement meetings are a time when the `conda` engineers will transition issues from "Triage" to "Backlog". Additionally, this time of handoff will include discussions around the kind of issues that were raised, which provides an opportunity to identify any patterns that may point to a larger problem.


### What is the purpose of a "development sprint"?

[TODO]


### How does labeling work?

[TODO]


### How are new labels defined?

[TODO]


### Who triages?

[TODO]

<!-- List of names/GitHub handles here? -->
