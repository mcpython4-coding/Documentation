***block/BlockHandler.py - documentation***
___

This file is used for dealing with blocks and keeping track about
what blocks the game can use.


1. def register_block(registry: event.Registry.Registry, blockclass)
    
    Called by the registry when an new object is registered. Generates
    also needed table entries in the registry object. Will raise 
    ValueError when non-block-subclass is tried to be registered.
    
    WARNING: when direct calling this method for registration, the 
    system may not work correct. There is stuff handled direct by the
    registry system outside these function.
    
2. line 25 - 27: create block registry

3. def load()

    Called by the loading system for loading the block stuff
    
4. line 38: register (3) to the loading system

5. line 41-42: import of block helper files

