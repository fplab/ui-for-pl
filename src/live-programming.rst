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

Game Development
----------------

Live Coding
===========

TODO: in music

Programmable Physical Environments
==================================

Overview
--------
A Programmable physical environment is an interactively programmable physical system that can sense and respond to the real world. Programmable physical environments are an active research area with many applications, including in education, manufacturing, internet of things, building architecture, biology, and virtual/augmented reality.

Motivation
----------
Programmable physical environments emphasize the physicality of programming: programmers interact with physical devices, and programs ultimately affect the physical world. Several authors have remarked on the need for a more expansive view of programming that accounts for and takes advantage of this physicality.

.. container:: bib-item

  .. bibliography:: programmable_PE.bib
    :filter: key == "bret2011rant"

  The author states that tools address human needs by amplifying human capabilities. Tools convert what people can do to what people want to do. However, most technologies for now focus more on what they can fit people's needs, but less on how they can fit people's capabilities.

.. container:: bib-item

  .. bibliography:: programmable_PE.bib
    :filter: key == "bret2014humanethought"

  The author holds the opinon that humans think not only through their sentences, like visual or auditory, but with their whole body.

This relates to the theory of embodied cognition.

.. container:: bib-item

  .. bibliography:: programmable_PE.bib
    :filter: key == "sep-embodied-cognition"

  Embodied cognition is the theory that many features of cognition are shaped by aspects of the entire body of the organism. The article gives a very detailed definition for embodied cognition and other related Philosophy fields.

In the term programmable physical environment, "environment" is one of the most important part to its definition. Based on the theory of embodied cognition, programmable physical environment should give more focus on interaction between people and the system. For the future design, how people will interact with the environment should be considered more carefully.


Applications
------------

In this section, we will list some applications of programmable physical environments.

Dynamicland
~~~~~~~~~~~

`Dynamicland <https://dynamicland.org>`_ is a research group that is inventing a new computational medium where people work together with real objects in the real world, not alone with virtual objects on screens.

The group does work rooted in the theory of embodied cognition. The computational media is derived from everyday things, like paper, which people can physically manipulate. These objects have computational meaning with the help of cameras, projectors and sensors on the ceiling. The idea is to make a whole room a computer.

.. container:: bib-item

  .. bibliography:: programmable_PE.bib
    :filter: key == "steve2018phenomenalworld"

  The author describes some of his experience with Dynamicland and gives an explanation on the idea of the research group.

One example of what people can do in Dynamicland is the following.

.. container:: bib-item

  .. bibliography:: programmable_PE.bib
    :filter: key == "omar2018geokit"

  The `Geokit` is a tool that users can use to build and interact with maps. These maps appear on physical pieces of paper.


Educational Use
~~~~~~~~~~~~~~~

One common application of programmable physical system is in the education field, especially for children. LEGO programmable brick is a tool that enable children to apply simple programs to LEGO bricks. The whole complicated programs are wrapped in a device and by working with instructions showed by the device, children, who usually don't have any knowledge of programming, can set some behaviours for LEGO bricks or motors.
Some research dig more about the programmable bricks and make more developments.

.. container:: bib-item

  .. bibliography:: programmable_PE2.bib
    :filter: key == "gindling1995lego"

  The paper presents an educational environment, LEGOsheets. It works with the prgrammable brick to provide a gentle introduction to programming and the design of mechanical artifacts.

Industrial Automation
~~~~~~~~~~~~~~~~~~~~~

The automation of industrial manufacture has a long history of development. In the 20th century, industrial automation was well advanced in two areas of manufacture, including homogeneous products and mass manufacture of discrete products. In old time, the industrial automation was still a kind of "hard" or "fixed" automation, which doesn't enable much flexibility.

.. container:: bib-item

  .. bibliography:: programmable_PE3.bib
    :filter: key == "nitzan1976industrial"

  The article gives an early idea of industrial automation. It also gives a classification on automation applied in industry.

.. container:: bib-item

  .. bibliography:: programmable_PE2.bib
    :filter: key == "saraswat1994factory"

  The paper presents a research on the development of concepts of a programmable factory and an altemative adaptable manufacturing systems approach to integrated circuit fabrication. The approach can offer more economical small or large scale production and higher flexibility to accommodate many products on several processes.

However, many physical machines are not or hard to be programmable in an industrial environment. Many of the machines still need traditional pre-programming methods to ensure stable functionalities. Making environments shared between humans and robots more programmable remains an area of ongoing and future research.

Internet of Things (IOT)
~~~~~~~~~~~~~~~~~~~~~~~~

A possible future is that computing will be ouside the realm of the traditional desktops. Many of the objects surrouding people's life will be on the network in certain form. There are more ways for people to have interaction with such a network of physical things. For now, there are many active research or application in the field of internet of things, inlcuding `IFTTT <https://ifttt.com/>`_ and `Zapier <https://zapier.com/>`_, tools that help people connect software and devices together, and intelligent virtual assistants, including `Alexa <https://www.alexa.com>`_ and `Siri <https://www.apple.com/siri/>`_ etc.

.. container:: bib-item

  .. bibliography:: programmable_PE2.bib
    :filter: key == "lee2015iot"

  The article gives the background of IOT and presents various technologies in different fields. It also evaluates the technology projects and illustrates how the real option approach can be applied for IoT investment. Finally it gives a discussion on the challenges of this field.

.. container:: bib-item

  .. bibliography:: programmable_PE3.bib
    :filter: key == "luigi2012socialiot"

  The article identifies appropriate policies for the establishment and the management of navigable social relationships between objects. It describes a possible architecture for the IOT that includes the functionalities required to integrate things into a social network.

An example of the interactive interface to IOT is the Echo Dot of Amazon, a kind of intelligent virtual assistants. Similar products in people's life include Siri, Assistant Cortana. Such intelligent virtual assistants can provide many functions for people's daily life. With connection to cloud database, they can compute various requests from people. Besides fetching data from cloud database, they can have control of other physical objects in the network. They serve as an interface to IOT and internet for people to interact with.

However, these virtual assistants are not very programmable. Though they can handle some immediate commands from people, they cannot deal with more complicated requests, for example, conditional instructions.

Though the intelligent virtual assistants give a good start to programmable IOT interfaces, there are worries about the security and privacy. There's still a long way for it to become a mature programmable physical environment.

.. container:: bib-item

  .. bibliography:: programmable_PE3.bib
    :filter: key == "chung2017alexa"

  The article describes some possible security problems for intelligent virtual assistants.

Another related research is about aggregate programmaing, which refers to program an aggregate of individual devices as a whole. It provides a way that simplifies the design, creation, and maintenance of complex IOT software systems. The main strategies include making implicit interaction between devices, composing geometric constructions, summarizing data and streaming to other regions, and generalizably constructions for space–time computing.

.. container:: bib-item

  .. bibliography:: programmable_PE3.bib
    :filter: key == "beal2015aggregate"

  The article describes advantages of aggregate programming in IOT field that simplifies the design, creation, and maintenance of complex IOT software systems. Aggregate programming makes the basic unit of computing a cooperating collection of devices instead of a single device. The article gives a detailed discussion on different dimensions of aggregate programming APIs applied to IOT.

Building Architecture
~~~~~~~~~~~~~~~~~~~~~

Traditionally, buildings and houses are designed to protect people from external threats, which requires the buildings to be solid and hard. However, this feature also makes the architecture hard to fit the dynamic demands of people to the space. One way to add flexibility to architectures is to turn them into programmable physical environment.

One example is `Squama`, a modular visiblity control of walls and windows for programmable physical architecture.

.. container:: bib-item

  .. bibliography:: programmable_PE.bib
    :filter: key == "rekimoto2012squama"

  The article presents a grid-like programmable wall and window, which can change transparency in modular way. It can enable people to configure the mask area on the surface to have control of certain resources in the real world. Squama can be used to hide confidential content in the room and control incident light from outside.


There are also applications in security of physical architecture. One example is a programmable wireless environment for physical layer security.

.. container:: bib-item

  .. bibliography:: programmable_PE2.bib
    :filter: key == "chen2019intelligent"

  The research team developed an intelligent reflecting surface. By adjusting the reflecting coefficient, the surface can send the incident electromagnetic wave to desired direction, which can improve the secrecy of information transport.

Biology
~~~~~~~

Programmable physical interfaces have also appeared in biology field. One example is the Body Integrated Programmable Joints Interface described in the following paper.

.. container:: bib-item

  .. bibliography:: programmable_PE2.bib
    :filter: key == "leigh2016biojoint"

  The project aims at building flexible physical interfaces that enable wearable devices to augment human capabilities. The paper presents a wrist-worn joints device that can suit to different tasks. Motions of the machine joints can be controlled with muscle signals, working as a direct extension of human body.

`Tangible Media group <http://tangible.media.mit.edu>`_, from MIT Media Lab, have designed many human-computer interactive systems, ans many of them are quite related to creating a programmable physical environment.

One example is the Programmable Droplets, where the group designed a surface with special material, and people can manipulate droplets efficiently with the help of the surface.

.. container:: bib-item

  .. bibliography:: programmable_PE3.bib
    :filter: key == "umapathi2018"

  Programmble Droplets is system that enables scientists to efficiently control the mixing of small droplets at a low cost.




  .. container:: hidden

    :cite:`sep-embodied-cognition`
    :cite:`bret2011rant`
    :cite:`bret2014humanethought`
    :cite:`omar2018geokit`
    :cite:`steve2018phenomenalworld`
    :cite:`umapathi2018`
    :cite:`rekimoto2012squama`
    :cite:`chen2019intelligent`
    :cite:`gindling1995lego`
    :cite:`leigh2016biojoint`
    :cite:`saraswat1994factory`
    :cite:`lee2015iot`
    :cite:`beal2015aggregate`
    :cite:`luigi2012socialiot`
    :cite:`nitzan1976industrial`
    :cite:`chung2017alexa`
