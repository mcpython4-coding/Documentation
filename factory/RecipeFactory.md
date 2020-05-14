***RecipeFactory.py - documentation - last updated on 14.5.2020 by uuk***
___

    class ShapedCraftingRecipeFactory
        function __init__(self, output)
        function set_input(self, position, itemname)
        function finish(self)

    class ShapelessCraftingRecipeFactory
        function __init__(self, output)
        function add_item(self, item, count=1)
        function finish(self)