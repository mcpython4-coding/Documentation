***BiomeMap.py - documentation - last updated on 11.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @shared.world_generation_handler class BiomeMap extends mcpython.server.worldgen.map.AbstractChunkInfoMap.AbstractMap

        variable NAME

        function __init__(self, chunk)

        function load_from_saves(self, data)

                        variable index

                            variable previous_column

        function dump_for_saves(self)

                    variable previous_column

                        variable biome

                            variable previous_column

        function get_at_xz(self, x: int, z: int) -> str

        function get_at_xyz(self, x: int, y: int, z: int) -> str

        function set_at_xz(self, x: int, z: int, biome: str)

        function set_at_xyz(self, x: int, y: int, z: int, biome: str)