<!--copied from google classroom, excuse the formatting-->

This question modifies the Skeleton Program to introduce the concept of “Flying
Ant Day”. Introduce a 20% chance of a queen giving birth to a flying ant when the
stage is advanced. A flying ant takes three stages to mature in its own nest and
has a small food capacity of five units. Once it has matured it should move to a
random location within the bounds of the grid and set up a new nest. The new
location should not already contain a nest. The program should tell the user which
cell the flying ant has flown to. The new nest should be set up with the normal nest
parameters as per the simulation. Once a flying ant has set up a new nest, the
flying ant dies.
This question only needs to operate with a simulation starting with a
standard single nest.
What you need to do
Task 1
Create a new FlyingAnt class with the required methods to operate as described.
Update the Nest class to introduce a 20% change of a FlyingAnt being instantiated
when the stage is advanced. Modify the AdvanceStage method in the Simulation
class to inform the user when a FlyingAnt is born and when it has flown the nest to
set up a new nest. When setting up a new nest, cull the FlyingAnt.
Task 2
Test that the changes you have made work:
• Run the Skeleton Program.
• Enter 1 to start simulation 1.
• Enter 5 to advance multiple stages.
• When prompted, enter 5 stages. (More stages may be required if the
simulation does not instantiate a flying ant in this time.)
• Show the program displaying a suitable message that a flying ant has been
created and where it is setting up a new nest.
• Enter 4 three more times to advance the simulation three stages.
• Enter 1 to display the overall details of the simulation.
• Show the program displaying more than one nest in the simulation.
