***CraftingHandler.py - documentation - last updated on 6.6.2020 by uuk***
___

    class CraftingHandler

        function __init__(self)

            variable self.recipeinfotable

            variable self.crafting_recipes_shapeless
                all shapeless recipes sorted after item count

            variable self.crafting_recipes_shaped
                all shaped recipes sorted after item count and than size

            variable self.furnace_recipes
                all smelting outputs sorted after ingredient

            variable self.loaded_mod_dirs

        function __call__(self, obj)

        static
        function add_recipe(recipe: mcpython.crafting.IRecipeType.IRecipe)

        function add_recipe_from_data(self, data: dict)

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