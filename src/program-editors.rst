.. :Authors: - Cyrus Omar

.. title:: Program Editors

Overview
========

TODO: Overview

Language Servers
================

TODO: OCaml language server paper, others

Structure Editors
=================

TODO: historical examples, studies, etc.

Visual Programming Languages
----------------------------

TODO: examples, cognitive dimensions studies, etc.

Program Navigation
==================

TODO: code bubbles and related work

Collaborative Editing
=====================

TODO: Thomas' papers, and other related work

TODO: work on operational transforms, CRDTs, and other techniques

TODO: work on version control systems

Accessibility
=============

Introduction and Overview
----------------------------

Accessibility in computing refers to the development and design of both software and hardware systems to be usable by people with disabilities. Broadly, "Providing accessibility means removing barriers that prevent people with disabilities from participating in substantial life activities, including the use of services, products, and information." :cite:`bergman1995towards`. This includes providing screen readers for those with visual impairments and alternative input devices for those with motor impairments. 

Additionally, advances in computing technology over the previous decades have enabled richer communication for individuals with impairments. For example, augmentative and alternative communication (AAC) tools such as video calling or speech generating devices assist individuals with impairments in producing or comprehending speech.

First, This section will briefly give some context by going over some historic events regarding the accessibility of computing. Next, this section will discuss accessible design philosophy in general and some important characteristics. Finally, this section will discuss three important areas within that space as they relate to programming interfaces specifically: tools for programmers with visual impairments, tools for programmers with motor impairments, and writing accessible software. This section discusses those two types of impairments specifically as they are highly relevant to programming tasks and most research seems to be centered around those categories.

History
----------------------------

Although personal computers were first sold to the general public in the 1970s, the process of making this technology accessible began to become more common around 1990. **For example:**

.. container:: bib-item

  .. bibliography:: program-editors2.bib
    :filter: key == 'cooke'

  The IBM Screen Reader for DOS was created in 1986 (initially only for employees).

.. container:: bib-item

  .. bibliography:: program-editors.bib
    :filter: key == 'history'

  In 1995, Windows 95 became the first Windows OS to have built in accessibility features, rather than as add-ons. 

.. container:: bib-item

  .. bibliography:: program-editors.bib
    :filter: key == 'ada'

  It’s also important to note that the Americans with Disabilities Act (ADA) was passed in 1990.

**Accessibility research** also appeared around this time. Like many HCI topics, it first emerged from the field of **human factors.** 

.. container:: bib-item

  .. bibliography:: program-editors.bib
    :filter: key == 'vanderheiden1990thirty'

  Vanderheiden highlights the need to consider individuals with impairments in product design and development. 

.. container:: bib-item

  .. bibliography:: program-editors.bib
    :filter: key == 'bergman1995towards'

  Bergman and Johnson provide an overview of accessibility as it relates specifically to HCI; Readers should refer to this work for an in-depth history. Note that more up to date accessibility standards exist.

Background
----------------------------

Modern work has continued to explore **design philosophies** of accessible computing.

.. container:: bib-item

  .. bibliography:: program-editors.bib
    :filter: key == 'wobbrock2011ability'

  Notably, Wobbrock et al. propose a shift in the frame of reference for thinking about accessible interfaces from disability to ability, and encourage designers to think about and adapt to what users can do. Specifically, the authors note that the goal that existing assistive technology holds of "fitting non-standard users to a standard system" has a few disadvantages: first, that the burden of procurement and change is placed on the user; and second, that it can create 'separate but equal' solutions. Instead, what if it was up to the system to model the user’s abilities and make the necessary adaptations automatically?

  The authors present seven principles for this design approach: 
  
  1. Ability: Focus on what users can do
  2. Accountability: Change systems, not users
  3. Adaptation: Interfaces match to users’ abilities
  4. Transparency: Interfaces give awareness of adaptations
  5. Performance: Systems may model user performance
  6. Context: Systems may model the effects of different contexts
  7. Commodity: Systems may use low-cost, available hardware.
 
Visual Impairments
----------------------------
Many programming environments are not purely text based, and use layout, icons, color, and other visual indicators to communicate code structure, known as 'secondary notation'. Additionally, many IDEs will convey real time error and debug information which can be extremely valuable; similarly programming courses often use diagrams to convey abstract concepts.

Traditional screen readers may not convey all of this information to visually impaired developers:

.. container:: bib-item

  .. bibliography:: program-editors.bib
    :filter: key == 'doustdar_2016'

  A blog post explaining the experiences of a blind programmer.

Thus, prior research has analyzed typical behaviors of developers with visual impairments and has proposed systems to aid them in various tasks.
 
Behaviors of Blind Programmers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
First and foremost, it’s important to have an understanding of how blind software developers currently use the tools available to them.

.. container:: bib-item

  .. bibliography:: program-editors.bib
    :filter: key == 'mealin2012exploratory'

  Mealin and Murphy-Hill conducted an exploratory study to understand the tools and practices that blind developers use and problems that they face while working. They aimed to characterize behavior through four research questions:

  1. What tools do blind software developers use?
  2. What practices do blind software developers use?
  3. How do blind software developers collaborate with other software developers?
  4. What attitudes do blind software developers hold about software development?
  
  They conducted qualitative interviews with eight developers with varying amounts of experience. Significant findings are summarized below:

  1. All particpants relied heavily on screen readers. Two participants noted that braille displays were useful for matching parenthesis. A wide range of IDEs were used. Debuggers were rarely used.
  2. Participants relied heavily on documentation and keywords to understnad code structure. Participants often also used temporary text files to save variable names or quickly edit single blocks.
  3. Participants reported mixed success communicating with coworkers using visual diagrams; some translated them to text, while others reported that complex diagrams were often too abstract and were inaccessible.
  4. Generally, participants noted difficulty with tasks that have a visual component, and also finding math formulas and research online.

.. container:: bib-item

  .. bibliography:: program-editors.bib
    :filter: key == 'armaly2017comparison'

  Armaly et al. conducted a study comparing reading behaviors between blind and sighted programmers. They asked 12 blind developers to read and summarize code, tracking their cursor and mouse movements, and compared the observed behaviors to a previous eye tracking study. They found that both groups prioritized reading method signatures, and that blind programmers returned to method signatures more often, highlighting the importance of readable function names.

Assistive Software for Blind Programmers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A variety of tools have been developed to improve upon the accessibility of programming languages and development environments in general. 

One example is CodeTalk, a programming environment that attempts to extend the benefits of fully-featured IDEs to visually impaired developers.

.. container:: bib-item

  .. bibliography:: program-editors2.bib
    :filter: key == 'codetalk'

  CodeTalk offers a variety of features focusing on four areas: 
  
  1. Discoverability: Allow the user to find features in a system to increase proficiency over time
  2. Glanceability: Unobtrusively provide input to the IDE user about code structure and context
  3. Navigability: Allow the user to quickly navigate through code blocks and files across windows
  4. Alertability: Allow the user to access to real-time information

  Features include quick ways to get context of the current cursor location, and auditory cues while debugging (which are incredibly customizable). CodeTalk was evaluated through a qualitative exploratory study and survey of six participants, and is currently available as an extension for Visual Studio. One quote from a participant was particularly telling:

    *“I never knew how much information I was not getting because I was using a screen reader. I had no clue sighted users had this much information available.”* (P1)

.. container:: bib-item

  .. bibliography:: program-editors2.bib
    :filter: key == 'sanchez2005blind'

  APL (Auditory Programming Language) is a programming language designed specifically for blind developers that uses both sound icons and text. Preliminary findings indicate that rich audio environments may better support blind developers mental models.
 
Additionally, prior research has explored more task specific tools:

.. container:: bib-item

  .. bibliography:: program-editors2.bib
    :filter: key == 'baker2015structjumper'

  StructJumper is an extension for Eclipse that creates a tree structure from code to help blind programmers navigate code. StructJumper was evaluated by 7 blind developers. Participants were asked to complete a series of tasks with and without the extension, and found that StructJumper allowed participants to complete tasks faster than without.

.. container:: bib-item

  .. bibliography:: program-editors2.bib
    :filter: key == 'potluri2019ai'

  Potluri et al. consider tools that could assist with the task of UI design. The authors describe existing methods that blind and low-vision creators use to get a sense of UI aesthetics, including physical prototyping, and discuss the potential use of AI for assistance in this task, especially for higher-level features, such as color and general ‘look’.
 
Programming Education for Students with Visual Impairments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As previously mentioned, programming education often uses diagrams to represent abstract concepts, a barrier for visually impaired students. A variety of tools have aimed to address this and related issues:

.. container:: bib-item

  .. bibliography:: program-editors2.bib
    :filter: key == 'stefik2011design'

  Stefik et al. present an educational infrastructure for blind and visually impaired middle and high school students that consists of Sodbeans, an auditory programming environment, Hop, a programming language, and a multi-sensory curriculum. They conducted an empirical study at a programming summer camp with 12 blind participants to evaluate their framework. 

.. container:: bib-item

  .. bibliography:: program-editors2.bib
    :filter: key == 'milne2018blocks4all'

  Similarly, Blocks4All is a block-based, touchscreen programming environment aimed at elementary aged students. The authors identify accessibility barriers, as well as appropriate touchscreen interactions.

Motor Impairments
----------------------------
Motor impairments also require input devices other than the traditional keyboard and mouse, which can be painful or impossible to use for some. One alternative mode is speech based interaction.

.. container:: bib-item

  .. bibliography:: program-editors2.bib
    :filter: key == 'begel2006assessment'

  For example, Begel and Graham evaluate a speech-based programming system called SPEED (SPEech EDitor). The system presented uses additional contextual information provided by the code to filter out incorrect and inappropriate interpretations, leaving the human programmer to intervene only when the computer cannot fully disambiguate. The paper describes two studies: one performed with an automated speech recognizer, and one Wizard of Oz study.

  They found that participants were hesitant to speak natural language words, and requested additional features, such as access to code templates in Eclipse, autocompletion, and other additional commands. However, it’s important to note that they evaluated this system with programmers who did not have motor disabilities, but by virtue of their careers, were at risk for repetitive strain injuries. Overall though, the evaluation and issues uncovered with this system point to an extremely high need for customizability and higher efficiency in code speaking systems.

.. container:: bib-item

  .. bibliography:: program-editors2.bib
    :filter: key == 'saphra_2019'

  Naomi Saphra describes in a blog post the challenges faced by a developer who lost the use of her hands. She uses Talon, a highly customizable speech recognition system to program. For example, she has custom speech commands for open parenthesis, close parenthesis, and pairs of parenthesis. Additionally, she describes her "most precious script": an indexed clipboard where she can quickly copy snippets and assign them spoken command names for fast access later. Clearly, Talon is a powerful system. 
  
  However, despite the improvements, speech recognition systems are limited in a variety of ways:

    *“Speech recognition technology is not perfect, and the error rate is even higher if you have an unusual accent. Furthermore, it may force you to take time off from programming every time you develop a cold or sore throat. I live in fear of even minor colds.”*
 
Writing Accessible Software
-----------------------------
Despite decades of accessibility research, a large proportion of software systems, websites, and mobile apps are not accessible to those that rely on screen readers or other accessibility technologies. Those who create such systems may justify this choice in a variety of ways, for example, they may not know how, they may consider it 'too expensive', or they may delay adding accessibility features but say they will be added later.

Yet, there are many clear obligations and benefits to creating accessible software, for example, features may be useful in a wide range of cases, such as temporary or situational disabilities; there is an economic benefit created by boosting productivity; and finally, there are legal and moral imperatives. Prior work has tried to address this issue in a variety of ways.

.. container:: bib-item

  .. bibliography:: program-editors3.bib
    :filter: key == 'ludi2007introducing'

  One method for improving software accessibility may be to educate people about the importance sooner. This paper presents a study in which people with disabilities gave feedback on projects in an undergraduate course. Overall, this did provide some benefit to correcting student’s misconceptions and introduce more nuance into how they thought about users, instead of simply listing one category of ‘disabled users’ in their design process. Generally, the approach does not scale well.

.. container:: bib-item

  .. bibliography:: program-editors3.bib
    :filter: key == 'choo2019examining'

  Another potential barier is that non-disabled users may not know how a disabled user would experience their software. This paper explores using virtual reality (VR) to simulate vision impairments for accessibility testing.

.. container:: hidden

  :cite:`mealin2012exploratory`
  :cite:`armaly2017comparison`
  :cite:`doustdar_2016`
  :cite:`wobbrock2011ability`
  :cite:`bergman1995towards`
  :cite:`vanderheiden1990thirty`
  :cite:`ada`
  :cite:`history`
  :cite:`cooke`
  :cite:`sanchez2005blind`
  :cite:`codetalk`
  :cite:`baker2015structjumper`
  :cite:`potluri2019ai`
  :cite:`stefik2011design`
  :cite:`milne2018blocks4all`
  :cite:`saphra_2019`
  :cite:`begel2006assessment`
  :cite:`ludi2007introducing`
  :cite:`moreno2010toward`
  :cite:`gonzalez2005platform`
  :cite:`choo2019examining`