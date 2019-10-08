.. :Authors: - Cyrus Omar

.. title:: Notation

Overview
========

Humans visually represent **mathematical structures** using **mathematical notation**.  
There can be many different notations for any given structure, and these notations can be compared along various cognitive dimensions. As such, **notation design** is a subfield of user interface design.

Mathematical notation is often defined informally, e.g. by example, rather than by specifying a formal syntax.
**Programs** are exceptional mathematical structures in this regard: they are typically governed by more formal specifications. The **abstract syntax** of a programming language specifies the formation rules for these structures. A **concrete syntax** formally specifies notation for these structures. Programming language specifications typically privilege a single concrete syntax, and it is common to refer to this as *the* concrete syntax of the language. 

History of Mathematical Notation
================================


.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'cajori1993history'

  This book provides a thorough historical account of mathematical notation, starting from antiquity. Notably, diagrammatic notation was evident in the earliest mathematical writing, e.g. in Euclid's *Elements*. Symbolic notation, in contrast, was relatively slow to evolve, arising mainly in the last several centuries. Before that, mathematical statements were written out in natural language. 

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'wolfram2000mathematical'

  `This article <https://www.stephenwolfram.com/publications/mathematical-notation-past-future/>`_ by Stephen Wolfram provides a more concise overview of the history of mathematical notation, and includes some discussion of notational choices in the Mathematica programming language.


Cognitive Dimensions of Notation
================================

Notations designed for consumption and manipulation by humans (as opposed to those where a machine is the intended consumer, e.g. bar codes) can be meaningfully compared along various *cognitive dimensions*. 

.. todo::

	Include some example cognitive dimensions, e.g. closeness of mapping and viscosity, here.

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'green1989cognitive'

  The original article by Green introduces the cognitive dimensions framework, which provides vocabulary that can be used to compare different designs. The emphasis is on the notation within a particular environment, e.g. an editor.


.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'blackwell2003notational' or key == 'blackwell2001cognitive'

  Subsequent papers have proposed a number of additional cognitive dimensions beyond those given as examples by Green. These two papers summarize both the original work and some of these subsequent developments.

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'pane1996usability'

  This detailed technical report defines a number of useful design dimensions. The focus is nominally on novice programming systems, but many of the dimensions are relevant beyond that domain.

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'iverson1987notation'

  Iverson's Turing Award lecture discussed notation, and programming languages more generally, as "tools for thought" and suggested a number of relevant cognitive dimensions.

.. todo::

  There has been a lot more work on cognitive dimensions. Include it either here, or in a new detail page?


Textual Notation
================

Most programming languages today specify a textual notation. In other words, programs are represented as text, a.k.a. strings,  consisting of a sequence of characters drawn from some suitable alphabet, typically ASCII or Unicode. It is typically desirable for there to be at most one structure for any given string. This property is known as *determinism*.

Parsing
-------

A parser is a function that takes an arbitrary string as input and returns a corresponding structure. If this is not possible, e.g. because there is no corresponding structure, then parsers exhibit various behaviors. In practice, they produce error messages that attempt to identify to a human where they may have made a syntax error. 

There is substantial literature on specifying *formal languages*, a term which refers specifically to string languages. A formal grammar is a specification of a formal language. It is quite common to define the  concrete syntax of a programming language by giving a formal grammar.

.. todo::

  How much detail do we want to go into about parsers and grammars and so on here?


Unparsing
---------
An unparser, a.k.a. a pretty printer, is a function that takes a structure as input and produces a corresponding string representation. Parsers are inverse to pretty printers. 

It is often the case that there are multiple valid string representations of a structure, e.g. because whitespace is ignored. Different pretty printers are therefore free to make different choices, often with the goal of generating a "pretty" output, i.e. one that follows typical secondary notational conventions around the use of whitespace.

.. todo::
  cite papers about pretty printing, secondary notation


Diagrams and Graphical Notation
===============================

Diagrammatic notation has been used to describe structures that arise in fields other than pure mathematics. Examples include `juggling notation <http://www.solipsys.co.uk/new/JugglingTalkSummary.html?JugglingTalk>`_, `knot notation <https://www.maths.ed.ac.uk/~v1ranick/papers/conway.pdf>`_ (see `Katherine Ye's Strange Loop 2015 talk <https://www.youtube.com/watch?v=Wahc9Ocka1g>`_), and `notation for kinetic sculptures <https://github.com/hypotext/notation#channa-horwitzs-sonakinetography>`_. These examples come from Katherine Ye's excellent notes on `notations and thought <https://github.com/hypotext/notation#notation-and-thought>`_, which contains a number of other examples, quotations, and musings on notation.

.. todo::

  Cite Katherine's work on generating diagrams from symbolic descriptions of structures.

Interactive Notation
====================

TODO: Graphite
TODO: Projectional Editors

Customizable Notation
=====================

Grab stuff from background section of Cyrus' PhD thesis

Programs construct and manipulate expressions of various types. Notation specific to a certain type of data is known as **literal notation** for that type. An instance of this notation is called a *literal*. For example, the concrete syntax of many programming languages defines list literals.  


.. container:: hidden

  :cite:`cajori1993history`
  :cite:`wolfram2000mathematical`
  :cite:`green1989cognitive`
  :cite:`blackwell2003notational`
  :cite:`blackwell2001cognitive`
  :cite:`pane1996usability`
  :cite:`iverson1987notation`
