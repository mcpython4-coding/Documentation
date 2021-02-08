***Chunk.py - documentation - last updated on 8.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class Chunk extends mcpython.common.world.AbstractInterface.IChunk
        
        representation of an chunk in the world


        variable now - when is now?

        variable attributes - an dict representing the default attributes of an chunk

        static
        function add_default_attribute(name: str, reference: typing.Any, default: typing.Any)
            
            will add an config entry into every new chunk instance
            :param name: the name of the attribute
            :param reference: the reference to use; unused internally
            :param default: the default value
            WARNING: content must be saved by owner, not auto-saved
            todo: make class based


        function __init__(
                self,
                dimension: mcpython.common.world.AbstractInterface.IDimension,
                position: typing.Tuple[int, int],
                ):
            
            Will create a new chunk instance
            :param dimension: the world.Dimension.Dimension object used to store this chunk
            :param position: the position of the chunk
            WARNING: use Dimension.get_chunk() where possible [saver variant, will do some work in the background]


            variable self.dimension

            variable self.position

            variable self.is_ready
                used when the chunks gets invalid or is loaded at the moment

            variable self.visible
                used when the chunk should be visible

            variable self.loaded
                used if load success

            variable self.generated
                used if generation success

            variable self.dirty
                if the chunk was modified since last save

                variable v

                    variable v

                variable self.attr[attr]

        function tick(self)

        function save(self)

        function as_shareable(self) -> mcpython.common.world.AbstractInterface.IChunk

        function mark_dirty(self)

        function get_dimension(self)

        function get_position(self)

        function get_maximum_y_coordinate_from_generation(self, x: int, z: int) -> int
            
            Helper function for getting the y height at the given xz generation based on the generation code
            :param x: the x coord
            :param z: the y coord
            :return: the y value at that position


        function set_value(self, name: str, value)
            
            Will set an attribute of the chunk
            :param name: the name to use
            :param value: the value to use


        function get_value(self, name: str)
            
            Will get the value of the given name
            :param name: the name to get
            :return: the data stored


        function draw(self)
            
            Will draw the chunk with the content for it


        variable ALL_FACES_EXPOSED

        function exposed_faces(
                self, position: typing.Tuple[int, int, int]
                ) -> typing.Dict[str, bool]:
            
            Returns an dict of the exposed status of every face of the given block
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

        function is_position_blocked(self, position: typing.Tuple[float, float, float]) -> bool
            
            will return if at an given position is an block or an block is scheduled
            :param position: the position to check
            :return: if there is an block


        function add_block(
                self,
                position: tuple,
                block_name: typing.Union[str, Block.AbstractBlock],
                immediate=True,
                block_update=True,
                block_update_self=True,
                lazy_setup: typing.Callable[[Block.AbstractBlock], None] = None,
                check_build_range=True,
                block_state=None,
                ):
            
            Adds an block to the given position
            :param position: the position to add
            :param block_name: the name of the block or an instance of it
            :param immediate: if the block should be shown if needed
            :param block_update: if an block-update should be send to neighbors blocks
            :param block_update_self: if the block should get an block-update
            :param lazy_setup: an callable for setting up the block instance
            :param check_build_range: if the build limits should be checked
            :param block_state: the block state to create in, or None if not set
            :return: the block instance or None if it could not be created


            variable r
                check if it is in build range

                variable block

                variable block.position

                variable block.dimension

                variable table

                variable block

                variable block.position

                variable block.dimension

            variable self._world[position]

        function on_block_updated(
                self, position: typing.Tuple[int, int, int], include_itself=True
                ):
            
            will call to the neighbor blocks an block update
            :param position: the position in the center
            :param include_itself: if the block itself should be updated


                            variable b: Block.AbstractBlock

        function remove_block(
                self,
                position: typing.Union[typing.Tuple[int, int, int], Block.AbstractBlock],
                immediate: bool = True,
                block_update: bool = True,
                block_update_self: bool = True,
                reason=Block.BlockRemovalReason.UNKNOWN,
                ):
            
            Remove the block at the given `position`.
            :param position: The (x, y, z) position of the block to remove.
            :param immediate: Whether or not to immediately remove block from canvas.
            :param block_update: Whether an block-update should be called or not
            :param block_update_self: Whether the block to remove should get an block-update or not
            :param reason: the reason why the block was removed


                variable position

        function check_neighbors(self, position: typing.Tuple[int, int, int])
            
            Check all blocks surrounding `position` and ensure their visual
            state is current. This means hiding blocks that are not exposed and
            ensuring that all exposed blocks are shown. Usually used after a block
            is added or removed.
            :param position: the position as the center


        function show_block(
                self,
                position: typing.Union[typing.Tuple[int, int, int], Block.AbstractBlock],
                immediate: bool = True,
                ):
            
            Show the block at the given `position`. This method assumes the
            block has already been added with add_block()
            :param position: The (x, y, z) position of the block to show.
            :param immediate: Whether or not to show the block immediately.


                variable position

        function hide_block(
                self,
                position: typing.Union[typing.Tuple[int, int, int], Block.AbstractBlock],
                immediate=True,
                ):
            
            Hide the block at the given `position`. Hiding does not remove the
            block from the world.
            :param position: The (x, y, z) position of the block to hide.
            :param immediate: Whether or not to immediately remove the block from the canvas.


                variable position

        function show(self, force=False)
            
            will show the chunk
            :param force: if the chunk show should be forced or not


            variable self.visible

        function hide(self, force=False)
            
            will hide the chunk
            :param force: if the chunk hide should be forced or not


            variable self.visible

        function is_visible(self) -> bool

        function update_visible_block(self, position: typing.Tuple[int, int, int], hide=True)

        function exposed(self, position: typing.Tuple[int, int, int]) -> bool

        function update_visible(self, hide=True, immediate=False)
            
            will update all visible of all blocks of the chunk
            :param hide: if blocks should be hidden if needed
            :param immediate: if immediate call or not


        function hide_all(self, immediate=True)
            
            will hide all blocks in the chunk
            :param immediate: if immediate or not


        function get_block(
                self, position: typing.Tuple[int, int, int]
                ) -> typing.Union[Block.AbstractBlock, str, None]:
            
            will get the block at an given position
            :param position: the position to check for, must be normalized
            :return: None if no block, str if scheduled and Block.Block if created
            todo: split up into get_block_generated and get_block_un_generated


        function __str__(self)

        function is_loaded(self) -> bool

        function is_generated(self) -> bool

        function get_entities(self)