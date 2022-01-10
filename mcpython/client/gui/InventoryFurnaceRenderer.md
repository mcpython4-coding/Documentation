***InventoryFurnaceRenderer.py - documentation - last updated on 28.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class InventoryFurnaceRenderer extends mcpython.client.gui.ContainerRenderer.ContainerRenderer
        
        Inventory renderer class for the furnace
        todo: move a LOT of stuff to the container


        variable TEXTURE_BG
            The texture properties, provided when reloading

        variable TEXTURE_BG_SIZE

        variable TEXTURE_ARROW

        variable TEXTURE_ARROW_SIZE

        variable TEXTURE_FIRE

        variable TEXTURE_FIRE_SIZE

            variable texture

            variable size

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

        static
        function get_config_file(cls) -> str or None

        static
        function is_fuel(cls, itemstack)

        function __init__(self, block, types: typing.List[str])

            variable self.block
                todo: this should be at the container

            variable self.fuel_left

            variable self.fuel_max

            variable self.xp_stored

            variable self.smelt_start: typing.Optional[float]

            variable self.old_item_name

            variable self.recipe

            variable self.progress

            variable self.types

                variable self.custom_name

            variable slots
                1 input, 1 fuel and 1 output

            variable self.fuel_left

            variable self.fuel_max

            variable self.xp_stored

            variable self.smelt_start

            variable self.progress

            variable self.types

        function reset(self)

        function update_status(self)

                variable self.old_item_name

                variable self.smelt_start

                        variable recipe

                variable self.recipe: mcpython.common.container.crafting.FurnaceCraftingHelper.FurnaceRecipe

                variable self.block.active

            variable slot_copy

        function on_input_update(self, player=False)

        function on_fuel_slot_update(self, player=False)

        function on_output_update(self, player=False)

        function draw(self, hovering_slot=None)
            
            Draws the inventory


        function get_interaction_slots(self)

            variable elapsed_time

                variable self.fuel_left

                variable self.progress

                variable self.progress

            variable self.smelt_start

        function load(self, data: dict) -> bool

            variable self.fuel_left

            variable self.fuel_max

            variable self.xp_stored

            variable self.progress

        function save(self)