***BlockChest.py - documentation - last updated on 3.7.2020 by uuk***
___

    variable BBOX - the bounding box of the chest

    @G.registry class BlockChest extends Block.Block
        
        The Chest block class


        variable now: datetime - now

        variable is_christmas: bool - if christmas is today

        variable NAME: str - the name of the chest

        variable HARDNESS

        variable BLAST_RESISTANCE

        variable BEST_TOOLS_TO_BREAK

        function __init__(self, *args, **kwargs)
            
            creates an new BlockChest


            variable self.front_side

                    variable self.front_side

        function can_open_inventory(self) -> bool
            
            checks if the inventory can be opened
            :return: if the block can be opened


        function on_player_interact(self, player, itemstack, button, modifiers, exact_hit) -> bool

        function get_inventories(self)

        function get_provided_slot_lists(self, side): return self.inventory.slots, self.inventory.slots
                
                def set_model_state(self, state: dict):

        function set_model_state(self, state: dict)

        function get_model_state(self) -> dict

        static
        function get_all_model_states() -> list

        function get_view_bbox(self): return BBOX
                
                @classmethod
                def set_block_data(cls, iteminst, block):

        static
        function set_block_data(cls, iteminst, block)

        function on_request_item_for_block(self, itemstack)

        function on_remove(self)

        static
        function modify_block_item(cls, itemfactory)

        function save(self)

        function load(self, data)