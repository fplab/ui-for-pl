.. :Authors: - Cyrus Omar

.. title:: Program Editors

Overview
========

TODO: Overview

Language Servers
================

TODO: OCaml language server paper, others

Structure Editors
=================

TODO: historical examples, studies, etc.

Visual Programming Languages
----------------------------

TODO: examples, cognitive dimensions studies, etc.

Visual DataFlow Programming
---------------------------

Overview
~~~~~~~~

Dataflow programming is a programming paradigm that models a program as a directed graph of the data flowing between operations, thus implementing dataflow principles and architecture.
Dataflow programming which was written in textual editors has been around since the 1970s but visual dataflow programming didn't become popular until the 1990s when reasonably priced workstations became powerful enough to run 
visual editors. The pure dataflow model basically contains 4 essential parts: node (unit of computation), arc (data dependency), token (unit of data), port (node/arc juncture). The fundamental process is that: the node take one or 
more inputs (global variable is disallowed) and produces one or more outputs. And the most important part of the model is the arc which can express data dependencies among nodes.

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'dfl2012'

This article mainly introduce the basic concepts of DataFlow Programming in terms of a research topic of Software Engineering. The difference with traditional Von Neumann model has also been mentioned and the importance of DFP as the 
core to most visual programming languages indent to provide end-user programming.


Motivations
~~~~~~~~~~~

In terms of the editing aspects of visual dataflow languages, usability improvement is what we most care about since that's where the programming efficiency increases. By applying Cognitive Dimensions framework to evaluate the visual 
dataflow language tools like LabVIEW, it is obvious that visual dataflow programming language has a higher usability than tradional programming languages, espeically for end users with limited understanding of programming. Another point 
that programmers / researchers feel excited about visual dataflow programming is that the execution sequence of a data flow program is not determined by a program counter taking through an ordered series of instructions as we would have 
in Von Neumann style program but is instead contingent upon data dependencies becoming satisfied, which actually allows automatic parallelism to become realizable without traditional multi-threaded programming techniques.

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'vpl1996usability'

This article introduces the ‘Cognitive Dimensions’ Framework technique to evaluate the usability of Visual Programming Environments. The researched tools are LabVIEW and Prograph.

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'dpl2014compiler'

This article illustrate how a compiler framework can enable the implementation of a stream system called COStream which is based on the dataflow programming paradigm that improves programming productivity.

Applications
~~~~~~~~~~~~

LabVIEW
^^^^^^^

LabVIEW (Laboratory Virtual Instrument Engineering Workbench) is a system-design platform and development environment for a visual programming language designed by National Instruments based on visual data-flow language paradigm.
LabVIEW followed the convention of a box-line structure and enriched it with constructs for conditionals, loops and sequences. And different types of lines represent different types of data (numbers, booleans, strings, arrays ...) 
flowing among boxes. The operators provided perfectly covered almost all needs to construct a virtual electronic instrument operating in real time but make considerably less coverage provision for other domains of computing.
Besides the usability, LabVIEW has been keeping a great contribution on researches about cognitive effects of visual programming representations.

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'vp2001labview'

This article reports the results of an exploratory survey of experienced LabVIEW
users, a main goal being to learn how LabVIEW programmers think that the visual
representation of LabVIEW affects their programming.

Prograph
^^^^^^^^

Prograph is a visual data flow and object-orientated language marketed by TGS Systems.
The architecture comprises methods (subroutines) represented
as icons and connected by the usual lines, carrying data objects from top to bottom of
the screen. A method browser is used to browse methods and cases displayed in a seperate window.
The dataflow lines cannot contain bends but can be placed diagonally which is different from LabVIEW.

Luna
^^^^

Luna is a textual and visual functional programming language, which provides a data processing and visualization environment which is able to immediately 
connect programmers to what they are building. Instead of being hard coded, components in Luna are simply nested and editable data flow graphs which allows immersive programming experience.


others
^^^^^^

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'gui2017vpl'

This article introduced a very interesting invention based on visual dataflow programming paradigm. The invention is about method for adapting GUI-based instrument components in a visual dataflow programming language.

Drawbacks
~~~~~~~~~

Scale issue
^^^^^^^^^^^

Given the fact that visual representations of programming languages can usually manifest as much detail of a program as possible, a new concern will automatically arise when one is trying to program in a large scale using 
a visual data flow programming language, when dataflows become very complex and hierarchical.

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'vp2017lvss'

This article describes a visual programming environment
that we are extending toward a visual software engineering
envimnment by explicitly providing mechanisms to address
the issues of in "visual programming-in-the-large."

Data Transfer problem
^^^^^^^^^^^^^^^^^^^^^

Since dataflow programming heavily depends on the capability of compiler to both parse the graphical notation and generate corresponding machine code. However, the optimization is required to enable the compiler process, 
especailly for multi-threaded cases. The overhead of data tranfer either from node to node or from core to core is the killer of system efficiency.

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'co2017adt'

This article introduced the current obstacles and potential approaches in terms of analysis and schedule data transfer.


Program Navigation
==================

TODO: code bubbles and related work

Collaborative Editing
=====================

TODO: Thomas' papers, and other related work

TODO: work on operational transforms, CRDTs, and other techniques

TODO: work on version control systems

Accessibility
=============

TODO: accessibility-related discussion


.. container:: hidden

  :cite:`dfl2012`
  :cite:`vpl1996usability`
  :cite:`dpl2014compiler`
  :cite:`vp2001labview`
  :cite:`gui2017vpl`
  :cite:`co2017adt`
  :cite:`vp2017lvss`
