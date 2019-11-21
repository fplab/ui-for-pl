.. :Authors: - Cyrus Omar

.. title:: Interactive Theorem Prover

Overview
========
.. container:: bib-item

  .. bibliography:: itp.bib
    :filter: key == 'Klein2009'

  Complete formal verification is the only known way to guarantee that a system is free of programming errors. 

There are various applications of formal verification. A cryptographic system must ensure that its protocal is error free,

.. container:: bib-item

  .. bibliography:: itp.bib
    :filter: key == '10.1007/BFb0000430'

  while the flaws are counterintuitive enough so that an informal analysis may be too prone to error
  to be reliable.

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

Polymorphic Blocks ``[PB]``
===========================
`Polymorphic Blocks <https://cseweb.ucsd.edu/~lerner/pb.html>`_ is purely graphical, and allow users to 
prove simple formulas in propositional logic. The idea is to use shapes to represent boolean connectives and
variables, blocks to represent inference rules and theorems, and composition of blocks to represent formal deductions.
In this paper they concludes the puzzle game like tool helps users to do proof much faster than a pen-and-paper interface,
even with some guidance of a peer instructor. It also results in more accuracy and engagement. The tool has a potential of teaching
logic, however the tool only teaches the user strategies of applying inference rules without going into details, and it is no clear
whether it helps the user understand the symbolic meaning of the formulas. The paper also states that this tool has a potential of
laying the foundation for crowdsourcing proofs via gamification.

Proof General
=============
Proof General is a generic interface for various theorem provers based on Emacs. 
It abstacts away the file system and the prover core. User can edit the proof
stripts, see current goal, and receive feed back from the theorem prover. 
Sophisticated functionality are implemented later. Proof General Kit[PGkit] implements a protocal for communicating between
theorem provers, display and other auxiliary tools, and it integrate features such as browsing and searching loaded theorems. 


Geometry Interactive Theorem Prover (GTP)
=========================================
[G] provides a way to combine a dynamic geometry software with Coq, using both automated and interactive approaches.
The geometry software is used for drawing geometric figures and invent conjectures by using feedbacks from the geometric software
, and theorem proves are used to prove the conjectures.
In the automatic mode, the conjecture along with the graph created by the user is rewritten and translated to the automatic theorem prover.
The user can choose certain strategies such as setting searchning depth for the automated theorem prover, but has no control during proving,
except interrupting it.
In the interactive mode, the process is similar, except that the conjecture along with the graph is limited into those that can be 
translated into Coq, and the proof must be done by the user in Coq.

A few results of the GTPs are: Pappus' theorem is proven with GTP[p]; `Tarski's axioms <https://en.wikipedia.org/wiki/Tarski%27s_axioms>`_, which are axioms for Euclidean geometry,
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


Usability Evaluation of Interactive Theorem provers
=========================================================
[EVAL] performs usability evaluation using focus groups.
It studies the difference of the user's understanding (user's model) and the actual proof performed 
by the prover (prover's model) at some state of the proof. The hypothesis, which is at the same time one of their conclusion,
is that bridging the gap between the two is "the paramount and prominent challenge for efficient and effectively
usable general theorem provers". 

The evaluation involves discussion about two interactive theorem provers, KeY and Isabelle.
The KeY system is an interactive verification system for programs
written in Java annotated with the Java Modelling Language. The user interface is tree-structured,
each node is an intermediate goal, and the children are derived from applying formulas to their parent node,
whereas Isabelle only shows the current goal, and by applying tactics (sometimes called methods), which are essentially 
a set of inference rules and lemmas, the current goal is reduced to smaller goals, but the intermediate state 
between two goals is invisible.  

There are a few pros and cons of the two provers identified with regard to interacting with the tools. 
The detailed tree-structured proof in KeY is both an advantage and a
disadvantage, since the user can go into details as much as he wants to, but at the same time 
it gives too much information that the user does not care about. 
However KeY users oftenly have to interact with
low-level logic formulas rather than doing proof on the notation level, and low-level steps are oftenly repeated by hand. 
Isabelle, on the other hand, produces intuitive proof.
It also has tools that helps automation such as automated counter example finding. One of the down side of Isabelle is that, finding the right tactic
is hard, and if the tactic fails, the user can hardly find the reason. 
Also, the nature of the proof in Isabelle being hard to read requires a clean up,
however Isabelle does not provide help refactoring the proof. 

The users also reports that in the middle of a proof, they develop the proof by experience, 
mainly because theorem provers provides little guidance. They spend time on comprehending the current state of proof, or
finding the cause of a failed proof attempt. The paper concludes that, Isabelle should be able to display intermediate steps of a tactic,
and KeY should be able to fold the details in a proof tree when necessary, to keep it high level.


.. todo::
  fix citations

.. container:: hidden

  :cite:`Klein:2009`
  :cite:`10.1007/BFb0000430`
  [3]:cite:`appel1976`
  [4]https://www.ams.org/notices/200811/tx081101382p.pdf
  [k]https://link.springer.com/content/pdf/10.1007%2Fs11786-017-0302-8.pdf
  [p]https://hal.inria.fr/hal-01176508
  [T]https://hal.archives-ouvertes.fr/hal-01282550
  [G]https://link.springer.com/content/pdf/10.1007%2Fs10817-007-9071-4.pdf
  [PPT]https://www.uc.pt/en/congressos/thedu/thedu18/ficheiros/TalkNarboux
  [PGkit]http://proofgeneral.inf.ed.ac.uk/Kit/docs/pgipimp.pdf
  [PB]https://cseweb.ucsd.edu/~lerner/papers/polymorphic-blocks-chi15.pdf command block