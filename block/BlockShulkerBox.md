***BlockShulkerBox.py - documentation - last updated on 16.5.2020 by uuk***
___

    function create_shulker_box(name)

        @G.registry class BlockShulkerBox extends Block.Block

            function __init__(self, *args, **kwargs)

                variable self.inventory

            variable NAME

            function on_player_interact(self, player, itemstack, button, modifiers, exact_hit) -> bool

            function get_inventories(self)

            variable HARDNESS

            variable MINIMUM_TOOL_LEVEL

            variable BEST_TOOLS_TO_BREAK

            function get_provided_slots(self, side)

            static function modify_block_item(cls, itemconstructor: factory.ItemFactory.ItemFactory)

            static function set_block_data(cls, iteminst, block)

            function on_request_item_for_block(self, itemstack)

            function on_remove(self)