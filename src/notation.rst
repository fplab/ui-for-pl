.. :Authors: - Cyrus Omar, Yongwei Yuan

.. title:: Notation

Overview
========

Humans visually represent **mathematical structures** using **mathematical notation**.  
There can be many different notations for any given structure, and these notations can be compared along various cognitive dimensions. As such, **notation design** is a subfield of user interface design.

Mathematical notation is often defined informally, e.g. by example, rather than by specifying a formal syntax.
**Programs** are exceptional mathematical structures in this regard: they are typically governed by more rigorous specifications. The **abstract syntax** (a.k.a. **structural syntax**) of a programming language specifies the formation rules for these structures. A **concrete syntax** (a.k.a. **surface syntax**) formally specifies a notation for these structures. Programming language specifications typically privilege a single concrete syntax, and it is common in practice to refer to this as *the* concrete syntax of the language. 

Programs construct and manipulate expressions of various types. Notation specific to a certain type of data is known as **literal notation** for that type. An instance of this notation is called a *literal*. For example, the concrete syntax of many programming languages allows for list literals like ``[1, 2, 3]``.

History of Mathematical Notation
================================

Diagrammatic notation was evident in the earliest mathematical writing, e.g. in Euclid's *Elements*. Symbolic notation, in contrast, was relatively slow to evolve, arising mainly in the last several centuries. Before that, mathematical statements were written out in natural language.

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'cajori1993history'

  This book provides a thorough historical account of mathematical notation, starting from antiquity.

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'wolfram2000mathematical'

  `This article <https://www.stephenwolfram.com/publications/mathematical-notation-past-future/>`_ provides a more concise overview of the history of mathematical notation, and includes some discussion of notational choices in the Mathematica programming language.


Cognitive Dimensions of Notation
================================

Notations designed for consumption and manipulation by humans (as opposed to those where a machine is the only intended consumer, e.g. bar codes) can be meaningfully compared along various *cognitive dimensions*. Examples include *diffuseness* (the amount of space that the notation takes up) and *role-expressiveness* (the extent to which the purpose of a notational entity is readily apparent) :cite:`blackwell2001cognitive`. To properly perform a  cognitive dimensions analysis, one needs to specify an appropriately specific context (e.g. by specifying who the intended user is, and the affordances available in the editing environment). Because cognitive dimensions involve cognitive operations, cognitive dimensions analyses are typically qualitative in nature, though in some cases a quantitative metric can also be relevant.

.. note::
  In much of the literature on cognitive dimensions of notation, the word "notation" is used liberally -- researchers will analyze a full language or system design rather than focusing strictly on visual representations.


.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'iverson1987notation'

  Iverson's Turing Award lecture discussed various "important characteristics of notation", and identified programming languages as powerful "tools for thought".

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'green1989cognitive'

  Green introduced the "cognitive dimensions" framework, which provides vocabulary that can be used to compare different designs. The emphasis is on the notation within a particular environment, e.g. an editor.


.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'blackwell2001cognitive' or key == 'blackwell2003notational'

  Subsequent papers have proposed a number of additional cognitive dimensions beyond those given as examples by Green. These two papers summarize both the original work and some of these subsequent developments.

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'pane1996usability'

  This detailed technical report defines a number of useful dimensions. The focus is nominally on novice programming systems, but many of the dimensions are relevant beyond that domain.

.. todo::

  A more thorough bibliography covering cognitive dimensions analysis might be useful as a subpage.

Secondary Notation
==================
Additional cues are often systematically inserted when editing or rendering notation in order to improve readability and other cognitive dimensions. These additional cues are called *secondary notation* if they are formally redundant. 

For example, a human might insert formally unnecessary indentation to better communicate nested scopes to human readers, place conceptually related items near each other, or include natural language comments. 

A **pretty printer** is a function that takes a structure as input and generates a visual representation of it suitable for human consumption, using both primary and secondary notation. A program editor or pretty printer might use syntax highlighting and typography to communicate structural or semantic information.

.. note::
  If, for example, indentation is required (as in Python) or color is used to communicate information not available by any other means, then these cues are not secondary notation, but rather part of the primary notation. However, these notational design choices are typically motivated by many of the same cognitive considerations as secondary notation.

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'petre1995looking'

  This paper introduces the phrase "secondary notation" and discusses, by way of examples, how important and subtle notation design can be.

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == "petre2006cognitive"

  This paper reflects on cognitive dimensions theory as a whole and, in particular, states, based on observations made in other studies, that experts are more adept at using secondary notation than novices.

.. container:: bib-item

  .. bibliography:: notation2.bib
    :filter: key == "brown1992color"

 This paper focuses on the use of color and sound in **algorithm animation** systems by evaluating their previous work, *Zeus*, a system for algorithm animation and multi-view editing. Color has been used in *Zeus*, for the purpose of encoding the state of data structures, tying views together, highlighting activity, emphasizing patterns, and making history visible. In addition, sound has been used to reinforce visual views, convey patterns, replaces visual views and signals exceptional conditions. For instance, a sound effects "visualization" produces a tone whose pitch rises with the number of active threads. See :ref:`language-usability:Algorithm Animation` for more details about *Zeus* and other algorithm animation systems.

Textual Notation
================

Most programming languages today specify a textual notation. In other words, programs are represented and edited as text, a.k.a. strings, consisting of a sequence of characters drawn from some suitable alphabet, typically ASCII or Unicode. It is typically desirable for there to be at most one structure for any given string. This property of a syntax is known as *determinism*.

Parsers
-------

A parser is a function that takes an arbitrary string as input and returns a corresponding structure. If this is not possible, e.g. because there is no corresponding structure, then parsers exhibit various behaviors. In practice, they produce error messages that attempt to identify to a human where they may have made a syntax error.

Parser Generators
~~~~~~~~~~~~~~~~~

Parsers are sometimes written by hand (a.k.a. "hand-rolled"). More commonly, however, they are generated programmatically. For example, a *parser generator* generates a parser given a formal grammar equipped with logic for each production that generates the corresponding structure. Another method is to use a *parser combinator* library, which generates a parser by executing a program that applies various functions to define parts of the parser and then combine them.

.. todo::

  Is there a good survey or book on parsers and parser generators? Someone's thesis might have a good survey on the topic in it? Does someone want to make a subpage on the topic of parsers and parser generators?

Syntax Errors
~~~~~~~~~~~~~
.. todo::
  Summarize the literature on syntax errors.

Unparsers
---------
An unparser is a function that takes a structure as input and produces a string representation which, if parsed, will produce the original structure (or in some cases one merely equivalent to it, for some suitable notion of equivalence).  

It is often the case that there are multiple valid string representations of a structure, e.g. because whitespace might be ignored. Different unparsers are therefore free to make different choices within this space. 

Some unparsers are pretty printers: they will choose a "pretty" string representation, e.g. one that follows secondary notational conventions about the use of whitespace. 

.. container:: bib-item

  .. bibliography:: notation2.bib
    :filter: key == "hughes95"

  This paper introduces the basic mechanisms behind many textual pretty printer libraries.

.. container:: bib-item

  .. bibliography:: notation2.bib
    :filter: key == "wadler2003prettier"

  This paper refines Hughes' design.

.. container:: bib-item

  .. bibliography:: notation2.bib
    :filter: key == "bernardy17"

  This paper further improves on Hughes' and Wadler's designs, specifying a number of design criteria explicitly and supporting more flexible alignment specifications.

Not all unparsers are pretty printers. An unparser's goal may simply be to minimize the size of the resulting string representation, or to intentionally obfuscate the code.

Diagrams and Graphical Notation
===============================

Mathematical notation is often non-textual. For example, it is common to lay out fractions vertically, or to use square root notation that requires placing a line over a sub-expression.
In other cases, mathematical notation is even more overtly diagrammatic or graphical. For example, matrix notation lays out sub-expressions in a grid. Set intersection is diagrammed using overlapping circles.

Diagrammatic notation is also used to represent structures that arise in fields other than pure mathematics. Examples include `juggling notation <http://www.solipsys.co.uk/new/JugglingTalkSummary.html?JugglingTalk>`_, `knot notation <https://www.maths.ed.ac.uk/~v1ranick/papers/conway.pdf>`_ (see `Katherine Ye's Strange Loop 2015 talk <https://www.youtube.com/watch?v=Wahc9Ocka1g>`_), and `notation for kinetic sculptures <https://github.com/hypotext/notation#channa-horwitzs-sonakinetography>`_. These examples come from Katherine Ye's excellent notes on `notations and thought <https://github.com/hypotext/notation#notation-and-thought>`_, which contain a number of other examples, quotations, and musings on notation.

.. todo::

  Cite Katherine's work on generating diagrams from symbolic descriptions of structures.

.. todo::

  Amy Ko's graduate work, and other work on projectional editors, including mbeddr

.. todo::

  Graphite 

Customizable Notation
=====================

.. todo::
  
  Cite Cyrus' PhD thesis + ECOOP and ICFP papers

.. todo::

  Cite Erdweg's work

.. todo:: 

  Cite Schwerdfeger and Van Wyk

.. container:: hidden

  :cite:`cajori1993history`
  :cite:`wolfram2000mathematical`
  :cite:`green1989cognitive`
  :cite:`blackwell2003notational`
  :cite:`pane1996usability`
  :cite:`iverson1987notation`
  :cite:`petre1995looking`
  :cite:`petre2006cognitive`
  :cite:`hughes95`
  :cite:`wadler2003prettier`
  :cite:`bernardy17`
  :cite:`brown1992color`
