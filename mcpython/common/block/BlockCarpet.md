***BlockCarpet.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    variable carpet_bbox

    class ICarpet extends mcpython.common.block.AbstractBlock.AbstractBlock
        
        base class for every carpet


        variable DEFAULT_FACE_SOLID

        function on_block_update(self)

        function get_view_bbox(self)

        static
        function modify_block_item(cls, factory)

    function create_carpet(carpet_color: str)
        
        generator function for carpets. Will create an new class for an carpet
        :param carpet_color: the color name of the carpet
        :return: the generated class


        @shared.registry class Carpet extends ICarpet

            variable NAME: str - the name of the block

    @shared.mod_loader("minecraft", "stage:block:load")
    function load()