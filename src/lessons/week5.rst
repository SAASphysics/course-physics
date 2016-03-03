Week 5 Materials  
################

:date: 2016-01-11
:summary: Energy and interactions and potential energy and dissipation
:category: lessons
:tags: energy, conservation, closed, open, elastic, kinetic, collision, potential, interaction



=====
Day 1
=====

 1. Debrief the nail-drop experiment. What should we have expected to see?

 2. Potential energy and why is there a one-half in the kinetic energy equation?

 3. New homework assignment and project problems



What was the velocity of the block of wood, just before it impacts the nail?

:math:`\begin{eqnarray}
acceleration:&&& a(t) &=& a\\
velocity:&&& v(t) &=& v_i + at\\
position:&&& x(t) &=& x_i + v_it + \frac{1}{2}at^2\\
combine 2 \& 3:&&& v_f^2 - v_i^2 &=& 2a\Delta x
\end{eqnarray}`

These are the kinematic equations, which we got by using the "area under the line" argument earlier in the year.  Equation (4) tells us the velocity as a function of displacement when the acceleration is constant.  In this case, the initial velocity is zero, the acceleration is due to gravity (so :math:`a = g` or :math:`9.8 \frac{m}{sec^2}`), and the displacment is the height the block is dropped from (:math:`\Delta x = h`).

This means that

:math:`\begin{eqnarray}
v_f^2 &=& 2gh\\
v_f &=& \sqrt{2gh}
\end{eqnarray}`

The kinetic energy at impact is the kinetic energy associated with the mass of the block of wood at this impact velocity, 

:math:`\begin{eqnarray}
KE_{impact} & = & \frac{1}{2}mv^2 \\
& = & \frac{1}{2}(m)(\sqrt{2gh})^2\\
& = & mgh
\end{eqnarray}`

This impact kinetic energy in (9) is definitely linearly proportional to mass and to the strength of gravity and to the height we drop the block from.  Does that mean that the penetration depth of the nail into the styrofoam block should be linearly proportional to those?


Not necessarily.

It depends on what kind of material we are talking about.  Imagine running on the beach, near the wet sand / dry sand line.  If you *run*, the sand feels like concrete -- a big impact kinetic energy leads to a very small penetration depth.  If you walk slowly or stand still, your feet will slowly sink into the sand -- a small impact kinetic energy can lead to a very large penetration depth.

If you put a nail into silly putty and hit it with a block, small drop heights will lead to larger penetration depths.  But for large drop heights (and corresponding large impact kinetic energies), the putty response can be so strong as to drive the nail *back upward*.  

So in those two cases, the penetration depth is *not* linearly proportional to the dropped mass or the drop height even thoug the impact kinetic energy is, because those materials respond in a "weird" way.

But for "normal" materials, and in this case, styrofoam is a "normal" material, the penetration depth *is* linearly proportional to the impact kinetic energy, because, if you think about it, what the styrofoam does is to stop the nail completely by entirely dissipating the kinetic energy at impact into heat, sound, and splitting the foam apart.  If the penetration depth is doubled, that means that twice the foam has been split, twice the heat has been generated, etc.  If you the depth is cut in half, then half as much of the foam has been destroyed, thus half as much energy has been dissipated.

So if the dissipated energy is directly proportional to the depth, and the dissipated energy is *equal* to the impact kinetic energy (and it has to be, right?), then the impact kinetic energy is proportional to the depth.  So:

:math:`\begin{eqnarray}
Depth & \propto & E_{dissipated} = KE_{impact} = mgh\\
Depth & \propto & mgh
\end{eqnarray}`

the depth is linearly proportional to the mass, the strength of gravity, and to the drop height.

And, coincidentally, this expression :math:`mgh` is what we also call Gravitational **Potential Energy** -- this is the energy you put into the block by lifting it up into the air, which you get back as kinetic energy when you drop it, and which you lose to heat and sound and ripping when the nail is stopped by the styrofoam.



=====
Day 2
=====

 1. QUIZ
 2. Choose project problems
 3. Problem 7.4 from last week's homework:

We discussed this problem yesterday, but I thought it would be worthwhile to write about it here.  The question asked to figure out the ratio of the velocities of two objects that start at rest and then "interact" *somehow*, without specifying what kind of interaction it is.  One of the keys here is that *it doesn't matter what kind of interaction it is* -- there are things that we can predict about the result of *any* interaction.

So what do we know?

We know that the momentum is always conserved in closed systems.  This is equivalent to the statement that the changes in the two momenta are equal and opposite (Newton's third law):

:math:`\begin{eqnarray}
\text{Equal & opposite}:&&& \Delta p_1 & = & - \Delta p_2\\
:&&&m_1 v_{1f} - m_1 v_{1i} & = & - (m_2 v_{2f} - m_2 v_{2i})\\
V_i \text{  is Zero}:&&&m_1 v_{1f} & = & -m_2 v_{2f}\\
\text{Divide to get ratios}:&&&\frac{v_{1f}}{v_{2f}} & = & - \frac{m_2}{m_1}
\end{eqnarray}`

Why is it negative?  (Because the objects move off in opposite directions)

Why are the masses flipped from the velocities?  (Because the bigger mass picks up a smaller velocity and the smaller mass a bigger velocity)

All of algebra (and much of physics) is saying the same thing many times in different ways, to make it easier to recognize what was true but not apparent in the first statement.  In this case, the first statement is that momentum is conserved.  It turns out that this means that the velocities are in an inverse ratio to the masses.




=====
Day 3
=====

 1. Newton's 2nd
 2. Free body diagrams
 3. Project time

=====
Day 4
=====

 1. Quiz debrief
 2. Project time



