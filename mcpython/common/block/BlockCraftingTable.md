***BlockCraftingTable.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class BlockCraftingTable extends AbstractBlock.AbstractBlock
        
        Class for the crafting table


        variable NAME: str

        variable HARDNESS

        variable ASSIGNED_TOOLS

        function on_player_interaction(
                self, player, button: int, modifiers: int, hit_position: tuple
                ):

        function get_inventories(self)

        function on_block_remove(self, reason)

        static
        function modify_block_item(cls, factory)

    @shared.mod_loader("minecraft", "stage:block:load")
    function load()