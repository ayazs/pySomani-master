"""Draw module for X's and O's

This module is able to draw an X's and O's game board or series of moves
that comprise a game.

The module is specifically intended to be run in a Google Colab notebook 
and requires that `ColabTurtle` be installed within the notebook
environment. This can be installed using the following command:

```!pip3 install ColabTurtle```

This module and contains the following functions:

    * drawNewBoards - initializes and draws a new blank game board
    * drawMarker - draws an X or O marker in a position on a game board
    * drawBoard - draws a complete game board as passed in as a 2D representation
    * drawGame - draws a complete game board as passed in as a sequence of moves
"""

from ColabTurtle.Turtle import *
import math

_BOARDSIZE = 180
_X_COLOUR = 'red'
_Y_COLOUR = 'green'


def drawNewBoard(size=180, colour='white', margin=30):
  """Draws a new empty game board

  Parameters
  ----------
  size : int
      The size in pixels of one side of the square game board
  colour : str
      The colour of the game board 
  margin : int
      The size of the margin around the board in pixels 

  Returns
  -------
  None

  """

  # Calculate parameters used in this method
  cellSize = math.floor(size / 3)
  boardSize = (cellSize * 3, cellSize * 3)
  canvasSize = (size + (2 * margin), size + (2 * margin))

  # Create a new turtle session and clear the canvas
  initializeTurtle(10, canvasSize)
  hideturtle()
  color(colour)

  # Draw the left vertical line
  penup()
  goto(margin + cellSize, margin)
  pendown()
  goto(margin + cellSize, margin + boardSize[1])

  # Draw the right vertical line
  penup()
  goto(margin + boardSize[0] - cellSize, margin)
  pendown()
  goto(margin + boardSize[0] - cellSize, margin + boardSize[1])

  # Draw the upper horizontal line
  penup()
  goto(margin, margin + cellSize)
  pendown()
  goto(margin + boardSize[0], margin + cellSize)

  # Draw the lower horizontal line
  penup()
  goto(margin, margin + boardSize[1] - cellSize)
  pendown()
  goto(margin + boardSize[0], margin + boardSize[1] - cellSize)


def drawMarker(team = 'X', pos = (1,1), size=180, colour='white', margin=30) :
  """Draws an X or O marker on a game board

  Parameters
  ----------
  team : string
      Either 'X' or 'O'
  pos : tuple
      Position on the game board (row, col)
  size : int
      Size of one side of the square game board
  colour : str
      The colour of the marker 
  margin : int
      The size of the margin around the board in pixels 

  Returns
  -------
  None

  """

  # Calculate parameters used in this method
  cellSize = math.floor(size / 3)
  boardSize = (cellSize * 3, cellSize * 3)
  canvasSize = (size + (2 * margin), size + (2 * margin))

  # Calculate offset parameters used to position X's and O's
  x_offset = math.floor(cellSize * 0.2)
  o_offset_horizontal = math.floor(cellSize * 0.2)
  o_offset_vertical = math.floor(cellSize / 2)

  # Set the drawing parameters
  hideturtle()
  color(colour)

  # Draw instructions for an O
  if (team.lower() == 'o') :
    penup()

    # Go to the start position for drawing the marker
    goto(margin + (cellSize * pos[1]) + o_offset_horizontal,
        margin + (cellSize * pos[0]) + o_offset_vertical)
    pendown()

     # Draw the O scaled based on the size of the board
    steps = math.floor(1.4 * cellSize) - (o_offset_horizontal * 2)
    step_len = 2
    for s in range(steps) :
      for ss in range(step_len) :
        right(360 / (steps * step_len))
        forward(math.floor(1))
  
# Draw instructions for an X
  elif (team.lower() == 'x') :

    # Draw the first line of the X (top-left to bottom-right)
    penup()
    goto(margin + (cellSize * pos[1]) + x_offset, 
         margin + (cellSize * pos[0]) + x_offset)
    pendown()
    goto(margin + (cellSize * pos[1]) + (cellSize - x_offset), 
         margin + (cellSize * pos[0]) + (cellSize - x_offset))

    # Draw the second line of the X (top-right to bottom-left)
    penup()
    goto(margin + (cellSize * pos[1]) + (cellSize - x_offset), 
         margin + (cellSize * pos[0]) + x_offset)
    pendown()
    goto(margin + (cellSize * pos[1]) + x_offset, 
         margin + (cellSize * pos[0]) + (cellSize - x_offset))


def drawWin(startPos = (0,0), endPos = (2,2), size=180, colour='yellow', margin=30) :
  """Draws an win line on a game board

  Parameters
  ----------
  startPos : tuple
      Start position of win line on the game board (row, col)
  endPos : tuple
      End position of win line on the game board (row, col)
  size : int
      Size of one side of the square game board
  colour : str
      The colour of the win line
  margin : int
      The size of the margin around the board in pixels 

  Returns
  -------
  None

  """

  # Calculate parameters used in this method
  cellSize = math.floor(size / 3)
  boardSize = (cellSize * 3, cellSize * 3)
  canvasSize = (size + (2 * margin), size + (2 * margin))

  # Calculate offset parameter used to position the win line
  offset = math.floor(cellSize / 2)

  # Set the drawing parameters
  hideturtle()
  color(colour)

  # Draw instructions
  # Go to the start position for drawing the marker
  penup()
  goto(margin + (cellSize * startPos[1]) + offset,
      margin + (cellSize * startPos[0]) + offset)

  # Draw win line 
  pendown()
  goto(margin + (cellSize * endPos[1]) + offset,
      margin + (cellSize * endPos[0]) + offset)


def drawBoard(board = [], size=180, board_colour='white', xy_colour={'X':'red', 'O':'green', '':'white'}, margin=30, newBoard = False) :
  """Draws an entire game board

  Parameters
  ----------
  board : 2D array
      [3][3] array of 'X', 'O' or '' representing the game board
  size : int
      Size of one side of the square game board
  board_colour : str
      The colour of the game board 
  xy_colour : dict
      Dictionary of markers to colours they should be displayed in
  margin : int
      The size of the margin around the board in pixels 
  newBoard : bool
      Set to true if a new board should be drawn

  Returns
  -------
  None

  """

  # If en empty board is passed or newBoard is true, draw a new board.
  if ((len(board) == 0) or newBoard) :
    drawNewBoard(size=size, colour=board_colour, margin=margin)
    
  # If the board is not a 2D array, return
  if (len(board) < 1) : 
    return
  if (len(board[0]) < 1) :
    return
  
  # Iterate through the board array and draw the markers in their cells
  for i in range(len(board) * len(board[0])) :
    row = math.floor(i / len(board))
    col = i % len(board)
    team = board[row][col]
    drawMarker(team, (row, col), size, xy_colour[team], margin)
    #print('[' + str(row) + '][' + str(col) + ']: ' + team)


def drawGame(game=[], numMoves=1, size=180, board_colour='white', xy_colour={'X':'red', 'O':'green', '':'white'}, margin=30, newBoard = False) :
  """Draws an entire game board based on a list of positions

  Parameters
  ----------
  game : array
    sequence of tuples of (row, col, team) each representing a sigle move made by one team
  numMoves : int
    How many moves to draw, starting from the most recent. Use -1 to indicate all moves.
  size : int
    Size of one side of the square game board
  board_colour : str
    The colour of the game board 
  xy_colour : dict
    Dictionary of markers to colours they should be displayed in
  margin : int
    The size of the margin around the board in pixels 
  newBoard : bool
    Set to true if a new board should be drawn

  Returns
  -------
  None

  """

  # If the game array is empty or newBoard is True, draw a new board.
  if ((len(game) < 1) or newBoard) :
    drawNewBoard(size=size, colour=board_colour, margin=margin)

  # Calculate the indices of the first and last moves to draw
  firstMove = len(game) - numMoves
  if (numMoves < 1) :
    firstMove = 0
  lastMove = len(game)

  # Iterate through the sequence of game moves and draw them in order
  for i in range(firstMove,lastMove) :
    row = game[i][0]
    col = game[i][1]
    team = game[i][2]
    drawMarker(team, (row, col), size, xy_colour[team], margin)
    #print('[' + str(row) + '][' + str(col) + ']: ' + team)

