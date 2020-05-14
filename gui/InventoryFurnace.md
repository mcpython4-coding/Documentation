***InventoryFurnace.py - documentation - last updated on 14.5.2020 by uuk***
___

    variable arrow


    variable fire


    class InventoryFurnace extends gui.Inventory.Inventory
        
        inventory class for the furnace
        

        function __init__(self, block, types)
        static function get_config_file() -> str or None
        function reset(self)
        function update_status(self)
        function create_slots(self) -> list
        static function is_fuel(cls, itemstack)
        static function on_shift(slot, x, y, button, mod, player)
        function on_input_update(self, player=False)
        function on_fuel_slot_update(self, player=False)
        function on_output_update(self, player=False)
        function on_activate(self)
        function on_deactivate(self)
        function draw(self, hoveringslot=None)
            
            draws the inventory
            

        function get_interaction_slots(self)
        function on_key_press(self, symbol, modifiers)
        function on_tick(self, dt)
        function finish(self)
        function load(self, data: dict) -> bool
        function save(self)