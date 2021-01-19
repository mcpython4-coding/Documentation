***GridRecipeInstances.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    function transform_to_item_stack(item, table: dict) -> list
        
        Transforms an item name from recipe to an valid item list to compare with
        :param item: the item name given
        :param table: optional: an table of items which were decoded previous
        :return: an transformed name list of (item name, amount)


    class AbstractCraftingGridRecipe extends  mcpython.common.container.crafting.IRecipeType.IRecipe,  ABC 

        variable RECIPE_VIEW_PROVIDER

        function as_grid_for_view(
                self, max_size=(3, 3)
                ) -> typing.Tuple[typing.List[typing.List[typing.List[ItemStack]]], ItemStack]:

        function __repr__(self)

    @shared.crafting_handler class GridShaped extends AbstractCraftingGridRecipe

        variable RECIPE_NAMES

        static
        function from_data(cls, data: dict)

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

        function register(self)

        function as_grid(self)

        function as_grid_for_view(
                self, max_size=(3, 3)
                ) -> typing.Tuple[typing.List[typing.List[typing.List[ItemStack]]], ItemStack]:

            variable grid

        static
        function tag_to_stacks(cls, name: str, count: int = None)

    @shared.crafting_handler class GridShapeless extends AbstractCraftingGridRecipe

        variable RECIPE_NAMES

        static
        function from_data(cls, data: dict)

        function __init__(
                self,
                inputs: typing.List[typing.List[typing.Tuple[str, int]]],
                output: typing.Tuple[str, int],
                ):

            variable self.inputs

            variable self.output

        function register(self)

        function as_grid_for_view(
                self, max_size=(3, 3)
                ) -> typing.Tuple[typing.List[typing.List[typing.List[ItemStack]]], ItemStack]:

            variable stacks

            variable grid