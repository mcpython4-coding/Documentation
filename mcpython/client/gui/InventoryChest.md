***InventoryChest.py - documentation - last updated on 28.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class InventoryChest extends mcpython.client.gui.ContainerRenderer.ContainerRenderer
        
        Inventory class for chest
        Defines the default chest layout


        variable TEXTURE

        variable TEXTURE_SIZE

            variable texture

            variable size

            variable texture

            variable size

            variable texture

            variable cls.TEXTURE

            variable cls.TEXTURE_SIZE

        static
        function get_config_file() -> str or None

        function __init__(self, block=None)

            variable self.block

                variable self.custom_name

                    variable self.custom_name

        function draw(self, hovering_slot=None)

        function get_interaction_slots(self)

        function update_shift_container(self)