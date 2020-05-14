***InventoryFurnace.py - documentation - last updated on 14.5.2020 by uuk***
___

    variable arrow

    variable fire

    class InventoryFurnace extends gui.Inventory.Inventory
        
        inventory class for the furnace


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

        static function get_config_file() -> str or None

        function reset(self)

            variable self.block.active

            variable self.smelt_start

            variable self.recipe

            variable self.old_item_name

        function update_status(self)

                        variable fuel

                        variable self.fuel_max

                variable self.old_item_name

                variable self.smelt_start

                        variable recipe

                variable self.recipe: crafting.FurnaceCrafting.FurnesRecipe

                variable self.block.active

        function create_slots(self) -> list

            variable slots
                36 slots of main, 1 input, 1 fuel and 1 output

        static function is_fuel(cls, itemstack)

        static function on_shift(slot, x, y, button, mod, player)

            variable slot_copy

        function on_input_update(self, player=False)

        function on_fuel_slot_update(self, player=False)

        function on_output_update(self, player=False)

        function on_activate(self)

        function on_deactivate(self)

        function draw(self, hoveringslot=None)
            
            draws the inventory


                variable self.bgsprite.position

        function get_interaction_slots(self)

        function on_key_press(self, symbol, modifiers)

        function on_tick(self, dt)

                variable self.fuel_left

                variable elapsed_time

                variable self.progress

        function finish(self)

            variable self.smelt_start

        function load(self, data: dict) -> bool

            variable self.fuel_left

            variable self.fuel_max

            variable self.xp_stored

            variable self.progress

        function save(self)