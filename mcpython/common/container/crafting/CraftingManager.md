***CraftingManager.py - documentation - last updated on 18.4.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class CraftingManager

        variable RECIPE_VIEW_INVENTORY

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

        function check_relink(self, recipe: mcpython.common.container.crafting.IRecipe.IRecipe)

        function __call__(self, obj)

        function add_recipe(
                self, recipe: mcpython.common.container.crafting.IRecipe.IRecipe, name: str
                ):

            variable recipe.name

            variable self.recipe_table[name]

        function add_recipe_from_data(self, data: dict, name: str, file: str = None)

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

        function show_to_player(self, recipe_name: str)

            variable recipe

                variable self.RECIPE_VIEW_INVENTORY

    variable shared.crafting_handler

    function load_recipe_providers()