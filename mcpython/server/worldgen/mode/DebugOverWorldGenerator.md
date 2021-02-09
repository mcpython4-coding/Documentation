***DebugOverWorldGenerator.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class BlockInfo

        variable TABLE - {chunk: tuple<x, z> -> {position<x,z> -> blockname}}

        static
        function construct(cls)

            variable block_table

            variable blocklist

            variable size

            variable hsize

                variable chunk

                    variable rx

    class DebugWorldGenerator extends  mcpython.server.worldgen.mode.IWorldGenConfig.IWorldGenConfig 

        variable NAME

        variable DIMENSION

        variable DISPLAY_NAME

        static
        function on_chunk_prepare_generation(
                cls,
                chunk,
                array: mcpython.server.worldgen.WorldGenerationTaskArrays.WorldGenerationTaskHandlerReference,
                ):

                variable height_map

                variable block_map

            variable shared.world.get_active_player().flying