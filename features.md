***features.md - documentation***
___

This file is used for inter-mod communication. It provides a table
system to insert data under an given entry to share with other mods.
When used by mods, make sure to store the result of the set-method, the
system will decide by itself which element to use. If you doing some
performance-relevant stuff, you can check it before.

Please, if you need an entry in this table, contact the project 
developers for making an general named entry out of it so other mods can
rely on this name and also yourself.

This is an stand-alone module, so it can not be only accessed
during certain moments of loading, instead always.

1. class FeatureTable(object)

    The class to use to share data
    
    1. def \_\_init__(self, name)
        
        constructor of FeatureTable. "name" is the name of the table.
    
    2. def add_holder(self, name: str, info: str)
    
        adds an entry into the table. info is an description on what is 
        does. These function sets the value to None, not any other value.
    
    3. set_attribute(self, name: str, data) -> object
    
        Sets an value in the table. If name is not found, ValueError is
        raised. Returns data if it is the first set for the value, otherwise
        the value set before.
        
    4. exists_in_table(self, name: str) -> bool
    
        returns if name is an entry in table with value set. raises NO
        ValueError if name does not exist.

2. variable features.FeatureTable ITEMS: table for items

3. variable features.FeatureTable BLOCKS: table for blocks

4. variable features.FeatureTable Material: table for materials
    