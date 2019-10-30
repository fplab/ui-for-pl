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

Application Programming Interfaces (APIs) are a set of functions and procedures
that enable an application to access services or data from another source.
Examples include software libraries and frameworks, OS system calls, and web protocols.
APIs are a ubiquitous aspect of programming.
Almost every program written will use an API :cite:`myers2016improving`.

The goal of the API designer is to create an API that a broad range of
programmers can use for their applications.
This goal mirrors the goals of programming language designers --
an API designer must a create a service that is "usable" to
a broad and vaguely scoped audience.
Like languages, creating APIs is a challenging design problem of making
a complex service simple enough to be used
by users who may be are unaware of the inner workings of the API.

However, unlike language design, which may begin with a "bottom-up" approach,
designing APIs is often a problem of taking an already large and complex
system and simplifying it for a user.
This adds another layer of complexity in designing APIs.
To illustrate this diffulty:

    "The enormous size of public APIs contributes to these difficulties; for example, the Java Platform, Standard Edition API Specification includes more than 4,000 classes with more than 35,000 different methods, and Microsoft’s .NET Framework includes more than 140,000 classes, methods, properties, and fields."
    :cite:`myers2016improving`.


API Design Aspects
------------------

..
  Outline
  * Many aspects to design
  * Also tradeoffs between aspects.
    * Broad tradeoff - learnability and complexity
  * Paper: Improving API usability work
  * Paper: Automated measure paper
..

There are several design aspects to desiging usable APIs.
A broad aspect of usability identified by both :cite:`myers2016improving`
and :cite:`scheller2015automated` is the effect of *complexity* on usability.
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
  an automated method for measuring API usability, which they test in a user study.

User Studies
------------

..
  Outline
  * User study studying global usability of APIs very difficult, so many factors
  * Most user studies in API examine a specific aspect of api design and test it
  * Paper: Usability Implications of Requiring Parameters in Objects' Constructors
  * Paper: The Implications of Method Placement on API Learnability
..

Testing how to best design APIs is immensely difficult, as the numerous API design
decisions all affect the overall usability interdependently
:cite:`myers2016improving`. Testing the high-level and global design decisions
is often intractable because of this. Most user studies in API usability
examine a specific aspect of API design :cite:`stylos2007usability`
:cite:`stylos2008implications`.

.. container:: bib-item

  .. bibliography:: api-usability.bib
    :filter: key == 'stylos2007usability'

  This paper examines the impact of requiring parameters in
  objects' constructors on usability. The study in this paper showed that developers
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
  were orders of magnitudes faster in their tasks.

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

API usability can also be improved by creating better tools for understanding and searching through APIs -- improving API documentation
:cite:`stylos2009improving` :cite:`dekel2009improving` :cite:`stylos2006mica`.
Documentation represents another distinction of API design from language design.
The usage of APIs is so closely tied with using the API documentation that
the documentation can be considered part of the API.
A good documentation is integral in making an inherently complex API more learnable.

.. container:: bib-item

  .. bibliography:: api-usability.bib
    :filter: key == 'stylos2009improving'

  This paper presents Jadeite, a tool for improving API documentation by
  letting API users add "pretend" classes or methods in places where
  they expect a class or method to exist. This method helps alleviate
  the problem where classes or methods are located in unexpected locations
  :cite:`stylos2008implications`.

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

  This paper presents Mica, a tool for helping API users search through APIs.
  Mica is built on Google and analyzes the content of Google results to
  give more relevant results for programmers.

Program Comprehension
=====================

Domain-Specific Languages 
=========================
