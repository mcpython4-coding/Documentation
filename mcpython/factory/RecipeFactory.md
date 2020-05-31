***RecipeFactory.py - documentation - last updated on 6.6.2020 by uuk***
___

    class ShapedCraftingRecipeFactory

        function __init__(self, output)

            variable self.grid

            variable self.output

        function set_input(self, position, itemname)

        function finish(self)

    class ShapelessCraftingRecipeFactory

        function __init__(self, output)

            variable self.output

            variable self.items

        function add_item(self, item, count=1)

        function finish(self)