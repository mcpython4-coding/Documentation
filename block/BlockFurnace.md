----

**block/BlockFurnace.py - Documentation - Last updated on 17.04.2020 by uuk**

----

This file contains the classes for the furnace-block and its specific sub-furnaces


    class BlockFurnce extends block.Block.Block
        static attribute FURNACE_RECIPES: list<str[recipe type]>: a list of furnace recipes to use
        
        overriding static attribute NAME: str - the name of the block
        
        attribute facing: str - where the block faces to
        
        attribute active: bool - if something is processing in the furnace
        
        attribute inventory: gui.Inventory.Inventory - the inventory of the furnace
        
        function __init__ [...]
            construct an new Furnace-block
            
        overriding function get_model_state -> dict<str -> str>
            gets the model-state of the block
            
        overriding function set_model_state state: dict<str -> str>
            injects the model state
            
        overriding static function get_all_model_states -> list<dict<str -> str>>
            gets all model states
            
        overriding function on_player_interact [...]
            will open inventory if needed
            
        overriding function get_inventories -> list<gui.Inventory.Inventory>
            will return the inventory of the block
            
        overriding function get_provided_slots [...]
            will return the slots for the side
            
        overriding function on_remove
            will make sure that items are dropped
            
    class BlastFurnace extends block.BlockFurnace.BlockFurnace
        overriding attribute NAME: str - the name of the block
        
        overriding attribute FURNACE_RECIPES: list<str> - the recipe names
        
    class Smoker extends block.BlockFurnace.BlockFurnace
        overriding attribute NAME: str - the name of the block
        
        overriding attribute FURNACE_RECIPES: list<str> - the recipe names

