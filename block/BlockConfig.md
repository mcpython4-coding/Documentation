----

**block/BlockConfig.py - Documentation - Last updated on 03.03.2020 by uuk**

----

This file holds some code to "tag" block with special properties

WARNING: will be moved in the future to tag-system


    class BlockConfigEntry
        attribute name: str - the name of the config
        
        attribute affects: list - an list of objects this affects, may be str-only
    
        function __init__ configname: str
            creates an new BlockConfigEntry-object
            
        function add_data data: list
            adds new affected data to the config
        
        function contains & __contains__ item: object -> bool
            returns if the item is affected
