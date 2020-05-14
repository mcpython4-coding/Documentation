***BlockChest.py - documentation - last updated on 14.5.2020 by uuk***
___

    variable BBOX

    @G.registry class BlockChest extends Block.Block

        variable now

        variable is_christmas

        variable NAME

        function __init__(self, *args, **kwargs)

            variable self.front_side

                    variable self.front_side

                    variable self.front_side

                    variable self.front_side

                    variable self.front_side

            variable self.inventory

            variable self.loot_table_link

            variable self.face_solid

        function can_open_inventory(self) -> bool

            variable blockinst

        function on_player_interact(self, player, itemstack, button, modifiers, exact_hit) -> bool

                    variable self.loot_table_link

        function get_inventories(self)

        variable HARDNESS

        variable BEST_TOOLS_TO_BREAK

        function get_provided_slots(self, side)

        function set_model_state(self, state: dict)

                variable face

                    variable self.front_side

                    variable self.front_side

        function get_model_state(self) -> dict

        static function get_all_model_states() -> list

        function get_view_bbox(self)

        static function set_block_data(cls, iteminst, block)

                variable block.inventory

        function on_request_item_for_block(self, itemstack)

                variable itemstack.item.inventory

        function on_remove(self)

        static function modify_block_item(cls, itemfactory)

        function save(self)

        function load(self, data)

                variable self.loot_table_link