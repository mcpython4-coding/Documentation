***InventoryBarrel.py - documentation - last updated on 20.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class InventoryBarrel extends mcpython.client.gui.ContainerRenderer.ContainerRenderer
        
        inventory class for chest


        function __init__(self, block)

            variable self.block

                variable self.custom_name

        static
        function get_config_file() -> str or None

            variable self.block.opened

            variable self.block.opened

        function draw(self, hovering_slot=None)

        function get_interaction_slots(self)

        function update_shift_container(self)