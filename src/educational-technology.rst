.. :Authors: - Cyrus Omar, Hannah Potter

.. title:: Educational Technology

Overview
========

Educational technology is primarily focused at facilitating learning. This includes supporting novice programmers learning the fundamentals
of programming, supplying tools that promote knowledge sharing, assisting educators in their teaching objectives, and 
facilitating learning of new technologies and systems. 

Programming environments that are being used during a learning process focus on different design needs than those that are
designed to be useful for experts. Educational programming environments typically focus on trying to mitigate what people typically
find to be hard about programming while supporting the motivations that different people have for trying to learn these new skills :cite:`guzdial2004programming` :cite:`kelleher2005lowering`.
A few general strategies that are employed to accomplish these goals are developing special programming languages for learning and developing special
environments (without changing the programming language).

There are a few key design principles that are often used in either of these strategies. One is to try to minimize frustration while still being
challenging enough to maintain interest, with the related principle of incorporating motivations for learning these skills. 
Another is related to being as concrete as possible versus abstract, as people need to understand concrete concepts before they
can begin to apply abstractions. Additionally, educational programming environments often are designed to give immediate feedback, often 
in a visual way that is easy for a learner to understand and see what is happening.

.. container:: bib-item

  .. bibliography:: educational-technology.bib
    :filter: key == 'guzdial2004programming'

  This paper gives an overview of a variety of different programming environments for novices. The educational environments are explored
  under the lense of how they try to answer the question of "What makes programming hard?"

.. container:: bib-item

  .. bibliography:: educational-technology.bib
    :filter: key == 'kelleher2005lowering'

  This paper also gives an overview of various programming languages and environments that were designed for supporting novice programmers. 
  These languages and environments are explored under the lense of supporting the different answers to "What is a person's motivation for trying
  to learn programming?"

Games
=====

Programming to acheive an objective in a game is a common technique for introducing individuals to programming skills such
as problem solving. This is especially true when the audience is children, who may need more motivation to engage in these forms of learning activities than adults actively seeking
out education in programming.

.. container:: bib-item

  .. bibliography:: educational-technology.bib
    :filter: key == 'fessakis2013problem'

  This paper goes over the effectiveness of integrating a programming activity into a regular kindergarten class using puzzles
  that give movement directions to a lady bug to reach some designated destination. The students in the class overall had fun
  solving the puzzles. The children solved the problems in a step-wise fasion, typically only giving the lady bug 1-3 move 
  commands before running the actions and checking to where the lady bug moved.

.. todo:: 
    Add other game based programming environments

Block-Based Environments
========================

Block-based environments are often used for teaching young students (pre-university) and students who have had little or no previous exposure to programming.
These environments have the advantage that there is a reduced coginitive load on learners when it comes to syntax. Block-based environments can limit or eliminate syntax errors
which saves novices time and confusion resolving such errors and allows them to focus on the higher level concepts. Additionally, the use of blocks
minimizes the demand for typing and shows program construction in a graphical way, which is especially helpful for children.

.. container:: bib-item

  .. bibliography:: educational-technology.bib
    :filter: key == 'wyeth2001electronic'

  Electronic blocks are physical blocks that are designed for young children to familiarize themselves with concepts related to programming (like input and output).
  There are three types of blocks, sensor (e.g. sound), logic (e.g. not), and action (e.g. light that turns on and off), that can be combined to form stacks. The researchers ran a study with a class of preschoolers. They found that in general
  the kids seemed to have fun with the blocks. The children had a hard time understanding the logic blocks, but were in general able to understand
  the sensor and action blocks. The preschoolers had an easier time building complexity between interactions of two stacks as opposed to within a single stack.

.. container:: bib-item

  .. bibliography:: educational-technology.bib
    :filter: key == 'maloney2010scratch'

  This paper gives an overview of the design of the Scratch programming environment. Scratch is a graphical, block-based programming environment
  designed for kids who have no programming experience. The system strives to make execution visible and allow for tinkering (learning by trying). The
  code is live such that any code fragment can be executed simply by clicking on it (no compile-link-run cycle to go through).

.. todo:: 
    Find evaluation of effectiveness of Scratch

Feedback Generation
===================

With the growing number of people interested in learning programming skills, institutions have difficulty getting the number of instrutors
needed to give students valuable one-on-one feedback. Thus, automatic feedback generation is innvaluable in the current learning climate.

There are various ways for students to get feedback. One way that automatic feedback is being generated is in systems that perform as "autograders" where
students can upload submissions and get information back on how their solutions performed against test suites. This however still leaves a burden
on students to search out where their solution went wrong, which may be difficult for novices. Thus, feedback that can guide students through
debugging code with errors in it can be far more valuable to the learning process than what is returned by standard autograders.

.. container:: bib-item

  .. bibliography:: educational-technology.bib
    :filter: key == 'suzuki2017exploring'

  Five types of common hints that teachers give to help students fix their code that can be generated using program synthesis
  are itentified: transformations (what to change to make the program work), locations (the line(s) that need to be changed to make the program work),
  data (demonstrating where a variable takes on the wrong value), behavior (identifying where the program is not behaving how it is supposed to), and
  examples (examples of inputs and correct outputs). Additionally, four principles of feedback design are identified: 1) help students locate bugs, 2)
  demonstrate instances in which code fails, 3) explain behavior of code with visual execution, and 4) help students understand the relationship
  between the cause of an error and its symptoms.

Tutoring Systems
================

Large class sizes and the growing number of people learning computer programming through online courses makes the 
development of tutoring systems valuable. Tutoring systems provide visualizations and walkthroughs of the execution
of code. Additionally, they may guide students through developing a program. Students may remain more engaged with the system
and learn more if there is interaction that demonstrates whether or not the student is understanding and following along.

.. container:: bib-item

  .. bibliography:: educational-technology.bib
    :filter: key == 'guo2013online'

  Python Tutor is an online tutoring system. This is a form of program visualization that shows the state of memory (stack frames and the heap)
  as a piece of code executes, essentially creating visual code traces. 

.. todo::
    Add information about systems that introduce the programming language a bit at a time (like SP/k)

.. todo::
    Find interactive tutoring systems

Educator Support
================

In the space of education technology, there is needed support for educators. This can either be in an informal context of peer-to-peer knowledge-sharing
or in the context of a more formal classroom setting. 

Informal knowlege sharing allows peers to share information they have learned with one another. Different environments support this to 
varying levels with some allowing users to explore and modify projects made by other users and to ask clarifying questions.
For a more formal classroom setting, teachers can often use support in getting a better understanding of what topics
their students are excelling at understanding and what topics their students are struggling to understand.

.. container:: bib-item

  .. bibliography:: educational-technology.bib
    :filter: key == 'glassman2015overcode'

  OverCode is a system designed to allow instructors of large programming classes to automatically group solutions that may have 
  irrelavent syntactic differences but are semantically equivalent. This should allow instructors to get a high-level overview of
  the understandings and misunderstandings of their students more quickly than filtering through raw solutions. When evaluated against
  only having access to raw solutions, users were able to review more students' code in less time and felt that they had a better high-level
  overview of ways that the coding problems were solved. 

.. container:: bib-item

  .. bibliography:: educational-technology.bib
    :filter: key == 'head2018interactive'

  CodeScoop is an interactive example extraction system that allows users to quickly pull out examples from an existing code
  base. Given selected lines to be included in an example, the system iteratively checks for ommitted
  lines of code that may be valuable (such as control flow) to help the example writer not leave critical information out. More participants
  in the study were able to complete an example extraction exercise when using CodeScoop compared to a text editor and liked their end result
  example better.

Domain Specific Environments
============================

.. todo::
    Add information about environments/languages targeting users who have very specific goals for learning to program (don't need general knowledge)

.. container:: hidden

  :cite:`wyeth2001electronic`
  :cite:`maloney2010scratch`
  :cite:`suzuki2017exploring`
  :cite:`guo2013online`
  :cite:`glassman2015overcode`
  :cite:`head2018interactive`
  :cite:`fessakis2013problem`