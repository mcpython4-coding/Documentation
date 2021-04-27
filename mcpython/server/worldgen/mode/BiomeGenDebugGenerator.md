***BiomeGenDebugGenerator.py - documentation - last updated on 27.4.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
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

            variable height_map

                    variable biome

                    variable block

            variable shared.world.get_active_player().flying