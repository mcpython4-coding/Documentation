***InventoryCraftingTable.py - documentation - last updated on 14.5.2020 by uuk***
___

    class InventoryCraftingTable extends gui.Inventory.Inventory
        
        inventory class for the crafting table
        

        static function get_config_file() -> str or None
        function __init__(self, *args, **kwargs)
        function create_slots(self) -> list
        function on_activate(self)
        function on_deactivate(self)
        function draw(self, hoveringslot=None)
            
            draws the inventory
            

        function get_interaction_slots(self)
        function on_key_press(self, symbol, modifiers)
        function update_shift_container(self)