# Data is the new oil

The simulation does not currently log any data about the state of the simulation over time. A good simulation will log certain key metrics, including total food collected, and food collected per time step.

**What you need to do:**
- **Task 1:** Modify the `Simulation` class to include the following private attributes:
  - `_TotalFoodCollected` - total amount of food collected by all ants and brought back to their nests
  - `__FoodCollectedThisStage` - amount of food collected during the current time step
- **Task 2:** Implement methods to update these attributes as the simulation progresses.
- **Task 3:** Edit `GetDetails` to include a summary of these statistics:
  - Total food collected
  - Food collected in the current time step
- **Task 4:** Test the updated `Simulation` class using the following steps:
  - Start
  - Enter '1'
  - Enter '5'
  - Enter '10'
  - Enter '1'

**Evidence you need to provide:**
1. Your PROGRAM SOURCE CODE for the modified `Simulation` class, including the new attributes and methods.
2. SCREEN CAPTURE(S) showing the above test.
