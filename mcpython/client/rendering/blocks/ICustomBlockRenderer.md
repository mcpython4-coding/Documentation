***ICustomBlockRenderer.py - documentation - last updated on 18.11.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ICustomBlockRenderer extends ABC

        function __init__(self)

            variable self.block

        function on_block_exposed(self, block)

        function on_block_fully_hidden(self, block)

    class ICustomBatchBlockRenderer extends ICustomBlockRenderer,  ABC

        function add(self, position: typing.Tuple[int, int, int], block, face, batches)

        function add_multi(
                self, position: typing.Tuple[int, int, int], block, faces: int, batches
                ):

            variable d

        function remove(self, position: typing.Tuple[int, int, int], block, data, face)

        function remove_multi(self, position: typing.Tuple[int, int, int], block, data)

    class ICustomDrawMethodRenderer extends ICustomBlockRenderer,  ABC

        variable DRAW_PHASE

        function on_block_exposed(self, block)

            variable block.face_info.bound_rendering_info

        function on_block_fully_hidden(self, block)

        function draw(self, position: typing.Tuple[int, int, int], block)