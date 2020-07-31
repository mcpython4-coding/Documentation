***BlockShulkerBox.py - documentation - last updated on 31.7.2020 by uuk***
___

    function create_shulker_box(name)

        @G.registry class BlockShulkerBox extends Block.Block

            function __init__(self, *args, **kwargs)

                variable self.inventory

            variable NAME

            function on_player_interaction(self, player, button: int, modifiers: int, hit_position: tuple)

            function get_inventories(self)

            variable HARDNESS

            variable MINIMUM_TOOL_LEVEL

            variable BEST_TOOLS_TO_BREAK

            function get_provided_slot_lists(self, side): return self.inventory.slots, self.inventory.slots
                    
                    @classmethod
                    def modify_block_item(cls, itemconstructor: mcpython.factory.ItemFactory.ItemFactory):

            static
            function modify_block_item(cls, itemconstructor: mcpython.factory.ItemFactory.ItemFactory)

            static
            function set_block_data(cls, iteminst, block)

            function on_request_item_for_block(self, itemstack)

            function on_remove(self)

    @G.modloader("minecraft", "stage:block:load")
    function load()