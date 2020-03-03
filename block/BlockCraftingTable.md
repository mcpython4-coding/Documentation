----

**block/BlockCraftingTable.py - Documentation - Last updated on 02.03.2020 by uuk**

----


This file contains the code for the crafting table block


    class BlockCraftingTable extends block.Block.Block
        static attibute inventory: gui.InventoryCraftingTable.InventoryCraftingTable - stores the global crafting table, WARNING: may be moved in the future to player-class
        
        static overriding attribute NAME: str - the name of the block
        
        overriding function on_player_interact [...]
            opens the inventory when needed
            
        overriding function get_inventories -> list
            returns the inventory of the block
            
        overriding function get_hardness -> float
            returns the inventory of the block
            
        overriding function get_best_tools -> list
            returns axe as the best tool to brake the block
            
        overriding function on_remove
            closes the inventory when inventory is open
            
        static overriding function modify_block_item itemfactory: factory.ItemFactory.ItemFactory
            sets the fuel level of the block
