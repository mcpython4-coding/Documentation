***Carpet.py - documentation - last updated on 25.4.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable carpet_bbox

    class AbstractCarpet extends mcpython.common.block.AbstractBlock.AbstractBlock,  ABC
        
        base class for every carpet


        variable DEFAULT_FACE_SOLID

        function on_block_update(self)

        function get_view_bbox(self)

        static
        function modify_block_item(cls, factory)

    function create_carpet_block(carpet_color: str)
        
        generator function for carpets. Will create an new class for an carpet
        :param carpet_color: the color name of the carpet
        :return: the generated class


        @shared.registry class Carpet extends AbstractCarpet

            variable NAME: str - the name of the block

    function load()