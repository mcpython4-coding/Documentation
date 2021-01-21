***InventoryHandler.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class OpenedInventoryStatePart extends mcpython.client.state.StatePart.StatePart
        
        class for inventories as state
        todo: make A LOT OF THINGS public and static
        todo: move inventory interaction handling to separated class


        function __init__(self)

            variable self.active

            variable self.slot_list

            variable self.moving_itemstack

            variable self.mode - possible: 0 - None, 1: equal on all slots, 2: on every slot one more, 3: fill up slots

            variable self.original_amount

            variable self.tool_tip_renderer

        function bind_to_eventbus(self)

        function on_key_press(self, symbol, modifiers)

        function on_draw_2d(self)

        function _get_slot_for(self, x, y) -> mcpython.client.gui.Slot.Slot
            
            get slot for position
            :param x: the x position
            :param y: the y position
            :return: the slot or None if none found
            todo: move to InventoryHandler


        function _get_slot_inventory_for(self, x, y)
            
            get slot for position
            :param x: the x position
            :param y: the y position
            :return: the slot and the inventory or None and None if none found
            todo: move to InventoryHandler


        function on_mouse_press(self, x, y, button, modifiers)

        function on_mouse_release(self, x, y, button, modifiers)

        function deactivate(self)

        function on_mouse_drag(self, x, y, dx, dy, button, modifiers)

        function reorder_slot_list_stacks(self)

        function on_mouse_scroll(self, x, y, dx, dy)

    variable inventory_part

    class InventoryHandler
        
        main class for registration of inventories
        Will handle every inventory created at any time. Will keep track of which inventories are open and to send the
            events to their event bus.
        Please do not mess around with the internal lists as they are representing the state of the inventory system.


        function __init__(self)

            variable self.opened_inventory_stack

            variable self.always_opened

            variable self.inventories

            variable self.moving_slot: mcpython.client.gui.Slot.Slot

        function tick(self, dt: float)

        function update_shift_container(self)

        function add(self, inventory)
            
            add an new inventory
            :param inventory: the inventory to add


        function reload_config(self)

        function show(self, inventory)
            
            show an inventory
            :param inventory: the inventory to show


        function hide(self, inventory)
            
            hide an inventory
            :param inventory: the inventory to hide


        function remove_one_from_stack(self)
            
            removes one inventory from stack
            :return: the inventory removed or None if no is active


        function close_all_inventories(self)
            
            close all inventories


    variable shared.inventory_handler