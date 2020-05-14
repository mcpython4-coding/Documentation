***BlockCraftingTable.py - documentation - last updated on 14.5.2020 by uuk***
___

    @G.registry class BlockCraftingTable extends Block.Block

        variable NAME

        function on_player_interact(self, player, itemstack, button, modifiers, exact_hit) -> bool
        function get_inventories(self)
            
            called to get an list of inventories
            


        variable HARDNESS


        variable BEST_TOOLS_TO_BREAK

        function on_remove(self)
        static function modify_block_item(cls, itemfactory)