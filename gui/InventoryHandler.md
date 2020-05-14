***InventoryHandler.py - documentation - last updated on 14.5.2020 by uuk***
___

    class OpenedInventoryStatePart extends state.StatePart.StatePart
        
        class for inventories as state
        todo: make A LOT OF THINGS public and static
        

        function __init__(self)
        function bind_to_eventbus(self)
        function on_key_press(self, symbol, modifiers)
        function on_draw_2d(self)
        function _get_slot_for(self, x, y) -> gui.Slot.Slot
            
            get slot for position
            :param x: the x position
            :param y: the y position
            :return: the slot or None if none found
            

        function on_mouse_press(self, x, y, button, modifiers)
        function on_mouse_release(self, x, y, button, modifiers)
        function deactivate(self)
        function on_mouse_drag(self, x, y, dx, dy, buttons, modifers)
        function reorder_slot_list_stacks(self)
        function on_mouse_scroll(self, x, y, dx, dy)

    variable inventory_part


    class InventoryHandler
        
        main class for registration of inventories
        Will handle every inventory created at any time. Will keep track of which inventories are open and to send the
            events to their event bus.
        Please do not mess around with the internal lists as they are representing the state of the inventory system.
        

        function __init__(self)
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
            


    variable G.inventoryhandler
