***InventoryPlayerMain.py - documentation - last updated on 12.6.2020 by uuk***
___

    class InventoryPlayerMain extends mcpython.gui.Inventory.Inventory
        
        inventory class for the main part of the inventory


        function __init__(self, hotbar)

            variable self.hotbar

            variable inputs

            variable self.recipeinterface

        static
        function get_config_file() -> str or None

        function create_slots(self) -> list

        function armor_update(self, player=None)

        function remove_items_from_crafting(self)

        function on_deactivate(self)

        function update_shift_container(self)