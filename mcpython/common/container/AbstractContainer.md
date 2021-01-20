***AbstractContainer.py - documentation - last updated on 20.1.2021 by uuk***
___

    class AbstractContainer extends ABC
        
        Base class for containers
        Currently, unused
        Later planned to be part of the inventory system; the shared part [the inventory is client-only]
        Currently, the API is only a copy of Inventory parts for shared
        todo: do more here!


        static
        function create_renderer(cls)
            
            Called when loading a client to create the renderer; this is the only part which should interact
            with client-only code


        function __init__(self)

            variable self.slots

        function tick(self, dt: float)

        function is_closable_by_escape(self) -> bool

        function is_always_open(self) -> bool

        function is_blocking_interactions(self) -> bool

        function on_world_cleared(self)

        function get_interaction_slots(self)

        function clear(self)

        function copy(self)

        function load(self, data) -> bool
            
            serializes the data into the inventory
            :param data: the data saved
            :return: if load is valid or not


        function post_load(self, data)
            
            serializes stuff after the the slot data is loaded
            :param data: the data stored


        function save(self)
            
            serializes the inventory into an pickle-able data stream
            :return: the data


        function insert_items(
                self, items: list, random_check_order=False, insert_when_same_item=True
                ) -> list:

            variable skipped

                variable stack

        function insert_item(
                self, itemstack, random_check_order=False, insert_when_same_item=True
                ) -> bool:

            variable slots

                        variable overflow

                        variable slot.itemstack.amount

        function update_shift_container(self)
            
            called when the inventory should update the content of the ShiftContainer of the inventory-handler
