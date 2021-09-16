***StateHandler.py - documentation - last updated on 16.9.2021 by uuk***
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
        
        Manager for states of the game.
        The game is a state machine, so we need somebody to keep track of it...
        Seems to be this class
        How does it work?
        - One instance per game, more will break stuff
        - stored @ shared.state_handler


        function __init__(self)

            variable self.active_state: typing.Optional[AbstractState.AbstractState]

            variable self.global_key_bind_toggle

        function change_state(self, state_name: str, immediate=True)
            
            Will change the current state of the "machine"
            :param state_name: the name to switch to
            :param immediate: now or next scheduled event cycle (so afterwards), defaults to True


        function inner_change_state(self, state_name: str)
            
            Internal change_state
            DO NOT USE!


            variable previous

            variable self.active_state: AbstractState.AbstractState

        function add_state(self, state_instance: AbstractState.AbstractState)

        function update_mouse_exclusive_state(self)

    variable handler

    function load_states()