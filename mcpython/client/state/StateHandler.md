***StateHandler.py - documentation - last updated on 13.5.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class StateHandler

        function __init__(self)

            variable self.states

            variable self.CANCEL_SWITCH_STATE

            variable self.global_key_bind_toggle

        function change_state(self, state_name: str, immediate=True)

        function inner_change_state(self, state_name: str)

            variable previous

            variable now

            variable self.active_state: State.State

        function add_state(self, state_instance: State.State)

        function update_mouse_exclusive_state(self)

    variable handler

    @onlyInClient()
    function load()