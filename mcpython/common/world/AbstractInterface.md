***AbstractInterface.py - documentation - last updated on 16.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
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

    class ISupportWorldInterface extends ABC
        
        Abstract intermediate common to chunk & dimension; Defines interaction with underlying world


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

        function check_neighbors(self, position: typing.Tuple[int, int, int])

        function update_visible_block(self, position: typing.Tuple[int, int, int])

        function exposed(self, position: typing.Tuple[int, int, int])

        function get_block(
                self, position: typing.Tuple[int, int, int], none_if_str=False
                ) -> typing.Union[typing.Any, str, None]:

    class IChunk extends ISupportWorldInterface,  ABC
        
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

            variable self.data_maps

        function clear(self)

        function get_map(self, name: str)

        function get_all_data_maps(self)

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
            
            Getter for the dimension of the chunk


        function get_position(self) -> typing.Tuple[int, int]
            
            Getter for the chunk position
            :return:


        function get_maximum_y_coordinate_from_generation(self, x: int, z: int) -> int
            
            Helper for finding the highest position in the chunk from generation
            todo: migrate to special system for world generation attributes


        function exposed_faces(
                self, position: typing.Tuple[int, int, int]
                ) -> typing.Dict[mcpython.util.enums.EnumSide, bool]:
            
            Helper for getting exposed faces of a block
            todo: add iterating variant


        function exposed_faces_iterator(
                self, position: typing.Tuple[int, int, int]
                ) -> typing.Iterator[mcpython.util.enums.EnumSide]:
            
            Variant of exposed_faces yielding the exposed faces instead of using a dict


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


        function update_all_rendering(self)

        function show(self)
            
            Shows the entire chunk


        function hide(self)
            
            Hides an entire chunk
            :param force: if to force-hide


        function update_visible_block(self, position: typing.Tuple[int, int, int])
            
            Calls Block.face_state.update()
            :param position: the position to update at


        function exposed(self, position: typing.Tuple[int, int, int])
            
            Checks if the given position is exposed so it should be shown
            :param position: the position to check


        function update_visible(self, immediate=False)
            
            Updates the visible state of ALL blocks in the chunk
            :param immediate: immediate execute tasks or scheduling for later?


        function hide_all(self, immediate=True)
            
            Hides all chunks in the chunk
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

        function __getitem__(self, item)

        function __setitem__(self, key, value)

        function __delitem__(self, key)

        function __contains__(self, item)

        function __iter__(self)

        function __eq__(self, other: "IChunk")

        function __hash__(self)

        function entity_iterator(self) -> typing.Iterable

        function dump_debug_maps(self, file_formatter: str)

    class IDimension extends ISupportWorldInterface,  ABC

        function __init__(self)

            variable self.loaded

        function get_world_height_range(self) -> typing.Tuple[int, int]

        function get_dimension_id(self)

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

        function entity_iterator(self) -> typing.Iterable

        function get_world(self) -> "IDimension"

        function dump_debug_maps_all_chunks(self, file_formatter: str)

        function chunk_iterator(self)

    class IWorld extends ABC

        function get_dimension_names(self) -> typing.Iterable[str]

        function add_player(
                self, name: str, add_inventories: bool = True, override: bool = True
                ):

        function get_active_player(self, create: bool = True) -> typing.Optional

        function get_player_by_name(self, name: str)

        function player_iterator(self) -> typing.Iterable

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

        function entity_iterator(self) -> typing.Iterable