***InventoryBarrel.py - documentation - last updated on 14.5.2020 by uuk***
___

    class InventoryBarrel extends gui.Inventory.Inventory
        
        inventory class for chest


        function __init__(self, block)

            variable self.block

        static function get_config_file() -> str or None

        function on_activate(self)

            variable self.block.opened

        function on_deactivate(self)

            variable self.block.opened

        function create_slots(self) -> list

        function draw(self, hoveringslot=None)

                variable self.bgsprite.position

        function get_interaction_slots(self)

        function on_key_press(self, symbol, modifiers)

        function update_shift_container(self)

            variable G.inventoryhandler.shift_container.container_A

            variable G.inventoryhandler.shift_container.container_B