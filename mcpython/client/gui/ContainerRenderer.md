***ContainerRenderer.py - documentation - last updated on 27.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class ContainerRenderer extends ABC
        
        Base class for rendering a container at the client
        Client-only code


        static
        function get_config_file() -> typing.Optional[str]
            
            :return: the location of the inventory config file (if provided)


        function __init__(self, container=None)

            variable self.container

            variable self.active

            variable self.bg_sprite: typing.Optional[pyglet.sprite.Sprite]

            variable self.bg_image_size

            variable self.bg_anchor

            variable self.window_anchor

            variable self.position

            variable self.bg_image_pos

            variable self.uuid

            variable self.slots

            variable self.config

        function reload_config(self)
            
            Reload the config file


                variable slot_id

                variable entry

                    variable self.slots[slot_id].position

                    variable self.slots[slot_id].interaction_mode[1]

                    variable self.slots[slot_id].interaction_mode[0]

                    variable self.slots[slot_id].interaction_mode[2]

                        variable image

                        variable image

                        variable self.slots[slot_id].empty_image

                    variable self.slots[slot_id].allowed_item_tags

                variable self.bg_image_size

                variable self.bg_anchor

                variable self.window_anchor

                variable self.position

                        variable self.bg_sprite

                        variable self.bg_sprite

                variable self.bg_image_pos

        function on_reload(self)

        function tick(self, dt: float)

        function create_slot_renderers(self) -> list
            
            Creates the slots
            :return: the slots the inventory uses


        function get_position(self)
            
            :return: the position of the inventory
            todo: add cache
            todo: recalculate on resize than


                variable x

                variable y

        function on_activate(self)
            
            Called when the inventory is shown


        function on_deactivate(self)
            
            Called when the inventory is hidden


        function is_closable_by_escape(self) -> bool

        function is_always_open(self) -> bool

        function is_blocking_interactions(self) -> bool

        function get_draw_slots(self)
            
            Helper function for getting the slots to draw on screen


        function draw(self, hovering_slot=None)
            
            Draws the inventory
            Feel free to copy code into your own inventory and write your rendering around it


                    variable self.custom_name_label.text

                variable self.custom_name_label.x

                variable self.custom_name_label.y

        function on_world_cleared(self)

        function get_interaction_slots(self)

        function clear(self)

        function copy(self)

        function load(self, data) -> bool
            
            Deserializes the data into the inventory
            :param data: the data saved
            :return: if load is valid or not


        function post_load(self, data)
            
            Deserializes stuff after the the slot data is loaded
            :param data: the data stored


        function save(self)
            
            Serializes the inventory into an pickle-able data stream
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