***Chunk.py - documentation - last updated on 14.5.2020 by uuk***
___

    class Chunk

        variable now

        variable attributes

        static function add_default_attribute(name, reference, default, authcode=None) -> int

        function __init__(self, dimension, position)

            variable self.dimension

            variable self.position

            variable self.world

            variable self.is_ready - used when the chunks gets invalid or is loaded at the moment

            variable self.visible - used when the chunk should be visible

            variable self.loaded - used if load success

            variable self.generated - used if generation success

            variable self.attr - todo: rewrite!

                variable self.attr[attr]

            variable self.positions_updated_since_last_save

            variable self.entities

        function set_value(self, name, value)

            variable self.attr[name]

        function get_value(self, name)

        function draw(self)

        function exposed(self, position)
            


                variable pos

                variable chunk

                    variable block

        function exposed_faces(self, position)

            variable faces

            variable blockinst

                variable pos

                variable chunk

                    variable faces[face]

                    variable block

                    variable else: faces[face]

        function is_position_blocked(self, position)

        function add_block(self, position: tuple, block_name
            
            adds an block to the given position
            :param position: the position to add
            :param block_name: the name of the block or an instance of it
            :param immediate: if the block should be shown if needed
            :param block_update: if an block-update should be send to neighbors blocks
            :param blockupdateself: if the block should get an block-update
            :param args: the args to create the block with
            :param kwargs: the kwargs to create the block with
            :return: the block instance or None if it could not be created


                variable blockobj

                variable blockobj.position

                variable table

                variable blockobj

            variable self.world[position]

        function on_block_updated(self, position, itself=True)

                            variable b: Block.Block

        function remove_block(self, position, immediate=True, block_update=True, blockupdateself=True)
            
            Parameters
            :param position: tuple of len 3
                The (x, y, z) position of the block to remove.
            :param immediate: bool
                Whether or not to immediately remove block from canvas.
            :param block_update: bool
                Whether an block-update should be called or not
            :param blockupdateself:
                Whether the block to remove should get an block-update or not


                variable position

        function check_neighbors(self, position)
            
            state is current. This means hiding blocks that are not exposed and
            ensuring that all exposed blocks are shown. Usually used after a block
            is added or removed.


                variable key

                variable b

        function show_block(self, position, immediate=True)
            
            block has already been added with add_block()
            Parameters
            ----------
            position : tuple of len 3
                The (x, y, z) position of the block to show.
            immediate : bool
                Whether or not to show the block immediately.


                variable position

        function _show_block(self, position, block)
            
            Parameters
            ----------
            position : tuple of len 3
                The (x, y, z) position of the block to show.
            block: the blockinstance to show


        function hide_block(self, position, immediate=True)
            
            block from the world.
            Parameters
            ----------
            position : tuple of len 3
                The (x, y, z) position of the block to hide.
            immediate : bool
                Whether or not to immediately remove the block from the canvas.


                variable position

        function _hide_block(self, position)
            


        function show(self)

            variable self.visible

        function hide(self)

            variable self.visible

        function update_visable_block(self, position, hide=True)

        function update_visable(self, hide=True, immediate=False)

        function hide_all(self, immediate=True)

        function get_block(self, position)

            variable position

        function __del__(self)

        function __str__(self)