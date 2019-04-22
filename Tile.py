from random import shuffle


# Create a class that assigns each tile with a color and declares that all cards start unmatched and face down
class Tile:
    def __init__(self, color):
        self.color = color
        self.match = False
        self.faceUp = False

# These are to put each tile into the tile class and define what color they are. Each tile will have 1 match


tile1 = Tile("Blue")
tile2 = Tile("Blue")
tile3 = Tile("Red")
tile4 = Tile("Red")
tile5 = Tile("lightGreen")
tile6 = Tile("lightGreen")
tile7 = Tile("Yellow")
tile8 = Tile("Yellow")
tile9 = Tile("Purple")
tile10 = Tile("Purple")
tile11 = Tile("White")
tile12 = Tile("White")
tile13 = Tile("Gray")
tile14 = Tile("Gray")
tile15 = Tile("darkGreen")
tile16 = Tile("darkGreen")
tile17 = Tile("Teal")
tile18 = Tile("Teal")

# Here is a list of all the possible tiles
tiles = [tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9, tile10,
         tile11, tile12, tile13, tile14, tile15, tile16, tile17, tile18]

# This function will shuffle the cards every time the user opens
shuffle(tiles)
