***InventoryFurnace.py - documentation - last updated on 26.7.2020 by uuk***
___

    class InventoryFurnace extends mcpython.gui.Inventory.Inventory
        
        inventory class for the furnace


        variable arrow

        variable fire

        static
        function reload(cls)

        function __init__(self, block, types)

            variable self.block

            variable self.fuel_left

            variable self.fuel_max

            variable self.xp_stored

            variable self.smelt_start

            variable self.old_item_name

            variable self.recipe

            variable self.progress

            variable self.types

        static
        function get_config_file() -> str or None

        function reset(self)

        function update_status(self)

        function create_slots(self) -> list

        static
        function is_fuel(cls, itemstack)

        static
        function on_shift(slot, x, y, button, mod, player)

        function on_input_update(self, player=False)

        function on_fuel_slot_update(self, player=False)

        function on_output_update(self, player=False)

        function on_activate(self)

        function on_deactivate(self)

        function draw(self, hovering_slot=None)
            
            draws the inventory


        function get_interaction_slots(self)

        function on_key_press(self, symbol, modifiers)

        function on_tick(self, dt)

        function finish(self)

        function load(self, data: dict) -> bool

        function save(self)