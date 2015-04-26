# Kinds of evaluation, reasons to evaluate

There are several aspects of a FOSS project that can be evaluated. Depending on the reasons to evaluate, one or more of these aspects will be relevant. This chapter will review some of the kinds of evaluation that are usual, before entering in more detail in the following chapters in specific examples of these kinds of evaluation.

## Steps in evaluation

Most evaluation methods follow the following steps:

* Conduct a market research, to decide the subjects (products or projects) to evaluate.
* Define the evaluation criteria.
* Perform the actual evaluation, producing the evaluation results.

The first two can be preformed in any order, and both lead to the actual evaluation. In some cases, the process is iterative:

* some subjects are selected, and evaluated according to certain criteria
* based on the results, the criteria are refined, and the list of subjects redefined
* a new evaluation is performed, which leads to more precise criteria and subjects, until enough data for a final decision is obtained

### Market research

Before starting the actual evaluation, the set of subjects to evaluate must be defined. For that, an extensive research for potential subjects is needed. But this research is not only a matter of finding all options. It would be desiderable to find all the products or projects that could have the slightest possibility of being the most appropriate ones, but that is usually impractical. A more cost-effective approach is to perform an extensive market research, but then follow some criteria to produce a short list for evaluation.

Depending on the resources available for the evaluation, on how expensive that evaluation will be per subject, and on the expected benefits, the size of the this list can be shorter or longer.

In some cases the subjects are already decided beforehand, and this step is skipped. This happens, for example, when a community decides to evaluate itself, or when a company wants to evaluate the products on which they relay for a service they provide.

### Defining evaluation criteria

The evaluation criteria will determine the information to be obtained after the evaluation process. It is important to fit those criteria to the objectives of the evaluation. It is quite different, for example, to evaluate some products with the aim of selecting the most mature one, than the one with most perspectives of being improved for a long period.

Therefore, the evaluation criteria are tightly tied to the objectives of the evaluation, and it is necessary to make this relationship explicit. One way is to start by clearly stating the objectives, then map them to specific characteristics of the subject to evaluate, and finally define a procedure to evaluate those chatacteristics.

The mapping of objectives to characteristics is not easy, since it is not always obvious which characteristics will have a greater impact on the objectives. For example, if the objective is to select a project with a community easy to join, which characteristics would be evaluated? Maybe how long does it to newcomers to reach the core development team? Maybe how many contributions were performed by newcomers in the past? Maybe the details of formal policies encouraging the participation of newcomers? Or maybe the friendliness of conversations in mailing lists and forums in whcih necomers participate?

It is clear how for making this mapping of objectives to characteristics, we needed a model of how the latter lead to the former. Those can rante from informal, simple, rule of thumb models, to formal, theory-backed, and empirically-tested ones. In any case, we need some expertise on how characteristics of projects and products may influence the objectives.

The definition of procedures to evaluate the characteristicas can also be tricky. You need to know what can be evaluated, and how you can apply that knowledge to the characteristics of interest.

It is very rare that you just find the exact evaluation for your characteristic of choice. For example, how could you characterize expertise in a development community? At least two dimensions are involved: the individual expertise of individuals, and how that expertise permeates the community to be useful to newcomers. But both dimensions are difficult to evaluate, and you usually need to relay on proxies, such as how long have developers stayied in the community, and how experienced people collaborate with newcomers to solve issues and take decissions.

Because of all these reasons, it is a hard job to start from scratch when evaluating. It is much better if we can find an evaluation model that fits our needs, and we just map it to our specific objectives. A large part of this text will describe some existing models that you could find useful.

In addition, it is convenient to explain how these models can be produced in systematic way. For that we will introduce the goal-question-metric (GQM) method in a [later section](#sec:gqm). It will serve both as an illustration of how models can be produced, and as a tool to produce new models, if you need that. But you can use GQM not only to derive your own models, if you have the expertise and resources for that, but also to adapt existing ones to your specific environment. 

### Performing evaluation

Once the characteristics to evaluate are clear, and the methods to evaluate them too, you can start the actual evaluation. Depending on how you defined the evaluation methods, several actions may be performed, such as:

* Surveys, for example to know about perceived quality by users, or about effort estimation of their own work by developers. 
* Interviews with experts, for example to know about how mature a certain product is considered.
* Study of documentation, to learn about how a product interoperates with others, and to which extent that is described.
* Analysis of source code, to characterize some quality parameters.
* Analysis of messages in mailing lists, to characterize the flow of information in the project.
* Study of the project bylaws, to determine how formal decisions are taken.

These are just examples: many other actions are possible. But usually, we can classify their results in two cathegories:

* Qualitative evaluations. They produce a description of the quality of the evaluated characteristic.
* Quantitative evaluations. They produce a quantitative description of the evaluated characteristic. It can be for example a number, or a grade in a scale.

Qualitative evaluations can be converted into quantitative ones but using the descriptions to select from a scale of valuers. That allows for easier comparison, but usually some information is lost, the kind of shadows and details that qualitative descriptions provide.

Quantitative evaluations can be converted in qualitative by producing predetermined "factoids". That allows for easier interpretation, but it is convenient to remember that those are "syntetized" qualities: the underlying information is quantitative, and the derived factoids are just descriptions of those quantities.

NOTE: TODO. Example of both conversions

## Goal-question-metric
<a name="sec:gqm"></a>

The baseline rationale of the goal-question-matric GQM metric for deteriming the characteristics of subjects to evaluate, and how to evaluate them can be summarized as follows:

> "The Goal Question Metric (GQM) approach is based upon the assumption that for an organization to measure in a purposeful way it must first specify the goals for 
itself and its projects, then it must trace those goals to the data that are intended to define those 
goals operationally, and finally provide a framework for interpreting the data with respect to the stated goals."

> [The Goal Question Metric Approach](bib:basili-gqm).

In other words, you first have to state the goals of the evaluation. Then, you have to map those goals to characteristics of the subject of evaluation, and how they are going to be evaluated. Finally, you have to find out how to interpret the results of the evaluation with respect to the intended objectives.

Using the terms proposed by GQM, you have to define:

* Goals, at the conceptual level.
* Questions, at the operational level.
* Metrics, at the quantitative level.


## What is different in FOSS evaluation

Evaluation of FOSS products is different for the following reasons:

* The easy access to the product to evaluate.
* The quantity and quality of available information
* The importance of the community
* The competing market for deep support

### Access to the product

In the case of non-FOSS, the first barrier to evaluate is the access to the product. For FOSS, the evaluator is usually one download away from evaluating any FOSS product which is adequately packaged. For non-FOSS, just accessing may mean signing a contract, paying for a regular non-exclusive license, or obtaining a usually limited evaluation version.

This means that with FOSS, evaluating the real thing promplty, to any detail, withouth strings of any kind attached is much more simple.

### Available information

For FOSS products, not only the exectuable version of the software is availalble. Per definition, source code is available as well, which allows for its inspection, and the evaluation of aspects of quality that need access to it, such as code quality.

For some non-FOSS, source code may be available, either for all potential users or for those with a certain negotiation power. But it is a rare event.

In addition, if the development model is open, the development information for the FOSS product is kept avaible to anyone with the devloping community. Even when a single company drives the development of a FOSS product, they may decide to run all development in the open. When it is produced by a community, the rule is that the development information is available.

Therefore, the evaluation by third parties of the development processes is possible in the case of FOSS using open development models.

TBD: repositories where the information about development is available.

## Community

Development and user communities are usually key factors for FOSS products. Healthy development communities ensure the future survivability of the product even better than strong companies. Large, involved user communites ensure the needed pressure to keep the product in the leading edge.

Therefore, the evaluatilon of communities is of great importance in the case of FOSS.

## Competing market

The existence of a competing market, with many providers of in-depth support, independent of each other, is possible in the case of FOSS. In the case of non-FOSS, due to the strict control granted by maintaining all copyright rights, only companies in agreement with the producer can provide this kind of services, and therefore no real competing market exists.

TBD: importance of evaluating if such a competing market existis or not, and how it is.

## The importance of transparency

### The many facets of transparency

## Quantitative versus qualitative evaluation

## Criteria for evaluation

* Intangible factors
* Risk
* Functionality
* ...


## Evaluation of functionality

This is one of the more commons evaluations that are done when selecting tools, either to use or to integrate with others. Usually, this is done in the context of a product acquisition procedure, and considers mainly compliance with requirements, quality, and adaption to certain needs. The evaluation can be used to balance against cost, or to select among products that could fit the requirements.

Most of this evaluation is not different for FOSS and non-FOSS programas, except for the easy of access to the elements to evaluate: source code for the program (for assessing certain aspects of quality) and executable program.

## Evaluation of suitability

Example: OpenBRR

## Evaluation of quality

Example: QSOS, Qualoss

## Evaluation of maturity

Example: Polarsys Maturity Model

## Evaluation of community and development processes

Example: The Bitergia evaluation
