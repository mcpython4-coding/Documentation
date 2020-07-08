***IRecipeType.py - documentation - last updated on 12.6.2020 by uuk***
___

    class IRecipe

        static
        function get_recipe_names() -> list

        static
        function from_data(cls, data: dict)

        function __init__(self)

            variable self.uuid

            variable self.name

        function register(self)