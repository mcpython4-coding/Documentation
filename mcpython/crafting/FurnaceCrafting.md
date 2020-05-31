***FurnaceCrafting.py - documentation - last updated on 6.6.2020 by uuk***
___

    @G.craftinghandler class FurnesRecipe extends mcpython.crafting.IRecipeType.IRecipe

        static
        function get_recipe_names() -> list

        static
        function from_data(cls, data: dict)

        function __init__(self, t, i, o, xp, time)

            variable self.input

            variable self.output

            variable self.xp

            variable self.time

            variable self.type

        function register(self)