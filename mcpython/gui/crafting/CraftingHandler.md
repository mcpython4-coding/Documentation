***CraftingHandler.py - documentation - last updated on 20.7.2020 by uuk***
___

    class CraftingHandler

        function __init__(self)

            variable self.recipeinfotable
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

        function check_relink(self, recipe)

        function __call__(self, obj)

        function add_recipe(self, recipe: mcpython.gui.crafting.IRecipeType.IRecipe, name)

        function add_recipe_from_data(self, data: dict, name: str)

        function add_recipe_from_file(self, file: str)

        function load(self, modname, check_mod_dirs=True, load_direct=False)

        function reload_crafting_recipes(self)

            variable self.crafting_recipes_shapeless
                all shapeless recipes sorted after item count

            variable self.crafting_recipes_shaped
                all shaped recipes sorted after item count and than size

            variable self.furnace_recipes
                all smelting outputs sorted after ingredient

    variable G.craftinghandler

    function load_recipe_providers()