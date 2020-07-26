***Inventory.py - documentation - last updated on 26.7.2020 by uuk***
___

    class Inventory
        
        base inventory class
        todo: split up into the storage part and the rendering part


        static
        function get_config_file() -> str
            
            :return: the location of the inventory config file (if provided)


        function __init__(self)

            variable self.active

            variable self.bgsprite: pyglet.sprite.Sprite

            variable self.bgimagesize

            variable self.bganchor

            variable self.windowanchor

            variable self.position

            variable self.bg_image_pos

            variable self.slots

            variable self.config

            variable self.uuid

        function reload_config(self)
            
            reload the config file
            todo: make public


        function on_reload(self)
            
            creates the slots
            :return: the slots the inventory uses


        @deprecation.deprecated("dev1-2", "a1.3.0")
        function _get_position(self)

        function get_position(self)
            
            :return: the position of the inventory


        function deactivate(self):  # todo: remove
                G.inventoryhandler.hide(self)
                
                def on_activate(self):

        function on_activate(self)
            
            called when the inventory is shown


        function on_deactivate(self)
            
            called when the inventory is hidden


        function is_closable_by_escape(self) -> bool: return True  # todo: make attribute
                
                def is_always_open(self) -> bool: return False  # todo: make attribute
                
                def draw(self, hoveringslot=None):

        function is_always_open(self) -> bool: return False  # todo: make attribute
                
                def draw(self, hoveringslot=None):

        function draw(self, hoveringslot=None)
            
            draws the inventory

            
            draw the background

            
            draw between background and slots

            
            draw between slots and counts

            
            draw over anything else


        function get_interaction_slots(self):  # todo: make attribute
                return self.slots
                
                def clear(self):

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


        function insert_items(self, items: list, random_check_order=False, insert_when_same_item=True)

        function insert_item(self, itemstack, random_check_order=False, insert_when_same_item=True)

        function update_shift_container(self)
            
            called when the inventory should update the content of the ShiftContainer of the inventory-handler


        function __del__(self)