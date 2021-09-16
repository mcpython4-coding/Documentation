***World.py - documentation - last updated on 16.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class World extends mcpython.common.world.AbstractInterface.IWorld
        
        Class holding all data of the world


        function __init__(self, filename: str = None)

            variable shared.world

            variable self.dimensions

            variable self.active_dimension: int
                todo: change to str; todo: move to player; todo: make property

            variable self.gamerule_handler

            variable self.hide_faces_to_not_generated_chunks: bool
                todo: move to configs / game rules

            variable self.filename: str
                the file-name to use, todo: make None if not needed

            variable self.save_file: mcpython.common.world.SaveFile.SaveFile
                the save file instance

            variable self.players

            variable self.local_player: str
                The name of the local player; None on dedicated servers

            variable self.world_loaded - describes if the world is loaded or not

            variable self.world_generation_process

        function tick(self)

        function add_player(
                self, name: str, add_inventories: bool = True, override: bool = True
                ):
            
            Will add a new player into the world
            :param name: the name of the player to create
            :param add_inventories: if the inventories should be created
            :param override: if the player should be re-created if it exists in memory
            :return: the player instance


            variable self.players[name]

        function get_active_player(
                self, create: bool = True
                ) -> typing.Union[mcpython.common.entity.PlayerEntity.PlayerEntity, None]:
            
            Returns the player instance for this client
            :param create: if the player should be created or not (by calling add_player())
            :return: the player instance or None if no player with the name is arrival


        function get_player_by_name(self, name: str)

        function player_iterator(self) -> typing.Iterable

        function entity_iterator(self) -> typing.Iterable

        function reset_config(self)
            
            Will reset the internal config of the system.
            todo: change game rule handler reset to an non-new-instance
            calls event world:reset_config in the process


            variable self.config

            variable self.gamerule_handler

        function get_active_dimension(
                self,
                ) -> typing.Union[mcpython.common.world.AbstractInterface.IDimension, None]:
            
            will return the dimension the player is in
            :return: the dimension or None if no dimension is set
            todo: move to player


        function get_dimension_names(self) -> typing.Iterable[str]

        function get_dimension_by_name(
                self, name: str
                ) -> mcpython.common.world.AbstractInterface.IDimension:

        function add_dimension(
                self, dim_id: int, name: str, dim_config=None
                ) -> mcpython.common.world.AbstractInterface.IDimension:
            
            will add an new dimension into the system
            :param dim_id: the id to create under
            :param name: the name of the dimension
            :param dim_config: the dim_config to use as gen config
            :return: the dimension instance


                variable dim_config

            variable dim

            variable self.dim_to_id[dim.name]

        function join_dimension(self, dim_id: int)
            
            will change the dimension of the active player
            :param dim_id: the dimension to change to todo: make str
            todo: move to player


            variable sector

            variable old

            variable self.active_dimension

        function get_dimension(
                self, dim_id: int
                ) -> mcpython.common.world.AbstractInterface.IDimension:
            
            will get an dimension with an special id
            :param dim_id: the id to use
            :return: the dimension instance or None if it does not exist


        function hit_test(
                self,
                position: typing.Tuple[float, float, float],
                vector: typing.Tuple[float, float, float],
                max_distance: int = 8,
                ) -> typing.Union[
                typing.Tuple[
                typing.Tuple[int, int, int],
                typing.Tuple[int, int, int],
                typing.Tuple[float, float, float],
                ],
                typing.Tuple[None, None, None],
                ]:
                """
                Line of sight search from current position. If a block is
                intersected it is returned, along with the block previously in the line
                of sight. If no block is found, return None, None, None
                
                Will check for bounding boxes of blocks
                
                :param position: The (x, y, z) position to check visibility from
                :param vector: The line of sight vector
                :param max_distance: How many blocks away to search for a hit
                
                todo: cache the bbox of the block
                todo: move to dimension
                todo: add variant only taking the player
                todo: cache when possible
                todo: add variant for entities
                """
                m = shared.world.gamerule_handler.table[
                "hitTestSteps"
                ].status.status  # get m from the gamerule
                x, y, z = position
                dx, dy, dz = vector
                dx /= m
                dy /= m
                dz /= m
                previous = None
                for _ in range(max_distance * m):
            
            Line of sight search from current position. If a block is
            intersected it is returned, along with the block previously in the line
            of sight. If no block is found, return None, None, None
            Will check for bounding boxes of blocks
            :param position: The (x, y, z) position to check visibility from
            :param vector: The line of sight vector
            :param max_distance: How many blocks away to search for a hit
            todo: cache the bbox of the block
            todo: move to dimension
            todo: add variant only taking the player
            todo: cache when possible
            todo: add variant for entities


            variable m

            variable previous

                variable key

                variable block

                    variable previous

        function show_chunk(
                self,
                chunk: typing.Union[
                typing.Tuple[int, int], mcpython.common.world.AbstractInterface.IChunk
                ],
                ):
            
            Ensure all blocks in the given chunk that should be shown are
            drawn to the canvas.
            :param chunk: the chunk to show


                variable chunk

        function hide_chunk(
                self,
                chunk: typing.Union[
                typing.Tuple[int, int], mcpython.common.world.AbstractInterface.IChunk
                ],
                ):
            
            Ensure all blocks in the given chunk that should be hidden are
            removed from the canvas.
            :param chunk: the chunk to hide


                variable chunk

        function change_chunks(
                self,
                before: typing.Union[typing.Tuple[int, int], None],
                after: typing.Union[typing.Tuple[int, int], None],
                generate_chunks=True,
                load_immediate=True,
                ):
            
            Move from chunk `before` to chunk `after`
            :param before: the chunk before
            :param after: the chunk after
            :param generate_chunks: if chunks should be generated
            :param load_immediate: if chunks should be loaded immediate if needed
            todo: move to dimension


            variable before_set

            variable after_set

            variable pad

            variable hide
                show = after_set - before_set

                        variable chunk

        function cleanup(self, remove_dims=False, filename=None)
            
            will clean up the world
            :param remove_dims: if dimensions should be cleared
            :param filename: the new filename if it changes
            todo: make split up into smaller functions


                variable shared.world.get_active_player().flying

            variable self.spawn_point

        function setup_by_filename(self, filename: str)
            
            will set up the system for an new file name
            :param filename: the file name to use
