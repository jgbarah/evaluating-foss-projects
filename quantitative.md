# Basics of quantitative evaluation

Quantitative evaluation is based on the identification of quantitative parameters that can be significant, and the definition of measurement models for them.

## Goal-question-metric

### Definition of goals

### Definition of questions

### Definition of metrics

## Automatic or manual quantitative evaluation

## The Polarsys Maturity Model case

## Activity

In this context, evaluating activity refers to finding signs and traces of activity performed to make the project advance towards its goals. Activity can be of different kinds, such as:

* committing patches to the source code management system
* reporting, commenting or fixing bugs in the issue tracking system
* submitting patches or reviewing them in the code review system
* sending messages to mailing lists or synchronous communication systems

Not all the activity is observable, and suitable for evaluation. For example, in mailing lists it is easy to know when a message is sent: it is enough to explore the list archive. But it is difficult to know who received that message (the list recipients is usually not public), and almost impossible to know who read it (reading is a private activity performed in your own mailer program).

But the observable activity is usually good enough to know about the heartbeat of the project, about how many people is active in different roles, and about the general trends. 

There are several analysis of activity suitable for evaluation. The most common are:

* Parameters reflecting activity for a certain period. For example, number of changes to the source code for the whole history of the project, or number of messages sent to mailing lists of the project during a certain week.
* People active for a certain period. For example, people fixing bugs during a release period, or people providing code review advise during the last month.
* Evolution of any of them. For example, new tickets per month for the whole live of the project, or messages sent to IRC channels per week.
* Trends for any of them. For example, increase (or decrease) in number of messages posted in the forums for the project from December 2014 to January 2015.

![Activity in Puppet (commits per month) circa June 2015](activity-puppet-commits.png)
*Number of commits per month for Puppet, as [shown by Grimoire Dashboard](http://bitergia.dev.puppetlabs.com), circa June 2015. Trends for the last year, month and week are shown as well.*

Parameters by themselves only provide a first hint. Saying that a project is performing 2,303 commits in one month is a first indicator about how active is the project, but doesn't provide too much information. Putting it into context starts to make things more interesting. For example, comparing two projects with similar functionality, but one of them committing five times the other, is a first step towards comparing their activities.

However, commit patterns may be very different from project to project, and a simple comparison may be misleading. For example, one of them may be committing a very single change proposal, just to improve them later. Another one, meanwhile, may be following an stringent code review process, committing only after several iterations that improved change proposals. The first pattern will produce much more commits than the second. The same can be said for other parameters.

Comparisons within the same project are usually much more interesting and fair. If the project didn't change policies nor patterns during the last two months, comparing activity parameters will provide a good idea of trends. Comparisons over larger periods of time will allow for detecting the impact of changes in policies, tools or patterns. For excample, changes of the source code management system, or the introduction of code review, or policies on closing old tickets are reflected in the long-term charts about activity. And of course, growth, stagnation or decrease in activity can be clearly perceived over time.

In addition to the raw parameters on activity, the parameters related to persons performing that activity are also relevant. They allow for a first characterization of the active community in several areas. An exponential growth in code authors, or a steady decline in bug fixers will certainly be interesting subjects of further analysis.

Seen several of these parameters together allows for a multifaceted view of the project. As an example, next figures show a summary of activity of the same project, OpenStack, as shown in three different dashboards: Grimoire, Stackalitics, and Open Hub.

![Activity in OpenStack as shown by Grimoire Dashboard, circa June 2015](activity-openstack.png)
*Activity in OpenStack: summary of activity in serveral repositories over time, as [shown by Grimoire Dashboard](http://activity.openstack.org), circa June 2015.*

The Grimoire Dashboard shows activity in each kind of repository, which allows for easy comparison, while at the same time the general trends of activity in the project are visible. It shows some metrics about the people active in different roles.

![Activity in OpenStack as shown by Stackalytics, circa June  2015](activity-openstack-stackalytics.png)
*Activity in OpenStack: summary of code merges over time, and split by company and module, as [shown by Stackalytics](http://stackalytics.com), circa June  2015.*

Stackalytics focuses on changes merged, although it shows other activity as well. The summary includes activity by company and by module.

![Activity in OpenStack as shown by Open Hub, circa June 2015](activity-openstack-openhub.png)
*Activity in OpenStack: summary of activity over time, as [shown by Open Hub](https://www.openhub.net/p/openstack), circa June 2015.*

Open Hub shows a chart with the history of the activity, and some factoids about it, with a focus on activity in the source code management system.

### Activity in source code management

Activity in source code management reflects how the project is in producing changes for the products they build. Source code management stores "commits", each of them being a change (or "patch") to the source code. Each change is different in nature, size, complexity, etc., which makes it difficult to compare individual changes. However, when we consider large collections of changes, trends become apparent.



### Activity in code review and ticketing systems

### Activity in communication systems


## Performance

### New features

### Bug fixing

### Code review

## Diversity in supporting organizations

Activity by company.

## Structure of the community

## Evaluating effort
