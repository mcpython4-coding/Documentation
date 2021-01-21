***StateHandler.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class StateHandler

        function __init__(self)

            variable self.states

            variable self.CANCEL_SWITCH_STATE

        function switch_to(self, state_name: str, immediate=True)

        function _switch_to(self, statename: str)

        function add_state(self, state_instance: State.State)

        function update_exclusive(self)

    variable handler

    @onlyInClient()
    function load()