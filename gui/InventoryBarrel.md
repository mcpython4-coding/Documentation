***InventoryBarrel.py - documentation - last updated on 30.5.2020 by uuk***
___

    class InventoryBarrel extends gui.Inventory.Inventory
        
        inventory class for chest


        function __init__(self, block)

            variable self.block

        static
        function get_config_file() -> str or None

        function on_activate(self)

        function on_deactivate(self)

        function create_slots(self) -> list

        function draw(self, hoveringslot=None)

        function get_interaction_slots(self)

        function on_key_press(self, symbol, modifiers)

        function update_shift_container(self)