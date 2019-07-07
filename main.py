#  __    __  ____    __    ____         __   
# |  |  |  | \   \  /  \  /   /        / /   
# |  |__|  |  \   \/    \/   / ______ / /_   
# |   __   |   \            / |______| '_ \  
# |  |  |  |    \    /\    /         | (_) | 
# |__|  |__|     \__/  \__/           \___/  

# imports
import os

# check if the input size is in terminal boundaries
def validSize(rows, columns):
  c, r = os.get_terminal_size(0)
  return rows <= (r/2) and columns <= (c/2)

# Draw a table based on dashes and pipes.
#  You can set the number of rows and columns.
#  If executes without arguments use the maximun 
#  of terimal's size.
def drawTable(rows=0, columns=0):
  # Default size based on terminal's maximun
  if not rows and not columns:
    c, r = os.get_terminal_size(0)
    rows = int(r/2)
    columns = int(c/2)
  # Check valid size
  if not validSize(rows, columns):
    return False

  # Build table
  for row in range(rows*2):
    if row%2 == 0:
      for column in range((columns * 2) - 1):
        if column%2 == 0:
          if column != ((columns * 2) -2):
            print(" ", end = "")
          else:
            # line break
            print(" ")
        else:
          # Column sapcer
          print("|", end = "")
    else:
      # Row spacer
      print("-" * ((columns * 2)))
  return True

# First, we check an invalid size (my terminal size is 37x139)
# IsMatrixOk = drawTable(38, 139);

# Now we check a valid size
# IsMatrixOk = drawTable(20, 15);

# We can also run the function with out parameters. Ops, we need the variable for error validation.
IsMatrixOk = drawTable()

# Print error and terminal size
if not IsMatrixOk:
  c, r = os.get_terminal_size(0)
  rows = int(r/2)
  columns = int(c/2)
  print("The input table size exceed", rows, "rows or ", columns, "columns")


          