.. :Authors: - Cyrus Omar, Anthony Liu

.. title:: Language Usability

Overview
========

TODO: Overview

Language Adoption
=================

Usability of Type Systems
=========================

API Usability
=============

..
  Outline
  * APIs are ubiquitous
  * Examples
  * High level goals of API
  * Difficulty in achieving goals of API
  * Distinction with language usability
..

Application Programming Interfaces (APIs) are user interfaces that serve a dual role: they are simultaneously the user interfaces that programmers use to interact with software components and formal interfaces that govern interactions between different software components.
Examples include software libraries and frameworks, OS system call interfaces, and web protocols.
Nearly every program written will use an API :cite:`myers2016improving`.

The goal of the API designer is to create an API that other
programmers can use in their applications.
This goal mirrors the goals of programming language designers --
an API designer must create a service that is "usable" to
a vaguely scoped audience.
This scope of an audience may be broad or narrow, depending on whether the API is general, or domain specific.
Like languages, APIs must be simple enough to be used
by users who are unaware of the inner workings of the API, whether the audience is broad or narrow.

APIs differ from Programming Languages (PL) in that PLs are axiomatic: a language definition defines a universe of programs. APIs operate within a programming language by making use of its primitive operations as well as other APIs.

Individual APIs are often organized into frameworks. Some of these frameworks are extremely large, contributing to the difficulty of their design.
Microsoft’s .NET Framework includes more than 140,000 classes, methods, properties, and fields :cite:`myers2016improving`.


API Design Considerations
-------------------------

..
  Outline
  * Many aspects to design
  * Also tradeoffs between aspects.
    * Broad tradeoff - learnability and complexity
  * Paper: Improving API usability work
  * Paper: Automated measure paper
..

There are several design aspects to desiging usable APIs.
Myers et al. identify 6 key design aspects of API design, which we describe here :cite:`myers2016improving`:

* Learnability - an API user should be able to learn how to use an API as quickly and easily as possible.
* Productivity - an API user should be able use the API effectively to create their program.
* Error-Prevention - an API user should be able to handle and prevent error cases when their program is used.
* Simplicity - the design of the API should be simple.
* Consistency - the design of the API should be consistent.
* Matching Mental Models - the API user should have an accurate mental model of how the API executes procedures.

A broad aspect of usability identified by both :cite:`myers2016improving`
and :cite:`scheller2015automated` is the effect of *complexity* on usability -- the opposite of simplicity.
Changing the inherant complexity exhibits one of the many tradeoffs between design aspects of APIs.
Making an API more powerful (allowing a user to do more things with the API)
by increasing complexity decreases the learnability of the API.
However, increasing the learnability of an API by lowering the complexity also lowers the power of the API.

.. container:: bib-item

  .. bibliography:: api-usability.bib
    :filter: key == 'myers2016improving'

  This paper provides an overview of the design aspects of API design
  (Learnability, Productivity, Error-Prevention, Simplicity, Consistency, and Matching Mental Models)
  and the stakeholders (API designer, API user, and customer) involved with each design aspect.
  This paper provides a high level survey on human-centered methods for designing APIs,
  evaluating APIs, mitigating problems in APIs, and tools for improving API usability.

.. container:: bib-item

  .. bibliography:: api-usability.bib
    :filter: key == 'scheller2015automated'

  This paper identifies key aspects in API usability, in an *API Concepts Framework*,
  a structure where *concepts* represent possible user actions, leading
  to measureable properties on usability. Using this framework, the paper introduces
  an automated method for measuring API usability, by statistically inferencing usability
  from the measurable properties of APIs they identify, including number of methods in classes,
  number of method parameters, number of methods with similar names, etc.
  They test their method in a user study and
  find their calculated values highly correlated with user measured time.

User Studies
------------

..
  Outline
  * User study studying global usability of APIs very difficult, so many factors
  * Most user studies in API examine a specific aspect of api design and test it
  * Paper: Usability Implications of Requiring Parameters in Objects' Constructors
  * Paper: The Implications of Method Placement on API Learnability
..

Testing API design is difficult, as the numerous API design
decisions all affect the overall usability interdependently.
Testing the high-level and global design decisions
is often intractable because of this. Most user studies in API usability
examine a specific aspect of API design.

.. container:: bib-item

  .. bibliography:: api-usability.bib
    :filter: key == 'stylos2007usability'

  This paper examines the usability implications of class constructor parameters in Java.
  The study in this paper showed that developers
  strongly preferred and were more effective with APIs that did not
  require parameters in object constructors. This contradicted the
  belief that object constructor parameters would "self-document"
  themselves and guide developers to using the objects correctly.

.. container:: bib-item

  .. bibliography:: api-usability.bib
    :filter: key == 'stylos2008implications'

  This paper examines the impact of method placement on usability.
  In the user study participants were given nearly identical APIs but
  the comparison group contained a method that was placed in an
  unexpected location. Participants with "correctly-placed" methods
  were 2-11 times faster in their tasks.

.. container:: bib-item

  .. bibliography:: api-usability.bib
    :filter: key == 'ellis2007factory'

  This paper examines the usability of the factory design pattern.
  Participants were asked to complete tasks that either used a
  factory pattern constructor or plain constructor in a user study.
  Participants were found to be significiantly slower when programming
  in tasks with a factory pattern.

Documentation Improving Tools
-----------------------------

..
  Outline
  * API usability can also be improved by creating better tools for understanding and searching API's -- documentation
  * Another distinction with language design - documentation is part of API. Using API is using documentation
  * Paper: Jadeite
  * Paper: Improving API Documentation Usability with Knowledge Pushing
  * Paper: Mica: A Web-Search Tool for Finding API Components and Examples
..

API usability can also be improved by creating better tools for understanding and searching through APIs.
Documentation represents another distinction of API design from language design.
The usage of APIs is so closely tied with using the API documentation that
the documentation can be considered part of the API.
Good documentation is integral in making an inherently complex API more learnable.

.. :cite:`stylos2009improving` :cite:`dekel2009improving` :cite:`stylos2006mica`.

.. container:: bib-item

  .. bibliography:: api-usability.bib
    :filter: key == 'stylos2009improving'

  This paper presents Jadeite, a tool for improving API documentation.
  In many APIs, users often expect a class or method to be placed in a
  different location than actual, slowing them down :cite:`stylos2007usability`.
  Jadeite allows API users to add "placeholder" classes or methods in places where
  they expect a class or method to exist, which can redirect API users to
  the correct location.

.. container:: bib-item

  .. bibliography:: api-usability.bib
    :filter: key == 'dekel2009improving'

  API functions often contain messsages written about rules or caveats to usage.
  However, these messages can be lost in verbose text, and missed by the API
  user. This paper shows this phenomenon occurs in real programming, and
  shows how a function decorator can help alert users of such messages.

.. container:: bib-item

  .. bibliography:: api-usability.bib
    :filter: key == 'stylos2006mica'

  This paper examines how API users use web search as a tool for learning APIs
  and identifies innefficiencies in this process when web search shows irrelevant results.
  This paper presents Mica, a tool for helping API users find more relevant results on Google.
  Mica analyzes the content of Google results, directly shows API classes and methods,
  and makes other UI changes to make relevant results visible.

Program Comprehension
=====================

Domain-Specific Languages 
=========================
