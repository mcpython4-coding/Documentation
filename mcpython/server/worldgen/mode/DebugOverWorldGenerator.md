***DebugOverWorldGenerator.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
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