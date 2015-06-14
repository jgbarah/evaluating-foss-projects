# Evaluation of FOSS communities

For many FOSS projects, the communities supporting them are the main responsibles for the evolution of the project. Evaluating the communities is therefore fundamental to evaluate the project.

## Different scopes: developers, contributors, users...

FOSS communities are diverse, and may include many different actors. But in general, attending to the scope, the following, usually overlapping, communities can be defined:

* The development community, composed by people in charge of developing and maintaining the software produced by the company.
* The contributing community, composed by all the people actively contributing, not only with code. Examples of contributors are: submitters of bug reports, participants in discussions in mailing lists, translators, writers of documentation, etc. The contributing community includes developers too.
* The user community, composed by users of the software participating somehow in the community. This can be by asking questions, by attending events, by joining social network groups with interest in the project. etc. Usually the user community includes the development and contributing communities, since they are also users of the system.
* The ecosystemn community, composed by all stakeholders not only in the project itself, but in all the ecosystem of projects related to it. The user community is a part of the ecosystem community.

We define these communities to hightlight different populations that may be relevant for an evaluation. It is important to realize that their borders are fuzzy, and people move from one to another as time passes.

For each of these scopes, different evaluation means can be used. Despite the apparent diversity, we can also identify some techniques and parameters that are useful for all of them.  The rest of this chapter will enter into the peculiarities of each community, and will show as well what they have in common and the techniques that are usful for evaluating all of them.

### Development community

The development community is composed of the persons developing and maintaining the products produced by the project: software and  related artifacts, such as documentation.

In the case of FOSS projects with open development models based on coordination tools, there is a lot of information available about them. Usually, data can be collected from the following repositories:

* Source code management repository. Almost all the information in is produced by the development community, since they are mainly changes to source code. In fact, one of the ways of defining the development communuity is as "those people who have contributed at least one change".
* Code review system. All reviewers can be considered as a part of the development communities. Most of the submitters of change proposals are also developers, or they are acquiring that status.
* Issue tracking system. Developers participate in ITS by opening, commenting and closing tickets. They are not the only ones opening or commenting, but usually only they can fix issues, and close tickets.
* Asynchronous and synchronous communication. It is very usual to have separate channels for developers, which allow for a separate tracking of this community.

In summary, most of the data in those SCM, CRS and ITS repositories are related to development activities, and developers usually have separate channels in ACS and SCS. Therefore, the evaluation of the development community in open projects, where all these repositories are public, can be very detailed.


### Contributing community

The contributing community is a bit in between the development community and the user community. Contributors are usually users that are in the road to become developers. But they may or may not walk that path towards the development community. This makes it difficult to specifically track contributors who are not developers.

* Issue tracking system.  Tickets are opened by contributors, be them developers or not. Since we consider both feature requests and bug reports as valuable contributions to the project, everything happening in the ITS is performed by the contributing community. However, the "responisve" part of the action is carried on by developers.
* Asynchronous and synchronous communication. Contributors may join development channels. But being they users as well, contributors are also present in user channels. This makes it difficult to track their activity, except that they can be identified in ITS, and their identity linked to ACS and SCS.

Since the difference between "contributor" and "developer" is a specially fuzzy one, in many cases both communities are considered as one. However, in some sense contributors are the pool where developers come from. People usually become developer after contributing to the project for a while. Therefore, for estimating the future of the development community, and the engagement of people who could become developers, studying the contributor community is specially interesting.

### Users community

The community of users of a FOSS projects is much more difficult to evaluate than those of contributors and developers. In fact, even estimating the number of users is usually difficult. Usage is in most cases passive, in the sense that almost no interaction with the project is needed to become user. In most cases of non-FOSS software, to become user implies purchasing a license, which is an action that can be tracked. But in the case of FOSS software, it is enough to get the software somehow, and start using it. No red tape is involved.

Therefore, the source of information to estimate the size of the community of users are indirect:

* Downloads. Many projects maintain a download area. When the primary usage of the product is via those areas, the number of downloads can be an estimator of the number of users. Of course, downloads of different releases have to be taken into account, and some model on when users reinstall with a newer version are needed. But this method can be enough to estimate trends and order-of-magnitude numbers. Of course, if most of the usage is not by direct download, the numbers are much less precise. This happens, for example, when the software is mainly available through FOSS distributions or via third party download areas.
* Questions and comments in user forums. Given that the ratio of users to contributors is very large in most cases, it can be assumed that questions and comments about the product in third party forums are mainly by users. Therefore, the number of those questions and numbers can be a proxy for estimating the user population. Some models to convert those numbers into number of users are needed, but again trends over time can be somewhat accurate.
* Presence in FOSS distributions. Some FOSS distributions maintain their own statistics about package (and therefore, product) installation. For example, in Debian the opt-in Popularity Contest maintains accurate stats of installed packages. From those numbers, and estimating the total population of Debian users, total usage in Debian can be estimated. From there, estimations for other distributions can be extrapolated. These numbers are probably not very accurate, but can provide an order-of-magnitude estimation.
* Answers to polls and surveys. Polls and surveys to specific populations or to the population in general can also be a source of information. This is a general technique to know about user adoption, which compared to the others has the main drawback of its cost. Only the really popular FOSS products will appear in general surveys, but in some cases this is enough to have an idea. For example, the usage of Firefox or Chrome web browsers can be estimated this way.
* Raw numbers in the Internet. Some services, such as Google trends, provide some information about how popular terms are in the web. In some cases, those numbers can be used to estimate trends in usage, assuming that the more popular a product, the more people appearences it will have in the global web.

There are some specific cases when a more concrete estimation, or at least a lower watermark for an estimation can be established:

* Software sending "beacons" to the project. This can be desktop or mobile software connecting to a certain location with a "Here I am" message, or a web product including components that are downloaed from a certain website. In both cases, since FOSS software can be changed, maybe there are versions of the product with the beacon removed. In addition, maybe there are products being used withouth Internet connection. But when these cases can be neglected, the estimation of usage can be very good. A very specific case is when the software, as a part of their normal functioning, identifies itself somehow. For example, web browsers send identification strings to web servers. These strings can be used to estimate usage.
* Software which answers when queried. This a very specific, but very accurate case, when the software can be located and queried. The most well known case is the estimation of web servers, where the user base of Apache or nginx is tracked periodically by querying web servers all over the world for their identification string.
* Software distributed through markets. When the product is distributed mainly through a market (a mobile or a distribution app market), usually it provides detailed numbers about installations, deinstallations, etc.

These three cases are rare, but when they happen, estimations can be very accurate. The next pictures show some cases (web browsers, web servers) for which these methodologies can be used. That allows for the usage estimation of some FOSS products, such as Apache HTTP Server, nginx, Chrome or Firefox.

![StatCounter stats of browser usage](evaluation-usage-statcounter.png)
![W3Counter stats of browser usage](evaluation-usage-w3counter.png)
*Example of usage estimation: [StatCounter top 9 browsers (May 2015)](http://gs.statcounter.com/#all-browser-ww-monthly-201505-201505-bar), top, and [W3Counter web browser market share](http://www.w3counter.com/globalstats.php) (May 2015), bottom. Both surveys are performed by using the identification information from web broswers in large collections of web sites. It is interesting noticing how they differ, even when they seem to use similar methodologies.*

![Netcraft stats of active servers](evaluation-usage-netcraft.png)
*Example of usage estimation: [Netcraft web server survey (May 2015)](http://news.netcraft.com/archives/2015/05/19/may-2015-web-server-survey.html). This survey is performed by querying web servers (in this case, the top million busiest sites) for their identification string.*

### Ecosystem community

The ecosystemm community is a kind of mega-community, including all the communities relevant to the project under evaluation. All the above comments for developer, contributing and user commities apply, since all of them are representer in this ecosystem community. But at the same time, there are more overlappings, since many developers, contributors or users may be in many of the communities in the ecosystem.

The ecosystem community is difficult to study because it is usually large, and is spread through many different infrastructures. In fact, the first problem to address is to find out all the projects that form a part of it, since interrelations between components can be complex. However, this mega-community is very important for the long term sustainability of the project under evaluation. Usually, resources for most projects, including developers and users, come primarily from their ecosystem communities. Some of them can work as attractors, bringing new resources to the ecosystem community from the outside world. Of course, identifying those projects that create and nurture an ecosystem community is very important to understand long term trends in FOSS techologies.

Just as an example, when studying the ecosystem for a GNOME application, all the GNOME ecosystem has to be taken into account, because it will be relevant for the future of the project. For example, if basic GNOME libraries stop evolving, it is difficult that the application keep pace with puture needs.

From another point of view, the definition of the ecosystem, and therefore of the ecosystem community, is something that depend on the objectives of the evaluation. The ecosystem can be defined only for those projects with strong ties and great dependency, or for all those on which the project depends to some extent. The former case is the most usual, since dependencies and relationships are easy to perceive. But the latter can lead to important conclussions, such as when many projects discoverd that they were hit by the Heartbleed bug, deep in a software produced by a handful of developers, which was included in many, many very popular programs.

## Common techniques

In addition to the analysis of the sources of information detailed in the previous chapter, there are some techniques that can be applied, mainly to find out about the non-developer communities.

### Surveys and interviews

### Traces in collaboration systems

### Evaluation of documentation and third party studies

## Quantitative analysis

### Activity

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

#### Activity in source code management

Activity in source code management reflects how the project is in producing changes for the products they build. Source code management stores "commits", each of them being a change (or "patch") to the source code. Each change is different in nature, size, complexity, etc., which makes it difficult to compare individual changes. However, when we consider large collections of changes, trends become apparent.



#### Activity in code review and ticketing systems

#### Activity in communication systems


### Demography

### Time zones

### Time of collaboration

### Affiliation

