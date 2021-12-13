***Chunk.py - documentation - last updated on 13.12.2021 by uuk***
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

            variable region

                variable data

            variable chunk_instance: mcpython.engine.world.AbstractInterface.IChunk

            variable shared.world_generation_handler.enable_generation
                Don't generate stuff while we are saving stuff

            variable data

            variable chunk_instance.generated

            variable inv_file
                This file stores the inventory data

                    variable data["block_palette"][i]

                variable position

                variable d

                    variable data_map_data

                    variable entity_instance

                variable entity_instance.rotation

                variable entity_instance.hearts

            variable chunk_instance.loaded

            variable chunk_instance.is_ready

            variable chunk_instance.visible

            variable shared.world_generation_handler.enable_generation

                    variable buffer

            variable flag

            variable region

            variable chunk_instance: mcpython.engine.world.AbstractInterface.IChunk

            variable data

                variable data

                variable cdata

                variable cdata

                variable override
                    And mark that all data should be written

            variable shared.world_generation_handler.enable_generation
                When doing stuff, please make sure that nothing fancy happens with chunks

            variable palette
                Load the block palette
                list of {"custom": <some stuff>, "name": <name>, "shown": <shown>, ...}

            variable inv_file
                where to dump inventory stuff

            variable overridden

                variable rel_position
                    the relative position to the chunk

                variable block

                variable buffer

                variable block_data

                    variable cdata["blocks"][rel_position]

                    variable cdata["blocks"][rel_position]

                variable entity_data

                    variable cdata["maps"][data_map.NAME]

            variable data[chunk] - dump the chunk into the region

            variable shared.world_generation_handler.enable_generation