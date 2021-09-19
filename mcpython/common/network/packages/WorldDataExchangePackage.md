***WorldDataExchangePackage.py - documentation - last updated on 19.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class DataRequestPackage extends AbstractPackage

        variable PACKAGE_NAME

        function __init__(self)

            variable self.request_world_info_state

            variable self.request_player_info_state

            variable self.requested_dimensions

            variable self.requested_chunks

        function request_world_info(self)

        function request_dimension_info(self, name: str)

        function request_chunk(self, dimension: str, cx: int, cz: int)

        function request_player_info(self)

        function write_to_buffer(self, buffer: WriteBuffer)

        function read_from_buffer(self, buffer: ReadBuffer)

        function handle_inner(self)

    class WorldInfoPackage extends AbstractPackage
        
        Package server -> client for sending requested data back to client.
        Mostly only for sync stuff, but dimensions should be created when needed


        variable PACKAGE_NAME

        function __init__(self)

            variable self.dimensions

            variable self.spawn_point

        function setup(self)

        function write_to_buffer(self, buffer: WriteBuffer)

        function read_from_buffer(self, buffer: ReadBuffer)

            variable self.dimensions

        function handle_inner(self)

                variable dim

                    variable new_dim

                    variable new_dim

                    variable new_dim.world_generation_config_objects

                    variable new_dim.batches

                        variable entity.dimension

    class DimensionInfoPackage extends AbstractPackage

        variable PACKAGE_NAME

        function __init__(self)

        function setup(self, dimension: str)

    class ChunkDataPackage extends AbstractPackage

        variable PACKAGE_NAME

        function __init__(self)

            variable self.dimension

            variable self.position

            variable self.blocks

        function setup(self, dim: str, position: typing.Tuple[int, int])

            variable chunk

                variable b

        function write_to_buffer(self, buffer: WriteBuffer)

        function read_from_buffer(self, buffer: ReadBuffer)

            variable self.dimension

            variable self.position

                variable name

                    variable instance

                    variable visible

        function handle_inner(self)

            variable i

                variable block

            variable chunk.loaded

    class ChunkUpdatePackage extends AbstractPackage

        variable PACKAGE_NAME