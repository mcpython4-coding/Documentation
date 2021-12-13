***ContainerRenderer.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class AbstractContainerRenderer extends ABC
        
        Base class for a rendering adapter for an AbstractContainer
        Create only on CLIENT! We do not guarantee the existence of pyglet on servers in the future!


        function __init__(self)

            variable self.container

            variable self.bg_sprite: typing.Optional[pyglet.sprite.Sprite]

            variable self.bg_anchor

            variable self.window_anchor

            variable self.position

            variable self.bg_image_pos

            variable self.custom_name_label

            variable self.custom_name_label.anchor_y

            variable self.slot_rendering_information

        function create_slot_rendering_information(self)

        function get_position(self)

                variable x

                variable y

        function bind_container(self, container: AbstractContainer)
            
            Invoked when a new container should be bound to this renderer
            When multiple containers use the same renderer, this may get invoked more than one time


        function draw(self)

                variable self.bg_sprite.position

    class ContainerRenderer extends IBufferSerializeAble,  ABC
        
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

            variable self.slots: typing.List[ISlot]

                variable slot.assigned_inventory

            variable self.config
                todo: add special class holding this information with serializer for it

            variable self.custom_name - the custom name; If set, rendered in the inventory
                asyncio.get_event_loop().run_until_complete(self.reload_config())

            variable self.custom_name_label

            variable self.custom_name_label.anchor_y

            variable self.active

            variable self.custom_name

                variable self.custom_name

                variable self.custom_name_label.text

            variable size

        function on_mouse_button_press(
                self,
                relative_x: int,
                relative_y: int,
                button: int,
                modifiers: int,
                item_stack,
                slot,
                ) -> bool:
            
            Reload the config file


                    variable self.config

                    variable self.config

                variable self.config

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

        function is_mouse_in_range(self, x: int, y: int) -> bool
            
            Called when the inventory is shown

            
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
