# Don't go over the edge!

The GetAreaDetails method retrieves details for a square area defined by the user. There is currently no validation on this grid, leading to potential out-of-bounds errors. Update the `GetAreaDetails` method to ensure it correctly handles edge cases and retrieves details only within the valid grid boundaries.

**What you need to do:**

- **Task 1:** Modify the `GetAreaDetails` method to include validation checks for the specified range. You may not edit the interface of the `GetAreaDetails` method.
- **Task 2:** If the specified range exceeds the grid boundaries, warn the user; any out of bounds values should be set to their maximum, acceptable values.
- **Task 3:** Test the updated method by entering the following:
  - Start
  - Enter '1'
  - Enter '2'
  - Enter '2'
  - Enter '2'
  - Enter '9'
  - Enter '3'

**Evidence you need to provide:**
1. Your PROGRAM SOURCE CODE for the amended `GetAreaDetails` method.
2. SCREEN CAPTURE(S) showing the above test.
