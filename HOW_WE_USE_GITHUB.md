<!-- absolute URLs -->
[conda-org]: https://github.com/conda
[sub-team]: https://github.com/conda-incubator/governance#sub-teams

[project-planning]: https://github.com/orgs/conda/projects/2/views/11
[project-sorting]: https://github.com/orgs/conda/projects/2/views/11
[project-support]: https://github.com/orgs/conda/projects/2/views/12
[project-backlog]: https://github.com/orgs/conda/projects/2/views/13
[project-in-progress]: https://github.com/orgs/conda/projects/2/views/14

[docs-toc]: https://github.blog/changelog/2021-04-13-table-of-contents-support-in-markdown-files/
[docs-actions]: https://docs.github.com/en/actions
[docs-saved-reply]: https://docs.github.com/en/get-started/writing-on-github/working-with-saved-replies/creating-a-saved-reply

[workflow-sync]: https://github.com/conda/infrastructure/blob/main/.github/workflows/sync.yml
[labels-global]: https://github.com/conda/infrastructure/blob/main/.github/global.yml
[stale]: https://github.com/conda/infrastructure/blob/main/.github/workflows/stale.yml
[cla]: https://github.com/conda/infrastructure/blob/main/.github/workflows/cla.yml
[lock]: https://github.com/conda/infrastructure/blob/main/.github/workflows/lock.yml
[project-workflow]: https://github.com/conda/infrastructure/blob/main/.github/workflows/project.yml

<!-- relative URLs -->
[workflow-issues]: /.github/workflows/issues.yml
[workflow-project]: /.github/workflows/project.yml
[labels-local]: /.github/labels.yml
[labels-page]: ../../labels

## How We Use GitHub

> **Note**
> For easy navigation use [GitHub's table of contents feature][docs-toc].

This document seeks to outline how we as a community use GitHub Issues to track bugs and feature requests while still catering to development practices & project management (*e.g.*, release cycles, feature planning, priority sorting, etc.).

<!-- only include high-level topics or particularly noteworthy sections here -->
Topics:
  - [What is Issue Sorting?](#what-is-issue-sorting)
  - [Issue Sorting Procedures](#issue-sorting-procedures)
  - [Types of tickets](#types-of-tickets)
    - [Normal Ticket/Issue](#normal-ticketissue)
    - [Epics](#epics)
    - [Spikes](#spikes)
  - [Working on tickets](#working-on-tickets)


### What is "Issue Sorting"?

> **Note**
> "Issue sorting" is similar to that of "triaging", but we've chosen to use different terminology because "triaging" is a word related to very weighty topics (*e.g.*, injuries and war) and we would like to be sensitive to those connotations. Additionally, we are taking a more "fuzzy" approach to sorting (*e.g.*, severities may not be assigned, etc.).

"Issue Sorting" refers to the process of assessing the priority of incoming issues. Below is a high-level diagram of the flow of tickets:

```mermaid
flowchart LR
    subgraph flow_sorting [Issue Sorting]
        board_sorting{{Sorting}}
        board_support{{Support}}

        board_sorting<-->board_support
    end

    subgraph flow_refinement [Refinement]
        board_backlog{{Backlog}}

        board_backlog-- refine -->board_backlog
    end

    subgraph flow_progress [In Progress]
        board_progress{{In Progress}}
    end

    state_new(New Issues)
    state_closed(Closed)

    state_new-->board_sorting
    board_sorting-- investigated -->board_backlog
    board_sorting-- duplicates, off-topic -->state_closed
    board_support-- resolved, unresponsive -->state_closed
    board_backlog-- pending work -->board_progress
    board_backlog-- resolved, irrelevant -->state_closed
    board_progress-- resolved -->state_closed
```

In order to explain how various `conda` issues are evaluated, the following document will provide information about our sorting process in the form of an FAQ.


#### Why sort issues?

At the most basic "bird's eye view" level, sorted issues will fall into the category of four main priority levels:

- Do now
- Do sometime
- Provide user support
- Never do (_i.e._, close)

At its core, sorting enables new issues to be placed into these four categories, which helps to ensure that they will be processed at a velocity similar to or exceeding the rate at which new issues are coming in. One of the benefits of actively sorting issues is to avoid engineer burnout and to make necessary work sustainable; this is done by eliminating a never-ending backlog that has not been reviewed by any maintainers.

There will always be broad-scope design and architecture implementations that the `conda` maintainers will be interested in pursuing; by actively organizing issues, the sorting engineers will be able to more easily track and tackle both specific and big-picture goals.

#### Who does the sorting?

Sorting engineers are a `conda` governance [sub-team][sub-team]; they are a group of Anaconda and community members who are responsible for making decisions regarding closing issues and setting feature work priorities, amongst other sorting-related tasks.


#### How do items show up for sorting?

New issues that are opened in any of the repositories in the [`conda` GitHub project][conda-org] will show up in the `Sorting` view of the [Planning project][project-planning]. This process is executed via [GitHub Actions][docs-actions]. The two main GitHub Actions workflows utilized for this purpose are [Issues][workflow-issues] and [Project][workflow-project].

The GitHub Actions in the `conda/infrastructure` repository are viewed as canonical; the [Sync workflow][workflow-sync] sends out any modifications to other `conda` repositories from there.


#### What is done about the issues in "sorting" mode?

Issues in the ["Sorting" tab of the project board][project-sorting] are considered ready for the following procedures:

- Mitigation via short-term workarounds and fixes
- Redirection to the correct project
- Determining if support can be provided for errors and questions
- Closing out of any duplicate/off-topic issues

The sorting engineers on rotation are not seeking to _resolve_ issues that arise. Instead, the goal is to understand the ticket and to determine whether it is an issue in the first place, and then to collect as much relevant information as possible so that the maintainers of `conda` can make an informed decision about the appropriate resolution schedule.

Issues will remain in the "Sorting" tab as long as the issue is in an investigatory phase (_e.g._, querying the user for more details, asking the user to attempt other workarounds, other debugging efforts, etc.) and are likely to remain in this state the longest, but should still be progressing over the course of 1-2 weeks.

For more information on the sorting process, see [Issue Sorting Procedures](#issue-sorting-procedures).


#### When do items move out of the "Sorting" tab?

Items move out of the "Sorting" tab once the investigatory phase described in [What is done about the issues in "sorting" mode?](#what-is-done-about-the-issues-in-sorting-mode) has concluded and the sorting engineer has enough information to make a decision about the appropriate resolution schedule for the issue. The additional tabs in the project board that the issues can be moved to include the following:

- **"Support"** - Any issue in the ["Support" tab of the Planning board][project-support] is a request for support and is not a feature request or a bug report. All issues considered "support" should include the https://github.com/conda/infrastructure/labels/type%3A%3Asupport label.
- **"Backlog"** - The issue has revealed a bug or feature request. We have collected enough details to understand the problem/request and to reproduce it on our own. These issues have been moved into the [Backlog tab of the Planning board][project-backlog] at the end of the sorting rotation during Refinement.
- **"Closed"** - The issue was closed due to being a duplicate, being redirected to a different project, was a user error, a question that has been resolved, etc.


#### Where do work tickets go after being sorted?

Once issues are deemed ready to be worked on, they will be moved to the [`conda` Backlog tab of the Planning board][project-backlog] on GitHub. Once actively in progress, the issues will be moved to the [In Progress tab of the Planning board][project-in-progress] and then closed out once the work is complete.


#### What is the purpose of having a "Backlog"?

Issues are "backlogged" when they have been sorted but not yet earmarked for an upcoming release.


#### What automation procedures are currently in place?

Global automation procedures synced out from the `conda/infrastructure` repo include:
- [Marking of issues and pull requests as stale][stale], resulting in:
  - issues marked as https://github.com/conda/infrastructure/labels/pending%3A%3Asupport being labelled stale after 21 days of inactivity and being closed after 7 further days of inactivity (that is, closed after 30 inactive days total)
  - all other inactive issues (not labelled as https://github.com/conda/infrastructure/labels/pending%3A%3Asupport) being labelled stale after 365 days of inactivity and being closed after 30 further days of inactivity (that is, closed after an approximate total of 1 year and 1 month of inactivity)
  - all inactive pull requests being labelled stale after 365 days of inactivity and being closed after 30 further days of inactivity (that is, closed after an approximate total of 1 year and 1 month of inactivity)
- [Locking of closed issues and pull requests with no further activity][lock] after 365 days
- [Adding new issues and pull requests to the respective project boards][project-workflow]
- [Creation of pull requests to facilitate easier adding of accounts that have signed the CLA][cla] to `.clabot`, following verification procedures
- [Syncing out of templates, labels, workflows and documentation][workflow-sync] from `conda/infrastructure` to the other conda organization repositories


### Issue Sorting Procedures

### How are issues sorted?

Issues in the ["Sorting" tab of the project board][project-sorting] are reviewed by issue sorting engineers, who take rotational sorting shifts. In the process of sorting issues, engineers label the issues and move them to the other tabs of the project board for further action.

Issues that require input from multiple members of the sorting team will be brought up during a weekly refinement meeting in order to understand how those particular issues fit into the short- and long-term roadmap of `conda`. These meetings enable the sorting engineers to get together to collectively prioritize issues, earmark feature requests for specific future releases (versus a more open-ended backlog), tag issues as ideal for first-time contributors, as well as whether or not to close/reject specific feature requests.

#### How does labeling work?

Labeling is a very important means for sorting engineers to keep track of the current state of an issue with regards to the asynchronous nature of communicating with users. Utilizing the proper labels helps to identify the severity of the issue as well as to quickly understand the current state of a discussion.

Each label has an associated description that clarifies how the label should be used. To see a label's description, find the label either in `conda/infrastructure`'s [`.github/global.yml` file][labels-global] or, if it is not there, in the relevant repository's `.github/labels.yml` file. Label colors are used to distinguish labels by category.

Generally speaking, labels with the same category are considered mutually exclusive but in some cases labels sharing the same category can occur concurrently as they indicate qualifiers as opposed to types. For example, we may have the following types, https://github.com/conda/infrastructure/labels/type%3A%3Abug, https://github.com/conda/infrastructure/labels/type%3A%3Afeature, and https://github.com/conda/infrastructure/labels/type%3A%3Adocumentation, where for any one issue there would be _at most_ **one** of these to be defined (_i.e._ an issue shouldn’t be a bug _and_ a feature request at the same time). Alternatively, with issues involving specific operating systems (_i.e._, https://github.com/conda/infrastructure/labels/os%3A%3Alinux, https://github.com/conda/infrastructure/labels/os%3A%3Amacos, and https://github.com/conda/infrastructure/labels/os%3A%3Awindows), an issue could be labeled with one or more depending on the system(s) the issue is occurring on.

Please note that there are also automation policies in place that are affected by labelling. For example, if an issue is labeled as https://github.com/conda/infrastructure/labels/pending%3A%3Asupport, that issue will be marked https://github.com/conda/infrastructure/labels/stale after 21 days of inactivity and auto-closed after seven more days without activity (30 inactive days total), which is earlier than issues without this label. See [What automation procedures are currently in place?](#what-automation-procedures-are-currently-in-place) for more details.


#### What labels are required for each issue?

At minimum, both `type` and `source` labels should be specified on each issue before moving it from "`Sorting`" to "`Backlog`". All issues that are bugs should also be tagged with a `severity` label.

The `type` labels are exclusive of each other: each sorted issue should have exactly one `type` label. These labels give high-level information on the issue's classification (e.g., bug, feature, tech debt, etc.)

The `source` labels are exclusive of each other: each sorted issue should have exactly one `source` label. These labels give information on the sub-group to which the issue's author belongs (e.g., a partner, a frequent contributor, the wider community). Through these labels, the conda organization hopes to gain insight into how well we're meeting the needs of various groups.

The `severity` labels are exclusive of each other and while required for the `type::bug` label it can also be applied to other types to indicate demand or need. These labels help us to prioritize our work. Severity is not the only factor for work prioritization, but it is an important consideration.

Please review the descriptions of the `type`, `source` and `severity` labels on the [labels page][labels-page] prior to use.


#### How are new labels defined?

Labels are defined using a scoped syntax with an optional high-level category (_e.g._, source, tag, type, etc.) and a specific topic, much like the following:

- `[topic]`
- `[category::topic]`
- `[category::topic-phrase]`

This syntax helps with issue sorting enforcement, as it helps to ensure that sorted issues are, at minimum, categorized by type and source.

There are a number of labels that have been defined for the different `conda` projects. In order to create a streamlined sorting process, label terminologies are standardized using similar (if not the same) labels.


#### How are new labels added?

New **global** labels (_i.e._, generic labels that apply equally to all `conda` repos) can be added to the `conda/infrastructure`'s [`.github/global.yml` file][labels-global]; new **local** labels (_i.e._, labels specific to particular `conda` repos) can be added to each repository's [`.github/labels.yml`][labels-local] file. All new labels should follow the labeling syntax described in the "How are new labels defined?" section of this document. Global labels are synced out to all repositories as part of the [workflow sync][workflow-sync] process.


#### Are there any templates to use as responses for commonly-seen issues?

Some of the same types of issues appear regularly (_e.g._, issues that are duplicates of others, tickets that should be filed in the Anaconda issue tracker, errors that are due to a user's specific setup/environment, etc.).

Below are some boilerplate responses for the most commonly-seen issues to be sorted:

<details>
<summary><b>Duplicate Issue</b></summary>

<pre>

This is a duplicate of <b>[link to primary issue]</b>; please feel free to continue the discussion there.
</pre>

> **Warning**
> Apply the https://github.com/conda/infrastructure/labels/duplicate label to the issue being closed and https://github.com/conda/infrastructure/labels/duplicate%3A%3Aprimary to the original issue.

</details>

<details>
<summary><b>Requesting an Uninstall/Reinstall of <code>conda</code></b></summary>

<pre>

Please uninstall your current version of `conda` and reinstall the latest version.
Feel free to use either the [miniconda](https://docs.conda.io/en/latest/miniconda.html)
or [anaconda](https://www.anaconda.com/products/individual) installer,
whichever is more appropriate for your needs.
</pre>

</details>

<details>
<summary><b>Redirect to Anaconda Issue Tracker</b></summary>

<pre>

Thank you for filing this issue! Unfortunately, this is off-topic for this repo.
If you are still encountering this issue please reopen in the
[Anaconda issue tracker](https://github.com/ContinuumIO/anaconda-issues/issues)
where `conda` installer/package issues are addressed.
</pre>

> **Warning**
> Apply the https://github.com/conda/infrastructure/labels/off-topic label to these tickets before closing them out.

</details>

<details>
<summary><b>Redirecting to Nucleus Forums</b></summary>

<pre>

Unfortunately, this issue is outside the scope of support we offer via GitHub;
if you continue to experience the problems described here,
please post details to the [Nucleus forums](https://community.anaconda.cloud/).
</pre>

> **Warning**
> Apply the https://github.com/conda/infrastructure/labels/off-topic label to these tickets before closing them out.

</details>

In order to not have to manually type or copy/paste the above repeatedly, please note that it's possible to add text for the most commonly-used responses via [GitHub's "Add Saved Reply" option][docs-saved-reply].


### Types of Tickets

#### Standard Ticket/Issue

TODO

#### Epics

TODO

#### Spikes

##### What is a spike?
"Spike" is a term that is borrowed from extreme programming and agile development. They are used when the **outcome of a ticket is unknown or even optional**. For example, when first coming across a problem that has not been solved before, a project may choose to either research the problem or create a prototype in order to better understand it.

Additionally, spikes represent work that **may or may not actually be completed or implemented**. An example of this are prototypes created to explore possible solutions. Not all prototypes are implemented and the purpose of creating a prototype is often to explore the problem space more. For research-oriented tasks, the end result of this research may be that a feature request simply is not viable at the moment and would result in putting a stop to that work.

Finally, spikes are **timeboxed**. This means that we set a definite limit on how long we want our contributors to work on a spike. We do this to prevent contributors from falling into a rabbit hole they may never return from (scary!). Instead, we set a time limit to perform work on the spike and then have the assignee report back to the project team. If the tasks defined in the spike have not yet been completed, a decision is made on whether it makes sense to perform further work on the spike.

Below is what that workflow looks like:

###### When do I create a spike?
A spike should be created when we do not have enough information to move forward with solving a problem. That simply means that, whenever we are dealing with unknowns or processes the project team has never encountered before, it may be useful for us to create a spike.

In day-to-day work, this kind of situation may appear when new bug reports or feature requests come in that deal with problems or technologies that the project team is unfamiliar with. All issues that the project team has sufficient knowledge of should instead proceed as regular issues.

###### When do I not create a spike?
Below are some common scenarios where creating a spike is not appropriate:

- Writing a technical specification for a feature we know how to implement
- Design work that would go into drafting how an API is going to look and function
- Any work that must be completed or is not optional


### Working on Tickets

#### How do I assign myself to a ticket I am actively reviewing?

If you do **not** have permissions, please indicate that you are working on an issue ticket by commenting on the issue. Someone who has permissions will assign you to the ticket. If two weeks have passed without a pull request or an additional comment requesting information, you may be removed from the issue and the issue reassigned.

If you are assigned to an issue but will not be able to continue work on it, please comment to indicate that you will no longer be working on it and press `unassign me`, next to your username in the `Assignees` section of the issue page (top right).

If you **do** have permissions, please assign yourself to the issue by pressing `assign myself` under the `Assignees` section of the issue page (top right).
