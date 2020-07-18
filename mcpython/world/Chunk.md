***Chunk.py - documentation - last updated on 18.7.2020 by uuk***
___

    class Chunk
        
        representation of an chunk in the world


        variable now - when is now?

        variable attributes - an dict representing the default attributes of an chunk; todo: replace by class-based system

        static
        function add_default_attribute(name: str, reference, default, authcode=None)
            
            will add an config entry into every new chunk instance
            :param name: the name of the attribute
            :param reference: the reference to use; unused internally
            :param default: the default value
            :param authcode: deprecated, will be removed
            WARNING: content must be saved separately


        function __init__(self, dimension, position: typing.Tuple[int, int])
            
            Will create an new chunk instance
            :param dimension: the world.Dimension.Dimension object used to store this chunk
            :param position: the position of the chunk
            WARNING: use Dimension.get_chunk() where possible


            variable self.dimension

            variable self.position

            variable self.world

            variable self.is_ready - used when the chunks gets invalid or is loaded at the moment

            variable self.visible - used when the chunk should be visible

            variable self.loaded - used if load success

            variable self.generated - used if generation success

            variable self.attr - todo: rewrite!

                variable v

                variable self.attr[attr]

        function get_maximum_y_coordinate_from_generation(self, x: int, z: int) -> int
            
            Helper function for getting the y height at the given xz generation based on the generation code
            :param x: the x coord
            :param z: the y corrd
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


        @deprecation.deprecated("dev3-1", "a1.3.0")
        function exposed(self, position): return any(self.exposed_faces(position).values())
                
                def exposed_faces(self, position: typing.Tuple[int, int, int]) -> typing.Dict[mcpython.util.enums.EnumSide, bool]:

        function exposed_faces(self, position: typing.Tuple[int, int, int]) -> typing.Dict[mcpython.util.enums.EnumSide, bool]
            
            returns an dict of the exposed status of every face of the given block
            :param position: the position to check
            :return: the dict for the status


        function is_position_blocked(self, position: typing.Tuple[float, float, float]) -> bool
            
            will return if at an given position is an block or an block is scheduled
            :param position: the position to check
            :return: if there is an block


        function add_block(self, position: tuple, block_name: str, immediate=True, block_update=True, blockupdateself=True,
                args=[], kwargs={}):
            
            adds an block to the given position
            :param position: the position to add
            :param block_name: the name of the block or an instance of it
            :param immediate: if the block should be shown if needed
            :param block_update: if an block-update should be send to neighbors blocks
            :param blockupdateself: if the block should get an block-update
            :param args: the args to create the block with
            :param kwargs: the kwargs to create the block with
            :return: the block instance or None if it could not be created


        function on_block_updated(self, position: typing.Tuple[float, float, float], itself=True)
            
            will call to the neighbor blocks an block update
            :param position: the position in the center
            :param itself: if the block itself should be updated


        function remove_block(self, position: typing.Union[typing.Tuple[int, int, int], Block.Block], immediate: bool = True,
                block_update: bool = True, blockupdateself: bool = True):
            
            Remove the block at the given `position`.
            :param position: The (x, y, z) position of the block to remove.
            :param immediate: Whether or not to immediately remove block from canvas.
            :param block_update: Whether an block-update should be called or not
            :param blockupdateself: Whether the block to remove should get an block-update or not


        function check_neighbors(self, position: typing.Tuple[int, int, int])
            
            Check all blocks surrounding `position` and ensure their visual
            state is current. This means hiding blocks that are not exposed and
            ensuring that all exposed blocks are shown. Usually used after a block
            is added or removed.
            :param position: the position as the center


        function show_block(self, position: typing.Union[typing.Tuple[int, int, int], Block.Block], immediate: bool = True)
            
            Show the block at the given `position`. This method assumes the
            block has already been added with add_block()
            :param position: The (x, y, z) position of the block to show.
            :param immediate: Whether or not to show the block immediately.


        function hide_block(self, position: typing.Union[typing.Tuple[int, int, int], Block.Block], immediate=True)
            
            Hide the block at the given `position`. Hiding does not remove the
            block from the world.
            :param position: The (x, y, z) position of the block to hide.
            :param immediate: Whether or not to immediately remove the block from the canvas.


                variable position

        function show(self, force=False)
            
            will show the chunk
            :param force: if the chunk show should be forced or not


        function hide(self, force=False)
            
            will hide the chunk
            :param force: if the chunk hide should be forced or not


        @deprecation.deprecated("dev1-4", "a1.4.0")
        function update_visable_block(self, position, hide=True)

        function update_visible_block(self, position: typing.Tuple[int, int, int], hide=True)

        @deprecation.deprecated("dev1-4", "a1.4.0")
        function update_visable(self, hide=True, immediate=False)

        function update_visible(self, hide=True, immediate=False)
            
            will update all visible of all blocks of the chunk
            :param hide: if blocks should be hidden if needed
            :param immediate: if immediate call or not


        function hide_all(self, immediate=True)
            
            will hide all blocks in the chunk
            :param immediate: if immediate or not


        function get_block(self, position: typing.Tuple[int, int, int]) -> typing.Union[Block.Block, str, None]
            
            will get the block at an given position
            :param position: the position to check for
            :return: None if no block, str if scheduled and Block.Block if created
            todo: split up into get_block_generated and get_block_un_generated


        function __del__(self)

        function __str__(self)