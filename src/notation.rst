.. :Authors: - Cyrus Omar

.. title:: Notation

Overview
========

Humans visually represent **mathematical structures**, including computer programs, using **mathematical notation**.  
There can be many different notations for a given structure, each differing along various cognitive dimensions. 
As such, notation design is a subfield of user interface design.

In mathematical writing, authors often define notation informally, e.g. by example.
It is common to be somewhat cavalier about notation in this setting, relying on the human reader to resolve ambiguities or insert missing details based on convention.

Programming language designers, in contrast, are typically more precise. 
In particular, a **concrete syntax** or **surface syntax** is a formal system that serves to map recognized notational forms to program structures.
The rules that fundamentally introduce program structures constitute the **abstract syntax** or **structural syntax** of the language.

.. note::

  The metalanguage that the abstract syntax operates within provides the ground notation used to identify program structures. 

  For example, if the abstract syntax defines programs as labeled inductive tree structures, as is common practice, then the metalanguage might identify one such "abstract syntax tree" by the form ``Plus(Num(2), Num(2))``. 
  A concrete syntax can then map the concrete form ``2 + 2`` to this tree structure.

Programming language definitions typically privilege a single concrete syntax, which is then referred to colloquially as *the* concrete syntax of the language. 
However, it is important to keep in mind that many languages now have popular third-party concrete syntaxes (e.g. `CoffeeScript <https://coffeescript.org/>`_ for JavaScript, `Reason <https://reasonml.github.io/>`_ for OCaml), and it is also possible to define a programming language without privileging any concrete syntax at all.
The underlying structures, not the surface forms, are what is meaningful, i.e. assigned meaning by the language definition.

Notation specific to a particular type of data is known as **literal notation** for that type. 
An instance of this notation is called a **literal**. 
For example, the concrete syntax of many programming languages allows for list literals like ``[1, 2, 3]``.

History of Mathematical Notation
================================

Diagrammatic notation is evident in early mathematical writing, e.g. in Euclid's *Elements*. 
Symbolic notation has been comparatively slow to emerge, arising mainly in the last several centuries. 
Before that, mathematical statements were written out in natural language (e.g. "The sum of 2 and 2 is 4.")

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'cajori1993history'

  This book provides a thorough historical account of mathematical notation, starting from antiquity.

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'wolfram2000mathematical'

  This article (`link <https://www.stephenwolfram.com/publications/mathematical-notation-past-future/>`_) provides a concise overview of the history of mathematical notation. 
  It also includes some discussion of the notational choices in the Mathematica programming language.


Cognitive Dimensions of Notations
=================================

Notations can be compared along various *cognitive dimensions*. 
Examples include *diffuseness* (the amount of space that the notation takes up) and *role-expressiveness* (the extent to which the purpose of a notational entity is readily apparent) :cite:`blackwell2001cognitive`. 

To properly perform a cognitive dimensions analysis, one needs to specify an appropriately specific context (e.g. by specifying who the intended user is, and the affordances available in the editing environment). 
Because cognitive dimensions analyses involve reasoning about cognitive operations, they are typically qualitative in nature, though in some cases a quantitative cost metric can also be relevant.

.. note::
  In much of the literature on cognitive dimensions of notations, the word "notation" is used liberally: researchers will analyze a complete language or system design rather than focusing strictly on notational choices.

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'iverson1987notation'

  Iverson's Turing Award lecture discussed various "important characteristics of notation", and identified programming languages as powerful "tools of thought".

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'green1989cognitive'

  Green introduced the "cognitive dimensions" framework, which provides vocabulary that can be used to compare different designs. 
  The emphasis is on the notation within a particular environment, e.g. an editor.

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'blackwell2001cognitive' or key == 'blackwell2003notational'

  Subsequent papers have proposed a number of additional cognitive dimensions beyond those given as examples by Green. 
  These two papers summarize both the original work and some of these subsequent developments, and are suitable as introductions to CD analysis.

.. container:: bib-item

  .. bibliography:: notation.bib
    :filter: key == 'pane1996usability'

  This detailed technical report details a large number of useful dimensions (going beyond notation in some cases). 
  The focus is nominally on novice programming systems, but many of the dimensions are relevant beyond that domain.

.. todo::

  A more thorough bibliography covering cognitive dimensions analysis and its applications might be useful, perhaps as a subpage.

Secondary Notation
==================
Additional cues are often systematically inserted by humans when editing, or by tools when rendering notation for display, in order to improve readability and other cognitive dimensions. 
These cues are called *secondary notation* if they are unnecessary from the perspective of the syntax and semantics.

For example, a human might (1) insert formally unnecessary indentation to better communicate nested scopes to human readers; 
or (2) place conceptually related items near each other; 
or (3) include natural language comments.

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

Most contemporary programming languages come equipped with textual notation. 
In other words, programs are represented and edited in textual form, i.e. as strings over some suitable alphabet, typically ASCII or Unicode. 
It is typically desirable for there to be at most one structure for any given string. 
This property of a textual syntax is known as *determinism*.

Parsers
-------

A parser is an implementation of a textual syntax, i.e. a function that takes a string as input and returns the corresponding structure (or structures, if the syntax is not deterministic). 
If this is not possible, e.g. because there is no corresponding structure, then parsers exhibit various behaviors. 
In practice, they produce error messages that attempt to identify and explain the parse error (a.k.a. syntax error) to the user.

Parser Generators
~~~~~~~~~~~~~~~~~

Parsers are sometimes written manually (a.k.a. "hand-rolled"). 
More commonly, however, they are generated programmatically using a parser generator.

Grammar-Based Parser Generators
*******************************
For example, *grammar-based parser generators* generate a parser given a formal grammar (written using some suitable grammar formalism) where each production is equipped with logic that determines the corresponding structure. 

.. todo::

  Is there a good survey or book on grammar-based parser generators? Someone's thesis might have a good survey on the topic in it?

Parser Combinators
******************
Another method is to use a *parser combinator* library, which generates a parser by executing a program that applies various functions (called `combinators`) to define and combine parsing rules.
In many cases, the goal is for the composition of various combinators to resemble a grammar-based specification, such that the resulting parser is an implementation of the corresponding grammar.

.. container:: bib-item

  .. bibliography:: notation2.bib
    :filter: key == 'hutton92'

  This paper describes the parser combinator technique by example. 
  The technique was known prior to this paper, but Hutton says that little was previously written about it.

.. container:: bib-item

  .. bibliography:: notation2.bib
    :filter: key == 'frost08'

  This paper describes a parser combinator library that can accommodate ambiguities and left-recursive grammars. 
  It is also asymptotically efficient. 
  It is implemented in Haskell.

.. todo::

  Is there other notable work on parser combinators, particularly after 2008?

Parse Errors
~~~~~~~~~~~~
When a piece of text cannot be successfully parsed, it is helpful to generate an error message that can help the programmer localize and fix the error. 
This is a challenging problem.

.. todo::
  Summarize the literature on parse/syntax errors.

Unparsers
---------
An unparser is a function that takes a structure as input and produces a textual representation which, if parsed, will produce the original structure (or in some cases one merely equivalent to it, for some suitable notion of equivalence).  

It is often the case that there are multiple valid string representations of a structure. 
Different unparsers are therefore free to make different choices within this space. 

Pretty Printers
~~~~~~~~~~~~~~~
For example, textual pretty printers are unparsers that choose a "pretty" textual representation, e.g. one that follows secondary notational conventions about the use of whitespace.

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

Minifiers and Obfuscators
~~~~~~~~~~~~~~~~~~~~~~~~~

Not all unparsers are pretty printers. 
An unparser's goal may instead be to minimize the size of the resulting string representation, or even to intentionally obfuscate the code.

.. todo::
  Are there papers on minifiers or obfuscators?

Graphical Notation
==================
Mathematical notation is often non-textual. 

For example, it is common to lay out fractions vertically, or to use square root notation :math:`\sqrt{e}`.
Matrix notation lays out sub-expressions in a grid. 
Set intersection is diagrammed using overlapping circles.

In applied mathematics, the sciences, and the arts, diagrammatic notation is quite common.
Examples include `juggling notation <http://www.solipsys.co.uk/new/JugglingTalkSummary.html?JugglingTalk>`_, 
`knot notation <https://www.maths.ed.ac.uk/~v1ranick/papers/conway.pdf>`_ (see `Katherine Ye's Strange Loop 2015 talk <https://www.youtube.com/watch?v=Wahc9Ocka1g>`_), 
and `notation for kinetic sculptures <https://github.com/hypotext/notation#channa-horwitzs-sonakinetography>`_. 
These examples come from Katherine Ye's excellent `notes on notations and thought <https://github.com/hypotext/notation#notation-and-thought>`_, 
which also contain a number of other examples, quotations, and musings on notation.

Some systems that support generating diagrams from textual descriptions of mathematical structures. Note that this is distinct from languages that simply provide low-level graphical primitives, e.g. lines and shapes, such as `TikZ <http://www.texample.net/tikz/>`_.

.. container:: bib-item

  .. bibliography:: notation2.bib
    :filter: key == "wode17"

  The `Penrose <https://penrose.ink/>`_ system, in development as of early 2020, supports generating graphical diagrams from textual descriptions of mathematical structures together with additional styling and layout optimization directives.

Few programming languages support non-textual primary notation, 
in part because doing so requires moving away from the use of standard text editors for writing programs.
We discuss systems that do support non-textual primary notation in the section on :ref:`Structure Editors`.
We also discuss systems that support locally integrating interactive graphical notation into a textual editing environment there.


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
  :cite:`hutton92`
  :cite:`frost08`
  :cite:`wode17`
  :cite:`ko06`