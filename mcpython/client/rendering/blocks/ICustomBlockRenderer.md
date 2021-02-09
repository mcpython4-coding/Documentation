***ICustomBlockRenderer.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class ICustomBatchBlockRenderer

        function add(self, position: typing.Tuple[int, int, int], block, face, batches)

        function remove(self, position: typing.Tuple[int, int, int], block, data, face)

    @onlyInClient() class ICustomDrawMethodRenderer

        function draw(self, position: typing.Tuple[int, int, int], block)

    @onlyInClient() class ICustomBlockVertexManager

        function handle(self, block, vertices, face, blockstate)