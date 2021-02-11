***HeightMap.py - documentation - last updated on 11.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @shared.world_generation_handler class HeightMap extends mcpython.server.worldgen.map.AbstractChunkInfoMap.AbstractMap

        variable NAME

        function __init__(self, chunk)

        function load_from_saves(self, data)

        function dump_for_saves(self)

        function get_at_xz(self, x: int, z: int)

        function set_at_xz(self, x: int, z: int, height)