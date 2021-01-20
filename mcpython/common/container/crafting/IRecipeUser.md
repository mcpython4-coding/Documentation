***IRecipeUser.py - documentation - last updated on 20.1.2021 by uuk***
___

    class IRecipeUser extends mcpython.common.event.Registry.IRegistryContent
        
        Abstract marker for a thing supporting recipes.
        Any recipe may be linked. There may be none recipe linked.
        Not every recipe type may link a IRecipeUser
        Recipe users capable of linking to a current inventory or similar should implement
        insert_items() and override CAN_INSERT_ITEMS to True


        variable TYPE

        variable CAN_INSERT_ITEMS

        variable RECIPE_TYPES: typing.List[str]

        static
        function on_recipe_resolved(
                cls, recipe: mcpython.common.container.crafting.IRecipe.IRecipe
                ):

        function insert_items_from(
                self,
                recipe: mcpython.common.container.crafting.IRecipe.IRecipe,
                item_source: typing.List[ItemStack],
                ) -> bool: