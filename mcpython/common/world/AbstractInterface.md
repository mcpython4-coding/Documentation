***AbstractInterface.py - documentation - last updated on 8.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class ChunkLoadTicketType extends enum.Enum

        variable SPAWN_CHUNKS

        variable FORCE_LOADED

        variable PLAYER_LOADED - needs player instance

        variable WORLD_GENERATION_LOADED

        variable BLOCK_LOOKUP_LOADED

        variable ENTITY_CHUNK_CHANGE_LOADED

        variable ENTITY_AI_PROCESSING_LOADED - needs entity instance

        function __iter__(self)

    class IChunk extends ABC
        
        Abstract class for chunks
        Belows follows an API description
        This API is STABLE, its implementation should NOT change dramatically if not needed
        Implementations beside the default Chunk implementation may change signature and calling type (async/await).
        They should try to be as close to the API as possible
        The following stuff MAY change in the near future:
            - structure / existence of __world-attribute
            - structure / existence of __positions_updated_since_last_save-attribute
            - existence of entities attribute
            - WIP of chunk_loaded_list attribute, together with add_chunk_load_ticket(...) and check_for_unload()


        function __init__(self)

            variable self._positions_updated_since_last_save

            variable self.entities: typing.Set[typing.Any]
                a set of entities in this chunk
                todo: maybe use per-sector?

            variable self.chunk_loaded_list
                inner API list for ChunkLoadTickets [WIP]
                todo: use something better...

        function clear_positions_updated_since_last_save(self)

        function get_positions_updated_since_last_save(self)

        function mark_position_dirty(self, position)

        function is_loaded(self) -> bool

        function is_generated(self) -> bool

        function is_visible(self) -> bool

        function add_chunk_load_ticket(self, ticket_type: ChunkLoadTicketType, data=None)
            
            Chunk load ticket API
            Adds a new ticket to the inner system for letting this chunk be loaded
            WIP
            todo: add timestamp
            todo: 16 lists are not good...
            todo: add way to remove ticket
            todo: save this to the save files


        function check_for_unload(self)
            
            Helper function for checking if this chunk should get unloaded or not
            todo: this is not optimal
            todo: do we really need to do this every tick?
            todo: 16 lists are bad!


        function get_dimension(self) -> "IDimension"

        function get_position(self) -> typing.Tuple[int, int]

        function get_maximum_y_coordinate_from_generation(self, x: int, z: int) -> int
            
            Helper for finding the highest position in the chunk from generation
            todo: migrate to special system for world generation attributes


        function exposed_faces(
                self, position: typing.Tuple[int, int, int]
                ) -> typing.Dict[mcpython.util.enums.EnumSide, bool]:
            
            Helper for getting exposed faces of a block
            todo: add iterating variant


        function is_position_blocked(self, position: typing.Tuple[float, float, float]) -> bool
            
            Checks if the given position is not air


        function add_block(
                self,
                position: tuple,
                block_name: typing.Union[str, typing.Any],
                immediate=True,
                block_update=True,
                block_update_self=True,
                lazy_setup: typing.Callable[[typing.Any], None] = None,
                check_build_range=True,
                block_state=None,
                ) -> typing.Optional[typing.Any]:
            
            Adds an block to the given position
            :param position: the position to add at
            :param block_name: the name of the block or an instance of it (typing.Any)
            :param immediate: if the block should be shown if needed or not
            :param block_update: if an block-update should be send to neighbors blocks
            :param block_update_self: if the block should get an block-update
            :param lazy_setup: an callable for setting up the block instance
            :param check_build_range: if the build limits should be checked
            :param block_state: the block state to create in, or None if not set
            :return: the block instance or None if it could not be created for some reason
            todo: add method which raises an exception on fail


        function on_block_updated(
                self, position: typing.Tuple[float, float, float], itself=True
                ):
            
            Updates the block at the given position


        function remove_block(
                self,
                position: typing.Union[
                typing.Tuple[int, int, int],
                typing.Any,
                ],
                immediate: bool = True,
                block_update: bool = True,
                block_update_self: bool = True,
                reason=None,
                ):
            
            Removes a block from a given position
            :param position: the position to remove at
            :param immediate: immediate hide?
            :param block_update: block update to the blocks around?
            :param block_update_self: block update to the current block?
            :param reason: why it is removed, see mcpython.common.block.AbstractBlock.BlockRemovalReason for possible
                values
            todo: add "unsafe" variant skipping various sanity checks
            todo: add option to not call on_remove on target block


        function check_neighbors(self, position: typing.Tuple[int, int, int])
            
            Checks the visual state of adjusting blocks to the given position
            todo: rename to something fitting!


        function show_block(
                self,
                position: typing.Union[
                typing.Tuple[int, int, int],
                typing.Any,
                ],
                immediate: bool = True,
                ):
            
            Client-only visual show function
            Unused internally
            todo: remove
            use block.face_state.update(True) instead


        function hide_block(
                self,
                position: typing.Union[
                typing.Tuple[int, int, int],
                typing.Any,
                ],
                immediate=True,
                ):
            
            Client-only visual hide function
            Unused internally
            todo: remove
            use block.face_state.hide_all() instead


        function show(self, force=False)
            
            Shows the entire chunk
            :param force: unused; todo: remove


        function hide(self, force=False)
            
            Hides an entire chunk
            :param force: if to force-hide; todo: remove


        function update_visible_block(self, position: typing.Tuple[int, int, int], hide=True)
            
            Calls Block.face_state.update()
            :param position: the position to update at
            :param hide: not for usage; todo: remove


        function exposed(self, position: typing.Tuple[int, int, int])
            
            Checks if the given position is exposed so it should be shown
            :param position: the position to check


        function update_visible(self, hide=True, immediate=False)
            
            Updates the visible state of ALL blocks in the chunk
            todo: merge with show()
            :param hide: unused; todo: remove
            :param immediate: immediate execute tasks or scheduling for later?


        function hide_all(self, immediate=True)
            
            Hides all chunks in the chunk
            todo: merge with hide()
            :param immediate: immediate execute tasks or scheduling for later?


        function get_block(
                self, position: typing.Tuple[int, int, int], none_if_str=False
                ) -> typing.Union[typing.Any, str, None]:
            
            Getter function for a block
            :param position: the position
            :param none_if_str: if the block instance would be a str, replace it by None?
            :return: the block instance, a str representing a block (e.g. for scheduled during generation) or None
                if there is no block


        function as_shareable(self) -> "IChunk"
            
            Creates a reference to this chunk which can be linked across threads / processes
            :return: this chunk instance
            INFO: currently not in use


        function mark_dirty(self)

        function get_entities(self)

        function tick(self)

        function save(self)

        function set_value(self, key: str, data)

        function get_value(self, key: str)

        function __getitem__(self, item)

        function __setitem__(self, key, value)

        function __delitem__(self, key)

        function __contains__(self, item)

        function __iter__(self)

        function __eq__(self, other: "IChunk")

        function __hash__(self)

    class IDimension extends ABC

        function __init__(self)

            variable self.loaded

        function get_dimension_range(self) -> typing.Tuple[int, int]

        function get_id(self)

        function get_chunk(
                self,
                cx: typing.Union[int, typing.Tuple[int, int]],
                cz: int = None,
                generate: bool = True,
                create: bool = True,
                ) -> IChunk:

        function get_chunk_for_position(
                self,
                position: typing.Union[
                typing.Tuple[float, float, float],
                typing.Any,
                ],
                **kwargs
                ) -> typing.Optional[IChunk]:

        function get_block(
                self, position: typing.Tuple[int, int, int], none_if_str=False
                ) -> typing.Union[typing.Any, str, None]:

        function add_block(
                self,
                position: tuple,
                block_name: str,
                immediate=True,
                block_update=True,
                block_update_self=True,
                lazy_setup: typing.Callable = None,
                check_build_range=True,
                block_state=None,
                ):

        function remove_block(
                self, position: tuple, immediate=True, block_update=True, block_update_self=True
                ):

        function check_neighbors(self, position: typing.Tuple[int, int, int])

        function hide_block(self, position, immediate=True)

        function get_world_generation_config_for_layer(self, layer_name: str)

        function get_world_generation_config_entry(self, name: str, default=None)

        function set_world_generation_config_entry(self, name: str, value)

        function set_world_generation_config_for_layer(self, layer_name, layer_config)

        function get_name(self) -> str

        function unload_chunk(self, chunk: IChunk)

        function tick(self)

    class IWorld extends ABC

        function get_dimension_names(self) -> typing.Iterable[str]

        function add_player(
                self, name: str, add_inventories: bool = True, override: bool = True
                ):

        function get_active_player(self, create: bool = True) -> typing.Optional

        function reset_config(self)

        function get_active_dimension(self) -> typing.Union[IDimension, None]

        function add_dimension(self, dim_id: int, name: str, dim_config=None) -> IDimension

        function join_dimension(self, dim_id: int)

        function get_dimension(self, dim_id: int) -> IDimension

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
                raise NotImplementedError
                
                def show_chunk(self, chunk: typing.Union[typing.Tuple[int, int], IChunk]):

        function show_chunk(self, chunk: typing.Union[typing.Tuple[int, int], IChunk])

        function hide_chunk(self, chunk: typing.Union[typing.Tuple[int, int], IChunk])

        function change_chunks(
                self,
                before: typing.Union[typing.Tuple[int, int], None],
                after: typing.Union[typing.Tuple[int, int], None],
                generate_chunks=True,
                load_immediate=True,
                ):

        function cleanup(self, remove_dims=False, filename=None)

        function setup_by_filename(self, filename: str)