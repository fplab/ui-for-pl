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

Background
----------------------------

Accessibility in computing refers to the development and design of both software and hardware systems so as to be usable by people with disabilities. This includes screen readers for those with visual impairments and alternative input devices for those with motor impairments. Additionally, advances in computing technology over the previous decades have enabled richer communication for individuals with impairments. For example, augmentative and alternative communication (AAC) tools such as video calling or speech generating devices have improved for assisting individuals with impairments in producing or comprehending speech.
 
Although personal computers were first sold to the general public in the 1970s, the process of making this technology accessible began to become more common around 1990. For example, the IBM Screen Reader for DOS was created in 1986 (initially only for employees) :cite:`cooke`, and in 1995, Windows 95 became the first Windows OS to have built in accessibility features, rather than as add-ons :cite:`history, microsoft`. It’s also important to note that the Americans with Disabilities Act (ADA) was passed in 1990 :cite:`ada`.
 
Accessibility research also appeared around this time. Like many HCI topics, it first emerged from the field of human factors. In ‘Thirty-Something Million: Should They Be Exceptions?’, Vanderheiden highlights the need to consider individuals with impairments in product design and development :cite:`vanderheiden1990thirty`. Bergman and Johnson provide an overview of accessibility as it relates specifically to HCI :cite:`bergman1995towards`; Readers should refer to this work for an in-depth history.
 
Modern work has continued to explore design philosophies of accessible computing. Notably, in ‘Ability-Based Design: Concept, Principles and Examples’, Wobbrock et al. propose a shift in the frame of reference for thinking about accessible interfaces from disability to ability, and encourages designers to think about and adapt to what users can do :cite:`wobbrock2011ability`.  The authors present seven principles for this design approach: ability (focus on what users can do), accountability (change systems, not users), adaptation (interfaces match to users’ abilities), transparency (interfaces give awareness of adaptations), performance (systems may model user performance), context (systems may model the effects of different contexts), and commodity (systems may use low-cost, available hardware).
 
Visual Impairments
----------------------------
Many programming environments are not purely text based, and use layout, icons, color, and other visual indicators to communicate code structure and debug information; similarly programming courses often use diagrams to convey abstract concepts. Traditional screen readers may not convey all of this information to visually impaired developers :cite:`doustdar_2016`. Thus, prior research has analyzed typical behaviors of developers with visual impairments and has proposed systems to aid them in various tasks.
 
Behaviors of Blind Programmers
----------------------------
Mealin and Murphy-Hill conducted an exploratory study to understand the tools and practices that blind developers use and problems that they face while working :cite:`mealin2012exploratory`. They conducted qualitative interviews with eight developers with varying amounts of experience. All interviewees relied heavily on documentation in order to understand code structure and the functions available to them. Additionally, most of the participants used a temporary text file to store identifiers such as method or variable names for faster access. Participants also reported mixed success communicating with coworkers using visual diagrams; some translated them to text, while others reported that complex diagrams were often too abstract and were inaccessible. 
 
Armaly et al. conducted a study comparing reading behaviors between blind and sighted programmers :cite:`armaly2017comparison`. They asked 12 blind developers to read and summarize code, tracking their cursor and mouse movements, and compared the observed behaviors to a previous eye tracking study. They found that both groups prioritized reading method signatures, and that blind programmers returned to method signatures more often, highlighting the importance of readable function names.
 
Assistive Software for Blind Programmers
----------------------------
A variety of tools have been developed to improve upon the accessibility of programming languages and development environments in general. One example is CodeTalk, a programming environment that attempts to extend the benefits of fully-featured IDEs to visually impaired developers :cite:`codetalk`. CodeTalk offers a variety of features focusing on 3 areas: glanceability, navigability, and debugging. Features include quick ways to get context of the current cursor location, and auditory cues while debugging. CodeTalk was evaluated through a qualitative exploratory study and survey of six participants, and is currently available as an extension for Visual Studio. APL (Auditory Programming Language) is a programming language designed specifically for blind developers that uses both sound icons and text. Preliminary findings indicate that rich audio environments may better support blind developers mental models :cite:`sanchez2005blind`.
 
Additionally, prior research has explored task specific tools. StructJumper is an extension for Eclipse that creates a tree structure from code to help blind programmers navigate code :cite:`baker2015structjumper`. StructJumper was evaluated by 7 blind developers. Participants were asked to complete a series of tasks with and without the extension, and found that StructJumper allowed participants to complete tasks faster than without. Potluri et al. consider tools that could assist with the task of UI design :cite:`potluri2019ai`. The authors describe existing methods that blind and low-vision creators use to get a sense of UI aesthetics, including physical prototyping, and discuss the potential use of AI for assistance in this task, especially for higher-level features, such as color and general ‘look’.
 
Programming Education for Students with Visual Impairments
----------------------------
As previously mentioned, programming education often uses diagrams to represent abstract concepts, a barrier for visually impaired students. Stefik et al. present an educational infrastructure for blind and visually impaired middle and high school students that consists of Sodbeans, an auditory programming environment, Hop, a programming language, and a multi-sensory curriculum :cite:`stefik2011design`. They conducted an empirical study at a programming summer camp with 12 blind participants to evaluate their framework. Similarly, Blocks4All is a block-based, touchscreen programming environment :cite:`milne2018blocks4all`. The authors identify accessibility barriers, as well as appropriate touchscreen interactions.
 
Motor Impairments
----------------------------
Motor impairments also require input devices other than the traditional keyboard and mouse, which can be painful or impossible to use for some :cite:`saphra_2019`. Alternatives can include speech based interaction. For example, Begel and Graham evaluate a speech-based programming system called SPEED (SPEech EDitor) :cite:`begel2006assessment`.
 
Writing Accessible Software
----------------------------
Despite decades of accessibility research, a large proportion of software systems, websites, and mobile apps are not accessible to those that rely on screen readers or other accessibility technologies. Prior work has tried to educate developers on making use of accessibility APIs in a variety of ways, for example, in undergraduate courses :cite:`ludi2007introducing`, or through the creation of new standards :cite:`moreno2010toward`. Gonzalez and Reid propose an accessbility approach based on DOM structure that can be platform independent :cite:`gonzalez2005platform`.
