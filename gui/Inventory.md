***Inventory.py - documentation - last updated on 16.5.2020 by uuk***
___

    class Inventory
        
        base inventory class


        static function get_config_file() -> str
            
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


        function create_slots(self) -> list:  # todo
            
            creates the slots
            :return: the slots the inventory uses


        function _get_position(self)
            
            :return: the position of the inventory


        function activate(self):  # todo

        function deactivate(self):  # todo

        function on_activate(self)
            
            called when the inventory is shown


        function on_deactivate(self)
            
            called when the inventory is hidden


        function is_closable_by_escape(self) -> bool: return True  # todo

        function is_always_open(self) -> bool: return False  # todo

        function draw(self, hoveringslot=None)
            
            draws the inventory


        function on_draw_background(self):  # todo
            
            draw the background


        function on_draw_over_backgroundimage(self):  # todo
            
            draw between background and slots


        function on_draw_over_image(self):  # todo
            
            draw between slots and counts


        function on_draw_overlay(self):  # todo
            
            draw over anything else


        function is_blocking_interactions(self) -> bool:  # todo

        function on_world_cleared(self):  # todo

        function get_interaction_slots(self):  # todo

        function clear(self)

        function copy(self)

        function load(self, data) -> bool
            
            serializes the data into the inventory
            :param data: the data saved
            :return: if load is valid or not


        function save(self)
            
            serializes the inventory into an pickle-able data stream
            :return: the data


        function insert_items(self, items: list, random_check_order=False, insert_when_same_item=True)

        function insert_item(self, itemstack, random_check_order=False, insert_when_same_item=True)

        function update_shift_container(self)
            
            called when the inventory should update the content of the ShiftContainer of the inventory-handler


        function __del__(self)