***BiomeGenDebugGenerator.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class DebugBiomeWorldGenerator extends  mcpython.server.worldgen.mode.IWorldGenConfig.IWorldGenConfig 

        variable NAME

        variable DISPLAY_NAME

        variable DIMENSION

        variable LAYERS

        variable BIOME_SOURCE

        variable BIOMES

        variable LANDMASSES

        variable BIOME_TO_BLOCK

        static
        function generate_table(cls)

        static
        function on_chunk_generation_finished(
                cls,
                chunk,
                ):

            variable biome_map

                    variable biome

                    variable block