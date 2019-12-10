.. :Authors: - Cyrus Omar, Yongwei Yuan

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

Program Comprehension
=====================

Software Visualization
----------------------

.. container:: bib-item

  .. bibliography:: language-usability.bib
    :filter: key == "price1993principled"

  The paper defines **software visualization** as the use of the crafts of typography, graphic design, animation, and cinematography with modern human-computer interaction technology to facilitate both the human understanding and effective use of computer software. This paper also gives a detailed "road map" of the work accomplished so far in **software visualization**, by identifying six broad categories of characteristics and by filling in the observed characteristics in each category.

  * Scope - what is the range of program that the SV system may take as input for visualization

  * Content - what subset of information about the software is visualized by the SV system

  * Form - what are the characteristics of the output of the system, i.e., the visualization

  * Method - what style of visualization specification is used

  * Interaction - how does the user of the SV system interact with and control it

.. container:: bib-item

  .. bibliography:: language-usability.bib
    :filter: key == "maletic2002task"

  Another paper revisits the definition of software visualization systems. By modeling the general way how the human perceives the mapping from data to a visual from, it defines five dimensions to describe several more recent software visualization systems that have very different features along those defined dimensions:

  * Tasks - *why* is the visualization needed?

  * Audience - *who* will use the visualization?

  * Target - *what* is the data source to represent?

  * Representation - *how* to represent it?

  * Medium - *where* to represent the visualization?

  By looking at the current software engineering problems along the given dimensions, open research issues are identified. The paper also discusses how cognitive psychology and information visualization can aid the design of software visualization. Additionally, the paper identifies the strengths of individual tools and the techniques they apply.

.. container:: bib-item

  .. bibliography:: language-usability2.bib
    :filter: key == "isohanni2014visualization"

  This paper studies by whom, how, why, and why not visualization is used in programming education by conduct a worldwide survey for over 250 teachers of programming. There is a trend that more visualization tools are used by teachers teaching teenagers. The topics where visualizations are used most often are basic programming and data structures. On the other hand, there are other reasons more related to teachers' preference, e.g. "I prefer to create my own visualization" or "I do not believe that visualizations are educationally effective in high-level programming courses". Especially noteworthy is that most often the visualization tool is used by the teacher, not the students, which should be taken into account in the future tool and material design and instructions on their usage.


.. container:: bib-item

  .. bibliography:: language-usability.bib
    :filter: key == "reiss2005paradox"

  This paper argues that most past and current work in the field is out of touch with the reality of software development and that new approaches and new ideas are needed. To be successful today or in the future, software visualization needs to address three kinds of reality.

  * the reality of understanding: Understanding involves design with specific problems that represent task-specific solutions.

  * the reality of software: Today's software are multi-threaded and heterogeneous.

  * the reality of programmer: Software developers want to do their development as quickly, as accurately, and as high quality as possible.

Algorithm Animation
^^^^^^^^^^^^^^^^^^^

**Algorithm animation** techniques aim to communicate the behavior of algorithms through animated visual notation, sometimes together with natural language commentary. It has been used with success in teaching computer science courses, designing and analyzing algorithms, producing technical drawings, tuning performance, and documenting programs.

.. container:: bib-item

  .. bibliography:: language-usability.bib
    :filter: key == "brown1991zeus"

  This paper presents a system for algorithm animation, *Zeus*. To a programmer, *Zeus* can be viewed as a general-purpose framework for associating multiple client-defined views with a set of client-defined events, emitted while an algorithm executes. According to the author, constructing animations in *Zeus* appears to be easy and straightforward. Particularly, object-oriented techniques make it easy to reuse views, and to build sophisticated views by composing and subclassing other views. However, those claims were not rigorously evaluated in the paper.

.. container:: bib-item

  .. bibliography:: language-usability.bib
    :filter: key == "stasko1993methodology"

  Instead of focusing on how to build an easy-to-use algorithm animation system, this paper discusses why we need different forms of visualization for different classes of algorithms, i.e. **application-specific** visualization, and specifically, what is the requirements for parallel program visualizations. Also, a program animation tool called POLKA is developed for case study. It is claimed that by taking advantage of such application-specific visualizations, programmers could rapidly assess the program's correctness, though without rigorous evaluation.

Program Visualization
^^^^^^^^^^^^^^^^^^^^^

**Program visualization** is the use of various techniques to help programmers comprehend computer programs. Program visualization techniques take into account various sources of information, including the structure of the source code and run-time behavior. Some program visualizations designed to aid significantly the practice of professional programming and software engineering, while others are focused on aiding the learning of computer science by novice programmers. Program visualization is different from algorithm visualization in that the latter focuses on the visualization of a high-level description of algorithm or a piece of software which is in contrast to program visualization where actual implemented code is visualized :cite:`price1993principled`.

.. container:: bib-item

  .. bibliography:: language-usability.bib
    :filter: key == "sorva2013review"

  This paper serves as a survey of program visualization systems whose **task** is to aid the learning and teaching of introductory programming, with an intended **audience** of novice programmers and *CS1* teachers. Even a visualization that has been painstakingly crafted to be as lucid as possible may fail to aid learning in practice. Therefore, the paper introduces a new taxonomy to describe how program visualization systems engage learners.

.. container:: bib-item

  .. bibliography:: language-usability.bib
    :filter: key == "murphy2010interactive"

  **Code smells** are characteristics of software that indicate that code may have a design problem. The paper propose a novel smell detector, Stench Blossom, that provides an iteractive ambient visualization designed to first give programmers a quick, high-level overview of the smells, and then to help in understanding the smells if users wish. As a result, the experiment confirmed that programmers identify more smells and make more confident and informed refactoring jedgements using the tool than not using the tool.

.. container:: bib-item

  .. bibliography:: language-usability.bib
    :filter: key == "de2002visualizing"

  Jinsight is a tool for exploring a Java program's runtime behavior visually, featuring a collection of linked views.

  - a basic visualization of resource consumption in terms of classes, instances, and methods
  - a reference pattern view with extraneous detail eliminated that could detect memory leak
  - a performance analysis by visualizing event sequences

  With Jinsight, users have successfully diagnosed numerous problems on large commercial applications. However, the visualization is specialized for particular tasks and the visualized application could only run on a single *JVM*.

.. container:: bib-item

 .. bibliography:: language-usability.bib
   :filter: key == "goodall2010visual"

 This paper describes a system that brings together the results of disparate software analysis tools into a visual environment to support the triage and exploration of code vulnerabilities. Note that it is an program visualization system because it actually visualizes the vulnerabilities information of a given program, though it takes advantage of other analysis tools. The system could give more confidence that the detected vulnerabilities are not false positive by correlating and normalizing the output of multiple software analysis tools. And also, as for some particular vulnerable code file, the system could figure out which programmer regularly checks in the file or who is the main developer that contribute the most. By choosing either heuristic approach, the user can associate the vulnerability with some programmer. This workflow allows the system to scale to large code bases with tens of thousands of vulnerabilities. However, the paper doesn't evaluate this prototype system at all.

.. container:: bib-item

  .. bibliography:: language-usability2.bib
    :filter: key == "david2016frappe"

  And it turns out that program visualization doesn't have to deal with toy programs. This video introduces a tool called Frappé. Code dependency of the codebase would be represented by a property graph including information of the code and data from different spaces like file system. By specifying queries in terms of the graph, the programmer could locate the code more accurately than traditional text-based searching.

TODO: maybe include more papers going over other data that could being visualized, i.e., increase the diversity of data sources

Domain-Specific Languages 
=========================

.. container:: hidden

  :cite:`brown1991zeus`
  :cite:`stasko1993methodology`
  :cite:`price1993principled`
  :cite:`maletic2002task`
  :cite:`sorva2013review`
  :cite:`murphy2010interactive`
  :cite:`reiss2005paradox`
  :cite:`de2002visualizing`
  :cite:`goodall2010visual`
  :cite:`david2016frappe`
  :cite:`isohanni2014visualization`
