***BlockBarrel.py - documentation - last updated on 14.5.2020 by uuk***
___

    @G.registry class BlockBarrel extends Block.Block

        variable NAME

        function __init__(self, *args, **kwargs)
        function on_player_interact(self, player, itemstack, button, modifiers, exact_hit) -> bool
        function get_inventories(self)

        variable HARDNESS


        variable BEST_TOOLS_TO_BREAK

        function get_provided_slots(self, side)
        function set_model_state(self, state: dict)
        function get_model_state(self) -> dict
        static function get_all_model_states() -> list
        static function set_block_data(cls, iteminst, block)
        function on_request_item_for_block(self, itemstack)
        function on_remove(self)
        static function modify_block_item(cls, itemfactory)