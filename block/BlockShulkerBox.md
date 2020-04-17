----

**block/BlockShulkerBox.py - Documentation - Last updated on 17.04.2020 by uuk**

----

This file contains code for the shulker box block


    function create_shulker_box name: str
        creates an new ShulkerBox-class
        
        class BlockShulkerBox extends block.Block.Block
        
            overriding static attribute NAME: str - the name of the block
            
            overriding static attribute HARDNESS: float - the hardness of the block
            
            overriding static attribute MINIMUM_HARDNESS: int - the minimum of level tool to break
            
            overriding static attribute BEST_TOOLS_TO_BREAK: list<util.enums.ToolType> - the best tools to break
            
            attribute inventory: gui.Inventory.Inventory - the inventory of the block
            
            function __init__ [...]
                creates an new shulker box instance
                
            overriding function on_player_interact [...]
                opens the inventory when needed
                
            overriding function get_inventories -> list<gui.Inventory.Inventory>
                returns the inventory of the block
                
            overriding function get_provided_slots -> list<gui.Slot.Slot>
                return an list of all slots
                
            overrriding static function modify_block_item [...]
                modifies the block item to extend item.IShulkerLikeItem
                
            overriding static function set_block_data
                copies inventory data
                
            overriding function on_request_item_for_block [...]
                copies the inventory to item
                
            overriding function on_remove
                will close inventory
    
    line 63-65
        create all shulker box classes

