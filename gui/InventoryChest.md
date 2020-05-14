***InventoryChest.py - documentation - last updated on 14.5.2020 by uuk***
___

    class InventoryChest extends gui.Inventory.Inventory
        
        inventory class for chest
        

        static function get_config_file() -> str or None
        function on_activate(self)
        function on_deactivate(self)
        function create_slots(self) -> list
        function draw(self, hoveringslot=None)
        function get_interaction_slots(self)
        function on_key_press(self, symbol, modifiers)
        function update_shift_container(self)