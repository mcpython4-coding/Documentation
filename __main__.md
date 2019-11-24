***\_\_main__.py - documentation***
___
This file is used for launching the game

It contains setup scripts & an \_\_name__ == "\_\_main__"-section

Everything is in an try-except block to make closing the resources simpler

1. line 10-14: code to print the log header with version
2. line 16-18: first imports
3. line 22-28: clean up the tmp-folder
4. line 30-38: other imports
5. line 40-41: prebuild check
6. line 43-44: load resources
7. line 46-50: search for mods & loading of them
8. line 52-64: again, imports
9. def setup()
    
    function to setup the game, including world objects, player system and OpenGL
    
10. def run()
    
    function to start mainloop of pyglet, creates the window
    
11. def main()
    
    function to run mcpython
    
12. line 90-93: on exception in this part, the game will be able to cleanup before crash

13. line 96-103: called when directly launched, calls (11) in an 
try-finally block to make cleanup easier