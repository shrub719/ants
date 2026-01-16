# Skeleton Program code for the AQA A Level Paper 1 Summer 2026 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.9 programming environment
# Version 2

import random

def Main():
    """Top level function. Big mama."""
    SimulationParameters = []
    SimNo = input("Enter simulation number: ")
    if SimNo == "1":
        SimulationParameters = [1, 5, 5, 500, 3, 5, 1000, 50]
    elif SimNo == "2":
        SimulationParameters = [1, 5, 5, 500, 3, 5, 1000, 100]
    elif SimNo == "3":
        SimulationParameters = [1, 10, 10, 500, 3, 9, 1000, 25]
    elif SimNo == "4":
        SimulationParameters = [2, 10, 10, 500, 3, 6, 1000, 25]
    ThisSimulation = Simulation(SimulationParameters)
    Choice = ""
    while Choice != "9":
        DisplayMenu()
        Choice = GetChoice()
        if Choice == "1":
            print(ThisSimulation.GetDetails())
        elif Choice == "2":
            StartRow = 0
            StartColumn = 0
            EndRow = 0
            EndColumn = 0
            StartRow, StartColumn = GetCellReference()
            EndRow, EndColumn = GetCellReference()
            print(ThisSimulation.GetAreaDetails(StartRow, StartColumn, EndRow, EndColumn))
        elif Choice == "3":
            Row = 0
            Column = 0
            Row, Column = GetCellReference()
            print(ThisSimulation.GetCellDetails(Row, Column))
        elif Choice == "4":
            ThisSimulation.AdvanceStage(1)
            print("Simulation moved on one stage\n")
        elif Choice == "5":
            NumberOfStages = int(input("Enter number of stages to advance by: "))
            ThisSimulation.AdvanceStage(NumberOfStages)
            print(f"Simulation moved on {NumberOfStages} stages" + "\n")
    input()

def DisplayMenu():
    """Print available menu options."""
    print()
    print("1. Display overall details")
    print("2. Display area details")
    print("3. Inspect cell")
    print("4. Advance one stage")
    print("5. Advance X stages")
    print("9. Quit")
    print()
    print("> ", end='')

def GetChoice():
    """
    Receive menu input from the user.
    :return: user input as string
    """
    Choice = input()
    return Choice

def GetCellReference():
    """
    Allow the user to input a cell reference by row and column.
    :return: row, column tuple
    """
    print()
    Row = int(input("Enter row number: "))
    Column = int(input("Enter column number: "))
    print()
    return Row, Column

class Simulation():
    """Simulation class that holds all global variables and class instances part of the simulation."""
    def __init__(self, SimulationParameters):
        """
        Create Simulation object.
        :param SimulationParameters: list of configuration values: [0] StartingNumberOfNests, [1] NumberOfRows, [2] NumberOfColumns, [3] StartingFoodInNest, [4] StartingNumberOfFoodCells, [5] StartingAntsInNest, [6] NewPheromoneStrength, [7] PheromoneDecay 
        """
        self._StartingNumberOfNests = SimulationParameters[0]
        self._NumberOfRows = SimulationParameters[1]
        self._NumberOfColumns = SimulationParameters[2]
        self._StartingFoodInNest = SimulationParameters[3]
        self._StartingNumberOfFoodCells = SimulationParameters[4]
        self._StartingAntsInNest = SimulationParameters[5]
        self._NewPheromoneStrength = SimulationParameters[6]
        self._PheromoneDecay = SimulationParameters[7]
        self._Nests = []
        self._Ants = []
        self._Pheromones = []
        self._Grid = []
        Row = 0
        Column = 0
        for Row in range(1, self._NumberOfRows + 1):
            for Column in range(1, self._NumberOfColumns + 1):
                self._Grid.append(Cell(Row, Column))
        self.SetUpANestAt(2, 4)
        for Count in range(2, self._StartingNumberOfNests + 1):
            Allowed = False
            while Allowed == False:
                Allowed = True
                Row = random.randint(1, self._NumberOfRows)
                Column = random.randint(1, self._NumberOfColumns)
                for N in self._Nests:
                    if N.GetRow() == Row and N.GetColumn() == Column:
                        Allowed = False
            self.SetUpANestAt(Row, Column)
        for Count in range(1, self._StartingNumberOfFoodCells + 1):
            Allowed = False
            while Allowed == False:
                Allowed = True
                Row = random.randint(1, self._NumberOfRows)
                Column = random.randint(1, self._NumberOfColumns)
                for N in self._Nests:
                    if N.GetRow() == Row and N.GetColumn() == Column:
                        Allowed = False
            self.AddFoodToCell(Row, Column,500)

    def SetUpANestAt(self, Row, Column):
        """
        Place a Nest with the starting amount of food.
        :param Row: row of Nest
        :param Column: column of Nest
        """
        self._Nests.append(Nest(Row, Column, self._StartingFoodInNest))
        self._Ants.append(QueenAnt(Row, Column, Row, Column))
        for Worker in range(2, self._StartingAntsInNest + 1):
            self._Ants.append(WorkerAnt(Row, Column, Row, Column))

    def AddFoodToCell(self, Row, Column, Quantity):
        """
        Increase amount of food in a cell.
        :param Row:
        :param Column:
        :param Quantity: quantity of food to add
        """
        self._Grid[self.__GetIndex(Row, Column)].UpdateFoodInCell(Quantity)

    def __GetIndex(self, Row, Column):
        """
        Get 1D list index of a specific grid cell.
        :param Row:
        :param Column:
        :return: index
        """
        return (Row - 1) * self._NumberOfColumns + Column - 1

    def __GetIndicesOfNeighbours(self, Row, Column):
        """
        Get 1D list index of the neighbours of a specific grid cell.
        :param Row:
        :param Column:
        :return: list of indices
        """
        ListOfNeighbours = []
        for RowDirection in [-1, 0, 1]:
            for ColumnDirection in [-1, 0, 1]:
                NeighbourRow = Row + RowDirection
                NeighbourColumn = Column + ColumnDirection
                if (RowDirection != 0 or ColumnDirection != 0) and NeighbourRow >= 1 and NeighbourRow <= self._NumberOfRows and NeighbourColumn >= 1 and NeighbourColumn <= self._NumberOfColumns:
                    ListOfNeighbours.append(self.__GetIndex(NeighbourRow, NeighbourColumn))
                else:
                    ListOfNeighbours.append(-1)
        return ListOfNeighbours

    def __GetIndexOfNeighbourWithStrongestPheromone(self, Row, Column):
        """
        Get 1D list index of the neighbour of a specific grid cell which contains the strongest pheromone.
        :param Row:
        :param Column:
        :return: 1 index
        """
        StrongestPheromone = 0
        IndexOfStrongestPheromone = -1
        for Index in self.__GetIndicesOfNeighbours(Row, Column):
            if Index != -1 and self.GetStrongestPheromoneInCell(self._Grid[Index]) > StrongestPheromone:
                IndexOfStrongestPheromone = Index
                StrongestPheromone = self.GetStrongestPheromoneInCell(self._Grid[Index])
        return IndexOfStrongestPheromone

    def GetNestInCell(self, C):
        """
        Get the Nest object in a specific Cell, or None if there is no cell.
        :param C: Cell object
        :return: Nest object, or None
        """
        for N in self._Nests:
            if N.InSameLocation(C):
                return N
        return None

    def UpdateAntsPheromoneInCell(self, A):
        """
        Make an Ant leave a new Pheromone on the Cell it's currently in.
        :param A: Ant
        """
        for P in self._Pheromones:
            if P.InSameLocation(A) and P.GetBelongsTo() == A.GetID():
                P.UpdateStrength(self._NewPheromoneStrength)
                return
        self._Pheromones.append(Pheromone(A.GetRow(), A.GetColumn(), A.GetID(), self._NewPheromoneStrength, self._PheromoneDecay))

    def GetNumberOfAntsInCell(self, C):
        """
        Get number of Ants in a Cell. (gasp!)
        :param C: cell
        :return: number of Ants
        """
        Count = 0
        for A in self._Ants:
            if A.InSameLocation(C):
                Count += 1
        return Count

    def GetNumberOfPheromonesInCell(self, C):
        """
        Get number of Pheromones in a Cell. (gasp!!)
        :param C: cell
        :return: number of Pheromones
        """
        Count = 0
        for P in self._Pheromones:
            if P.InSameLocation(C):
                Count += 1
        return Count

    def GetStrongestPheromoneInCell(self, C):
        """
        Get strength of the strongest Pheromone in a Cell.
        :param C: cell
        :return: strength of Pheromone
        """
        Strongest = 0
        for P in self._Pheromones:
            if P.InSameLocation(C):
                if P.GetStrength() > Strongest:
                    Strongest = P.GetStrength()
        return Strongest

    def GetDetails(self):
        """
        Get a string representation of the contents of every Cell in the grid.
        :return: multiline string
        """
        Details = ""
        for Row in range(1, self._NumberOfRows + 1):
            for Column in range(1, self._NumberOfColumns + 1):
                Details += f"{Row}, {Column}: "
                TempCell = self._Grid[self.__GetIndex(Row, Column)]
                if self.GetNestInCell(TempCell) is not None:
                    Details += "| Nest |  "
                NumberOfAnts = self.GetNumberOfAntsInCell(TempCell)
                if NumberOfAnts > 0:
                    Details += f"| Ants: {NumberOfAnts} |  "
                NumberOfPheromones = self.GetNumberOfPheromonesInCell(TempCell)
                if NumberOfPheromones > 0:
                    Details += f"| Pheromones: {NumberOfPheromones} |  "
                AmountOfFood = TempCell.GetAmountOfFood()
                if AmountOfFood > 0:
                    Details += f"| {AmountOfFood} food |  "
                Details += "\n"
        return Details

    def GetAreaDetails(self, StartRow, StartColumn, EndRow, EndColumn):
        """
        Get a string representation of the contents of every Cell in a square from (StartRow, StartColumn) to (EndRow, EndColumn).
        :return: multiline string
        """
        Details = ""
        for Row in range(StartRow, EndRow + 1):
            for Column in range(StartColumn, EndColumn + 1):
                Details += f"{Row}, {Column}: "
                TempCell = self._Grid[self.__GetIndex(Row, Column)]
                if self.GetNestInCell(TempCell) is not None:
                    Details += "| Nest |  "
                NumberOfAnts = self.GetNumberOfAntsInCell(TempCell)
                if NumberOfAnts > 0:
                    Details += f"| Ants: {NumberOfAnts} |  "
                NumberOfPheromones = self.GetNumberOfPheromonesInCell(TempCell)
                if NumberOfPheromones > 0:
                    Details += f"| Pheromones: {NumberOfPheromones} |  "
                AmountOfFood = TempCell.GetAmountOfFood()
                if AmountOfFood > 0:
                    Details += f"| {AmountOfFood} food |  "
                Details += "\n"
        return Details

    def AddFoodToNest(self, Food, Row, Column):
        """
        Increase the amount of food in any Nests at (Row, Column).
        :param Food: amount of food to add
        :param Row:
        :param Column:
        """
        for N in self._Nests:
            if N.GetRow() == Row and N.GetColumn() == Column:
                N.ChangeFood(Food)
                return

    def GetCellDetails(self, Row, Column):
        """
        Get a string representation of the contents of the Cell at (Row, Column), with more detail.
        :param Row:
        :param Column:
        """
        CurrentCell = self._Grid[self.__GetIndex(Row, Column)]
        Details = CurrentCell.GetDetails()
        N = self.GetNestInCell(CurrentCell)
        if N is not None:
            Details += f"Nest present ({N.GetFoodLevel()} food)" + "\n\n"
        if self.GetNumberOfAntsInCell(CurrentCell) > 0:
            Details += "ANTS\n"
            for A in self._Ants:
                if A.InSameLocation(CurrentCell):
                    Details += A.GetDetails() + "\n"
            Details += "\n\n"
        if self.GetNumberOfPheromonesInCell(CurrentCell) > 0:
            Details += "PHEROMONES\n"
            for P in self._Pheromones:
                if P.InSameLocation(CurrentCell):
                    Details += f"Ant {P.GetBelongsTo()} with strength of {P.GetStrength()}" + "\n\n"
            Details += "\n\n"
        return Details

    def AdvanceStage(self, NumberOfStages):
        """
        Advance the simulation by one "stage", ticking Pheromonones, food, and Ant positions.
        :param NumberOfStages: the number of stages to advance in one go
        """
        for Count in range(1, NumberOfStages + 1):
            PheromonesToDelete = []
            for P in self._Pheromones:
                P.AdvanceStage(self._Nests, self._Ants, self._Pheromones)
                if P.GetStrength() == 0:
                    PheromonesToDelete.append(P)
            for P in PheromonesToDelete:
                self._Pheromones.remove(P)
            for A in self._Ants:
                A.AdvanceStage(self._Nests, self._Ants, self._Pheromones)
                CurrentCell = self._Grid[self.__GetIndex(A.GetRow(), A.GetColumn())]
                if A.GetFoodCarried() > 0 and A.IsAtOwnNest():
                    self.AddFoodToNest(A.GetFoodCarried(), A.GetRow(), A.GetColumn())
                    A.UpdateFoodCarried(-A.GetFoodCarried())
                elif CurrentCell.GetAmountOfFood() > 0 and A.GetFoodCarried() == 0 and A.GetFoodCapacity() > 0:
                    FoodObtained = CurrentCell.GetAmountOfFood() + 1
                    while FoodObtained > CurrentCell.GetAmountOfFood() or (A.GetFoodCarried() + FoodObtained) > A.GetFoodCapacity():
                        FoodObtained = random.randint(1, A.GetFoodCapacity())
                    CurrentCell.UpdateFoodInCell(-FoodObtained)
                    A.UpdateFoodCarried(FoodObtained)
                else:
                    if A.GetFoodCarried() > 0:
                        self.UpdateAntsPheromoneInCell(A)
                    A.ChooseCellToMoveTo(self.__GetIndicesOfNeighbours(A.GetRow(), A.GetColumn()), self.__GetIndexOfNeighbourWithStrongestPheromone(A.GetRow(), A.GetColumn()))
            for N in self._Nests:
                self._Nests, self._Ants, self._Pheromones = N.AdvanceStage(self._Nests, self._Ants, self._Pheromones)

class Entity():
    """Abstract class for all things that can occupy a space on the grid."""
    def __init__(self, StartRow, StartColumn):
        """Create an Entity. Never directly called, instead intended as a base for child classes."""
        self._Row = StartRow
        self._Column = StartColumn
        self._ID = None

    def InSameLocation(self, E):
        """
        Check if this Entity is in the same location as another.
        :param E: the other Entity
        :return: boolean
        """
        return E.GetRow() == self._Row and E.GetColumn() == self._Column

    def GetRow(self):
        """
        Get the row of the Entity.
        :return: row number
        """
        return self._Row

    def GetColumn(self):
        """
        Get the column of the Entity.
        :return: column number
        """

        return self._Column

    def GetID(self):
        """
        Get the ID of the Entity.
        :return: ID
        """
        return self._ID

    def AdvanceStage(self, Nests, Ants, Pheromones):
        """Base method for what happens to an Entity every tick. Never directly called, instead intended as a base for child classes."""
        pass

    def GetDetails(self):
        """Base detail printing method. Never directly called, instead intended as a base for child classes."""
        return ""

class Cell(Entity):
    """Cell class that 'holds' all things at a certain grid position."""
    def __init__(self, StartRow, StartColumn):
        """
        Create a Cell with 0 food.
        :param StartRow:
        :param StartColumn:
        """
        super().__init__(StartRow, StartColumn)
        self._AmountOfFood = 0

    def GetAmountOfFood(self):
        """
        Get amount of food.
        :return: amount of food
        """
        return self._AmountOfFood

    def GetDetails(self):
        """
        Print details: food in the Cell.
        :return: multiline string
        """
        Details = f"{super().GetDetails()}{self._AmountOfFood} food present" + "\n\n"
        return Details

    def UpdateFoodInCell(self, Change):
        """
        Increase the amount of food in the Cell.
        :param Change: amount to change by. Negative change results in a decrease in food amount
        """
        self._AmountOfFood += Change

class Ant(Entity):
    """Ant class that represents a single wandering Ant that follows Phermonone trails and carries food."""
    _NextAntID = 1

    def __init__(self, StartRow, StartColumn, NestInRow, NestInColumn):
        """
        Create an Ant.
        :param StartRow:
        :param StartColumn:
        :param NestInRow: row of the Ant's home Nest
        :param NestInColumn: column of the Ant's home Nest
        """
        super().__init__(StartRow, StartColumn)
        self._NestRow = NestInRow
        self._NestColumn = NestInColumn
        self._ID = Ant._NextAntID
        Ant._NextAntID += 1
        self._Stages = 0
        self._AmountOfFoodCarried = 0
        self._FoodCapacity = 0
        self._TypeOfAnt = ""

    def GetFoodCapacity(self):
        """
        Get maximum capacity of stored food.
        :return: amount of food
        """
        return self._FoodCapacity

    def IsAtOwnNest(self):
        """
        Check if the Ant is home.
        :return: boolean
        """
        return self._Row == self._NestRow and self._Column == self._NestColumn

    def AdvanceStage(self, Nests, Ants, Pheromones):
        """
        Advance stage: increase number of stages alive.
        """
        self._Stages += 1

    def GetDetails(self):
        """
        Print details: ID, Ant type, stages alive
        :return: multiline string
        """
        return f"{super().GetDetails()}  Ant {self._ID}, {self._TypeOfAnt}, stages alive: {self._Stages}"

    def UpdateFoodCarried(self, Change):
        """
        Increase the amount of food carried by the Ant.
        :param Change: amount to change by. Negative Change results in a decrease in carried food.
        """
        self._AmountOfFoodCarried += Change

    def _ChangeCell(self, NewCellIndicator, RowToChange, ColumnToChange):
        """
        Move the Ant in a specific direction.
        :param NewCellIndicator: indicates direction in which to move, starting from 0 down-left and going clockwise
        :param RowToChange: current row
        :param ColumnToChange: current column
        :return: tuple of new row and new column
        """
        if NewCellIndicator > 5:
            RowToChange += 1
        elif NewCellIndicator < 3:
            RowToChange -= 1
        if NewCellIndicator in [0, 3, 6]:
            ColumnToChange -= 1
        elif NewCellIndicator in [2, 5, 8]:
            ColumnToChange += 1
        return RowToChange, ColumnToChange

    def _ChooseRandomNeighbour(self, ListOfNeighbours):
        """
        Pick a random inhabited grid position from a list of neighbours.
        :param ListOfNeighbours:
        :return: random index of inhabited cell in the list
        """
        Chosen = False
        while Chosen == False:
            RNo = random.randint(0, len(ListOfNeighbours) - 1)
            if ListOfNeighbours[RNo] != -1:
                Chosen = True
        return RNo

    def ChooseCellToMoveTo(self, ListOfNeighbours, IndexOfNeighbourWithStrongestPheromone):
        pass

    def GetFoodCarried(self):
        return self._AmountOfFoodCarried

    def GetNestRow(self):
        return self._NestRow

    def GetNestColumn(self):
        return self._NestColumn

    def GetTypeOfAnt(self):
        return self._TypeOfAnt

class QueenAnt(Ant):
    """Queen Ant. Surprisingly nothing functionally special, but is the last to be culled."""
    def __init__(self, StartRow, StartColumn, NestInRow, NestInColumn):
        super().__init__(StartRow, StartColumn, NestInRow, NestInColumn)
        self._TypeOfAnt = "queen"

class WorkerAnt(Ant):
    """Worker Ant class with a maximum food capacity of 30."""
    def __init__(self, StartRow, StartColumn, NestInRow, NestInColumn):
        super().__init__(StartRow, StartColumn, NestInRow, NestInColumn)
        self._TypeOfAnt = "worker"
        self._FoodCapacity = 30

    def GetDetails(self):
        return f"{super().GetDetails()}, carrying {self._AmountOfFoodCarried} food, home nest is at {self._NestRow} {self._NestColumn}"

    def ChooseCellToMoveTo(self, ListOfNeighbours, IndexOfNeighbourWithStrongestPheromone):
        if self._AmountOfFoodCarried > 0:
            if self._Row > self._NestRow:
                self._Row -= 1
            elif self._Row < self._NestRow:
                self._Row += 1
            if self._Column > self._NestColumn:
                self._Column -= 1
            elif self._Column < self._NestColumn:
                self._Column += 1
        elif IndexOfNeighbourWithStrongestPheromone == -1:
            IndexToUse = self._ChooseRandomNeighbour(ListOfNeighbours)
            self._Row, self._Column = self._ChangeCell(IndexToUse, self._Row, self._Column)
        else:
            IndexToUse = ListOfNeighbours.index(IndexOfNeighbourWithStrongestPheromone)
            self._Row, self._Column = self._ChangeCell(IndexToUse, self._Row, self._Column)

class Nest(Entity):
    _NextNestID = 1

    def __init__(self, StartRow, StartColumn, StartFood):
        super().__init__(StartRow, StartColumn)
        self._FoodLevel = StartFood
        self._NumberOfQueens = 1
        self._ID = Nest._NextNestID
        Nest._NextNestID += 1

    def ChangeFood(self, Change):
        self._FoodLevel += Change
        if self._FoodLevel < 0:
            self._FoodLevel = 0

    def GetFoodLevel(self):
        return self._FoodLevel

    def AdvanceStage(self, Nests, Ants, Pheromones):
        if Ants is None:
            return
        AntsToCull = 0
        Count = 0
        AntsInNestCount = 0
        for A in Ants:
            if A.GetNestRow() == self._Row and A.GetNestColumn() == self._Column:
                if A.GetTypeOfAnt() == "queen":
                    Count += 10
                else:
                    Count += 2
                    AntsInNestCount += 1
        self.ChangeFood(-int(Count))
        if self._FoodLevel == 0 and AntsInNestCount > 0:
            AntsToCull += 1
        if self._FoodLevel < AntsInNestCount:
            AntsToCull += 1
        if self._FoodLevel < AntsInNestCount * 5:
            AntsToCull += 1
            if AntsToCull > AntsInNestCount:
                AntsToCull = AntsInNestCount
            for A in range(1, AntsToCull + 1):
                RPos = random.randint(0, len(Ants) - 1)
                while not(Ants[RPos].GetNestRow() == self._Row and Ants[RPos].GetNestColumn() == self._Column):
                    RPos = random.randint(0, len(Ants) - 1)
                if Ants[RPos].GetTypeOfAnt() == "queen":
                    self._NumberOfQueens -= 1
                Ants.pop(RPos)
        else:
            for A in range(1, self._NumberOfQueens + 1):
                RNo1 = random.randint(0, 99)
                if RNo1 < 50:
                    RNo2 = random.randint(0, 99)
                    if RNo2 < 2:
                        Ants.append(QueenAnt(self._Row, self._Column, self._Row, self._Column))
                        self._NumberOfQueens += 1
                    else:
                        Ants.append(WorkerAnt(self._Row, self._Column, self._Row, self._Column))
        return Nests, Ants, Pheromones

class Pheromone(Entity):
    def __init__(self, Row, Column, BelongsToAnt, InitialStrength, Decay):
        super().__init__(Row, Column)
        self._BelongsTo = BelongsToAnt
        self._Strength = InitialStrength
        self._PheromoneDecay = Decay

    def AdvanceStage(self, Nests, Ants, Pheromones):
        self._Strength -= self._PheromoneDecay
        if self._Strength < 0:
            self._Strength = 0

    def UpdateStrength(self, Change):
        self._Strength += Change

    def GetStrength(self):
        return self._Strength

    def GetBelongsTo(self):
        return self._BelongsTo

if __name__ == "__main__":
    Main()
