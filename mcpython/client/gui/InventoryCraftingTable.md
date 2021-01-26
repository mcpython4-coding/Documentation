***InventoryCraftingTable.py - documentation - last updated on 26.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class InventoryCraftingTable extends mcpython.client.gui.ContainerRenderer.ContainerRenderer
        
        inventory class for the crafting table


        variable TEXTURE

        variable TEXTURE_SIZE

        static
        function update_texture(cls)

        static
        function get_config_file() -> str or None

        function __init__(self, *args, **kwargs)

            variable inputs

            variable self.recipeinterface

        function create_slot_renderers(self) -> list

        function on_activate(self)

        function on_deactivate(self)

        function draw(self, hovering_slot=None)
            
            draws the inventory


        function get_interaction_slots(self)

        function on_key_press(self, symbol, modifiers)

        function update_shift_container(self)