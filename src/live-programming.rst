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
  them. (add another sentence about analysis of Alice and Whyline)

.. container:: bib-item

  .. bibliography:: debugging.bib
    :filter: key == 'latoza2010reachability'

  This paper introduced the concept and formalism of
  *reachability questions*: searches across feasible paths through a
  program for target statements matching search criteria.
  (add another sentence about user studies and prevalence of reachability questions)


.. container:: bib-item

  .. bibliography:: debugging.bib
    :filter: key == 'lawrance2013foraging'

  This paper provided a theory of programmer navigation when debugging
  based on information foraging theory.
  (add sentence elaborating on connection to ift)
  (add sentence about user study)
  (add sentence about providing first principled design guidelines for making interactive debuggers)



Interactive Debuggers
---------------------

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

(add description of program slicing as decomposition of programs)
(provide some overview of different types of program slicing, e.g., static vs dynamic)

.. container:: bib-item

  .. bibliography:: debugging.bib
    :filter: key == 'weiser1981slicing'

  This paper introduced program slicing.
  (add details about static slices)

.. container:: bib-item

  .. bibliography:: debugging.bib
    :filter: key == 'ko2008whyline'

  (describe connection to earlier work on debugging theory)
  (describe the tool and how it uses dynamic program slicing)
  (describe user study and result)

.. container:: bib-item

  .. bibliography:: debugging.bib
    :filter: key == 'latoza2011reacher'

  (describe connection to earlier work on reachability questions)
  (describe the tool)
  (describe user study and results)
  (should probably move this out of program slicing)

.. container:: bib-item

  .. bibliography:: debugging.bib
    :filter: key == 'perera2012explain'

  (static and dynamic program slicing for functional programs)
  (no implementation or evaluation)


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
to determine whether an ET node for a pure functional program is correct, the
programmer need only check that the return value of the corresponding, referentially
transparent expression is the expected one, independent of any other ET node.
On the other hand, checking the correctness of an ET node for an imperative program
requires checking, in addition to the return value, that values in the heap have
been updated correctly---this can be difficult to ascertain because the programmer
must maintain an understanding of how any *subsequent ET node* depends on those updated
values.

Despite their useful guarantee of bug diagnosis, algorithmic debuggers have yet to enter
widespread use. (add note about functional programming research lagging in tooling)

.. container:: bib-item

  .. bibliography:: debugging.bib
    :filter: key == 'nilsson1994lazy'

  This paper introduced the use of algorithmic debugging---originally developed
  for logic programs---for debugging lazy functional programs. (add sentence about
  how algorithmic debugging is useful when evaluation order doesn't matter)

.. container:: bib-item

  .. bibliography:: debugging.bib
    :filter: key == 'silva2006adps'

  This paper noted the complementary strengths of program slicing and algorithmic
  debugging and unified them in a common theoretical framework.

.. container:: bib-item

  .. bibliography:: debugging.bib
    :filter: key == 'caballero2017survey'

  This paper surveys the state-of-the-art in algorithmic debugging
  (add some example observations)
  (add observation about algorithmic debugging still not reaching mature
  implementations or wide audiences)


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

