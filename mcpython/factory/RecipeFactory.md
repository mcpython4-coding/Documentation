***RecipeFactory.py - documentation - last updated on 10.6.2020 by uuk***
___

    @deprecation.deprecated("dev2-2", "a1.5.0") class ShapedCraftingRecipeFactory

        @deprecation.deprecated("dev2-2", "a1.5.0")
        function __init__(self, output)

            variable self.grid

            variable self.output

        @deprecation.deprecated("dev2-2", "a1.5.0")
        function set_input(self, position, itemname)

        @deprecation.deprecated("dev2-2", "a1.5.0")
        function finish(self)

    @deprecation.deprecated("dev2-2", "a1.5.0") class ShapelessCraftingRecipeFactory

        @deprecation.deprecated("dev2-2", "a1.5.0")
        function __init__(self, output)

            variable self.output

            variable self.items

        @deprecation.deprecated("dev2-2", "a1.5.0")
        function add_item(self, item, count=1)

        @deprecation.deprecated("dev2-2", "a1.5.0")
        function finish(self)