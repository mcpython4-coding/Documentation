***CraftingGridHelperInterface.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class IRecipeAdapter

        static
        function convert(
                cls, interface: "CraftingGridHelperInterface", recipe
                ) -> typing.Optional:

    class CraftingGridHelperInterface extends  mcpython.common.container.crafting.IRecipeUser.IRecipeUser 
        
        Recipe interface for an crafting grid of arbitrary size using the default recipe implementation
        todo: implement insert helper
        todo: add dynamic replacement table for items (e.g. stone may be replaced by diamond blocks),
            this MAY be data-driven


        variable ADAPTERS: typing.List[IRecipeAdapter]

        variable NAME

        function __init__(
                self,
                slot_input_map,
                slot_output_map,
                maxsize=None,
                minsize=None,
                enabled=True,
                enable_shaped_recipes=True,
                enable_shapeless_recipes=True,
                ):
            
            Creates an new grid recipe interface
            Recipe order: first in, first checked
            :param slot_input_map: an Slot[[ for input
            :param slot_output_map: an Slot for output
            :param maxsize: the max size for recipes. may be None for full grid size
            :param minsize: the min size for recipes. default is (1, 1)
            :param enabled: if recipes should be craft-able
            :param enable_shaped_recipes: if shaped recipes should be enabled
            :param enable_shapeless_recipes: if shapeless recipes should be enabled


            variable self.slot_input_map

            variable self.slot_output_map: mcpython.client.gui.Slot.Slot

            variable self.grid_size

            variable self.maxsize

            variable self.minsize

            variable slot_output_map.allow_half_getting

            variable slot_output_map.on_shift_click

            variable self.active_recipe

            variable self.shaped_enabled

            variable self.shapeless_enabled

        function check_recipe_state(self)
            
            Helper function for re-checking the items in the grid. Auto-called if a slot-itemstack
            assigned to this helper is updated


            variable self.active_recipe
                Reset the active stuff

            variable item_table

            variable sx

            variable sy

            variable size

            variable recipes
                decide which recipes may work

                    variable state

                    variable state

                            variable state

                    variable self.active_recipe

        static
        function minimize_slot_map(slot_map: dict) -> dict
            
            Helper function for minimizing the map stored by pos -> entry


        static
        function check_shaped(
                cls,
                recipe: mcpython.common.container.crafting.GridRecipeInstances.GridShaped,
                item_table: dict,
                ) -> bool:

                variable item

        static
        function check_match(cls, current, target) -> bool

        static
        function check_shapeless(
                recipe: mcpython.common.container.crafting.GridRecipeInstances.GridShapeless,
                items: list,
                ) -> bool:

            variable tasked

                variable tags

                            variable entry

        function update_output(self)

        function remove_input(self, count=1)
            
            removes from every input slot count item (called when an item is crafted)


        function on_input_update(self, player=False)

        function on_output_update(self, player=False)

        function on_output_shift_click(self, slot, x, y, button, modifiers, player)