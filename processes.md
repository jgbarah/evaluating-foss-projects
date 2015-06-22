# Evaluating development processes

Processes are fundamental in software development. We can model as processes most actions in development projects, from implementing a new feature, to fixing a bug, or even to make a decision about how to implement a feature. Many of these processes can be tracked using information available in software development repositories.

From this point of view, FOSS projects are not different from any other software development project. But, as we discussed in the case of activity, when the project follows an open development model, most of the information needed to track processes is public. Therefore, any third party can use it to evaluate how those processes are being completed.

## Performance

There are several metrics for evaluating performance in processes. Some of the most useful are:

* Efficiency. Defined as the ratio between finished processes and new (started) processes for a certain period. For example, efficiency in dealing with tickets can be defined as tickets closed / tickets opened per month. Efficiency lower than one means that the project is not coping with new processes: more processes are starting that the project is finishing. Every period that happens, the backlog of open processes will increase. The evolution over time of efficiency allows to understand the long-term trends, and whether a certain efficiency is something temporary, or a permanent trend.

![Efficiency in dealing with tickets, OpenStack project](bmiOpenStackSoftware.jpg)
*Example of efficiency: Ratio of closed to opened tickets per quarter for the OpenStack project. From the [OpenStack Community Activity Report, January-March 2015](), by Bitergia.*

* Backlog. Defined as the number of processes currently open at a certain moment. For example, the backlog of code review processes still in process on a certain date. The backlog is the workload the project has to deal with, assuming no new workload appears. If the backlog increases, efficiency is lower than one, and the project is not coping with new processes.
 
![Backlog of code reviews, Wikimedia projects](process-backlog-crs-wikimedia.png)
*Example of backlog: Pending code review processes in Wikimedia projects, evolution per month, circa July 2015.*

* Time to attend. Defined as the time since the moment a process is open, to the time it is first attended by the project. For example, the time to attend a certain bug report. Statistics about time to attend say about how responsive the project is, in regard of providing some early feedback to the initiator of the process. For some cases, this early action on the process may be automatic, performed by a bot. Even when this is still interesting, since in the end the opener gets some feedback, usually it is important when a human is dealing with the process for the first time. 
* Time to complete. Defined as the time since the moment a process is open, to the time it is finished. 

Both for time to attend and time to complete, the mean for a collection of processes is not significant, because the distribution of times is usually very skewed. Medians or quantiles can be more useful to characterize the time to attend for a collection of processes. You can remember what the median and quantiles mean:

> "A collection of processes has a median t of time-to-something if the longest of the 50% of processes with shortest time-to-something is t. In other words, 50% of the processes were shorter than t, and 50% were longest than t."

> "A collection of processes has a 0.95 quantil of time-to-something equal to t if the longest of the 95% of processes with shortest time-to-someting is t. In other words, 95% of the processes were shortest than t, and 5% were longest than t.

You can quickly notice that the median is the 0.5 quantil.

As an example, if the median of time-to-close tickets for a certain month was 23.34 hours, that means that 50% of the tickets were closed in less than 23.34 hours, or than 50% of the tickets took more than 23.34 hours to close.

As another example, if the 0.95 quantil of time-to-review a change is of 4.34 days, that means that 95% of the changes were reviewed in less than 4.34 days, but 5% of the changes were reviewed in more than 4.34 days.

You should notice as well that you can only measure time-to-X if X already happened. For example, time-to-close can only be measured for a ticket if it was already closed. Otherwise, you can only know that time-to-close will be longer than the time it has been open up to now, but nothing else. This is important, because it can cause counter-intuitive situations.

Assume for example a project with 100 still open tickets and 50 already closed tickets. All 50 closed tickets had a time-to-close of 2 days. All the 100 open tickets were open 60 dayss ago. If we measure the median of time-to-close now, it will be of 2 days, since it only applies to closed tickets. Now, the 100 still open tickets are closed during today. At the end of the day, we have 50 tickets with 2 days of time-to-close, and 100 with 60 days of time-to-close. That is, our median of time-to-close raised to 60 days, even when we closed a lot of old tickets. In other words, closing a lot of tickets raised time-to-close, which could be interpreted as a decrease in performance, when it is exaclty the other way around.

To avoid this effects, there are some other metrics, such as:

* time-open. It is defined as time-to-close for processes already closed, and time since opened for processes still open.

In the former example, time-open before closing the old 100 tickets would be of 2 days for the closed tickets, and of 60 days for still open tickets. That would be a median of 60 days. After closing the tickets, it would still be of 2 and 60 days, now keeping the median in 60 days, which at least remains constant.

* aggregated-time-open. It is defined as the sum of time-open for all tickets.

In the former example, before closing the tickets aggregated-time-open is of

```
50 x 2 + 100 x 60 = 6100 days
```

exactly as it will be after closing the 100 old tickets. This allows for a monotonic metric, which produces more intuitive results.

In the end, when you are interested in performance of closing processes, you should consider both the backlog and some statistics (usually the median or some quantile) of time-to-close. The backlog will tell you about how much work is pending. The time-to-close about how long did it take to finish the processes.

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
