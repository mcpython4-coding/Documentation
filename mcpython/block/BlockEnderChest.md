***BlockEnderChest.py - documentation - last updated on 31.7.2020 by uuk***
___

    class BlockEnderChest extends Block.Block
        
        class for the ender chest


        function __init__(self, *args, **kwargs)
            
            creates the ender chest block


            variable self.front_side

                    variable self.front_side

        variable NAME

        function on_player_interaction(self, player, button: int, modifiers: int, hit_position: tuple)

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

    @G.modloader("minecraft", "stage:block:load")
    function load()