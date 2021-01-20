***CraftingManager.py - documentation - last updated on 20.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class CraftingManager

        function __init__(self)

            variable self.recipe_info_table
                todo: add special registry for recipes

            variable self.recipe_table

            variable self.recipe_relink_table

            variable self.crafting_recipes_shapeless
                all shapeless recipes sorted after item count

            variable self.crafting_recipes_shaped
                all shaped recipes sorted after item count and than size

            variable self.furnace_recipes
                all smelting outputs sorted after ingredient

            variable self.loaded_mod_dirs

        function shuffle_data(self)

        function check_relink(
                self, recipe: mcpython.common.container.crafting.IRecipe.IRecipe
                ):

            variable name

        function __call__(self, obj)

        function add_recipe(
                self, recipe: mcpython.common.container.crafting.IRecipe.IRecipe, name: str
                ):

            variable recipe.name

            variable self.recipe_table[name]

        function add_recipe_from_data(self, data: dict, name: str, file=None)

        function add_recipe_from_file(self, file: str)

                variable data

            variable s

            variable name

            variable result
                todo: add option to run later

        function load(self, modname: str, check_mod_dirs=True, load_direct=False)

        function reload_crafting_recipes(self)

            variable self.crafting_recipes_shapeless
                all shapeless recipes sorted after item count

            variable self.crafting_recipes_shaped
                all shaped recipes sorted after item count and than size

            variable self.furnace_recipes
                all smelting outputs sorted after ingredient

    variable shared.crafting_handler

    function load_recipe_providers()