***GridRecipeInstances.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    function transform_to_item_stack(item, file: str) -> list
        
        Transforms an item name from recipe to a valid item list to compare with
        :param item: the item name given
        :param file: the file currently in
        :return: an transformed name list of (item name, amount)


            variable itemname

            variable values

            variable value

    class AbstractCraftingGridRecipe extends  mcpython.common.container.crafting.IRecipe.IRecipe,  ABC 

        variable RECIPE_VIEW

        function as_grid_for_view(
                self, size=(3, 3)
                ) -> typing.Tuple[typing.List[typing.List[typing.List[ItemStack]]], ItemStack]:

        function __repr__(self)

    @shared.crafting_handler class GridShaped extends AbstractCraftingGridRecipe

        variable RECIPE_TYPE_NAMES

        static
        function from_data(cls, data: dict, file: str)

            variable grid

            variable out

        function __init__(
                self,
                inputs: typing.Dict[typing.Tuple[int, int], typing.Tuple[str, int]],
                output: typing.Tuple[str, int],
                ):

            variable self.inputs

            variable self.output

            variable sx

            variable sy

            variable self.bboxsize

        function prepare(self)

        function as_grid(self, size=(3, 3))

        function as_grid_for_view(
                self, size=(3, 3)
                ) -> typing.Tuple[typing.List[typing.List[typing.List[ItemStack]]], ItemStack]:

            variable grid

        static
        function tag_to_stacks(cls, name: str, count: int = None, recipe_name=None)

    @shared.crafting_handler class GridShapeless extends AbstractCraftingGridRecipe

        variable RECIPE_TYPE_NAMES

        static
        function from_data(cls, data: dict, file: str)

        function __init__(
                self,
                inputs: typing.List[typing.List[typing.Tuple[str, int]]],
                output: typing.Tuple[str, int],
                ):

            variable self.inputs

            variable self.output

        function prepare(self)

        function as_grid_for_view(
                self, size=(3, 3)
                ) -> typing.Tuple[typing.List[typing.List[typing.List[ItemStack]]], ItemStack]:

            variable stacks

            variable grid