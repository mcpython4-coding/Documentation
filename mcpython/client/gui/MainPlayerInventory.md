***MainPlayerInventory.py - documentation - last updated on 28.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class MainPlayerInventory extends mcpython.client.gui.ContainerRenderer.ContainerRenderer
        
        inventory class for the main part of the inventory


        variable TEXTURE

        variable TEXTURE_SIZE

        variable INSTANCES: typing.List["MainPlayerInventory"]

        static
        function create(cls, hotbar)

            variable texture

            variable size

            variable texture

            variable size

            variable texture

            variable ground

            variable cls.TEXTURE

            variable cls.TEXTURE_SIZE

        static
        function get_config_file() -> str or None

        function __init__(self, hotbar)

            variable self.hotbar

            variable self.recipe_interface

                variable self.custom_name

            variable slots
                9x hotbar, 27x main, 4x armor, 5x crafting, 1x offhand

            variable inputs

            variable output

            variable self.recipe_interface

        function armor_update(self, player=None)

                variable shared.world.get_active_player().armor_level

        function draw(self, hovering_slot=None)

                variable itemstack

            variable shared.state_handler.active_state.parts[0].activate_mouse

        function update_shift_container(self)

        function free(self)