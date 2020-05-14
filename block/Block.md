***Block.py - documentation - last updated on 14.5.2020 by uuk***
___

    class Block extends event.Registry.IRegistryContent
        
        base class for all blocks
        


        variable CUSTOM_WALING_SPEED_MULTIPLIER - used when the player walks in an different speed on this block


        variable TYPE


        variable BLOCK_ITEM_GENERATOR_STATE - used internally to set the state the BlockItemGenerator uses


        variable BREAKABLE - If this block can be broken in gamemode 0 and 2


        variable HARDNESS


        variable MINIMUM_TOOL_LEVEL


        variable BEST_TOOLS_TO_BREAK


        variable SOLID - if the block is solid; None is unset and set by system by checking face_solid on an block instance


        variable CONDUCTS_REDSTONE_POWER - if the block can conduct redstone power; None is unset and set by system to SOLID


        variable CAN_MOBS_SPAWN_ON - if mobs can spawn on the block; None is unset and set by system to SOLID

        function __init__(self, position: tuple, set_to=None, real_hit=None, state=None)
            
            creates new Block
            :param position: the position to create the block on
            :param set_to: when the block is set to an block, these parameter contains where
            :param real_hit: were the block the user set to was hit on
            

        function __del__(self)
        function on_remove(self)
            
            called when the block is removed
            

        function on_random_update(self)
            
            called on random update
            

        function on_block_update(self)
            
            called when an near-by block-position is updated by setting/removing an block
            

        function on_redstone_update(self)
            
            special event called in order to update redstone state. Not used by vanilla at the moment
            

        function on_player_interact(self, player, itemstack, button, modifiers, exact_hit) -> bool
            
            called when the player pressed an mouse button on the block
            :param player: the entity instance that interacts. WARNING: may not be an player instance
            :param itemstack: the itemstack hold in hand, todo: remove
            :param button: the button pressed
            :param modifiers: the modifiers hold during press
            :param exact_hit: where the block was hit at
            :return: if default logic should be interrupted
            

        function save(self)
            
            :return: an pickle-able object representing the whole block, not including inventories
            

        function load(self, data)
            
            loads block data
            :param data:  the data saved by save()
            

        function get_inventories(self)
            
            called to get an list of inventories
            

        function get_model_state(self) -> dict
        function set_model_state(self, state: dict)
        function get_provided_slots(self, side)
        function get_view_bbox(self)
        function on_request_item_for_block(self, itemstack)
        function inject_redstone_power(self, side, level: int)
        function get_redstone_output(self, side)
        function get_redstone_source_power(self, side)
        static function modify_block_item(cls, itemconstructor): pass  # todo
        static function get_all_model_states() -> list: return [{}]  # todo