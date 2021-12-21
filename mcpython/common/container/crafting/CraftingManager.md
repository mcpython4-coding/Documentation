***CraftingManager.py - documentation - last updated on 20.12.2021 by uuk***
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

            variable self.static_recipes

            variable self.prepare_for_loading_lock

        function shuffle_data(self)

            variable recipe_group_copy

                    variable recipe_2

                    variable self.recipe_relink_table[recipe.name]

        function check_relink(self, recipe: mcpython.common.container.crafting.IRecipe.IRecipe)

        function __call__(self, obj)

            variable name: str

                variable name

                variable recipe.name

                variable self.recipe_table[name]

            variable recipe_type

                    variable recipe

                    variable recipe

                variable data

                variable data

            variable s

            variable name

            variable result
                todo: add option to run later

            variable self.crafting_recipes_shapeless
                all shapeless recipes sorted after item count

            variable self.crafting_recipes_shaped
                all shaped recipes sorted after item count and then size

            variable self.furnace_recipes
                all smelting outputs sorted after ingredient

                variable recipe

                variable recipe

                variable self.RECIPE_VIEW_INVENTORY

            variable recipes

            variable recipes

            variable self.RECIPE_VIEW_INVENTORY

                    variable self.RECIPE_VIEW_INVENTORY

    variable shared.crafting_handler