***ShulkerBoxRenderer.py - documentation - last updated on 19.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ShulkerBoxRenderer extends  mcpython.client.rendering.blocks.ICustomBlockRenderer.ICustomBatchBlockRenderer 
        
        Class defining how a shulker box is rendered
        todo: add open / close animations


        function __init__(self, texture_location: str)

            variable self.texture_location

            variable self.texture

            variable self.group

            variable self.box_model

        function add(self, position: typing.Tuple[int, int, int], block, face, batches)

        function add_multi(self, position: typing.Tuple[int, int, int], block, faces, batches)

        function play_open_animation(self, block)

        function play_close_animation(self, block)