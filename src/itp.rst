.. :Authors: - Cyrus Omar

.. title:: Language Usability

Overview
========

  Complete formal verification is the only known way (by 2009) to guarantee that a system is free of programming errors. ``[1]``

There are various applications of formal verification. A cryptographic system must ensure that its protocal is error free, 

  while the flaws are counterintuitive enough so that an informal analysis may be too prone to error
  to be reliable. ``[2]``

.. todo::
  some more motivation

An `interactive theorem prover <https://en.wikipedia.org/wiki/Proof_assistant>`_, sometimes refered as proof assistant, is a software that helps 
human to write `formal proofs <https://en.wikipedia.org/wiki/Formal_proof>`_. The `CompCert <http://compcert.inria.fr/doc/index.html>`_ 
compiler generats assembly code from a large subset C, and is written and checked in the interactive theorem prover `Coq <https://coq.inria.fr/documentation>`_.
Interactive theorem provers, in contrast to `automated theorem provers <https://en.wikipedia.org/wiki/Automated_theorem_proving>`_, require human guidance.

The famouse `four color theorem <https://en.wikipedia.org/wiki/Four_color_theorem>`_ is proved with a part of computer aid[3] at first,
and completely formalized in Coq later on.[4] 

It is worth noting that, when we say some formal proof done by a theorem prover works, 
we impose the implicit assumption that the theorem prover is error-free. In other words, we have to trust the theorem provers.

For theorems that are intuitively true and are easy to write down an informal proof,
it is often the case that they are usually tedious and tremendously hard to prove; 
depending on the underlying logic of the prover, 
the set of all theorems that can be proven is different, and it is even harder to 'prove' that, 
a theorem (nor its 'negation') can never be proven. To fully exert the strength of a theorem prover,
the user is supposed to have sophistications in mathematical logic and programming (usually functional), 
and sometimes type theory and so on.

In the following sections I will cover several different user interfaces for interactive theorem provers.

#REWRITE THIS SECTION FOR FINAL DRAFT
Some comments from M:
1. Want to see intermediate results, or read a proof. (Coq) Want to figure out where I am inside a proof.



Geometry Interactive Theorem Prover 
===================================
[G] provides a way to combine a dynamic geometry software with Coq, using both automated and interactive approaches.
The geometry software is used for drawing geometric figures and invent conjectures by using feedbacks from the geometric software
, and theorem proves are used to prove the conjectures.
In the automatic mode, the conjecture along with the graph created by the user is rewritten and translated to the automatic theorem prover.
The user can choose certain strategies such as setting searchning depth for the automated theorem prover, but has no control during proving,
except interrupting it.
In the interactive mode, the process is similar, except that the conjecture along with the graph is limited into those that can be 
translated into Coq, and the proof must be done by the user in Coq.


[GeoCoq]

A few achievements are: Pappus' theorem is proven with GTP[p]; `Tarski's axioms<https://en.wikipedia.org/wiki/Tarski%27s_axioms>`_, which are axioms for Euclidean geometry,
is formulated in first-order logic, are formalized in Coq, which 'paves the way for the use of algebraic automated 
deduction methods in synthetic geometry within the Coq proof assistant'[T]

Interactive theorem provers for geometry is also helpful for educational purposes. 
  A geometry book from the future would
  be a computer program, in which all the theorems can be automatically discovered (and of course proved) by
  computer and beautiful illustrations can be automatically generated and dynamically modified.[k]
[PPT] discusses more aspects of ITP applied to teaching: (should I cite a slide?)
1. The concepts, including the defnitions, deduction rules, axioms, hypothesis, etc, should be clarified.
2. There should be objective criterion for the validity of a proof.
3. feedbacks should be provided in time.
4. Users are motivated. Theorem proving as a game.

[1]https://dl.acm.org/citation.cfm?id=1629596
[2]https://link.springer.com/content/pdf/10.1007%2FBFb0000430.pdf
[3]https://projecteuclid.org/euclid.bams/1183538218
[4]https://www.ams.org/notices/200811/tx081101382p.pdf
[k]https://link.springer.com/content/pdf/10.1007%2Fs11786-017-0302-8.pdf
[p]https://hal.inria.fr/hal-01176508
[T]https://hal.archives-ouvertes.fr/hal-01282550
[G]https://link.springer.com/content/pdf/10.1007%2Fs10817-007-9071-4.pdf
[PPT]https://www.uc.pt/en/congressos/thedu/thedu18/ficheiros/TalkNarboux