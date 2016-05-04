Title: Design Considerations
Date: 2016-04-20
Tags: design, ubd
Category: overview
Summary: Simplified UBD template for the course




## Stage -1 - Goals

Optimizing on multiple axes at a time.  This is a recipe for madness:

*   Why.  (Philosophical purpose of class)
    *   

*   What. (Content and skills covered, assessed)
*   How.  




## Stage 0 - Assumptions

*   Audience
    *	Seniors who have not yet completed calculus
    *   Who have chosen this class for a variety of reasons
    *   Who have had an open-ended conceptual physical science course as 9th graders
    *   Who are all going to college  

*   Constraints
    *   Time
        *   Three 45 minute, one 95 minute session per week
        *   Two 11 week trimesters, one 4 week trimester
        *   Many broken weeks due to field trips, holidays, etc.
        *   Many absences due to extracurriculars, college meetings, etc.
        *   About 75% of seat time of "typical" 12th grade class
    *   Math experience
        *   Range from Algebra 3 to Precalculus to Calculus I
        *   All can compute slope, can graph, can solve linear and some quadratic equations
        *   Many are not clear on relationship between slope and rate of change
        *   All exposed to trig functions, few are totally comfortable with them
    *   Programming environment
        * wide range of experience, from None to Guru
        * [vpython](http://vpython.org "vpython") in [Jupyter](http://jupyter.org "Jupyter notebook") has debugging, exposes all of python and Pandas, docker/binder for pushing, github integration, ecosystem
    *   WORK
        * homework completion is poor and has not shown much benefit
        * 90% of work will need to be done in class
        * must have make-up plan for every class session (as in, How will student make up for having missed this?)

	
*   Lesson materials
    *   One lesson per week documenting the plan and what actually happened
    *   Gallery of pages, Notebooks, Desmos graphs, assignments, etc. organized by topic/tag
    *   [polleverywhere][polleverywhere] -- will design clicker personal response questions through polleverywhere 
    *   May use Haiku learning for SBG gradebook


*   See also:
    *   Links to similar courses and class materials 

## Stage 0.5 - Some project ideas

This is out of order for UBD, but I have to write them down

*   AAPT Photo contest
*   Framing device (?) of exploring the universe - start with special relativity
*   Coding challenges
*   Better know a scientist
*   Construct an exemplar problem for each unit.  Other students read all, solve one or two, and vote on best (for pedagogy and for interest) -- I use results to choose problems for the next year
*   Some students work as Learning Assistants in Science9 (or 6,7,8)
*   Students prepare and deliver outreach materials for middle school / community


## Stage 1 - Desired Results

### Goals

Big Ideas

 * I can use the ideas and methods of physics and science to better understand the world 
 * I can be a physicist / scientist
 * I can explain examples of the role physics has played in human history and culture
 * I can explain examples of the role culture has played and does play in physics as a discipline and a career
 * I can explain some of the most common barriers to success in physics as a class and as a career
 * Conservation laws constrain the possible results of interactions

Scientific Practices

 * I can use representations and models to communicate physical phenomena and solve problems
 * I can use mathematics appropriately
 * I can ask questions to extend my thinking and to guide investigation
 * I can plan and implement data collection strategies
 * I can perform data analysis and evaluation of evidence
 * I can use scientific explanations and theories to predict and to explain
 * I can construct models using appropriate tools and methods

[Core Skills / Concepts / Descriptions](standards.html "Standards")

 * Motion
     *  I know the difference between position, distance, and displacement
     *  I know the difference between speed and velocity
     *  I can solve problems involving average speed and velocity
     *  I can interpret/draw motion maps for objects moving with constant velocity
     *  I can interpret/draw position vs. time graphs for objects moving with constant velocity
     *  I can interpret/draw velocity vs. time graphs for objects moving with constant velocity
     *  I can translate between motion maps, position vs. time graphs, and velocity vs. time graphs
     *  I recognize when the constant velocity model applies and I use it when appropriate
     *  I can articulate the difference between a vector and a scalar
     *  I can find the magnitude of a vector
     *  I can use vector notation for appropriate quantities
     *  I can calculate the average velocity and speed of an object
     *  I can use the position update formula to relate changes in the position of an object to its average velocity
     *  I can use the position update formula to calculate the time take for an object to move from an initial to a final position

 * Acceleration
     *  I know the difference between acceleration and velocity
     *  I can calculate the acceleration of an object with direction and proper units
     *  I can interpret/draw motion diagrams for objects moving with changing velocity
     *  I can interpret/draw the position vs. time graph for an object moving with changing velocity
     *  I can interpret/draw the velocity vs. time graph for an object moving with changing velocity
     *  I can use motion concepts to solve problems involving objects with changing velocity
     *  I can use the position update formula to solve problems involving objects with changing velocity
     *  I can explain the relationship between the position update formula and graphical representations of an object's motion
     *  I can explain the relationship between the position update formula and functional representations of an object's motion

 * Momentum
     *  I can write the definition of momentum
     *  I can calculate the momentum of an object at any speed, with direction and proper units
     *  I can calculate the average rate of change of momentum


 * Energy

 * Interactions
     *  I can provide arguments for whether interactions are present in a given situation
   

 * Force
     *  I know the relationship between acceleration, force, and mass  
     *  I can use interaction and force concepts to solve problems involving objects with changing velocity

 * Work
 * Motion in a plane
    *  I can find the magnitude of a multi-component vector
    *  I can calculate the unit vector in the direction of a specified vector
    *  I can add and subtract vectors graphically and algebraically
    *  I can calculate the change in a vector quantity graphically and algebraically 
    *  I can draw arrows to represent the velocity or momentum of an object at a particular location along its trajectory


 * Gravitation
 * Special Relativity
    *  I can articulate when it is appropriate to use a non-relativistic approximation



 * Programming
   * I can write a correctly working program that has all the required features
   * I can output values that are labeled and have correct units
   * I can write a program with logical variable names, structure, and organization
   * I can use documentation to describe the physical reasoning and the function of the code
   * **I can write and analyse an accurate simulation of BLANK**



1.  Get learners to the stage decribed in the "Software" section of
    "[Good Enough Practices in Scientific Computing][good-enough]".
    *   Goals
        1.  Make it easy for people (including your future self) to understand and (re)use your code
        2.  Modular, comprehensible, reusable, and testable all come together
    *   Rules
        1.  Every analysis step is represented textually (complete with parameter values)
        2.  Every program or script has a brief explanatory comment at the start
        3.  Programs of all kinds (including "scripts") are broken into functions
        4.  No duplication
        5.  Functions and variables have meaningful names
        6.  Dependencies and requirements are explicit (e.g., a requirements.txt file)
            *   This rule is *not* covered in this lesson
        7.  Commenting/uncommenting are not routinely used to control program behavior
        8.  Use a simple example or test data set to run to tell if it's working at all and whether it gives a known correct output for a simple known input
        9.  Submit code to a reputable DOI-issuing repository upon submission of paper, just like data
            *   This rule is *not* covered in this lesson
2.  Enable them to make sense of other onlines tutorials and resources

### Summative Assessment

*   Midpoint: plot bar chart showing average GDP per continent
*   Final: debug and extend a short multi-function program to handle data laid out differently

### Essential Questions

How do I...

*   ...read, analyze, and visualize a tabular data set?
*   ...process multiple data sets?
*   ...tell if my program is working correctly?
*   ...fix it when it's not?
*   ...find and use software other people have written instead of writing my own?

### Learners Will Be Able To...

*   Run code interactively
*   Run code saved in a file
*   Write single-condition `if` statements
*   Convert between basic data types (integer, float, string)
*   Call built-in functions
*   Use `help` and online documentation
*   Import a library using an alias
*   Call something from an imported library
*   Read tabular data into an array or data frame
*   Do collective operations on arrays and data frames
*   Create simple plots of data in arrays and data frames
*   Interpret common error messages
*   Track down bugs by running small tests of program modules
*   Write non-recursive functions taking a fixed number of named parameters
*   Create literate programs in the Jupyter Notebook

### Learners Will Know...

*   That a program is a piece of lab equipment that implements an analysis
    *   Needs to be validated/calibrated before/during use
    *   Makes analysis reproducible, reviewable, shareable
*   That programs are written for people, not for computers
    *   Meaningful variable names
    *   Modularity for readability as well as re-use
    *   No duplication
    *   Document purpose and use
*   That there is no magic: the programs they use are no different in principle from those they build
*   How to assign values to variables
*   What integers, floats, strings, and data frames are
*   How to trace the execution of a `for` loop
*   How to create and index lists
*   How to trace the execution of `if`/`else` statements
*   The difference between defining and calling a function
*   What a call stack is
*   Where to find documentation on standard libraries
*   How to find out what else scientific Python offers

## Stage 2 - Learning Plan

### [Identity](identity.html)

*   Teaching: 3 days
*   Topics: history, implicit association, career statistics, personal stories, learning model, class model
*   Exercises: 0 min (accounted for in teaching time - no separate exercise)
    *   Run the Notebook
    *   Create a few Markdown cells (just formatted)
    *   Create and execute a Python cell that prints 1+2 (to show that cells can be executed)

### [Problem Solving](problems.html)
	
*   Teaching: 2 days
*   Topics: estimation, problem solving process and rubric
*   Exercises: 5 min
    *   Trace behavior of swapping values of two variables using an intermediate variable
    *   Calculate elapsed time in seconds using named values for seconds per minute, etc.

### [Motion](motion.html)

*   Teaching: 8 days
*   Topics: constant velocity, graphing, predicting position
*   Exercises: 5 min
    *   Predict result types (or errors) of various operations
    *   Add conversion functions to broken code to make it work

### [Built-in Functions and Help](04-built-in.html)

*   Teaching: 10 min
    *   Include re-running cells and re-running all
*   Exercises: 10 min
    *   Chain calculations with max and min
    *   Find a useful method using help(str)
    *   Parsons Problem to achieve specific results with string methods

### [Error Messages](05-error-messages.html)

*   Teaching: 5 min (review of error messages seen to date)
*   Exercises: 10 min
    *   Identify causes of common errors (but don't actually fix)

### [Libraries](06-libraries.html)

*   Teaching: 5 min
*   Exercises: 5 min
    *   Operations with math library
    *   Look things up in the python.org docs

### *[Coffee: 15 min](07-coffee.html)*

### [Reading Tabular Data](08-reading-tabular.html)

*   Teaching: 5 min
*   Exercises: 10 min (because some people will have trouble finding the data set's path)
    *   Read one continent's subset of gapminder CSV data
*   Callout:
    *   How to read data from Excel spreadsheets via export to CSV

### [Pandas Data Frames](09-data-frames.html)

*   Teaching: 10 min
*   Exercises: 10 min
    *   Create data frame manually
    *   Select individual values
    *   Select various subsets of data
    *   Normalize values (scale to 0..1)

### [Plotting](10-plotting.html)

*   Teaching: 10 min (to show a variety of plots and debug display problems)
*   Exercises: 10 min
    *   Plot normalized change in GDP over time (tweaking provided code)

### [Lists](11-lists.html)

*   Teaching: 5 min
    *   Note: `range` doesn't produce a simple list in Python 3, so we can't use that for teaching.
*   Exercises: 10 min
    *   Toy examples of lists, indexing, etc.

### [For Loops](12-for-loops.html)

*   Teaching: 10 min
*   Exercises: 10 min
    *   Reverse a string by repeated append
    *   Manually trace execution of loop
    *   Interrupt a running program

### [Looping Over Data Sets](13-looping-data-sets.html)

*   Teaching: 5 min (use `glob` to get filenames)
*   Exercises: 10 min
    *   Count rows of each data set
    *   Check number of columns in each data set is the same

### *[Lunch: 60 min](14-lunch.html)*

### [Conditionals](15-conditionals.html)

*   Teaching: 5 min (show conditionals inside loop)
*   Exercises: 10 min
    *   Count vowels
    *   Report badly-sized files inside loop

### [Writing Functions](16-writing-functions.html)

*   Teaching: 10 min
*   Exercises: 15 min
    *   Check size of a single data file
    *   Check sizes of all data files in a directory
        *   Write new function using previous function

### [The Call Stack](17-call-stack.html)

*   Teaching: 10 min
*   Exercises: 15 min
    *   Add docstrings to functions written earlier

### *[Coffee: 15 min](18-coffee.html)*

### [Defensive Programming](19-defensive.html)

*   Teaching: 10 min
*   Exercise: 15 min

### [Programming Style](20-style.html)

*   Teaching: 10 min (present checklist)
*   Exercises: 15 min
    *   Do a code review

### [Next Steps](21-next-steps.html)

*   Teaching: 15 min
    *   Where to look next
*   Exercises: 0 min

### [Wrap-Up](22-wrap.html)

*   Teaching: 15 min
    *   Where to look next
*   Exercises: 0 min

[dc-website]: http://datacarpentry.org
[gapminder-data]: http://www.gapminder.org/data/
[good-enough]: https://github.com/swcarpentry/good-enough-practices-in-scientific-computing
[instructor-training]: https://swcarpentry.github.io/instructor-training/
[swc-website]: http://software-carpentry.org
[polleverywhere]: http://pollev.com/betnel

1.  Assumptions

2.  Desired results:


3.  Learning plan:
    each episode has a heading that summarizes what will be covered,
    then estimates time that will be spent on teaching and on exercises,
    while the exercises are given as bullet points.

While it looks like a waterfall process, in practice I did this:

1.  Draft the assumptions.

2.  Do one bullet point for each of several learning milestones.

3.  Draft the desired results.

4.  Update the learning milestones (still as just one bullet point each, no time estimates or exercises).

5.  Get early feedback from four people.

6.  Do a full pass to flesh out the assumptions and add time estimates and exercises.

7.  Ask for feedback and start iterating (mostly to cut things).


