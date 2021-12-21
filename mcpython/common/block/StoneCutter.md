***StoneCutter.py - documentation - last updated on 20.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class StoneCutter extends IHorizontalOrientableBlock,  IRecipeUser
        
        Class for the stone cutter block


        variable NAME

        variable HARDNESS

        variable ASSIGNED_TOOLS

        variable MINIMUM_TOOL_LEVEL

        variable DEBUG_WORLD_BLOCK_STATES

        variable IS_SOLID

        variable DEFAULT_FACE_SOLID

        variable INVENTORY

        function __init__(self)

                variable self.inventory

                variable self.inventory

            variable self.inventory

        function get_inventories(self)

        function insert_items_from(
                self,
                recipe: StoneCuttingRecipe,
                item_source: typing.List[ItemStack],
                items_to_remove_consumer: typing.Callable[[ItemStack], None],
                ) -> bool:

            variable previous

            variable recipe_index_key

            variable index

            variable self.inventory.currently_selected

        static
        function set_block_data(cls, item, block)