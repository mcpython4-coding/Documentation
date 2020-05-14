***InventoryHandler.py - documentation - last updated on 14.5.2020 by uuk***
___

    class OpenedInventoryStatePart extends state.StatePart.StatePart
        
        class for inventories as state
        todo: make A LOT OF THINGS public and static


        function __init__(self)

            variable self.active

            variable self.slot_list

            variable self.moving_itemstack

            variable self.mode - possible: 0 - None, 1: equal on all slots, 2: on every slot one more, 3: fill up slots

            variable self.original_amount

        function bind_to_eventbus(self)

        function on_key_press(self, symbol, modifiers)

            variable slot

        function on_draw_2d(self)

            variable hoveringslot

                variable G.statehandler.states["minecraft:game"].parts[0].activate_keyboard

                variable G.statehandler.states["minecraft:game"].parts[0].activate_keyboard

                variable G.inventoryhandler.moving_slot.position

        function _get_slot_for(self, x, y) -> gui.Slot.Slot
            
            get slot for position
            :param x: the x position
            :param y: the y position
            :return: the slot or None if none found


        function on_mouse_press(self, x, y, button, modifiers)

            variable slot: gui.Slot.Slot

            variable self.moving_itemstack

                    variable flag

                    variable self.mode

                    variable amount

                    variable self.mode

                    variable self.mode

        function on_mouse_release(self, x, y, button, modifiers)

                variable self.moving_itemstack

                variable self.mode

                variable self.moving_itemstack

                variable self.mode

                variable self.moving_itemstack

                variable self.mode

                variable self.moving_itemstack

                variable self.mode

        function deactivate(self)

        function on_mouse_drag(self, x, y, dx, dy, buttons, modifers)

            variable slot

        function reorder_slot_list_stacks(self)

                variable total

                variable per_element

                variable overhead

                    variable x

                variable overhead

        function on_mouse_scroll(self, x, y, dx, dy)

            variable slot

    variable inventory_part

    class InventoryHandler
        
        main class for registration of inventories
        Will handle every inventory created at any time. Will keep track of which inventories are open and to send the
            events to their event bus.
        Please do not mess around with the internal lists as they are representing the state of the inventory system.


        function __init__(self)

            variable self.opened_inventorystack

            variable self.alwaysopened

            variable self.inventorys

            variable self.moving_slot: gui.Slot.Slot

            variable self.shift_container

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


            variable stack

        function close_all_inventories(self)
            
            close all inventories


    variable G.inventoryhandler