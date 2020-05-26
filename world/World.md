***World.py - documentation - last updated on 26.5.2020 by uuk***
___

    class IWorldAccess
        
        Abstract class for every world-access


    class World extends IWorldAccess
        
        base class for an world to access. Located at the server


        function __init__(self, filename: typing.Union[None, str] = None)
            
            will create an new ServerWorld-instance
            :param filename: the file name to use or None for default one


            variable G.world

            variable self.spawnpoint - todo: move this to world gen

            variable self.dimensions - an dict of dim id -> dim instance

            variable self.active_dimension - we are currently in the overworld, todo: make dimension str

            variable self.config - the world config, contains: seed

            variable self.gamerulehandler - the handler for game rules

            variable self.CANCEL_DIM_CHANGE - cancel for the dim change event

            variable self.hide_faces_to_ungenerated_chunks

            variable self.filename

            variable self.savefile - the access to the saves of the world

            variable self.players - when in an network, stores an reference to all other players

            variable self.active_player - we do NOT know the player yet, todo: store the player name in configs

        @G.EnumSide.SERVER function add_player(self, name: str, add_inventories: bool = True)
            
            will add an player
            :param name: the name of the player
            :param add_inventories: if the inventories should be created now or not
            :return: the created player
            Only arrival on Server


            variable self.players[name]

        @G.EnumSide.CLIENT function get_active_player(self)
            
            get the player currently active player
            :return: the player instance
            Only arrival on client


        @G.EnumSide.SERVER function reset_config(self)
            
            will reset the server config


        @G.EnumSide.CLIENT function get_active_dimension(self) -> world.Dimension.Dimension
            
            will return the dimension of the active player
            :return: the active dimension


        @G.EnumSide.SERVER function add_dimension(self, id, name, config={}) -> world.Dimension.Dimension
            
            will add an new dimension
            :param id: the id to use
            :param name: the name of the dimension
            :param config: the config to use
            :return:


        @deprecation.deprecated("dev1-3", "a1.3.0") @G.EnumSide.CLIENT function join_dimension(self, id, save_current=True)
            
            will change the dimension of the active player
            :param id: the id of the dimension as an int todo: make an str
            :param save_current: unused, always expected True
            todo: remove


        function hit_test(self, position: typing.Tuple[float, float, float], vector
            
            Line of sight search from current position. If a block is
            intersected it is returned, along with the block previously in the line
            of sight. If no block is found, return None, None.
            :param position: tuple of len 3, The (x, y, z) position to check visibility from.
            :param vector: tuple of len 3, The line of sight vector.
            :param max_distance:, How many blocks away to search for a hit.
            todo: vector should be lenght of three


        @deprecation.deprecated("dev1-3", "a1.4.0") function show_sector(self, sector: typing.Tuple[int, int], immediate: bool = False)
            
            Ensure all blocks in the given sector that should be shown are
            drawn to the canvas.
            :param sector: the chunk to show
            :param immediate: if immediate or not, unused


        @deprecation.deprecated("dev1-3", "a1.4.0") function hide_sector(self, sector: typing.Tuple[int, int], immediate: bool = False)
            
            Ensure all blocks in the given sector that should be hidden are
            removed from the canvas.
            :param sector: the chunk to hide
            :param immediate: if immediate or not, unused


        function change_sectors(self, before: typing.Tuple[int, int], after: typing.Tuple[int, int], immediate
            
            Move from sector `before` to sector `after`. A sector is a
            contiguous x, y sub-region of world. Sectors are used to speed up
            world rendering.
            :param before: where before was
            :param after: where after is
            :param immediate: if immediate should be shown/hidden, unused
            :param generate_chunks: if chunks should be generated when needed
            :param load_immediate: if chunks should be immediate loaded when needed
            todo: add variant with positions instead of vectors


                        variable chunk

        @deprecation.deprecated("dev1-3", "a1.3.0") function process_queue(self)

        @deprecation.deprecated("dev1-3", "a1.3.0") function process_tasks(self, timer=0.2)

        @deprecation.deprecated("dev1-3", "a1.3.0") function process_entire_queue(self)
            
            Process the entire queue with no breaks.


        @G.EnumSide.SERVER function cleanup(self, remove_dims: bool = False, filename: str = None, add_player: bool = False)
            
            will clean up the world
            :param remove_dims: if dimensions should be removed
            :param filename: the filename for the new world
            :param add_player: if the player should be re-created


        @G.EnumSide.SERVER function setup_by_filename(self, filename: str)
            
            will set up the system for an new world
            :param filename: the filename to use
