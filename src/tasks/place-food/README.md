# Dinner is served

There is no option for the user to amend the simulation as its going by adding food to specific locations. Amend the simulation to allow the user to add food to specific locations during the simulation.

**What you need to do:**
- **Task 1:** Modify `DisplayMenu` to include an option for adding food to a specific location, as '6. Add food to specific location'.
- **Task 2:** Modify `Main` to prompt for row, column, and amount of food to add. Create a new method within `Simulation` named `AddFoodToCellManually` that ensures that the specified location is within the grid boundaries, that the amount of food is a positive integer, and that food is not added to a nest location.
- **Task 3:** Add food to cell at specified location.
- **Task 4:** Test the updated menu by entering the following:
  - Start
  - Enter '1'
  - Enter '5'
  - Enter '10'
  - Enter '6'
  - Enter '3' (row)
  - Enter '4' (column)
  - Enter '200' (amount of food)
  - Enter '1'
  - Enter '6'
  - Enter '2'
  - Enter '4'
  - Enter '200'

**Evidence you need to provide:**
1. Your PROGRAM SOURCE CODE for the modified `DisplayMenu` method and `Simulation`.
2. SCREEN CAPTURE(S) showing the above test.
