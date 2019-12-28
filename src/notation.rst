.. :Authors: - Cyrus Omar

.. title:: Notation

Overview
========

Humans visually represent **mathematical structures**, notably including computer programs, using **mathematical notation**.  
There can be many different notations for a structure, each differing along various cognitive dimensions. 
As such, **notation design** is a subfield of user interface design.

Mathematicians often define notation informally, e.g. by example, in mathematical writing.
It is common to be somewhat cavalier about notation in this setting, relying on the human reader to resolve 
ambiguities or insert missing details based on experience.

Programming language designers, in contrast, typically define notation for programs by specifying a formal syntax, 
often called a **concrete syntax** or **surface syntax**, that serves to map forms to program structures.
The rules for forming program structures constitute the **abstract syntax**, a.k.a. **structural syntax**, of the language.

.. note::

  The phrases of the abstract syntax must themselves be expressed using some notation, e.g. ``Plus(x, y)``. 
  This notation is typically inherited from the metalanguage that 
  the language definition operates within, e.g. the ambient mathematics.

Programming language definitions typically privilege a single concrete syntax, which is then referred to colloquially as *the* concrete syntax of the language. 
However, many languages now have popular third-party concrete syntaxes (e.g. `CoffeeScript <https://coffeescript.org/>`_ for JavaScript, `Reason <https://reasonml.github.io/>`_ for OCaml).

Notation specific to a certain type of data is known as **literal notation** for that type. An instance of this notation is called a *literal*. For example, the concrete syntax of many programming languages allows for list literals like ``[1, 2, 3]``.

History of Mathematical Notation
================================

Diagrammatic notation was evident in early mathematical writing, e.g. in Euclid's *Elements*. Symbolic notation was comparatively slow to evolve, arising mainly in the last several centuries. Before that, mathematical statements were written out in natural language (e.g. "The sum of 2 and 2 is 4.")

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'cajori1993history'

  This book provides a thorough historical account of mathematical notation, starting from antiquity.

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'wolfram2000mathematical'

  This article (`link <https://www.stephenwolfram.com/publications/mathematical-notation-past-future/>`_) provides an overview of the history of mathematical notation. It also includes some discussion of notational choices in the Mathematica programming language.


Cognitive Dimensions of Notation
================================

Notations designed for consumption and manipulation by humans (as opposed to those where a machine is the only intended consumer, e.g. bar codes) can be meaningfully compared along various *cognitive dimensions*. 
Examples include *diffuseness* (the amount of space that the notation takes up) and *role-expressiveness* (the extent to which the purpose of a notational entity is readily apparent) :cite:`blackwell2001cognitive`. 

To properly perform a  cognitive dimensions analysis, one needs to specify an appropriately specific context (e.g. by specifying who the intended user is, and the affordances available in the editing environment). 
Because cognitive dimensions involve cognitive operations, cognitive dimensions analyses are typically qualitative in nature, though in some cases a quantitative metric can also be relevant.

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
Additional cues are often systematically inserted by humans when editing, or by tools when rendering notation for display, in order to improve readability and other cognitive dimensions. These cues are called *secondary notation* if they are unnecessary from the perspective of the syntax and semantics.

For example, a human might insert formally unnecessary indentation to better communicate nested scopes to human readers, or place conceptually related items near each other, or include natural language comments.

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'petre1995looking'

  This paper introduces the phrase "secondary notation" and discusses, by way of examples, the importance of good notation, and various subtletites that can arise.

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == "petre2006cognitive"

  This paper reflects on cognitive dimensions analysis and, in particular, states, based on observations made in other studies, that experts are more adept at using secondary notation than novices.


Textual Notation
================

Most programming languages today specify a textual notation. In other words, programs are represented and edited in textual form, a.k.a. as strings, consisting of a sequence of characters drawn from some suitable alphabet, typically ASCII or Unicode. It is typically desirable for there to be at most one structure for any given string. This property of a syntax is known as *determinism*.

Parsers
-------

A parser is a function that takes an arbitrary string as input and returns a corresponding structure. If this is not possible, e.g. because there is no corresponding structure, then parsers exhibit various behaviors. In practice, they produce error messages that attempt to identify and explain the problem to a human.

Parser Generators
~~~~~~~~~~~~~~~~~

Parsers are sometimes written by hand (a.k.a. "hand-rolled"). More commonly, however, they are generated programmatically. 
For example, a *parser generator* generates a parser given a formal grammar equipped with logic for each production that 
generates the corresponding structure. Another method is to use a *parser combinator* library, which generates a parser by 
executing a program that applies various functions to define and combine parsing rules.

.. todo::

  Is there a good survey or book on parsers and parser generators? Someone's thesis might have a good survey on the topic in it? Does someone want to make a subpage on the topic of parsers and parser generators?

Syntax Errors
~~~~~~~~~~~~~
.. todo::
  Summarize the literature on syntax errors.

Unparsers
---------
An unparser is a function that takes a structure as input and produces a string representation which, if parsed, will produce the original structure (or in some cases one merely equivalent to it, for some suitable notion of equivalence).  

It is often the case that there are multiple valid string representations of a structure. Different unparsers are therefore free to make different choices within this space. For example, pretty printers will choose a "pretty" string representation, e.g. one that follows secondary notational conventions about the use of whitespace.

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

Not all unparsers are pretty printers. An unparser's goal may instead be to minimize the size of the resulting string representation, or even to intentionally obfuscate the code.

.. todo::
  Are there papers on minifiers or obfuscators?

Graphical Notation
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

Programmable Notation
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