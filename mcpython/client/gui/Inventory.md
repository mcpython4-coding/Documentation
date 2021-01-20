***Inventory.py - documentation - last updated on 20.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class Inventory extends ABC
        
        base inventory class
        todo: split up into the storage part and the rendering part
            [WIP, see common/container/AbstractContainer.py]


        static
        function get_config_file() -> typing.Optional[str]
            
            :return: the location of the inventory config file (if provided)


        function __init__(self)

            variable self.active

            variable self.bg_sprite: typing.Optional[pyglet.sprite.Sprite]

            variable self.bg_image_size

            variable self.bg_anchor

            variable self.window_anchor

            variable self.position

            variable self.bg_image_pos

            variable self.slots

            variable self.config

            variable self.uuid

            variable self.custom_name

            variable self.custom_name_label

            variable self.custom_name_label.anchor_y

            variable self.custom_name_label.color

        function reload_config(self)
            
            reload the config file


        function on_reload(self)

        function tick(self, dt: float)

        function create_slots(self) -> list
            
            creates the slots
            :return: the slots the inventory uses


        function get_position(self)
            
            :return: the position of the inventory
            todo: add cache


        function on_activate(self)
            
            Called when the inventory is shown


        function on_deactivate(self)
            
            Called when the inventory is hidden


        function is_closable_by_escape(self) -> bool

        function is_always_open(self) -> bool

        function get_draw_slots(self)

        function draw(self, hovering_slot=None)
            
            Draws the inventory
            Feel free to copy code into your own inventory and write your rendering around it!


                    variable self.custom_name_label.text

                variable self.custom_name_label.x

                variable self.custom_name_label.y

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
