***BlockFurnace.py - documentation - last updated on 26.7.2020 by uuk***
___

    class BlockFurnace extends mcpython.block.IHorizontalOrientableBlock.IHorizontalOrientableBlock
        
        class for the furnace block


        variable FURNACE_RECIPES: list - the list of recipe groups to use for this furnace

        variable NAME: str

        function __init__(self, *args, **kwargs)
            
            creates an furnace block in the world


            variable self.active

            variable self.inventory

        function get_model_state(self) -> dict

        function set_model_state(self, state: dict)

        static
        function get_all_model_states(cls) -> list

        function on_player_interact(self, player, itemstack, button, modifiers, exact_hit) -> bool

        function get_inventories(self): return [self.inventory]
                
                def get_provided_slot_lists(self, side):

        function get_provided_slot_lists(self, side)

        function on_remove(self)

    class BlastFurnace extends BlockFurnace

        variable NAME: str

        variable FURNACE_RECIPES: list

    class Smoker extends BlockFurnace

        variable NAME: str

        variable FURNACE_RECIPES: list

    @G.modloader("minecraft", "stage:block:load")
    function load()