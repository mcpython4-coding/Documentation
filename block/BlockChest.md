----

**block/BlockChest.py - Documentation - Last updated on 16.04.2020 by uuk**

----

This file contains the block-class of the chest

    static attribute BBOX: block.BoundingBox.BoundingBox - the bounding box of an chest
    
    class BlockChest extends block.Block.Block
        class for the chest-block
        
        static attribute now: datetime.datetime - when is "now"
        
        static attribute is_christmas: bool - indicator if its christmas
        
        attribute inventory: gui.InventoryChest.InventoryChest - the inventory of the chest
        
        attribute loot_table_link: str - an link to an valid loot-table to roll into the inventory on next inv open
        
        static overriding attribute NAME: str - the name of the chest
        
        overriding function __init__ [...]
            sets up the chest data using where it was set to and creates the inventory
            
        function can_open_inventory -> bool
            returns if the block inventory can be opened by the player
            
        overriding function on_player_interact [...]
            opens the inventory when needed and rolls the loot table when needed
            
        overriding function get_inventories [...]
            returns the inventory of the chest
            
        overriding static attribute HARDNESS: float = 2.5
        overriding static attribuee BEST_TOOLS_TO_BREAK [...] - axe to break0
            
        overriding function get_best_tools [...]
            returns axe as the best tool to brake the block
            
        overriding function get_provided_slots side: enums.EnumSide.EnumSide -> list
            returns the slots of the inventory
            
        overriding function set_model_state state: dict
            sets the state of the block
            
        overriding function get_model_state -> dict
            returns the model state of the block
            
        overriding function get_all_model_states -> list<dict<str: str>>
            returns all states of chest-block
            
        overriding function get_view_bbox [...]
            returns the bbox of the block
            
        overriding function is_solid_side side: util.enums.EnumSide.EnumSide
            returns False since every side is not solid
            
        overriding function on_request_item_for_block [...]
            modifies the block item with inventory when needed
            
        overriding function on_remove
            gives all items to the player
            
        static overriding function modify_block_item [...]
            adds fuel level to block-item
            
        overriding save -> dict
            saves the model state and the loot table
            
        overriding load data: dict
            loads previous dumped data

