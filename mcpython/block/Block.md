***Block.py - documentation - last updated on 24.6.2020 by uuk***
___

    class Block extends mcpython.event.Registry.IRegistryContent
        
        base class for all blocks


        variable TYPE: str

        variable BREAKABLE: bool - If this block can be broken in gamemode 0 and 2

        variable HARDNESS: float - the hardness of the block

        variable BLAST_RESISTANCE: float - how good it is in resisting explosions

        variable MINIMUM_TOOL_LEVEL: float - the minimum tool level

        variable BEST_TOOLS_TO_BREAK: typing.List[mcpython.util.enums.ToolType] - the tools best to break

        variable ENABLE_RANDOM_TICKS

        function __init__(self, position: tuple, set_to=None, real_hit=None, state=None, player=None)
            
            creates new Block
            :param position: the position to create the block on
            :param set_to: when the block is set to an block, these parameter contains where
            :param real_hit: were the block the user set to was hit on


            variable self.position

            variable self.set_to

            variable self.real_hit

            variable self.face_state

            variable self.block_state

            variable self.face_solid

            variable self.uuid

            variable self.injected_redstone_power

        function __del__(self)
            
            used for removing the circular dependency between Block and BlockFaceState for gc


        function on_remove(self)
            
            called when the block is removed


        function on_random_update(self)
            
            called on random update


        function on_block_update(self)
            
            called when an near-by block-position is updated by setting/removing an block


        function on_redstone_update(self)
            
            special event called in order to update redstone state. Not used by vanilla at the moment


        function on_player_interact(self, player, itemstack, button, modifiers, exact_hit) -> bool
            
            Called when the player pressed on mouse button on the block.
            :param player: the entity instance that interacts. WARNING: may not be an player instance
            :param itemstack: the itemstack hold in hand, todo: remove as it is published by player
            :param button: the button pressed
            :param modifiers: the modifiers hold during press
            :param exact_hit: where the block was hit at
            :return: if default logic should be interrupted or not


        function save(self)
            
            :return: an pickle-able object representing the whole block, not including inventories


        function load(self, data)
            
            loads block data
            :param data:  the data saved by save()


        function get_inventories(self)
            
            Called to get an list of inventories
            FOR MODDERS: use get_provided_slot_lists() where possible


        function get_provided_slot_lists(self, side: mcpython.util.enums.EnumSide)
            
            Similar to get_inventories, but specifies only slots & the side on which the interaction can happen.
            Useful for e.g. furnaces which can get fuel from the side, but from top the item to smelt.
            gets slots for various reasons for an given side
            :param side: the side asked for
            :return: an tuple of lists of input slots and output slots


        function get_model_state(self) -> dict
            
            the active model state
            :return: the model state


        function set_model_state(self, state: dict)
            
            sets the model state for the block
            :param state: the state to set

            
            used to get the bbox of the block
            :return: the bbox


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
