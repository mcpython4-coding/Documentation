***BlockFurnace.py - documentation - last updated on 14.5.2020 by uuk***
___

    @G.registry class BlockFurnace extends block.Block.Block

        variable FURNACE_RECIPES


        variable NAME

        function __init__(self, *args, **kwargs)
        function get_model_state(self) -> dict
        function set_model_state(self, state: dict)
        static function get_all_model_states() -> list
        function on_player_interact(self, player, itemstack, button, modifiers, exact_hit) -> bool
        function get_inventories(self)
        function get_provided_slots(self, side)
        function on_remove(self)

    @G.registry class BlastFurnace extends BlockFurnace

        variable NAME


        variable FURNACE_RECIPES


    @G.registry class Smoker extends BlockFurnace

        variable NAME


        variable FURNACE_RECIPES
