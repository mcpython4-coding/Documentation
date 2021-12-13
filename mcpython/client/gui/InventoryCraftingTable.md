***InventoryCraftingTable.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
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

        function draw(self, hovering_slot=None)
            
            draws the inventory


        function get_interaction_slots(self)

        function update_shift_container(self)