# Presentation matters

To best visualise this simulation, the program needs to shift from presenting the output as a list of text data to a 2D Grid / Board Game. Currently, the program runs in the console and outputs linear lists of coordinates, which makes it very hard to see the "big picture."

**What you need to do:**
- **Task 1:** Modify `DisplayMenu` to include an option for viewing the world '7. World view'.
- **Task 2:** Modify `Main` to allow this menu choice. Create a new method within `Simulation` named `DisplayGrid` that converts the map data into an 2D ASCII grid where a Nest is represented by 'N', an Ant by 'A', Food by 'F' and an empty space with '.'.
- **Task 3:** Test the updated menu by entering the following:
  - Start
  - Enter '1'
  - Enter '7'
  - Enter '4'
  - Enter '7'

**Evidence you need to provide:**
1. Your PROGRAM SOURCE CODE for the modified `DisplayMenu` method and the newly created method `DisplayGrid`.
2. SCREEN CAPTURE(S) showing the above test.
