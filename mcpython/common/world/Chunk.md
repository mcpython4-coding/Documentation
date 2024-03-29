***Chunk.py - documentation - last updated on 9.2.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @forced_attribute_type("dirty", lambda: bool) @forced_attribute_type("generated", lambda: bool) @forced_attribute_type("loaded", lambda: bool) @forced_attribute_type("visible", lambda: bool) @forced_attribute_type("is_ready", lambda: bool) @forced_attribute_type("position", lambda: tuple) class Chunk extends mcpython.engine.world.AbstractInterface.IChunk
        
        Default representation of a chunk in the world
        Defines the default behaviour


        variable BLOCK_REGISTRY

        variable now - when is now?

        @builtins_are_static()
        function __init__(
                self,
                dimension: mcpython.engine.world.AbstractInterface.IDimension,
                position: typing.Tuple[int, int],
                ):
            
            Will create a new chunk instance
            :param dimension: the world.Dimension.Dimension object used to store this chunk
            :param position: the position of the chunk
            WARNING: use Dimension.get_chunk() where possible [saver variant, will do some work in the background]


            variable self.dimension

            variable self.position
                The position of the chunk

            variable self.is_ready
                Used when the chunks gets invalid or is loaded at the moment

            variable self.visible
                Indicated that the chunk is shown to the player
                todo: client-only

            variable self.loaded
                Indicated that the chunk is loaded

            variable self.generated
                Indicates that the chunk is generated

            variable self.dirty
                Indicated that the chunk was modified

        @builtins_are_static()
        function entity_iterator(self) -> typing.Iterable

        function tick(self)
            
            General chunk tick
            todo: move random ticks & entity ticks here


        function save(self)

        @returns_argument()
        function mark_dirty(self)

        @constant_operation()
        function get_dimension(self) -> mcpython.engine.world.AbstractInterface.IDimension

        @constant_operation()
        function get_position(self) -> typing.Tuple[int, int]

        function get_maximum_y_coordinate_from_generation(
                self, x: int, z: int, default=None
                ) -> int:
            
            Helper function for getting the y height at the given xz generation based on the generation code, by looking
                up the internal map
            :param x: the x coord
            :param z: the y coord
            :param default: the default value when no value is set
            :return: the y value at that position, maybe negative


            variable height_map

        @name_is_static("shared", lambda: shared)
        @builtins_are_static()
        function draw(self)
            
            Will draw the chunk with the content for it
            Draws all entities
            todo: for this, add a batch
            Will schedule a chunk load from saves when needed


        variable ALL_FACES_EXPOSED

        @name_is_static("position_to_chunk", lambda: position_to_chunk)
        @name_is_static("EnumSide", lambda: EnumSide)
        @builtins_are_static()
        @deprecation.deprecated()
        function exposed_faces(
                self, position: typing.Tuple[int, int, int]
                ) -> typing.Dict[str, bool]:
            
            Returns a dict of the exposed status of every face of the given block
            :param position: the position to check
            :return: the dict for the status


            variable instance

            variable faces

                variable pos

                variable chunk_position

                    variable chunk

                    variable chunk

                    variable faces[face.normal_name]

                    variable block

                    variable faces[face.normal_name]

        @name_is_static("position_to_chunk", lambda: position_to_chunk)
        @name_is_static("EnumSide", lambda: EnumSide)
        @builtins_are_static()
        @deprecation.deprecated()
        function exposed_faces_list(
                self, position: typing.Tuple[int, int, int]
                ) -> typing.List[bool]:

            variable instance

            variable faces

                variable pos

                variable chunk_position

                    variable chunk

                    variable chunk

                    variable faces[face.index]

                    variable block

                    variable faces[face.index]

        @name_is_static("position_to_chunk", lambda: position_to_chunk)
        @name_is_static("EnumSide", lambda: EnumSide)
        @builtins_are_static()
        function exposed_faces_flag(self, block: str | Block.AbstractBlock | None) -> int

            variable faces

                variable pos

                variable chunk_position

                    variable chunk

                    variable chunk

                    variable new_block

        @name_is_static("EnumSide", lambda: EnumSide)
        @builtins_are_static()
        function exposed_faces_iterator(
                self, position: typing.Tuple[int, int, int]
                ) -> typing.Iterator[EnumSide]:

            variable instance

                variable pos

                variable chunk_position

                    variable chunk

                    variable chunk

                    variable block

        function is_position_blocked(self, position: typing.Tuple[float, float, float]) -> bool
            
            Will return if at a given position is a block or a block is scheduled [e.g. by world generation]
            :param position: the position to check
            :return: if there is an block


        @deprecation.deprecated()
        function add_block_unsafe(self, *args, **kwargs)
            
            Adds a block (given by name or a block instance) to the given position in this chunk
            :param position: the position to add
            :param block_name: the name of the block or an instance of it
            :param immediate: if the block should be shown if needed
            :param block_update: if an block-update should be sent to neighbor blocks
            :param block_update_self: if the block should get an block-update
            :param lazy_setup: a callable for setting up the block instance
            :param check_build_range: if the build limits should be checked
            :param block_state: the block state to create in, or None if not set
            :param replace_existing: if existing blocks should be replaced
            :param network_sync: do network sync or not
            :return: the block instance or None if it could not be created


            variable r
                check if it is in build range

                variable block

                variable block.position

                variable block.dimension

                    variable result

                variable block_cls

                variable block

                variable block.position

                variable block.dimension

                    variable result

            variable self._world[position]
                store the block instance in the local world
            
            Will call to the neighbor blocks a block update
            :param position: the position in the center
            :param include_itself: if the block itself (the block at 'position') should be updated


            variable to_invoke

                variable b: Block.AbstractBlock

                variable b

            variable immediate: bool

            variable block_update: bool

            variable block_update_self: bool
            
            Remove the block at the given position. When no block is there, nothing happens
            :param position: The (x, y, z) position of the block to remove, or the block instance
            :param immediate: Whether or not to immediately remove block from canvas.
            :param block_update: Whether an block-update should be called or not
            :param block_update_self: Whether the block to remove should get an block-update or not
            :param reason: the reason why the block was removed
            :param network_sync: if to send an update over the network or not
            todo: remove from scheduled world generation if needed


                variable position

        @name_is_static("shared", lambda: shared)
        @name_is_static("EnmSide", lambda: EnumSide)
        @builtins_are_static()
        function check_neighbors(self, position: typing.Tuple[int, int, int])
            
            Check all blocks surrounding `position` and ensure their visual
            state is current. This means hiding blocks that are not exposed and
            ensuring that all exposed blocks are shown. Usually used after a block
            is added or removed.
            :param position: the position as the center


                variable block

        @name_is_static("shared", lambda: shared)
        @name_is_static("Block", lambda: Block)
        @builtins_are_static()
        function show_block(
                self,
                position: typing.Union[typing.Tuple[int, int, int], Block.AbstractBlock],
                immediate: bool = True,
                ):
            
            Show the block at the given `position`. This method assumes the
            block has already been added with add_block()
            :param position: The (x, y, z) position of the block to show.
            :param immediate: Whether to show the block immediately or not


                variable position

        @name_is_static("shared", lambda: shared)
        @name_is_static("Block", lambda: Block)
        @builtins_are_static()
        function hide_block(
                self,
                position: typing.Union[typing.Tuple[int, int, int], Block.AbstractBlock],
                immediate=True,
                ):
            
            Hide the block at the given `position`. Hiding does not remove the
            block from the world.
            :param position: The (x, y, z) position of the block to hide.
            :param immediate: Whether to immediately remove the block from the canvas or not.


                variable position

        @name_is_static("shared", lambda: shared)
        function show(self, force=False)
            
            Will show the chunk
            :param force: if the chunk show should be forced or not


            variable self.visible

        @name_is_static("shared", lambda: shared)
        function hide(self, force=False)
            
            will hide the chunk
            :param force: if the chunk hide should be forced or not


            variable self.visible

        @name_is_static("shared", lambda: shared)
        function is_visible(self) -> bool

        @name_is_static("shared", lambda: shared)
        function update_visible_block(self, position: typing.Tuple[int, int, int], hide=True)

        @builtins_are_static()
        function exposed(self, position: typing.Tuple[int, int, int]) -> bool

        @name_is_static("shared", lambda: shared)
        @object_method_is_protected("keys", lambda: dict.keys)
        function update_visible(self, hide=True, immediate=False)
            
            Will update all visible of all blocks of the chunk
            :param hide: if blocks should be hidden if needed
            :param immediate: if immediate call or not


        @name_is_static("shared", lambda: shared)
        function hide_all(self, immediate=True)
            
            Will hide all blocks in the chunk
            :param immediate: if immediate or not


        function get_block(
                self, position: typing.Tuple[int, int, int], none_if_str=True
                ) -> typing.Union[Block.AbstractBlock, str, None]:
            
            Will get the block at an given position
            :param position: the position to check for, must be normalized
            :param none_if_str: if none if the block instance is str, defaults to True
            :return: None if no block, str if scheduled and Block.Block if created
            todo: split up into get_block[_generated] and get_block_un_generated


        function __str__(self)

        function is_loaded(self) -> bool

        function is_generated(self) -> bool

        function get_entities(self)

        @object_method_is_protected("values", lambda: dict.values)
        @object_method_is_protected("format", lambda: str.format)
        function dump_debug_maps(self, file_formatter: str)

        function spawn_itemstack_in_world(
                self,
                itemstack: ItemStack,
                position: typing.Tuple[float, float, float],
                pickup_delay=0,
                ):

            variable entity