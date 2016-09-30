# cz1003project
**NTU Library Assistant**

**User Manual**

User manual of NTU Library Assistant

Thank you for using our bot. Please read this manual carefully for the
better use of the software.

**Contents**

Chapter 1 Introduction

1.1 Overview

2.  System Requirements

3.  Conventions

Chapter 2 Getting Started

Chapter 3 Finding a Seat in the lirary

3.1 Whether the Libraries are Open

3.2 Which Library is the Nearest

3.3 How Many People are There

3.4 How Many People will be There

**Chapter 1 Introduction**

**1.1 Overview**

This bot is a software designed for students who are looking for seats
for self- study in the libraries in NTU. It offers the following
information about the libraries: the opening time, the exact location,
the current and past-time status of selectable sections.

**1.2 System Requirements**

The bot requires Telegram versions released after 9 April, 2016 or
Telegram Web.

**1.3 Conventions**

In order to simplify the description, we define “Lee Wee Nam Library ”
as “LWN Lib”; “Business Library” as “BIZ Lib”; “Humanities & Social
Sciences Library ” as “HSS Lib”; “Chinese library” as “CHN Lib”; “Art,
Design & Media Library ” as “ADM Lib” in the program and the following
chapters.

**Chapter 2 Getting Started**

You should first open Python3 Shell and open file “cz1003bot.py”. Then
click “Run” and choose “Run Module” to start the bot. You will be able
to see the text “Listening ...” printed on the screen.

**Chapter 3 Finding a Seat in the Library **

**3.1 Whether the Libraries are Open**

While you start the bot, your message is read by the program. Then you
can receive outcome on whether the libraries are open. If the message is
not sent during opening time, the bot will inform you that the libraries
are closed by printing texts on the screen. Otherwise, you will be able
to see a greeting “Welcome to NTU library assistant, what can I do for
you?” and two buttons showing “Library Current Status Inquiry” and
“Library Status Prediction”. This means you are now able to view the
information about the libraries.

**3.2 Which Library is the Nearest**

If you want to find out the nearest library, you should first log on in
the opening time and lick the “Library Current Status Inquiry” button.
Then the bot will show you six keyboard buttons “Nearest Lib”, “LWN
Lib”, “BIZ Lib”, “HSS Lib”, “CHN Lib” and “ADM Lib”. You can then click
“Nearest Lib” to submit your coordinate and the program will
automatically return the library which has the smallest straightaway
distance from where you are. After that, you will be asked to choose the
floor and section of the chosen library.

**3.3 How Many People are There**

After starting the bot at the opening time of the libraries and
selecting “Library Current Status Inquiry”, you can see the bot presents
“Please Choose Your Library” and afterwards “Please Choose Your Floor
and Section”. Then you can choose the library and section you want, so
that the bot is going to consult the data and tell you the exact number
of seats available. Meanwhile, the program will also make a comment on
it ( More than 10 seats available will be considered as ”lots of space!”
).

**3.4 How Many People will be There**

This bot also offers the function to predict how many people will be in
the section you are going to. Accessing the interface where two buttons
“Library Current Status Inquiry” and “Library Status Prediction” are
presented, you are expected to click on the latter. After that, do the
same as the above-mentioned step to focus on one section. The program
will return you a computed number, which is the average of the last
several sets of data collected.
