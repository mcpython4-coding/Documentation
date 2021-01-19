***AbstractInterface.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
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

        function __init__(self)

        function add_chunk_load_ticket(self, ticket_type: ChunkLoadTicketType, data=None)

        function check_for_unload(self)

        function get_dimension(self) -> "IDimension"

        function get_position(self) -> typing.Tuple[int, int]

        function get_maximum_y_coordinate_from_generation(self, x: int, z: int) -> int

        function exposed_faces(
                self, position: typing.Tuple[int, int, int]
                ) -> typing.Dict[mcpython.util.enums.EnumSide, bool]:

        function is_position_blocked(self, position: typing.Tuple[float, float, float]) -> bool

        function add_block(
                self,
                position: tuple,
                block_name: typing.Union[
                str, mcpython.common.block.AbstractBlock.AbstractBlock
                ],
                immediate=True,
                block_update=True,
                block_update_self=True,
                lazy_setup: typing.Callable[
                [mcpython.common.block.AbstractBlock.AbstractBlock], None
                ] = None,
                check_build_range=True,
                block_state=None,
                ) -> typing.Optional[mcpython.common.block.AbstractBlock.AbstractBlock]:
            
            Adds an block to the given position
            :param position: the position to add at
            :param block_name: the name of the block or an instance of it (mcpython.common.block.AbstractBlock.AbstractBlock)
            :param immediate: if the block should be shown if needed or not
            :param block_update: if an block-update should be send to neighbors blocks
            :param block_update_self: if the block should get an block-update
            :param lazy_setup: an callable for setting up the block instance
            :param check_build_range: if the build limits should be checked
            :param block_state: the block state to create in, or None if not set
            :return: the block instance or None if it could not be created


        function on_block_updated(
                self, position: typing.Tuple[float, float, float], itself=True
                ):

        function remove_block(
                self,
                position: typing.Union[
                typing.Tuple[int, int, int],
                mcpython.common.block.AbstractBlock.AbstractBlock,
                ],
                immediate: bool = True,
                block_update: bool = True,
                block_update_self: bool = True,
                reason=mcpython.common.block.AbstractBlock.BlockRemovalReason.UNKNOWN,
                ):

        function check_neighbors(self, position: typing.Tuple[int, int, int])

        function show_block(
                self,
                position: typing.Union[
                typing.Tuple[int, int, int],
                mcpython.common.block.AbstractBlock.AbstractBlock,
                ],
                immediate: bool = True,
                ):

        function hide_block(
                self,
                position: typing.Union[
                typing.Tuple[int, int, int],
                mcpython.common.block.AbstractBlock.AbstractBlock,
                ],
                immediate=True,
                ):

        function show(self, force=False)

        function hide(self, force=False)

        function update_visible_block(self, position: typing.Tuple[int, int, int], hide=True)

        function exposed(self, position: typing.Tuple[int, int, int])

        function update_visible(self, hide=True, immediate=False)

        function hide_all(self, immediate=True)

        function get_block(
                self, position: typing.Tuple[int, int, int]
                ) -> typing.Union[mcpython.common.block.AbstractBlock.AbstractBlock, str, None]:

        function as_shareable(self) -> "IChunk"

        function is_loaded(self) -> bool

        function is_generated(self) -> bool

        function set_value(self, key: str, data)

        function get_entities(self)

        function get_value(self, key: str)

        function is_visible(self) -> bool

        function mark_dirty(self)

        function tick(self)

        function save(self)

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
                mcpython.common.block.AbstractBlock.AbstractBlock,
                ],
                **kwargs
                ) -> typing.Optional[IChunk]:

        function get_block(
                self, position: typing.Tuple[int, int, int]
                ) -> typing.Union[mcpython.common.block.AbstractBlock.AbstractBlock, str, None]:

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
                raise NotImplementedError()
                
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