Week 2 Materials  
################

:date: 2015-12-07
:summary: Starting off with energy, hour of code
:category: lessons
:tags: energy, conservation, closed, open, elastic, kinetic, collision, simulation, trinket



=====================
Simulating Collisions
=====================

.. raw:: html

  <iframe src="https://trinket.io/embed/glowscript/ae714e24b9" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
..

 1. This trinket shows a "correct" way to handle acceleration.  Notice that it uses the formula for displacement that we obtained in chapter 3 as the "update" method.  At every moment in time, the way you find out where the particle goes in the next instant, you have to ask how far it will move in the next instant.  This depends on the current speed, the duration of the next instant (are you looking 1 second into the future?  Or 0.1 seconds into the future?), and how much the object accelerates during this instant (finding the area of the velocity curve).

:math:`x(now + dt) = x_{now} + v_{now}\cdot dt + 0.5 a (dt)^2`

the first term tells you where you are now, the second term tells you how far you would move if you were going at a constant velocity, and the third term tells you how far you move because of the acceleration.

 2. Make a copy of your most recent coding assignment, title it (your last name - ch5b - bounce), and update it to use this method for finding the position of the cars.

 3. Figure out how to make the cars bounce off each other *using the positions of the cars as the condition to stop*.

 4. If the cars bounce off perfectly elastically, what will the new velocities be just after the bounce?

 5. Make your simulation do this:

.. raw:: html

  <iframe src="https://trinket.io/embed/glowscript/53c83f0dc3?outputOnly=true" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
..


 6. How would you change the code to handle bounces that are

  a. perfectly elastic
  b. pefectly inelastic
  c. partially inelastic
  d. with a wall
  e. involving cars of different masses


 7. How could you use the code to compute the momentum and the kinetic energy?  Could you output those numbers to make graphs?

=======
Project
=======

 Make your simulation correctly execute a completely inelastic collision. You should be able to change the masses and initial velocities of the two cars and the program will correctly calculate the result of the collision.

 Produce graphs of the momentum, kinetic energy, velocity, and position of the two cars in the completely inelastic collision.  Write about how these graphs demonstrate that kinetic energy is *not* conserved in an inelastic collision, but that momentum *is*.


   
