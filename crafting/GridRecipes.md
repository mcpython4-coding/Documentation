***GridRecipes.py - documentation - last updated on 14.5.2020 by uuk***
___

    function transform_to_item_stack(item, table: dict) -> list
        
        transforms an item name from recipe to an valid item list to compare with
        :param item: the itemname given
        :param table: optional: an table of items which were decoded previous
        :return: an transformed name list of (itemname, amount)


    @G.craftinghandler class GridShaped extends crafting.IRecipeType.IRecipe

        static function get_recipe_names() -> list

        static function from_data(cls, data: dict)

        function __init__(self, inputs, output)

            variable self.inputs

            variable self.output

            variable sx

            variable sy

            variable self.bboxsize

        function register(self)

    @G.craftinghandler class GridShapeless extends crafting.IRecipeType.IRecipe

        static function get_recipe_names() -> list

        static function from_data(cls, data: dict)

        function __init__(self, inputs, output)

            variable self.inputs

            variable self.output

        function register(self)