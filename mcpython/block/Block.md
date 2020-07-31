***Block.py - documentation - last updated on 31.7.2020 by uuk***
___

    class Block extends mcpython.event.Registry.IRegistryContent
        
        (Abstract) base class for all blocks
        Provides the normal interfaces for an block.
        All block classes should extend this.
        WARNING: These part should be STABLE. Please do NOT override these class


        variable TYPE: str - internal registry name

        variable BREAKABLE: bool
            If this block can be broken in gamemode 0 and 2

        variable HARDNESS: float - the hardness of the block

        variable BLAST_RESISTANCE: float - how good it is in resisting explosions

        variable MINIMUM_TOOL_LEVEL: float - the minimum tool level

        variable BEST_TOOLS_TO_BREAK: typing.List[mcpython.util.enums.ToolType] - the tools best to break

        variable ENABLE_RANDOM_TICKS - if the random tick function should be called if needed or not

        variable NO_COLLISION

        function __init__(self, position: tuple, set_to=None, real_hit=None, state=None, player=None)
            
            creates new Block-instance.
            sets up basic stuff and creates the attributes
            :param position: the position to create the block on
            :param set_to: when the block is set to an block, these parameter contains where
            :param real_hit: were the block the user set to was hit on
            Sub-classes may want to override the constructor and super().__init__(...) this


            variable self.position

            variable self.set_to

            variable self.real_hit

            variable self.face_state

            variable self.block_state

            variable self.face_solid

            variable self.uuid

            variable self.injected_redstone_power

        function __del__(self)
            
            Used for removing the circular dependency between Block and BlockFaceState for gc
            Internal use only


        function on_remove(self)
            
            Called when the block is removed
            Not cancelable. Block show data is removed, but the "current" state of the block is still stored.
            After this, the block might stay for some time in memory, but may also get deleted.


        function on_random_update(self)
            
            Called on random update
            Needs ENABLE_RANDOM_TICKS to be set to True for being invoked


        function on_block_update(self)
            
            Called when an near-by block-position is updated by setting/removing an block
            Invokes an redstone update by default. Call if needed.


        function on_redstone_update(self)
            
            Special event called in order to update redstone state. Not used by vanilla at the moment
            Is also invoked on "normal" block update


        function on_player_interaction(self, player, button: int, modifiers: int, hit_position: tuple)
            
            Called when the player pressed on mouse button on the block.
            :param player: the entity instance that interacts. WARNING: may not be an player instance
            :param button: the button pressed
            :param modifiers: the modifiers hold during press
            :param hit_position: where the block was hit at
            :return: if default logic should be interrupted or not


        function on_player_interact(self, player, itemstack, button, modifiers, exact_hit) -> bool

        function on_no_collide_collide(self, player, previous: bool)
            
            Called when NO_COLLIDE is True and the player is in the block every collision check
            :param player: the player entering the block
            :param previous: if the player was in the block before


        function save(self)

        function dump(self) -> bytes
            
            :return: bytes representing the whole block, not including inventories


        function load(self, data)
            
            loads block data
            :param data:  the data saved by save()
            WARNING: if not providing DataFixers for old mod versions, these data may get very old!


        function inject(self, data: bytes)
            
            loads block data
            :param data:  the data saved by save()
            WARNING: if not providing DataFixers for old mod versions, these data may get very old!


        function get_inventories(self)
            
            Called to get an list of inventories
            FOR MODDERS: use get_provided_slot_lists() where possible as it is the more "save" way to interact with the block


        function get_provided_slot_lists(self, side: mcpython.util.enums.EnumSide)
            
            Similar to get_inventories, but specifies only slots & the side on which the interaction can happen.
            Useful for e.g. furnaces which can get fuel from the side, but from top the item to smelt.
            gets slots for various reasons for an given side
            :param side: the side asked for
            :return: an tuple of lists of input slots and output slots
            Slots may be in inputs AND output.
            todo: make default return None, None


        function get_model_state(self) -> dict
            
            the active model state
            :return: the model state as an dict
            todo: allow string


        function set_model_state(self, state: dict)
            
            sets the model state for the block
            :param state: the state to set as an dict


        function get_view_bbox(self) -> typing.Union[mcpython.block.BoundingBox.BoundingBox, mcpython.block.BoundingBox.BoundingArea]
            
            used to get the bbox of the block for ray collision
            :return: the bbox instance


        function get_collision_bbox(self) -> typing.Union[mcpython.block.BoundingBox.BoundingBox, mcpython.block.BoundingBox.BoundingArea]
            
            used to get the bbox of the block for phyical body collision
            :return: the bbox instance


        function on_request_item_for_block(self, itemstack: mcpython.gui.ItemStack.ItemStack)
            
            used when an item is requested exactly for this block. Useful for setting custom data to the itemstack
            :param itemstack: the itemstack generated for the block


        function inject_redstone_power(self, side: mcpython.util.enums.EnumSide, level: int)
            
            used to inject an redstone value into the system
            :param side: the side from which the redstone value comes
            :param level: the level of redstone, between 0 and 15


        function get_redstone_output(self, side: mcpython.util.enums.EnumSide) -> int
            
            gets the redstone value on an given side
            :param side: the side to use
            :return: the value, as an integer between 0 and 15


        function get_redstone_source_power(self, side: mcpython.util.enums.EnumSide)
            
            gets source power of an given side
            :param side: the side to use
            :return: an value between 0 and 15 representing the redstone value

            
            gets the slots for an given side
            :param side: the side to check
            :return: an list of slot of the side
