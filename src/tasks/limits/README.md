# Stay within our limits

Currently, ants have an unlimited range that they can move within the grid. This is unrealistic, as ants typically have a limited range from their nest. Modify the `AdvanceStage` method to limit the movement of ants to a maximum distance from their nest. If an ant attempts to move beyond this range, it should be prevented from doing so and should instead stay in its current position.

The ant's maximum distance from the nest should be a private attribute of the `Ant` class that defaults to 5.

Distance from the nest should be calculated using the Manhattan distance formula, which is the sum of the absolute differences of their Cartesian coordinates. For example, if an ant is at position (x1, y1) and its nest is at position (x2, y2), the Manhattan distance would be calculated as |x1 - x2| + |y1 - y2|. This should be a new method within the `Nest` class, which takes an object as a parameter and calculates the distance from the nest to that object.

Ensure that the user is informed whenever an ant is prevented from moving due to this range limitation.

**What you need to do**
- **Task 1**: Modify the `Ant` and `Nest` classes to achieve the above.
- **Task 2**: Test the changes you've made, by running the simulation for 10 stages or until an ant is prevented from moving due to the range limitation (whichever occurs earliest). Run the simulation for a further 5 stages.

**Evidence that you need to provide**
1. Your PROGRAM SOURCE CODE for the modified `Ant` and `Nest` classes, as well as any other methods or subroutines changed.
2. SCREEN CAPTURE(S) for the above task.
