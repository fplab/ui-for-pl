.. :Authors: - Cyrus Omar

.. title:: Live Programming

Overview
========

TODO: Overview

Interleaving editing and execution

TODO: background, papers

REPLs
=====

Data Analysis Environments
==========================

Debugging
=========

  "The EDSAC was on the top floor of the building and the tape-punching
  and editing equipment one floor below... It was on one of my journeys
  between the EDSAC room and the punching equipment that...the realization
  came over me with full force that a good part of the remainder of my
  life was going to be spent in finding errors in my own programs."

  -- *Memoirs of a Computer Pioneer*, Maurice Wilkes

Much of the activity of programming involves **debugging**, i.e.,
diagnosing and preventing undesired program behavior.
Wilkes's early realization of this fact was echoed and amplified in a 2002
study of the U.S. software industry, which found that software engineers
spent an average of 70-80% of their time testing and debugging, with
the average bug taking 17.4 hours to fix.
Thus, debuggers form a crucial component of an effective programming system.
(needs better finish)

Software bugs manifest at three levels. Typically a bug is first
observed as a **runtime failure**, an instance of external program
behavior that does not comply with the intended design. Underlying
the runtime failure are **runtime faults**, aberrations
in machine or program state (e.g., a wrong value in a CPU register,
an uninitialized object) that lead to the noncompliant behavior.
Finally, causing the runtime faults are the **software errors** in
the source code.

Using these terms, debugging may be understood
more precisely as the collective processes of determining what runtime
faults led to a runtime failure, determining what software errors
led to those faults, and modifying the code to prevent the faults from
occurring. A **debugger** is a tool that allows the programmer to observe
the machine state during program execution, thereby making it possible to
identify runtime faults.

Theories of Human Debugging
---------------------------

Debugging is a complex activity. Recent work develops frameworks and
theories for understanding the cognitive processes underlying
programmer errors and debugging strategies, and the ways that
debugging interfaces influence those processes.

.. container:: bib-item

  .. bibliography:: debugging.bib
    :filter: key == 'ko2005framework'

  Noting the inadequacy of existing HCI frameworks at the time
  for analyzing error-prone processes like programming, this paper
  proposed a framework and methodology for analyzing and designing
  programming systems that focuses specifically on software errors.
  The framework deconstructs the various cognitive breakdowns that may
  occur throughout software development and characterizes software
  errors in terms of the *chains of cognitive breakdowns* that lead to
  them. Cognitive breakdowns are characterized, in turn, by their breakdown type,
  the action being performed by the programmer, the interface being
  used to perform the action, and the information being acted upon.
  For example, an interruption may cause a programmer to experience
  an inattention breakdown upon creating a loop header in their program
  editor and forget to include the closing brace, introducing a syntax
  error.
  The paper described the application of this methodology to
  evaluate the Alice programming environment by coding and quantifying
  users' common breakdown chains.
  The use of this framework directly inspired the design of new programming
  tools such as the Whyline :cite:`ko2008whyline`.

.. container:: bib-item

  .. bibliography:: debugging.bib
    :filter: key == 'lawrance2013foraging'

  Prior to this paper, theories of debugging relied on complex
  mental constructs and were
  mostly developed in an age in which programming environments were
  relatively simple. These theories did not take into account the substantial
  navigational activities performed in modern IDEs and offered little
  practical advice to builders of software engineering tools.
  This paper presented a theory of programmer navigation when debugging
  based on information foraging theory.
  Information foraging theory is an instance of rational analysis, a
  methodology for modeling cognitive processes as optimization functions
  over environmental and (minimally assumed) cognitive constraints---in
  particular, without reliance on hypothesized mental structures.
  This paper followed Sjøberg et al.'s theory-building process
  :cite:`sjoberg2008building`: it adapted the constructs of information
  foraging theory to programmer navigation during debugging; empirically
  investigated the circumstances in which the theory is applicable; and
  empirically evaluated the theory's predictive power.


Interactive Debuggers
---------------------

.. todo::
  describe history of transition from physical computing
  systems to observing core dumps
  to more interactive stepping and navigation, graphical
  projections of execution behavior onto source code, etc

Interactive Breakpoints
^^^^^^^^^^^^^^^^^^^^^^^
.. todo::
  bibliography on breakpoints

Time-Travel Debugging
^^^^^^^^^^^^^^^^^^^^^
.. todo::
  bibliography on time-travel debugging,
  distinguishing between record-replay and
  reversible/omniscient debugging

Program Slicing
^^^^^^^^^^^^^^^

**Program slicing** is a technique for computing, given some subset of a program's behavior,
the corresponding subset of the program that produces that behavior.
A **slicing criterion** specifies the target behavior; the corresponding program subset
is called a **program slice**.
For example, in the original formulation :cite:`weiser1981slicing`, Weiser defined a
slicing criterion as consisting of a program statement and a subset of program
variables; a program slice is an executable subset of the original program, obtained by
deleting program statements that do not affect the criterion variables' runtime
values at the criterion statement.

Since Weiser's introduction of program slicing, researchers have proposed many
variations and extensions. For example, whereas Weiser's notion of a program
slice is a **backwards** slice consisting of statements that may affect the
slicing criterion, a **forwards** slice consists of statements that may be
influenced by the slicing criterion.
Weiser focused on **static** slicing, which takes into account all possible
executions of the program, while other tools incorporate **dynamic** slicing,
which computes program slices with respect to a specific execution.
Additional variations are reviewed in :cite:`xu2005survey`.

.. container:: bib-item

  .. bibliography:: debugging.bib
    :filter: key == 'weiser1981slicing'

  This paper introduced the concept of program slicing.
  The specific proposed technique would now be categorized as static, backward slicing.
  In this work, the slicing criterion is a program statement and a subset of program
  variables; a program slice is an executable subset of the original program, obtained
  by deleting program statements that do not affect the criterion variables' runtime
  values at the criterion statement.
  The paper showed that the problem of computing minimal static slices is undecidable,
  but that approximate static slices can be found using data flow analysis.

.. container:: bib-item

  .. bibliography:: debugging.bib
    :filter: key == 'xu2005survey'

  This paper surveyed a wide variety of extensions and variations of program slicing
  that had been developed since Weiser first proposed the technique in 1981
  :cite:`weiser1981slicing`.


.. container:: bib-item

  .. bibliography:: debugging.bib
    :filter: key == 'ko2008whyline'

  This paper presented a new debugging interface for Java programs called Whyline.
  Unlike prior debugging interfaces---which typically require the user to select
  particular pieces of code of interest and, thus, require translation of questions
  into code queries---Whyline allows the user to select a "why did" or "why didn't"
  question about some program output and then generates an answer using dynamic,
  backward program slicing.
  The answer is presented as a visualization of the relevant execution slice,
  which the user can explore interactively, again by selecting "why did"
  and "why didn't" questions about runtime values.
  The paper described aspects of the Whyline's design and implementation---in
  particular, how the tool derives useful questions about program output.
  The authors noted that effective question generation was highly domain-dependent
  ---in this case, the program output was graphical.
  An evaluation of the Whyline on one task showed that novice programmers
  with Whyline were twice as fast as expert programmers without it.

.. container:: bib-item

  .. bibliography:: debugging.bib
    :filter: key == 'perera2012explain'

  This paper developed novel foundations and conceptual user interactions
  for dynamic, backward program slicing of higher-order functional programs.
  Prior slicing methods, primarily developed for imperative programs, were
  restricted to slicing at the granularity of variables---a poor fit for
  the complex values (e.g., higher-order functions, recursive data types)
  prevalent in the functional setting.
  In this work, given a program execution, a slicing criterion is a partial
  manifestation of the output value, in which only subvalues of interest
  are present and all others are replaced with holes;
  a program slice is a partial program expression, where
  subexpressions irrelevant to the criterion are replaced by holes.
  The paper also developed a corresponding notion of an execution slice---
  a tree-structured "unrolling" of the reduction steps leading to
  the specified partial value, where criterion-irrelevant nodes are
  are also replaced by holes.
  The paper presented algorithms for computing least program and trace
  slices, proved the algorithms correct, and presented a prototype
  implementation of these techniques as a tool called Slicer.
  Given a program execution and a slicing criterion, Slicer generates
  a visualization of the least program and execution slice.
  While these visualizations are static, the authors use them to sketch
  the concept of a novel interactive debugging interface, leaving
  the implementation and evaluation of such an interface to future work.

  .. note::
    The authors presented execution slicing as a novel concept, but variants
    had already appeared in prior work, e.g., slicing ARTs in
    :cite:`silva2006adps`, the execution slice visualization in WhyLine
    :cite:`ko2008whyline`.

Reachability Questions
^^^^^^^^^^^^^^^^^^^^^^

A *reachability question* is a search across feasible paths through a
program for target statements matching search criteria.
Common reachability questions are expressed as queries about statements
that can execute downstream/upstream from a particular origin/destination
program statement.
Program slicing may be viewed as an instance of a reachability question,
where the query is to return all control and data dependencies of some
statement.

.. container:: bib-item

  .. bibliography:: debugging.bib
    :filter: key == 'latoza2010reachability'

  This paper introduced the concept and formalism of reachability questions.
  It reported the results of three separate studies---a lab study of 13 developers,
  a survey of 460 developers, and a field study of 17 developers---and found that
  reachability questions are quite prevalent and often time consuming to answer.
  In the survey, developers reported asking questions that could be expressed as
  reachability questions more than 9 times a day. In the field study, the authors
  found that 9 of the 10 longest activities were associated with reachability
  questions.

.. container:: bib-item

  .. bibliography:: debugging.bib
    :filter: key == 'latoza2011reacher'

  Motivated by the results of :cite:`latoza2010reachability`, this paper presented
  a novel debugging tool called Reacher that directly supports asking and answering
  reachability questions. Upon user selection of an origin/destination statement,
  Reacher supports searching downstream/upstream along feasible control
  flow paths for statements matching user-specified criteria. Search results
  selected by the user are aggregated and visually displayed as a call graph.
  Users can interact with the call graph to navigate to corresponding source
  code and to iteratively refine the graph to display more details as needed.
  In a lab study with 12 participants, users with Reacher were over 5 times more successful
  completing their tasks in significantly less time than with an existing IDE.


Algorithmic Debugging
^^^^^^^^^^^^^^^^^^^^^

*Algorithmic debugging* (also called *declarative debugging*) is a semi-automatic
debugging technique in which the debugger automatically generates a series of
questions to which the programmer's answers guide the search toward the bug.
The debugger constructs an *execution tree* (ET), a data structure representing a
program execution, and traverses it using some search strategy, asking the
programmer at each ET node whether the represented subcomputation is correct
in order to determine the next step.
This technique guarantees that, if the programmer answers all the questions correctly,
the bug will eventually be found.

Although algorithmic debugging can be applied in any language paradigm, it is most
suited for declarative languages, e.g., pure functional languages.
To determine whether an ET node for a pure functional program is correct, the
programmer need only check that the return value of the corresponding, referentially
transparent expression is the expected one, independent of any other ET node.
On the other hand, checking the correctness of an ET node for an imperative program
requires checking, in addition to the return value, that values in the heap have
been updated correctly---this can be difficult to ascertain because the programmer
must maintain an understanding of how any *subsequent ET node* depends on those updated
values.

Despite their useful guarantee of bug diagnosis, algorithmic debuggers have yet to enter
widespread use.

.. container:: bib-item

  .. bibliography:: debugging.bib
    :filter: key == 'shapiro1982ad'

  Ehud Shapiro first developed algorithmic debugging for Prolog, a logic programming
  language, during his PhD research. His PhD thesis on the topic was
  selected as a 1982 ACM Distinguished Dissertation.

.. container:: bib-item

  .. bibliography:: debugging.bib
    :filter: key == 'nilsson1994lazy'

  This paper proposed algorithmic debugging techniques for lazy functional programs.
  Traditional debugging techniques are ill-suited for lazily evaluated programs
  because computations generally do not take place in the order one might expect
  from reading the source code, thus leading to difficulty orienting oneself in the
  the process of following program execution. Algorithmic debugging, on the other
  hand, allows the user to concentrate on the declarative semantics of a program,
  rather than its operational aspects such as evaluation order. While basic algorithmic
  debugging :cite:`shapiro1982ad` may readily be used for lazy functional languages,
  the prevalance of partially evaluated expressions during lazy evaluation makes
  the questions generated by the debugger difficult to comprehend and answer.
  This paper first identified this problem and proposed a solution that provides
  the user with a *strictified* view of the execution tree.

.. container:: bib-item

  .. bibliography:: debugging.bib
    :filter: key == 'silva2006adps'

  This paper combined program slicing and algorithmic debugging
  into a unified debugging framework for functional programs, adapting
  similar combinations applied to logic and imperative programs.
  The paper was motivated by the authors' observation that AD tools would produce
  long series of semantically loosely connected and, from the user's perspective,
  redundant questions.
  Program slicing provides a complementary remedy: rather than just 'correct'
  or 'incorrect',
  the user may provide a slicing criterion specifying which parts of the
  subcomputation's result are incorrect; the slicing criterion is used to prune
  the debugging tree of irrelevant subcomputations, leading to more semantically
  connected questions.
  The paper adapted program slicing concepts to the Augmented Redex Trail (ART), a
  trace structure that can be the basis for both AD and program slicing, and presented
  an algorithm for slicing ARTs.

  .. note::
    The debugging interface sketched in :cite:`perera2012explain` may be viewed
    as combining program slicing and algorithmic debugging.

.. container:: bib-item

  .. bibliography:: debugging.bib
    :filter: key == 'caballero2017survey'

  This paper surveyed the state-of-the-art in AD in
  2017, 35 years since the technique's conception.
  Motivating this survey was the authors' observation that, despite the many
  useful properties of AD, the technique has yet to be
  realized in a mature tool used in industry.
  In the first half, the survey reviews the general principles of AD and
  discusses the adaptation of these principles to various programming paradigms,
  including logic, functional, imperative, and object-oriented programming.
  In the second half, it takes a critical view and enumerates the historical
  issues that have prevented widespread adoption of AD.
  It notes, in addition to resource scalability challenges, several issues
  with the user experience of AD, including inflexible navigation of the
  debugging tree and difficult-to-answer generated questions.
  It then reviews a variety of proposed solutions to many of these issues,
  but also notes in a review of existing implementations that current
  tools remain largely sequestered within academia and do not integrate
  many known solutions.

Program Visualization
---------------------


Programming by Demonstration
============================

Direct Manipulation Programming
===============================

Graphical User Interface Design
-------------------------------

Game Development
----------------

Live Coding
===========

TODO: in music

Programmable Physical Environments
==================================

