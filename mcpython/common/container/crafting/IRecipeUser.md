***IRecipeUser.py - documentation - last updated on 20.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


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