***World.py - documentation - last updated on 31.5.2020 by uuk***
___

    class World
        
        class holding all data of the world


        function __init__(self, filename: str = None)

            variable G.world

            variable self.active_dimension: int - todo: change to str; todo: move to player; todo: make property

            variable self.CANCEL_DIM_CHANGE: bool - flag for canceling the dim change event

            variable self.hide_faces_to_ungenerated_chunks: bool - todo: move to configs

            variable self.filename: str - the file-name to use, todo: make None if not needed

            variable self.savefile: storage.SaveFile.SaveFile - the save file instance

            variable self.active_player: str - todo: make property, make None-able & set default None when not in world
                self.add_player("unknown", add_inventories=False)

        function add_player(self, name: str, add_inventories: bool = True, override: bool = True)
            
            will add an new player into the world
            :param name: the name of the player to create
            :param add_inventories: if the inventories should be created
            :param override: if the player should be re-created if it exists in memory
            :return: the player instance


        function get_active_player(self, create: bool = True) -> typing.Union[world.player.Player, None]
            
            returns the player instance for this client
            :param create: if the player should be created or not
            :return: the player instance or None if no player is set


        function reset_config(self)
            
            Will reset the internal config of the system.
            todo: change game rule handler reset to an non-new-instance
            calls event world:reset_config in the process


            variable self.config

            variable self.gamerulehandler

        function get_active_dimension(self) -> typing.Union[world.Dimension.Dimension, None]
            
            will return the dimension the player is in
            :return: the dimension or None if no dimension is set
            todo: move to player


        function add_dimension(self, dim_id: int, name: str, dim_config=None, config=None) -> world.Dimension.Dimension
            
            will add an new dimension into the system
            :param dim_id: the id to create under
            :param name: the name of the dimension
            :param config: deprecated, replaced by dim_config
            :param dim_config: the dim_config to use as gen config
            :return: the dimension instance


        function join_dimension(self, dim_id: int, save_current=None)
            
            will change the dimension of the active player
            :param dim_id: the dimension to change to todo: make str
            :param save_current: unused, deprecated; always set to True now
            todo: move to player


        function get_dimension(self, dim_id: int) -> world.Dimension.Dimension
            
            will get an dimension with an special id
            :param dim_id: the id to use
            :return: the dimension instance or None if it does not exist

            
            Line of sight search from current position. If a block is
            intersected it is returned, along with the block previously in the line
            of sight. If no block is found, return None, None, None
            Will check for bounding boxes of blocks
            :param position: The (x, y, z) position to check visibility from
            :param vector: The line of sight vector
            :param max_distance: How many blocks away to search for a hit
            todo: cache the bbox of the block


            variable m - get m from the gamerule

            variable previous

                variable key

                variable blocki

                    variable previous

        @deprecation.deprecated("dev1-4", "a1.3.0")
        function show_sector(self, sector): self.show_chunk(sector)
                
                def show_chunk(self, chunk: typing.Union[typing.Tuple[int, int], world.Chunk.Chunk]):

        function show_chunk(self, chunk: typing.Union[typing.Tuple[int, int], world.Chunk.Chunk])
            
            Ensure all blocks in the given chunk that should be shown are
            drawn to the canvas.
            :param chunk: the chunk to show


        @deprecation.deprecated("dev1-4", "a1.3.0")
        function hide_sector(self, sector, immediate=False): self.hide_chunk(sector)
                
                def hide_chunk(self, chunk: typing.Union[typing.Tuple[int, int], world.Chunk.Chunk]):

        function hide_chunk(self, chunk: typing.Union[typing.Tuple[int, int], world.Chunk.Chunk])
            
            Ensure all blocks in the given chunk that should be hidden are
            removed from the canvas.
            :param chunk: the chunk to hide


        @deprecation.deprecated("dev1-4", "a1.3.0")
        function change_sectors(self, before, after, immediate=False, generate_chunks=True, load_immediate=False)

        function change_chunks(self, before: typing.Tuple[int, int], after: typing.Tuple[int, int], generate_chunks=True,
                load_immediate=True):
            
            Move from chunk `before` to chunk `after`
            :param before: the chunk before
            :param after: the chunk after
            :param generate_chunks: if chunks should be generated
            :param load_immediate: if chunks should be loaded immediate if needed


                        variable chunk

        @deprecation.deprecated("dev1-4", "a1.3.0")
        function process_queue(self)

        @deprecation.deprecated("dev1-4", "a1.3.0")
        function process_tasks(self, timer=0.2)

        @deprecation.deprecated("dev1-4", "a1.3.0")
        function process_entire_queue(self)

        function cleanup(self, remove_dims=False, filename=None, add_player=False)
            
            will clean up the world
            :param remove_dims: if dimensions should be cleared
            :param filename: the new filename if it changes
            :param add_player: if the player should be added
            todo: make split up into smaller functions


        function setup_by_filename(self, filename: str)
            
            will set up the system for an new file name
            :param filename: the file name to use
