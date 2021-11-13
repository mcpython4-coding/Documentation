***IButton.py - documentation - last updated on 27.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class IButton extends IAllDirectionOrientableBlock

        variable DEBUG_WORLD_BLOCK_STATES

        function __init__(self)

            variable self.powered

        function check_block_behind(self)

            variable dimension

            variable block

        function on_block_update(self)

        function get_model_state(self) -> dict

            variable d["powered"]

        function set_model_state(self, state: dict)

                variable self.powered