***ICustomBlockRenderer.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class ICustomBatchBlockRenderer

        function add(self, position: typing.Tuple[int, int, int], block, face, batches)

        function remove(self, position: typing.Tuple[int, int, int], block, data, face)

    @onlyInClient() class ICustomDrawMethodRenderer

        function draw(self, position: typing.Tuple[int, int, int], block)

    @onlyInClient() class ICustomBlockVertexManager

        function handle(self, block, vertices, face, blockstate)