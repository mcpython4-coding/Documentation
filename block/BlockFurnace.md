***BlockFurnace.py - documentation - last updated on 16.5.2020 by uuk***
___

    @G.registry class BlockFurnace extends block.Block.Block
        
        class for the furnace block


        variable FURNACE_RECIPES: list - the list of recipe groups to use for this furnace

        variable NAME: str

        function __init__(self, *args, **kwargs)
            
            creates an furnace block in the world


            variable self.facing

            variable self.active

            variable self.inventory

        function get_model_state(self) -> dict

        function set_model_state(self, state: dict)

        static function get_all_model_states() -> list

        function on_player_interact(self, player, itemstack, button, modifiers, exact_hit) -> bool

        function get_inventories(self)

        function get_provided_slots(self, side)

        function on_remove(self)

    @G.registry class BlastFurnace extends BlockFurnace

        variable NAME: str

        variable FURNACE_RECIPES: list

    @G.registry class Smoker extends BlockFurnace

        variable NAME: str

        variable FURNACE_RECIPES: list