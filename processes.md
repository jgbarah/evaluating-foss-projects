# Evaluating development processes

Processes are fundamental in software development. We can model as processes most actions in development projects, from implementing a new feature, to fixing a bug, or even to make a decision about how to implement a feature. Many of these processes can be tracked using information available in software development repositories.

From this point of view, FOSS projects are not different from any other software development project. But, as we discussed in the case of activity, when the project follows an open development model, most of the information needed to track processes is public. Therefore, any third party can use it to evaluate how those processes are being completed.

## Performance

There are several metrics for evaluating performance in processes. Some of the most useful are:

* Efficiency. Defined as the ratio between finished processes and new (started) processes for a certain period. For example, efficiency in dealing with tickets can be defined as tickets closed / tickets opened per month. Efficiency lower than one means that the project is not coping with new processes: more processes are starting that the project is finishing. Every period that happens, the backlog of open processes will increase. The evolution over time of efficiency allows to understand the long-term trends, and whether a certain efficiency is something temporary, or a permanent trend.

![Efficiency in dealing with tickets, OpenStack project](bmiOpenStackSoftware.jpg)
*Example of efficiency: Ratio of closed to opened tickets per quarter for the OpenStack project. From the [OpenStack Community Activity Report, January-March 2015](), by Bitergia.*

* Backlog. Defined as the number of processes currently open at a certain moment. For example, the backlog The backlog is the workload the project has to deal with, assuming no new workload appears. If the backlog increases, efficiency is lower than one, and the project is not coping with new processes.
* Time to attend. Defined as the time since the moment a process is open, to the time it is first attended by the project. 

All these metrics have to be considered in the context of activity. This applies specially to efficiency and backlog, but affect other metrics too. For example, in the context of a project where activity is growing quickly, it is relatively normal that efficiency is less than one, but still the project is healthy in the long term. When activity is growing quickly, usually the project is receiving more resources, and its community is growing accordingly.

But allocating new effort to deal with processes may take some time, while the growth in activity is directly linked to the opening of new processes. Therefore, it is usual that there is a certain lag between needs to close processes, and new people dealing with them. As the project stabilizes, it will start to create new processes more slowly, efficiency will increase, and backlog will start to decrease.

### New features

### Bug fixing

### Code review

## Workflow patterns

Projects use different workflows to deal with processes. In many cases, even they can have specific policies, such as defining allowed state transitions to deal with tickets, or review patterns to deal with proposals of change to the source code. When the different states and transitions are recorded in some development repository, the complete process can be tracked. This allows for the analysis of the real workflows, and their compliance with good practices or project policies. In addition, time between transitions can be measured, to detect bottlenecks and compute time for different workflows.

### Example: code review

In code review, the workflow can be divided between two stated: waiting for review and waiting for new change proposals.

### Example: tickets

Closing tickets usually means workflows moving through a complex collection of states.

Some of the states may imply dependencies on communication with users, or on external projects fixing some issue. Therefore, the detailed analysis of state changes can also be used to attribute delays to developers, to users, or to external projects.

## Participation

We can also analyze who participated in specific processes in a project. From that point on, we can assess on several dimensions, discussed in sections below, such as diversity in participation or neutrality.

### Ticket closing

### Code review

### Mailing lists


## Interaction with users

Communication channels can be used by users to solve problems or report them. This interaction can be monitored in several repositories. In our experience, this can be done mainly on both ticketing and asynchronous communication systems. From those, it can be known:

* Who asks for help, or in general comments on issues related to the project.
* Who participates in solving those issues.
* Who of those who participate are developers.

## Diversity in participation

There are several aspects about participation in processes where diversity has a role:

* Participation from diverse time zones in specific process, which may help to speed the process up, or to slow it down, depending on how is that participation.
* Participation by diverse companies.

## Neutrality
