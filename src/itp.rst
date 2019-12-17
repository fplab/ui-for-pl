.. :Authors: - Ke Du

.. title:: Interactive Theorem Provers

Overview
========
  


  "Complete formal verification is the only known way to guarantee that a system is free of programming errors." :cite:`klein09` 

Important applications of formal verification include: aerospace softwares such as those who prevent airplane collision;
microprocessor producers such as Intel have their own verification team.
A cryptographic system must ensure that its protocol is error free, while the errors are hard to notice.

An interactive theorem prover (ITP), sometimes refered to as proof assistant, is a programming environment that helps 
humans to write formal proofs. In contrast to automated theorem provers, ITPs require human guidance, 
though they also have a certain level of automation power. 
Different to a traditional proof conducted through a pen-and-paper approach, a formal proof conducted by computers
is completely rigorous, and is oftenly tedious and hard. Similarly, a machine proof is usually cumbersome as well.
For example, seL4, a verified microkernel that we will mention later, takes a total of about 23 person years for its 
development of framework, libraries and functional correctness proof, and those sums up to 200,000 lines of code in the ITP Isabelle. :cite:`klein09`

It is worth noting that, usually we treat the theorem prover as a trusted computing base (TCB). In other words, we have to trust the theorem provers.



Notable Computer-Aided Proofs
=============================
.. container:: bib-item

  .. bibliography:: itp.bib
    :filter: key == 'leroy09'

  The `CompCert <http://compcert.inria.fr/doc/index.html>`_ 
  compiler generates assembly code from a large subset of C, and is written and checked in the interactive theorem prover `Coq <https://coq.inria.fr/documentation>`_.
  
.. container:: bib-item

  .. bibliography:: itp.bib
    :filter: key == 'klein09'

  seL4 is a formally verified microkernel. It provides high performance comparable to other L4 kernels, 
  while it is also guaranteed never to crush,
  never to perform an unsafe operation, and its behavior is completely predictable in every situation.

.. container:: bib-item

  .. bibliography:: itp.bib
    :filter: key == 'gonthier08'

  The famouse four color theorem is proved with the aid of a computer at first,
  and completely formalized in Coq later on.


Gamification
============
Gamification of ITPS is translating them into games. 
Check out one of them: `Polymorphic Blocks <https://cseweb.ucsd.edu/~lerner/pb.html>`_ .

.. container:: bib-item

  .. bibliography:: itp.bib
    :filter: key == 'lerner15'

  Polymorphic Blocks is purely graphical, and allows users to 
  prove simple formulas in propositional logic. The idea is to use shapes to represent boolean connectives and
  variables, blocks to represent inference rules and theorems, and composition of blocks to represent formal deductions.

  In their evaluation, they recruited about 30 high school students who have no experience with logic, and randomly divided into two
  groups; in the symbol group, students are required to do formal proofs about propositional logic, while in the game group, they are
  required to do the exact same problem sets in the Polymorphic Blocks game. The average completion time of the game group is about half
  of the symbolic group. After that, each group is given the same additional problem set, and participants are asked to work on that for
  at least 5 minutes. They observed that in the game group, everyone finished the problems, while in the symbol group, most of them gave
  up in the middle.

  This paper concludes that the puzzle game like tool helps users to do proof much faster than a pen-and-paper interface.
  It also results in more accuracy and engagement. The tool has a potential of teaching
  logic, however the tool only teaches the user strategies of applying inference rules without going into details, and it is not clear
  whether it helps the user understand the symbolic meaning of the formulas. The paper also states that this tool has a potential of
  laying the foundation for crowdsourcing proofs via gamification.

Unifying ITPs
=============
There are many different ITPs, and an extension for one of them
does not easily transport to another. Proof General, a canonical IDE for ITPs,
is a framework that tackles this problem.

.. container:: bib-item

  .. bibliography:: itp.bib
    :filter: key == 'aspinall00'

  Proof General is a generic interface for various theorem provers based on Emacs. It features in simplified communication with the 
  theorem prover by providing a GUI. Scripts displayed by the GUI are syncronized with the prover. User can edit the proof
  stripts, see the current goal, and receive feed back from the theorem prover.

.. container:: bib-item

  .. bibliography:: itp.bib
    :filter: key == 'aspinall07'

  Proof General Kit implements a protocol for communicating between
  theorem provers, display and other auxiliary tools, and it integrates features such as browsing and searching loaded theorems.


Now there are `more features, <http://proofgeneral.inf.ed.ac.uk/htmlshow.php?title=Proof+General+user+manual&file=releases%2FProofGeneral%2Fdoc%2FProofGeneral%2FProofGeneral_2.html>`_
supported by proof general, such as proof by pointing (appropriate tactics or lemmas are automatically applied
when clicking on a subterm of a goal) and proof-tree visualization.


Geometry Interactive Theorem Prover (GTP)
=========================================

Geometry Interactive Theorem Provers (GTP) are used for proving geometric properties.

GTPs has potential for education. 
This book describes a possible direction of developing GTP:

.. container:: bib-item

  .. bibliography:: itp.bib
    :filter: key == 'quaresma17'

  A geometry book from the future would
  be a computer program, in which all the theorems can be automatically discovered (and of course proved) by
  computer and beautiful illustrations can be automatically generated and dynamically modified. 
  
`This <https://www.uc.pt/en/congressos/thedu/thedu18/ficheiros/TalkNarboux>`_
discusses more aspects of ITP applied to teaching:

1. The concepts, including the defnitions, deduction rules, axioms, hypothesis, etc, should be clarified.
2. There should be objective criterion for the validity of a proof.
3. Feed back should be provided in time.
4. Users are motivated. Theorem proving as a game.

Let us look at a substantial example. 

.. container:: bib-item

  .. bibliography:: itp.bib
    :filter: key == 'narboux07'
  
  This tool provides a way to combine a dynamic geometry software with Coq, using both automated and interactive approaches.
  The geometry software is used for drawing geometric figures and inventing conjectures by using feed back from the geometric software
  , and a theorem prover is used to prove the conjectures.
  In the automatic mode, the conjecture along with the graph created by the user is rewritten and translated to the automatic theorem prover.
  The user can choose certain strategies such as setting searching depth for the automated theorem prover, but has no control during proving,
  except interrupting it.
  In the interactive mode, the process is similar, except that the conjecture along with the graph is limited into those that can be 
  translated into Coq, and the proof must be done by the user in Coq.

A few results of the GTPs are: 

.. container:: bib-item

  .. bibliography:: itp.bib
    :filter: key == 'braun17'
  
  Pappus' theorem;

.. container:: bib-item

  .. bibliography:: itp.bib
    :filter: key == 'boutry16'

  Tarski's axioms, which are axioms for Euclidean geometry,
  is formulated in first-order logic, are formalized in Coq, which "paves the way for the use of algebraic automated 
  deduction methods in synthetic geometry within the Coq proof assistant".

Usability Evaluation of Interactive Theorem Provers
=========================================================
.. container:: bib-item

  .. bibliography:: itp.bib
    :filter: key == 'beckert14'
    
  This paper performs usability evaluation using focus groups.
  It studies the difference of the user's understanding (user's model) and the actual proof performed 
  by the prover (prover's model) at some state of the proof. The hypothesis, which is at the same time one of their conclusion,
  is that bridging the gap between the two is "the paramount and prominent challenge for efficient and effectively
  usable general theorem provers". 

  The evaluation involves discussion about two interactive theorem provers, KeY and Isabelle.
  The KeY system is an interactive verification system for programs
  written in Java annotated with the Java Modeling Language. The user interface is tree-structured,
  each node is an intermediate goal, and the children are derived from applying formulas to their parent node.

  On the other hand, Isabelle only shows the current goal, and by applying tactics (sometimes called methods), which are essentially 
  a set of inference rules and lemmas, the current goal is reduced to smaller goals, but the intermediate state 
  between two goals is invisible.  

  There are a few pros and cons of the two provers identified with regard to interacting with the tools. 
  The detailed tree-structured proof in KeY is both an advantage and a
  disadvantage, since the user can go into details as much as she wants to, but at the same time 
  it gives too much information that the user does not care about. 
  However KeY users often have to interact with
  low-level logic formulas rather than doing proof on the notation level, and it is common for them to perform repeated low-level interactions. 
  Isabelle, on the other hand, produces a more intuitive proof.
  It also has tools that helps automation such as automated counter example finding. One of the down side of Isabelle is that, finding the right tactic
  is hard, and if the tactic fails, the user can hardly find the reason. 
  Also, the nature of the proof in Isabelle being hard to read requires a clean up,
  however Isabelle does not provide help refactoring the proof. 

  The users also reports that in the middle of a proof, they develop the proof by experience, 
  mainly because theorem provers provides little guidance. They spend time on comprehending the current state of proof, or
  finding the cause of a failed proof attempt. The paper concludes that, Isabelle should be able to display intermediate steps of a tactic,
  and KeY should be able to fold the details in a proof tree when necessary, to keep it high level.



.. container:: hidden

  :cite:`klein09`
  :cite:`gonthier08`
  :cite:`quaresma17`
  :cite:`braun17`
  :cite:`boutry16`
  :cite:`narboux07`
  :cite:`aspinall07`
  :cite:`lerner15`
  :cite:`aspinall00`
  :cite:`beckert14`
  :cite:`leroy09`