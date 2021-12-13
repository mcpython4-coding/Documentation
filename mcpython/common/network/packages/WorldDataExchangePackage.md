***WorldDataExchangePackage.py - documentation - last updated on 13.12.2021 by uuk***
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

            variable self.request_world_info_state

            variable self.request_player_info_state

            variable self.requested_dimensions

            variable self.requested_chunks

    class WorldInfoPackage extends AbstractPackage
        
        Package server -> client for sending requested data back to client.
        Mostly only for sync stuff, but dimensions should be created when needed


        variable PACKAGE_NAME

        function __init__(self)

            variable self.dimensions

            variable self.spawn_point

        function setup(self)

            variable self.spawn_point

            variable self.dimensions

            variable shared.world.spawn_point

                variable dim

                    variable new_dim

                    variable new_dim

                    variable new_dim.world_generation_config_objects

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

            variable self.force

            variable self.blocks

        function setup(self, dim: str, position: typing.Tuple[int, int], force=False)

            variable chunk

                variable b

            variable start

            variable chunk

            variable start

            variable self.dimension

            variable self.position

            variable self.force

                    variable name

                    variable instance

            variable start

            variable chunk

            variable i

                variable block

            variable chunk.loaded

    class ChunkBlockChangePackage extends AbstractPackage

        variable PACKAGE_NAME

        function __init__(self)

            variable self.dimension

            variable self.data

        function set_dimension(self, dimension: str)

        function change_position(
                self, position: typing.Tuple[int, int, int], block, update_only=False
                ):
            
            Updates the block data at a given position
            :param position: the position
            :param block: the block instance
            :param update_only: if to only update the block, not add a new one


            variable self.dimension

            variable dimension

                variable position

                    variable name

                        variable b

                        variable instance

            variable self.data

            variable dimension