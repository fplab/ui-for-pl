.. :Authors: - Cyrus Omar, Hannah Potter

.. title:: Educational Technology

Overview
========

Educational technology is focused on facilitating learning. This includes supporting novice programmers learning the fundamentals
of programming, supplying tools for developers that promote knowledge sharing, assisting educators in their teaching objectives, and 
facilitating learning for experienced programmers using new technologies and systems. 

Programming languages and environments that are designed for use during a learning process are governed by different design criteria than those that are
designed to be useful for experts. Educational programming environments typically focus on two problems. One is trying to flatten the 
steep learning curve often faced by novice programmers and help them overcome what is typically perceived as "hard" with 
programming :cite:`guzdial2004programming`. The second is supporting the motivations that different 
people have for trying to learn these new programming skills :cite:`kelleher2005lowering`.

There are a few key design principles that are often used in either of these strategies: 

* Try to minimize frustration while still being challenging enough to maintain interest
* Incorporate motivations for learning new skills 
* Help students learn abstract concepts using concrete instances
* Give :doc:`immediate feedback </live-programming>`

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
  solving the puzzles. The children solved the problems in a step-wise fashion, typically only giving the lady bug 1-3 move 
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
  There are three types of blocks, sensor (e.g. sound), logic (e.g. not), and action (e.g. light that turns on and off), that can be combined to form stacks. Researchers ran a study with a class of preschoolers. They found that in general
  the kids seemed to have fun with the blocks. The children had a hard time understanding the logic blocks, but were in general able to understand
  the sensor and action blocks. The preschoolers had an easier time building complexity between interactions of two stacks as opposed to within a single stack.

.. container:: bib-item

  .. bibliography:: educational-technology.bib
    :filter: key == 'maloney2010scratch'

  This paper gives an overview of the design of the Scratch programming environment. Scratch is a graphical, block-based programming environment
  designed for kids who have no programming experience. The system strives to make execution visible and allow for tinkering (learning by trying). The
  code is live such that any code fragment can be executed simply by clicking on it (no compile-link-run cycle to go through).

.. container:: bib-item

  .. bibliography:: educational-technology2.bib
    :filter: key == 'maloney2008programming'

  Scratch was introduced as an optional activity at an after-school technology center for traditionally disadvantaged youth in 
  an impoversished area. Little supervision or formal teaching was provided for the system. Over the course of two years,
  the youth used Scratch more than any other media-creation tool available at the center. They felt that Scratch
  was most similar to school activities that particularly supported creativity and personal expression, as opposed 
  to subject areas that are typically associated with programming.

.. container:: bib-item

  .. bibliography:: educational-technology2.bib
    :filter: key == 'wilson2010evaluating'

  Scratch was used for teaching lessons in an IT class for 8-9 year old students at a school. The study
  did not find evidence of whether or not using this programming environment helped the students develop cognitive abilities. 
  However, based on feedback from the students, they generally enjoyed and were enthusiastic about their lessons 
  that used Scratch. 

Feedback Generation
===================

With the growing number of people interested in learning programming skills, institutions have difficulty maintaining the number of instructors
needed to give students valuable one-on-one feedback. Thus, automatic feedback generation may be valuable in the current learning climate.

There are various ways for students to get feedback. One way that automatic feedback is being generated is in systems that perform as "autograders" where
students can upload submissions and get information back on how their solutions performed against test suites. This however still leaves a burden
on students to search out where their solution went wrong, which may be difficult for novices. Thus, feedback that can guide students through
debugging code with errors can be far more valuable to the learning process than what is returned by standard autograders.

.. container:: bib-item

  .. bibliography:: educational-technology.bib
    :filter: key == 'suzuki2017exploring'

  From analysis of Q&A posts on a discussion forum for a programming class as well as an interview of a teaching assistant
  for a college level introductory programming class, five types of common hints that teachers give to help students fix their 
  code that can be generated using program synthesis are itentified: 
  
  1) Transformations (what to change to make the program work)
  2) Locations (the line(s) that need to be changed to make the program work)
  3) Data (demonstrating where a variable takes on the wrong value)
  4) Behavior (identifying how the program is not behaving how it is supposed to)
  5) Examples (examples of inputs and correct outputs)
  
  Additionally, four principles of feedback design described in prior work are identified: 
  
  1) Help students locate bugs
  2) Demonstrate instances in which code fails
  3) Explain behavior of code with visual execution
  4) Help students understand the relationship between the cause of an error and its symptoms

Tutoring Systems
================

Large class sizes and the growing number of people learning computer programming through online courses makes the 
development of tutoring systems valuable. Tutoring systems provide visualizations and walkthroughs of the execution
of code. Additionally, they may guide students through developing a program and improving problem solving skills. Students may remain more engaged with the system
and learn more if there is interaction that demonstrates whether or not the student is understanding and following along.

.. container:: bib-item

  .. bibliography:: educational-technology.bib
    :filter: key == 'guo2013online'

  Python Tutor is an online tutoring system. This is a form of program visualization that shows the state of memory (stack frames and the heap)
  as a piece of code executes, essentially creating visual code traces. The tool was designed based on common features of other existing program visualization
  tools and then updated based on user feedback. The paper acknowledges that study results may determine
  that new features may be needed to support active learning, such as adding questions and quizzes along with the visualizations.

.. container:: bib-item

  .. bibliography:: educational-technology2.bib
    :filter: key == 'cazzola2015gradually'

  This paper goes over the potential benefits of introducing a programming language gradually instead of all at once.
  One such benefit is allowing students to focus on problem solving, rather than focusing on understanding
  the full features of a language. A series of subdivisions of Javascript (each subdivision only
  contains a subset of features of the language, such as conditional statements or functions) 
  was used to teach a few students in an introductory programming class. The study generally found 
  that students felt like they focused more on problem solving than learning the programming language.

.. container:: bib-item

  .. bibliography:: educational-technology2.bib
    :filter: key == 'gerdes2012interactive'

  This paper discusses an interactive tutoring system for students learning Haskell. The system provides
  feedback on if the student is on the right track solving the problem, hints if the student is stuck,
  and suggestions on how to refactor code if the student should iterate on their solution. Hints and 
  feedback are derived from annotated solutions to problems provided by a teacher. Students using
  the tutor build their solutions by filling in and refining "holes" in the program. Students taking a functional
  programming course who used the system in general appreciated the ability to see worked-out solutions
  generated by the system, but felt some work was needed to make the tutor more helpful when students
  deviate from correct solutions.

Educator Support
================

In the space of education technology, there is needed support for educators. This can either be in an informal context of peer-to-peer knowledge-sharing
or in the context of a more formal classroom setting. 

Informal knowlege sharing allows peers to share information they have learned with one another. Different environments support this to 
varying levels, with some allowing users to explore and modify projects made by other users and to ask clarifying questions.
For a more formal classroom setting, teachers can often use support in getting a clear view of what topics
their students are excelling at or struggling to understand.

.. container:: bib-item

  .. bibliography:: educational-technology.bib
    :filter: key == 'glassman2015overcode'

  OverCode is a system designed to allow instructors of large programming classes to automatically group solutions that may have 
  irrelevant syntactic differences but are semantically equivalent. This should allow instructors to get a high-level overview of
  the understandings and misunderstandings of their students more quickly than filtering through raw solutions. When evaluated against
  only having access to raw solutions, users were able to review more students' code in less time and felt that they had a better high-level
  overview of ways that the coding problems were solved. 

.. container:: bib-item

  .. bibliography:: educational-technology.bib
    :filter: key == 'head2018interactive'

  CodeScoop is an interactive example extraction system that allows users to quickly pull out examples from an existing code
  base. Given selected lines to be included in an example, the system iteratively checks for ommitted
  lines of code that may be valuable (such as control flow) to help the example writer not leave out critical information. 
  Study participants were asked to create an example from existing code to answer a fake Stack Overflow question. More participants
  in the study were able to complete this example extraction exercise when using CodeScoop compared to a text editor and liked their end result
  example better.

Domain-Specific and Task-Specific Environments
==============================================

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
  :cite:`maloney2008programming`
  :cite:`wilson2010evaluating`
  :cite:`cazzola2015gradually`
  :cite:`gerdes2012interactive`