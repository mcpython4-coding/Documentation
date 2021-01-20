***InventoryFurnace.py - documentation - last updated on 20.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class InventoryFurnace extends mcpython.client.gui.Inventory.Inventory
        
        Inventory class for the furnace


        variable TEXTURE_BG

        variable TEXTURE_BG_SIZE

        variable TEXTURE_ARROW

        variable TEXTURE_ARROW_SIZE

        variable TEXTURE_FIRE

        variable TEXTURE_FIRE_SIZE

        static
        function update_texture(cls)

            variable texture_bg

            variable size

            variable texture_bg

            variable cls.TEXTURE_BG

            variable cls.TEXTURE_BG_SIZE

            variable texture_arrow

            variable texture_arrow_size

            variable texture_arrow

            variable cls.TEXTURE_FIRE

            variable cls.TEXTURE_FIRE_SIZE

            variable texture_fire

            variable texture_fire_size

            variable texture_fire

            variable cls.TEXTURE_ARROW

            variable cls.TEXTURE_ARROW_SIZE

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

                variable self.custom_name

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
            
            Draws the inventory


        function get_interaction_slots(self)

        function on_key_press(self, symbol, modifiers)

        function on_tick(self, dt)

        function finish(self)

        function load(self, data: dict) -> bool

        function save(self)