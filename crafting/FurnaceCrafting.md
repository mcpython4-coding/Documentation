***FurnaceCrafting.py - documentation - last updated on 14.5.2020 by uuk***
___

    @G.craftinghandler class FurnesRecipe extends crafting.IRecipeType.IRecipe
        static function get_recipe_names() -> list
        static function from_data(cls, data: dict)
        function __init__(self, t, i, o, xp, time)
        function register(self)