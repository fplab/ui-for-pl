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


Programming by Demonstration
============================

Direct Manipulation Programming
===============================

Graphical User Interface Design
-------------------------------

User Interfaces for Game Development
====================================
.. :Authors: - Lei Zhang

Overview
--------
Starting with Spacewar in 1961, computer games have been around for over four and a half decades.
Computer games are becoming increasingly important in lots of industries including software development, entertainment, education, military, and medicine.
Game development itself has been considered as a combination of multiple disciplines including programming, design, art, modeling, animation, music, etc.

.. container:: bib-item

  .. bibliography:: game-development.bib
    :filter: key == 'blow2004game'

  This article presents a broad summary of the reasons why game development is hard nowadays.
  In a high level, the author classified the difficulties into two categories: problems due to overall project size and complexity and problems due to highly domain-specific requirements.
  Problems due to overall project size and complexity include the lack of excellent development tools, the inefficiency of development workflow, the barriers for multi-platform development, and the lack of excellent third-party components/engines.
  Problems due to highly domain-specific requirements include the domain-specific knowledge about programming, mathematics, algorithms, computer graphics, etc.

.. container:: bib-item

  .. bibliography:: game-development.bib
    :filter: key == 'washburn2016went'

  This paper presents an analysis of 155 postmortems published on the gaming site Gamasutra.com. 
  The paper identifies characteristics of game development, link the characteristics to positive and negative experiences in the postmortems and distill a set of best practices and pitfalls for game development.
  Based on the analysis, the authors made the following recommendations to game developers: First, be sure to practice good risk management techniques;
  Second, prescribe to an iterative development process and utilize prototypes as a method of proving features and concepts before committing them to the design;
  Third, do not be overly ambitious in the design.

As we can see in the above paper, there is a huge problem space in the game development domain including product (e.g. art, creativity, game design), development (e.g. tools, development process, team), resources (budge, hardware, publishers), and customer facing (e.g. marketing, feedback).
In this compendium, our scope covers only a tiny amount of the whole problem space (i.e. **tools** and **languages** for game development).

Professional Platforms for Game Development
-------------------------------------------------
In recent years, game engines such as Unity3D and Unreal Engine have been the most popular platforms for game development.
A game engine simplifies the task of the programmer by offering convenient abstractions for the hardware and operating systems on top of which the game runs.
Game engines also provides reusable components such as physics, game inputs, rendering, and Artificial Intelligence (AI).
Entity-component system and event-handling mechanism have been the major architecture of game engines nowadays.

.. container:: bib-item

  .. bibliography:: game-development.bib
    :filter: key == 'anderson2008case'

  This article presents a number of potential research topics with regard to the game engine development and architecture design.

.. container:: bib-item

  .. bibliography:: game-development.bib
    :filter: key == 'messaoudi2015dissecting'

  This paper dissected and analyzed the CPU and GPU performances of one of the most popular game engines, namely Unity3D.

.. container:: bib-item

  .. bibliography:: game-development.bib
    :filter: key == 'elvezio2018mercury'

  This paper presented a framework as an improvement for the existing game engine architecture.
  In 3D interactive systems that are developed using game engines, User Interface (UI) components are organized in a hierarchy that is used to propagate events among vertically connected components.
  However, programmers have to connect horizontal components manually and register/unregister events as needed in order to enable communications between those horizontal components.
  This paper introduced a messaging framework, Mercury, to facilitate communication among components.
  This framework simplifies message propagation for inter-component communication and provides support for UI management and sharing.

Non-imperative Programming Languages for Game Development
---------------------------------------------------------
Most game development platforms require highly domain-specific knowledge of imperative programming languages, which has a steep learning curve for end-users.
For example, Unity3D employs C# as its scripting language and Unreal Engine uses C++ as its scripting language.
In this subsection we examine Functional Reactive Programming as a declarative programming language in contrast to imperative programming languages.
We also introduce visual block-based programming languages and visual dataflow programming languages for game development.

.. container:: bib-item

  .. bibliography:: game-development.bib
    :filter: key == 'elliott1997functional'

  This paper introduced Fran, a functional reactive animation system which generated the paradigm called Functional Reactive Programming (FRP).
  The key ideas in functional reactive animation are its notions of *behaviors* and *events*.
  Behaviors are continuous, time-varying values.
  Events are values that occur at a single, discrete point in time, having no duration, such as a button press.

.. container:: bib-item

  .. bibliography:: game-development.bib
    :filter: key == 'maloney2010scratch'

  This paper introduced Scratch, a visual block-based programming environment that allows users to program animated stories and games.

.. container:: bib-item

  .. bibliography:: game-development.bib
    :filter: key == 'cooper2000alice'

  This paper introduced Alice, a 3D interactive animation environment.

.. todo::
    Cite Visual Scripting features from Unity and Unreal that use visual dataflow programming.

Game Description Languages
----------------------------------
Several attempts have been made in the past to model aspects of games and to encode game mechanics for analysis.

.. container:: bib-item

  .. bibliography:: game-development.bib
    :filter: key == 'ebner2013towards'

  This paper proposed to define the key requirements and challenges in constructing a new Video Game Description Language (VGDL).
  It proposed an initial design to the semantics of the language and the components required to define a given game.
  The core components required in order to represent a video game include map, objects, player definitions, avatars, physics, events, and rules.

.. container:: bib-item

  .. bibliography:: game-development.bib
    :filter: key == 'martens2015ceptre'

  This paper introduced Ceptre, a rule specification language to enable rapid prototyping for experimental game mechanics.
  Ceptre presents a correspondence between *gameplay* and *proof search* in linear logic.
  This methodology is proposed to help game designers and researchers in designing, analyzing, and debugging generative, multi-agent gameplay.

Game Development in Education
-------------------------------------------------
.. todo::
    Introduce game development in educational settings.

Live Coding
===========

TODO: in music

Programmable Physical Environments
==================================

