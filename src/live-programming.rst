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
Computer games have been around for over four and a half decades, starting with Spacewar in 1961.
Computer games are not just for fun. They are also being used for training and discovery in many areas including software development, entertainment, education, military, and medicine.
Game development involves multiple disciplines including programming, design, art, modeling, animation, and music.

.. container:: bib-item

  .. bibliography:: game-development.bib
    :filter: key == 'blow2004game'

  This article presents a broad summary of the reasons why game development is hard nowadays.
  At a high level, the author classified the difficulties into two categories: problems due to overall project size and complexity and problems due to highly domain-specific requirements.
  Problems due to overall project size and complexity include the lack of excellent development tools, the inefficiency of development workflow, the barriers for multi-platform development, and the lack of excellent third-party components/engines.
  Problems due to highly domain-specific knowledge requirements include the domain-specific knowledge about programming, mathematics, algorithms, and computer graphics.

.. container:: bib-item

  .. bibliography:: game-development.bib
    :filter: key == 'washburn2016went'

  This paper presents an analysis of 155 postmortems published on the gaming site Gamasutra.com. 
  The paper identifies characteristics of game development, links the characteristics to positive and negative experiences in the postmortems, and distills a set of best practices and pitfalls for game development.
  Based on the analysis, the authors made the following recommendations to game developers: (1) Be sure to practice good risk management techniques;
  (2) Prescribe to an iterative development process and utilize prototypes as a method of proving features and concepts before committing them to the design;
  (3) Do not be overly ambitious in the design.

As we can see in the above paper, there is a huge problem space in the game development domain including product (e.g. art, creativity, game design), development (e.g. tools, development process, team), resources (budget, hardware, publishers), and customer facing (e.g. marketing, feedback).
This compendium mainly covers **tools** and **languages** for game development.

Professional Platforms for Game Development
-------------------------------------------------
In recent years, game engines such as Unity3D and Unreal Engine have been the most popular platforms for game development.
A game engine simplifies the task of the programmer by offering convenient abstractions for the hardware and operating systems on top of which the game runs.
Game engines also provide reusable components such as physics, game inputs, rendering, and artificial intelligence (AI).
Entity-component-system (ECS) is an architectural pattern that is mostly used in game development, where every object in a game's scene is an entity (e.g. enemies, bullets, vehicles, etc.) and every entity consists of one or more components (implemented typically using structs, classes, or associative arrays) which add behavior or functionality.
Therefore the behavior of an entity can be changed at runtime by adding or removing components, which maximizes the reusability and interoperability of software modules.
ECS and event-handling mechanisms have been a fundamental feature of the software architecture of modern game engines.

.. container:: bib-item

  .. bibliography:: game-development.bib
    :filter: key == 'anderson2008case'

  While available research has mainly focused on game engine subsystems such as rendering and AI, the issues regarding the overall architecture design of game engines have received less coverage.
  This article, in response, presents a number of key aspects and potential research topics with regard to the architecture design of game engines.
  These topics include the establishment of a unified language of game development, the identification of software components that are common to many types of computer games, the definition of the role of content creation tools in the game development process and as part of game engines, and many others.

.. container:: bib-item

  .. bibliography:: game-development.bib
    :filter: key == 'elvezio2018mercury'

  This paper presents a framework as an improvement for the existing game engine architecture.
  In 3D interactive systems that are developed using game engines, User Interface (UI) components are organized in a hierarchy that is used to propagate events among vertically connected components.
  However, programmers have to connect horizontal components manually and register/unregister events as needed in order to enable communications between those horizontal components.
  This paper introduces a messaging framework, Mercury, to facilitate communication among components.
  This framework simplifies message propagation for inter-component communication for UIs in a structured way.

Declarative Programming Languages for Game Development
---------------------------------------------------------
Most game development platforms require highly domain-specific knowledge of imperative programming languages, which has a steep learning curve for end-users.
For example, Unity3D employs C# as its native language and Unreal Engine uses C++ as its native language.
In this section we examine Functional Reactive Programming, visual block-based programming languages, and visual dataflow programming languages for game development.

.. container:: bib-item

  .. bibliography:: game-development.bib
    :filter: key == 'elliott1997functional'

  This paper introduces Fran, a functional reactive animation system which introduced the paradigm called Functional Reactive Programming (FRP).
  FRP is a general framework for programming hybrid systems in a high-level, declarative manner.
  The key ideas in functional reactive animation are its notions of *behaviors* and *events*.
  Behaviors are continuous, time-varying values such as numbers and colors.
  Events are values that occur at a single, discrete point in time, having no duration, such as a button press.
  FRP aims to automate the low-level implementation details by providing the user high-level abstractions, which prevent them from having to explicitly manage common implementation chores that has nothing to do with the content of an animation.
  The concept of FRP has been proven to be viable in not only game development, but also data visualization and web development.

.. container:: bib-item

  .. bibliography:: game-development.bib
    :filter: key == 'cleary2015reactive'

  This paper presents the experience of using FRP to deliver a summer camp for students in grades 8 through 12.
  The authors used a system based on a declarative programming approach to allow students without a background in computing to explore a wide variety of subject material within a 3D virtual environment, including computer science, mathematics, physics, and art.
  The students experienced building 3D virtual worlds using the Panda3D game engin and an external FRP Python library called PyFRP.
  Using a series of topic examples, the paper demonstrates that FRP's declarative nature makes creating interactions and animations quick and painless and that FRP can be used to teach a variety of subjects.
  The paper also proves the feasibility of integrating the concept of FRP into game engines. 

.. container:: bib-item

  .. bibliography:: game-development.bib
    :filter: key == 'maloney2010scratch'

  This paper introduced Scratch, a visual block-based programming environment that allows users to program animated stories and games.
  Users can import or create images and sounds within the editor.
  Programming is done by dragging and snapping together colorful command blocks to control 2D graphical objects called sprites moving on a background called the stage.
  This paper also describes aspects of Scratch and the language design that make it easier for young people to explore, express themselves, and learn.

.. container:: bib-item

  .. bibliography:: game-development.bib
    :filter: key == 'blueprints'

  The Blueprints Visual Scripting system in Unreal Engine is a gameplay scripting system that uses the concept of dataflow programming to compose game elements from within the Unreal Editor.
  Users can use simple drag-and-drop operations to draw connections between nodes on the interface without writing code.
  The system is used to define object-oriented (OO) classes and objects in the engine.
  Specifically, Blueprints can handle extending classes, storing and modifying default properties, and managing components instancing for classes.


Game Description Languages
----------------------------------
Game description languages seek to express components expected in the state of a game, and the rules that induce transitions, resulting in a state-action space.
Such languages have the potential of enabling automatic game generation and offer opportunities to formalize the knowledge involved in game design and test game design theories.
Several attempts have been made in the past to model aspects of games and to encode game mechanics for analysis.

.. container:: bib-item

  .. bibliography:: game-development.bib
    :filter: key == 'ebner2013towards'

  This paper discusses the key requirements and challenges in constructing a new Video Game Description Language (VGDL).
  It proposed an initial design of the semantics of the language and the components required to define a given game.
  The core components required in order to represent a video game include map, objects, player definitions, avatars, physics, events, and rules.

.. container:: bib-item

  .. bibliography:: game-development.bib
    :filter: key == 'martens2015ceptre'

  This paper introduces Ceptre, a rule specification language to enable rapid prototyping for experimental game mechanics.
  Ceptre presents a correspondence between *gameplay* and *proof search* in linear logic.
  This methodology is proposed to help game designers and researchers in designing, analyzing, and debugging generative, multi-agent gameplay.

Game Development in Education
-------------------------------------------------
Researchers have explored how game development environments can teach computational concepts and broaden interest in computing amongst students in K-12 and university settings.

.. container:: bib-item

  .. bibliography:: game-development.bib
    :filter: key == 'werner2012children'

  This paper describes a semester-long game-programming course where 325 middle school students used Alice to make games.
  The authors aim to discover the CS concepts that are accessible with Alice programming contructs, the common programming constructs that are used by middle school students making games without required game specifications, and the programming constructs that are used successfully.
  They measured the frequency of successful execution of programming contructs based on an analysis of 231 final games.
  The results show that many games exhibit successful uses of high level computer science concepts such as student-created abstractions and modeling, concurrent execution, and event handlers.
  The most common constructs were methods, functions, and events.
  Surprisingly, there were few differences between the use and successful use of constructs, suggesting that if something was in the program, it was generally used correctly.

.. container:: bib-item

  .. bibliography:: game-development.bib
    :filter: key == 'kelleher2007storytelling'

  This paper introduces Storytelling Alice, a programming environment that introduces middle school girls to computer programming as a means to creating 3D animated stories.
  Alice is a visual block-based programming environment that makes it easy to create 3D animation or program simple games in 3D.
  Storytelling Alice provides supports for story creation including 1) a set of high-level animations, 2) a collection of 3D characters and scenery designed to spark story ideas, and 3) a tutorial that introduces users to writing.
  This paper presents a study comparing girls' experiences learning to program using Storytelling Alice and Generic Alice, a version of Alice without storytelling support.
  A total of 88 girls from local Girl Scout troops participated in the evaluation (45 assigned to Generic Alice and 42 assigned to Storytelling Alice).
  Users of Storytelling Alice were found more motivated to program; they spent 42% more time programming, were more than 3 times as likely to sneak extra time to work on their programs.

Live Coding
===========

TODO: in music

Programmable Physical Environments
==================================

