***GridRecipeInstances.py - documentation - last updated on 18.11.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    function transform_to_item_stack(item, file: str) -> typing.List[typing.Tuple[str, int]]
        
        Transforms an item name from recipe to a valid item list to compare with
        :param item: the item name given
        :param file: the file currently in
        :return: an transformed name list of (item name, amount)


            variable itemname

            variable values

            variable value

    class AbstractCraftingGridRecipe extends  mcpython.common.container.crafting.IRecipe.IRecipe,  ABC 

        variable RECIPE_VIEW

        variable CRAFTING_SUPPORT

        function __init__(self)

            variable self.grid_hash

        function __hash__(self)

        function calculate_hash(self) -> int

        function __eq__(self, other)

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
                inputs: typing.Dict[
                typing.Tuple[int, int], typing.List[typing.Tuple[str, int]]
                ],
                output: typing.Tuple[str, int],
                ):

            variable self.inputs

            variable self.output

            variable sx

            variable sy

            variable self.bounding_box_size

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

    @shared.crafting_handler class ArmorDyeRecipe extends AbstractCraftingGridRecipe

        variable RECIPE_TYPE_NAMES

        function as_grid_for_view(
                self, size=(3, 3)
                ) -> typing.Tuple[typing.List[typing.List[typing.List[ItemStack]]], ItemStack]:

        static
        function from_data(cls, data: dict, file: str)

    @shared.crafting_handler class BannerDuplicateRecipe extends AbstractCraftingGridRecipe

        variable RECIPE_TYPE_NAMES

        function as_grid_for_view(
                self, size=(3, 3)
                ) -> typing.Tuple[typing.List[typing.List[typing.List[ItemStack]]], ItemStack]:

        static
        function from_data(cls, data: dict, file: str)

    @shared.crafting_handler class BookCloningRecipe extends AbstractCraftingGridRecipe

        variable RECIPE_TYPE_NAMES

        function as_grid_for_view(
                self, size=(3, 3)
                ) -> typing.Tuple[typing.List[typing.List[typing.List[ItemStack]]], ItemStack]:

        static
        function from_data(cls, data: dict, file: str)

    @shared.crafting_handler class FireworkRocketRecipe extends AbstractCraftingGridRecipe

        variable RECIPE_TYPE_NAMES

        function as_grid_for_view(
                self, size=(3, 3)
                ) -> typing.Tuple[typing.List[typing.List[typing.List[ItemStack]]], ItemStack]:

        static
        function from_data(cls, data: dict, file: str)

    @shared.crafting_handler class FireworkStarRecipe extends AbstractCraftingGridRecipe

        variable RECIPE_TYPE_NAMES

        function as_grid_for_view(
                self, size=(3, 3)
                ) -> typing.Tuple[typing.List[typing.List[typing.List[ItemStack]]], ItemStack]:

        static
        function from_data(cls, data: dict, file: str)

    @shared.crafting_handler class FireworkStarFadeRecipe extends AbstractCraftingGridRecipe

        variable RECIPE_TYPE_NAMES

        function as_grid_for_view(
                self, size=(3, 3)
                ) -> typing.Tuple[typing.List[typing.List[typing.List[ItemStack]]], ItemStack]:

        static
        function from_data(cls, data: dict, file: str)

    @shared.crafting_handler class MapCloningRecipe extends AbstractCraftingGridRecipe

        variable RECIPE_TYPE_NAMES

        function as_grid_for_view(
                self, size=(3, 3)
                ) -> typing.Tuple[typing.List[typing.List[typing.List[ItemStack]]], ItemStack]:

        static
        function from_data(cls, data: dict, file: str)

    @shared.crafting_handler class MapExtendingRecipe extends AbstractCraftingGridRecipe

        variable RECIPE_TYPE_NAMES

        function as_grid_for_view(
                self, size=(3, 3)
                ) -> typing.Tuple[typing.List[typing.List[typing.List[ItemStack]]], ItemStack]:

        static
        function from_data(cls, data: dict, file: str)

    @shared.crafting_handler class RepairItemRecipe extends AbstractCraftingGridRecipe

        variable RECIPE_TYPE_NAMES

        function as_grid_for_view(
                self, size=(3, 3)
                ) -> typing.Tuple[typing.List[typing.List[typing.List[ItemStack]]], ItemStack]:

        static
        function from_data(cls, data: dict, file: str)

    @shared.crafting_handler class ShieldDecoration extends AbstractCraftingGridRecipe

        variable RECIPE_TYPE_NAMES

        function as_grid_for_view(
                self, size=(3, 3)
                ) -> typing.Tuple[typing.List[typing.List[typing.List[ItemStack]]], ItemStack]:

        static
        function from_data(cls, data: dict, file: str)

    @shared.crafting_handler class ShulkerboxColoringRecipe extends AbstractCraftingGridRecipe

        variable RECIPE_TYPE_NAMES

        function as_grid_for_view(
                self, size=(3, 3)
                ) -> typing.Tuple[typing.List[typing.List[typing.List[ItemStack]]], ItemStack]:

        static
        function from_data(cls, data: dict, file: str)

    @shared.crafting_handler class SuspiciousStewRecipe extends AbstractCraftingGridRecipe

        variable RECIPE_TYPE_NAMES

        function as_grid_for_view(
                self, size=(3, 3)
                ) -> typing.Tuple[typing.List[typing.List[typing.List[ItemStack]]], ItemStack]:

        static
        function from_data(cls, data: dict, file: str)

    @shared.crafting_handler class TippedArrowRecipe extends AbstractCraftingGridRecipe

        variable RECIPE_TYPE_NAMES

        function as_grid_for_view(
                self, size=(3, 3)
                ) -> typing.Tuple[typing.List[typing.List[typing.List[ItemStack]]], ItemStack]:

        static
        function from_data(cls, data: dict, file: str)