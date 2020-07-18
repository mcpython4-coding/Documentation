***BlockEnderChest.py - documentation - last updated on 18.7.2020 by uuk***
___

    @G.registry class BlockEnderChest extends Block.Block
        
        class for the ender chest


        function __init__(self, *args, **kwargs)
            
            creates the ender chest block


            variable self.front_side

                    variable self.front_side

        variable NAME

        function on_player_interact(self, player, itemstack, button, modifiers, exact_hit) -> bool

        function get_inventories(self)

        variable HARDNESS

        variable MINIMUM_TOOL_LEVEL

        variable BEST_TOOLS_TO_BREAK

        function get_provided_slots(self, side)

        function set_model_state(self, state: dict)

        function get_model_state(self) -> dict

        static
        function get_all_model_states() -> list

        function get_view_bbox(self)

        function on_remove(self)