----

**block/BlockCraftingTable.py - Documentation - Last updated on 16.04.2020 by uuk**

----


This file contains the code for the crafting table block


    class BlockCraftingTable extends block.Block.Block
        static attibute inventory: gui.InventoryCraftingTable.InventoryCraftingTable - stores the global crafting table, WARNING: may be moved in the future to player-class
        
        static overriding attribute NAME: str - the name of the block
        
        overriding function on_player_interact [...]
            opens the inventory when needed
            
        overriding function get_inventories -> list
            returns the inventory of the block
            
        overriding static attribute HARDNESS: float = 2.5

        overriding static attribute BEST_TOOLS_TO_BREAK [...]
            
        overriding function on_remove
            closes the inventory when inventory is open
            
        static overriding function modify_block_item itemfactory: factory.ItemFactory.ItemFactory
            sets the fuel level of the block
