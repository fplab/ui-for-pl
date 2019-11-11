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

Interactive Debuggers
---------------------

Program Visualization
---------------------

**Program visualization** is the use of various techniques to enhance the human understanding of computer programs from distinct aspects including the structure of the source code and run-time behavior.

There are **program visualization** systems designed to aid significantly the practice of professional programming and software engineering as well as the learning of computer science by novice programmers. And it turns out that **program visualization** doesn't have to deal with toy programs, e.g., `Frappe - Visualizing Code Dependency Graphs <https://softvis.wordpress.com/2018/08/31/frappe-visualizing-code-dependency-graphs/>`_.

.. container:: bib-item

  .. bibliography:: live-programming.bib
    :filter: key == "price1993principled"

 Note that **program visualization** is different from **software visualization** in that the latter includes the visualization of a high-level description of algorithm or a piece of software which is in contrast to **program visualization** where actual implemented code is visualized.

.. container:: bib-item

  .. bibliography:: live-programming.bib
    :filter: key == "maletic2002task"

 This paper defines five dimensions, Tasks, Audience, Target, Representation and Medium to describe several software visualization systems that have very different features along those defined dimensions. By realigning taxonomies with the perspective of current software engineering problems, open research issues are identified. Additionally, the paper identifies the strengths of individual tools and the techniques they apply.

.. container:: bib-item

  .. bibliography:: live-programming.bib
    :filter: key == "sorva2013review"

 This paper serves as a survey of program visualization systems whose **task** is to aid the learning and teaching of introductory programming, with an intended **audience** of novice programmers and *CS1* teachers. Even a visualization that has been painstakingly crafted to be as lucid as possible may fail to aid learning in practice. Therefore, the paper introduces a new taxonomy to describe how program visualization systems engage learners.

.. container:: bib-item

  .. bibliography:: live-programming.bib
    :filter: key == "murphy2010interactive"

 **Code smells** are characteristics of software that indicate that code may have a design problem. The paper propose a novel smell detector, Stench Blossom, that provides an iteractive ambient visualization designed to first give programmers a quick, high-level overview of the smells, and then to help in understanding the smells if users wish. As a result, the experiment confirmed that programmers identify more smells and make more confident and informed refactoring jedgements using the tool than not using the tool.

.. container:: bib-item

  .. bibliography:: live-programming.bib
    :filter: key == "reiss2005paradox"

 This paper argues that most past and current work in the field is out of touch with the reality of software development and that new approaches and new ideas are needed.

.. container:: bib-item

  .. bibliography:: live-programming.bib
    :filter: key == "de2002visualizing"

 Jinsight is a tool for exploring a Java program's runtime behavior visually, featuring a collection of linked views.

  - a basic visualization of resource consumption in terms of classes, instances, and methods
  - a reference pattern view with extraneous detail eliminated that could detect memory leak
  - a performance analysis by visualizing event sequences

 With Jinsight, users have successfully diagnosed numerous problems on large commercial applications. However, the visualization is specialized for particular tasks and the visualized application could only run on a single *JVM*.

.. container:: bib-item

 .. bibliography:: live-programming.bib
   :filter: key == "goodall2010visual"

 This paper describes a system that brings together the results of disparate software analysis tools into a visual environment to support the triage and exploration of code vulnerabilities. The system could give more confidence that the detected vulnerabilities are not false positive by correlates and normalizes the output of multiple software analysis tools. And the user may also wish to associate the vulnerability with the programmer who regularly checks in the code with vulnerabilities or the main developer that modifiers more code than anyone else. This workflow allows the system to scale to large code bases with tens of thousands of vulnerabilities.

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

.. container:: hidden

  :cite:`price1993principled`
  :cite:`maletic2002task`
  :cite:`sorva2013review`
  :cite:`murphy2010interactive`
  :cite:`reiss2005paradox`
  :cite:`de2002visualizing`
  :cite:`goodall2010visual`
