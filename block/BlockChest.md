***BlockChest.py - documentation - last updated on 14.5.2020 by uuk***
___

    variable BBOX


    @G.registry class BlockChest extends Block.Block

        variable now


        variable is_christmas


        variable NAME

        function __init__(self, *args, **kwargs)
        function can_open_inventory(self) -> bool
        function on_player_interact(self, player, itemstack, button, modifiers, exact_hit) -> bool
        function get_inventories(self)

        variable HARDNESS


        variable BEST_TOOLS_TO_BREAK

        function get_provided_slots(self, side)
        function set_model_state(self, state: dict)
        function get_model_state(self) -> dict
        static function get_all_model_states() -> list
        function get_view_bbox(self)
        static function set_block_data(cls, iteminst, block)
        function on_request_item_for_block(self, itemstack)
        function on_remove(self)
        static function modify_block_item(cls, itemfactory)
        function save(self)
        function load(self, data)