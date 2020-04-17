---
***block/BlockHandler.py - documentation - Last updated on 17.04.2020 by uuk***
___

This file is used for dealing with blocks and keeping track about
what blocks the game can use.

    function register_block registry: event.Registry.Registry blockclass: block.Block.Block
        Called by the registry when an new object is registered. Generates
        also needed table entries in the registry object. Will raise 
        ValueError when non-block-subclass is tried to be registered.
        
        WARNING: when direct calling this method for registration, the 
        system may not work correct. There is stuff handled direct by the
        registry system outside these function.
    
    line 22-23: create block registry

    function load
        Called by the loading system for loading the block stuff
    
    line 38: register load to the loading system

    line 41-42: import of block helper files

