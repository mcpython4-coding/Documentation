Main file for these program, used to launch the program

Everything in try-except to make closing the resources on crash
possible.

What line does what?
line 14-21: general imports of files needed

line 23-28: clear tmp-buffer directory in an while-loop with try-except 
to make sure it gets deleted also when user in directory.

WARNING: when you open an file in this directory, either the game or
you editor WILL crash!

line 30: import of globals, the file storing global information

line 32-33: read in the prebuilding flag and store it in globals

line 35: recreate previous deleted tmp-directory

line 37-38: load resources from path

line 40-44: setting up ModLoader

line 46-58: loading of other files that are not related to one of the 
above tasks

def setup():

pre-setup of the game, called before window is created. Creates the
world object, setting up OpenGL and preparing Language system

def run():

called by main() to run the game, creates the window & calls the startup event

def main():

run the game, calls the pre-setup-event & setup & main-functions

end of first try-except block, on except, try to close ResourceLocator's
resources

if \__name__ == "\__main__" & following:
runs the game when directly called by running main(), in an try-finally
block with on finally cleaning up the whole thing

