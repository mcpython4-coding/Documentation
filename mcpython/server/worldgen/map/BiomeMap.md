***BiomeMap.py - documentation - last updated on 16.1.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class BiomeMap extends mcpython.server.worldgen.map.AbstractChunkInfoMap.AbstractMap

        variable NAME

        variable VERSION

        function __init__(self, chunk)

            variable self.biome_data

            variable self.reference_table

            variable data

            variable self.biome_data[:]

            variable biomes

            variable self.reference_table

        function get_at_xyz(self, x: int, y: int, z: int) -> str | None

        function set_at_xyz(self, x: int, y: int, z: int, biome: str | None)

        function dump_debug_info(self, file: str)

                    variable seed

                    variable biome2color[biome]

        function get_biome_color_at(
                self, x: int, y: int, z: int
                ) -> typing.Tuple[float, float, float]:

            variable biome
                todo: implement biome color blending