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
* Time to finish. Defined as the time since the moment a process is open, to the time it is finished. 

Both for time to attend and time to complete, the mean for a collection of processes is not significant, because the distribution of times is usually very skewed. Medians or quantiles can be more useful to characterize the time to attend for a collection of processes. You can remember what the median and quantiles mean:

> "A collection of processes has a median t of time-to-something if the longest of the 50% of processes with shortest time-to-something is t. In other words, 50% of the processes were shorter than t, and 50% were longest than t."

> "A collection of processes has a 0.95 quantil of time-to-something equal to t if the longest of the 95% of processes with shortest time-to-someting is t. In other words, 95% of the processes were shortest than t, and 5% were longest than t.

You can quickly notice that the median is the 0.5 quantil.

As an example, if the median of time-to-close tickets for a certain month was 23.34 hours, that means that 50% of the tickets were closed in less than 23.34 hours, or than 50% of the tickets took more than 23.34 hours to close.

As another example, if the 0.95 quantil of time-to-review a change is of 4.34 days, that means that 95% of the changes were reviewed in less than 4.34 days, but 5% of the changes were reviewed in more than 4.34 days.

You should notice as well that you can only measure time-to-X if X already happened. For example, time-to-close can only be measured for a ticket if it was already closed. Otherwise, you can only know that time-to-close will be longer than the time it has been open up to now, but nothing else. This is important, because it can cause counter-intuitive situations.

Assume for example a project with 100 still open tickets and 50 already closed tickets. All 50 closed tickets had a time-to-close of 2 days. All the 100 open tickets were open 60 days ago. If we measure the median of time-to-close now, it will be of 2 days, since it only applies to closed tickets. Now, the 100 still open tickets are closed during today. At the end of the day, we have 50 tickets with 2 days of time-to-close, and 100 with 60 days of time-to-close. That is, our median of time-to-close raised to 60 days, even when we closed a lot of old tickets. In other words, closing a lot of tickets raised time-to-close, which could be interpreted as a decrease in performance, when it is exaclty the other way around.

To avoid this effects, there are some other metrics, such as:

* time-active. It is defined as time since the process started, only for processes which still didn't finish. In some sense, it is a complement to time-to-finish: while time-to-finish considers only finished processes, time-active provides a similar information, but only for processes still open.

In the former example, time-active before closing the old 100 tickets would be 100 days foro all tickets to consider (those still open). After closing those 100 tickets, there are no tickets to calculate time-active, since all of them are closed.

* time-open. It is defined as time-to-close for processes already closed, and time-active (time since opened) for processes still open.

In the former example, time-open before closing the old 100 tickets would be of 2 days for the closed tickets, and of 60 days for still open tickets. That would be a median of 60 days. After closing the tickets, it would still be of 2 and 60 days, now keeping the median in 60 days, which at least remains constant.

* aggregated-time-open. It is defined as the sum of time-open for all tickets.

In the former example, before closing the tickets aggregated-time-open is of

```
50 x 2 + 100 x 60 = 6100 days
```

* aggregated-time-open-diff. We define this as the difference with the previous time-open for all tickets. This allows us to have a comparison about how aggregated-time-open varies over time, if it is measured periodically.

exactly as it will be after closing the 100 old tickets. This allows for a monotonic metric, which produces more intuitive results.

Another example can illustrate a different scenario. Assume now that a project is opening 3 processes every day, and is closing them after two days (at the end of the second day). Metrics will be evaluated at the end of each day. In this case, metrics will evolve as follows:

|Day|New|Finished|Open|Closed|TTF (median)|TA (median)|TO (median)|ATO | ATOD |
|---|---|--------|----|------|------------|-----------|-----------|----|------|
| 1 | 3 | 0      | 3  | 0    | N/A        | 1         | 1         | 3  | N/A  |
| 2 | 3 | 3      | 3  | 3    | 2          | 1         | 1.5       | 9  | 6    |
| 3 | 3 | 3      | 3  | 6    | 2          | 1         | 2         | 15 | 6    |
| 4 | 3 | 3      | 3  | 9    | 2          | 1         | 2         | 21 | 6    |
*Table describing an scenario of a project opening and closing processes. Each row represents a day. New: number of new processes open during the day. Finished: number of processes finished during the day. Open: number of processes still open at the end of the day (this is the backlog of still open processes). Closed: number of processes already closed at the end of the day. TTF: time-to-finish (or time-to-close) for all closed processes at the end of the day. TA: time-active, for open processes. TO: time-open, for open and closed processes, at the end of the day. ATO: aggregrated-time-open at the end of the day. ATOD: aggregated-time-open-diff at the end of the day. For simplicity, we assume that new processes start at the beginning of the day, and finished processes finish at the end of the day. All times are in days.*

The median for time-to-finish quickly moves from N/A to 2 once the project starts to finish processes, and remain there since the time it takes to close tickets is constant. Time-active remains stable at 1, since at the end of the day, the processes from yesterday were closed, and only those opened when the day started are still active. Time-open reflects a bit more closely what is happening in days 1, 2, and 3, moving from 1 to 2 as more new processes start. Aggregated-time-open-diff shows the regularity of the system as well.

Now, let's see how the metrics reflect a peak in new processes. Let's assume that on day 5, in addition to the 3 new processes that are finished in two days, 10 new processes start, and they are not finished during the following days.

|Day|New|Finished|Open|Closed|TTF (median)|TA (median)|TO (median)|ATO | ATOD |
|---|---|--------|----|------|------------|-----------|-----------|----|------|
| 5 | 13| 3      | 13 | 12   | 2          | 1         | 1         | 37 | 16   |
| 6 | 3 | 3      | 13 | 15   | 2          | 2         | 2         | 53 | 16   |
| 7 | 3 | 3      | 13 | 18   | 2          | 2         | 2         | 69 | 16   |

On day 5, we have 13 new processes: the 3 "regular" ones, and that peak of 10 more. At the end of the day, we have closed the 3 processes that started on day 4. This means that 13 processes (all that started during the day) remain open at the end of the day. We have a total of 12 closed processes (we had 9 on day 4, plus three more we finished today). The median for time-to-finish remains at 2, since all closed processes took 2 days to finish. All processes still open were opened at the beginning of the day, therefore time-active is 1 for all of them, and the median too. The median for time-open, on the contrary, and maybe surprisingly, went down to 1. The accounting is as follows: 12 closed processes took 2 days to finish, while 13 open processes have been open for one day. Therefore, more than 50% of the process have a time-open of 1 day. Aggregated-time-open rose to 37: it was 21, plus 3 more days for the processes finished during the day, plus 13 more days for the new processes that started today. Aggregated-time-open-diff rose to 16 days (37 - 21).

On day 6, we have only three new "regular" processes, and we finish the three "regulars" that started on day 5. That means that the number of processes still open at the end of the day remains at 13, since none of the 10 "extra" processes that started on day 5 finished. The number of closed processes is rises to 15, with the 3 from day 5 that were finished. Time-to-finish remains at 2, since still all finished processes took 2 days to finish. Time-open now rises to 2, with the following accounting: 15 closed processes took 2 days to finish; 10 processes that started on day 5 have been open for 2 days; 3 processes open today were open for 1 day. In short: for 25 processes time-open is 2, for 3 it is 1. Therefore, the median is 2. From this accounting it is clear that aggregated-time-open is 53, and aggregated-time-open-diff is 16.

On day 7, new, finished and open remains as on day 6, since only 3 "regular" new processes start. Closed processes are increased with the 3 that are closed today. Time-to-finish remains at 2. Time-open is calculated as follows: 18 processes took two days to close, 10 processes were open for 3 days, 3 processes were open for 1 day. Therefore, the median of time-open remains at 2. From these numbers, aggregated-time-open is 36 + 30 + 3, that is 69. Aggregated-time-open-diff is 16 once again.

From this scenario, we can learn several lessons. Time-to-finish does not reflect new processes that are still not finished. They can last for long periods, but will not be reflected in time-to-finish until they are finished. That means that time-to-finish can grow quickly when old processes are finalized, which is natural as we defined the metric, but is maybe not what some people expect when consider a longer time-to-finish as a worse metric, when comparing.

Another lesson is that time-open can be masked by a large population of closed processes. In the example, assuming the pattern of new processes includes only "regular" processes, the median for time-open will remain at 2, even when a large amount of open tickets are unattened.

Aggregated-time-open and specially aggregated-time-open-diff reflect much better what is happening. Aggregated-time-open-diff, in particular shows how we have a continuous "lag" in dealing with processes, those 16 days of "increase" every day. That metric rose immediately when new processes entered, and will only go down when they are finished. It reflects to some extent the "amount of work still open".



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
