----

**block/BlockBarrel.py - Documentation - Last updated on 02.03.2020 by uuk**

----

This file contains the class for the barrel-block.
See https://minecraft.gamepedia.com/Barrel for more information.
    
    class BlockBarrel extends block.Block.Block
        class for the barrel block
        
        overriding static attribute NAME: str - the name of the block
        
        attribute facing: str - where the block faces to
        
        attribute opened: bool - if the barrel is opened or not
        
        attribute inventory: gui.InventoryBarrel.InventoryBarrel - the inventory of the block
        
        overriding function __init__
            sets up the barrel
            
        overrriding function on_player_interact itemstack: gui.ItemStack.ItemStack button: int modifiers: int exact_hit: tuple -> bool
            opens the inventory when needed
            
        overriding function get_inventories
            returns the inventory of the block
            
        overriding function get_hardness
            returns the hardness of the block
            
        overriding function get_best_tools -> list<util.enums.ToolType>
            returns axe as the best tool to brake the block with
            
        overriding function get_provided_slots side: util.enums.EnumSide
            returns the slots of the inventory of the block
            
        overriding function set_model_state state: dict
            sets the model state of the block
            
        overriding function get_model_state -> dict
            returns the state of the barrel
            
        overriding static function get_all_model_states -> list
            returns all possible states of the barrel
            
        static function set_block_data iteminst: item.Item.Item block: block.Block.Block
            loads the inventory if arrival from an item
            
        overriding function on_request_item_for_block itemstack: gui.ItemStack.ItemStack
            adds the inventory to the item when requested
            
        overriding function on_remove
            drops the items from the inventory if needed
            
        overiding static function modify_block_item itemfactory: factory.ItemFactory.ItemFactory
            sets the fuel level of the block