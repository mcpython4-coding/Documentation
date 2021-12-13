***ServerSelectionState.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ServerSelectionState extends AbstractState

        variable NAME

        function __init__(self)

            variable self.config_background

            variable self.back_button

            variable self.join_button

            variable self.server_ip_input

        function create_state_parts(self) -> list

            variable self.server_ip_input

            variable pair

    variable server_selection