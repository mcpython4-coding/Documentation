***InventoryPlayerMain.py - documentation - last updated on 14.5.2020 by uuk***
___

    class InventoryPlayerMain extends gui.Inventory.Inventory
        
        inventory class for the main part of the inventory


        function __init__(self, hotbar)

            variable self.hotbar

            variable inputs

            variable self.recipeinterface

        static function get_config_file() -> str or None

        function create_slots(self) -> list

        function on_activate(self)

        function armor_update(self, player=None)

            variable points
                todo: add toughness
                todo: move to player

            variable G.world.get_active_player().armor_level

        function on_deactivate(self)

                variable itemstack

            variable G.statehandler.active_state.parts[0].activate_mouse

        function update_shift_container(self)

            variable G.inventoryhandler.shift_container.container_A

            variable G.inventoryhandler.shift_container.container_B