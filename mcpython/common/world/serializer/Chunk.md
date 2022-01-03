***Chunk.py - documentation - last updated on 3.1.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @shared.registry class Chunk extends IDataSerializer.IDataSerializer

        variable PART

        variable IGNORED_BLOCKS: typing.Set[str]

        variable IGNORED_ENTITIES: typing.Set[str]

        variable CHUNK_DATA_VERSION

            variable region

            variable chunk_instance: IChunk

            variable shared.world_generation_handler.enable_generation

            variable region

            variable read_buffer: ReadBuffer

            variable version

                    variable fixer

                    variable target

                    variable result

                    variable read_buffer.stream

                variable data

                variable read_buffer.stream

            variable chunk_instance.generated

            variable palette

            variable block_data_buffer

            variable height

                variable index

                variable position

                    variable block_buffer

                    variable name

                    variable visible

                variable type_name

                variable buf

            variable current_type_name

                variable current_type_name

            variable chunk_instance.loaded

            variable chunk_instance.is_ready

            variable chunk_instance.visible

            variable shared.world_generation_handler.enable_generation

            variable region

            variable chunk_instance: IChunk

            variable region

            variable target_buffer

            variable shared.world_generation_handler.enable_generation
                When doing stuff, please make sure that nothing fancy happens with chunks

            variable block_buffer

            variable palette

                variable block

                    variable block_instance_buffer

                    variable block_data

            variable entity_buffer

                variable buf

            variable map_buffer

                variable buf

            variable shared.world_generation_handler.enable_generation
                re-enable world gen as we are finished