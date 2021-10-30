***CraftingTable.py - documentation - last updated on 30.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class CraftingTable extends AbstractBlock.AbstractBlock
        
        Class for the crafting table


        variable NAME: str

        variable HARDNESS

        variable ASSIGNED_TOOLS

        function on_player_interaction(
                self, player, button: int, modifiers: int, hit_position: tuple, itemstack
                ):

        function get_inventories(self)

        function on_block_remove(self, reason)

        static
        function modify_block_item(cls, factory)