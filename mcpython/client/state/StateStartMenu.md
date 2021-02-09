***StateStartMenu.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class StateStartMenu extends mcpython.client.state.State.State

        variable NAME

        variable CONFIG_LOCATION

        function __init__(self)

        function bind_to_eventbus(self)

        function activate(self)

        static
        function on_new_game_press(x, y)

        static
        function on_quit_game_press(x, y)

        static
        function on_draw_2d_pre()

        static
        function on_key_press(key, modifier)

    variable start_menu

    @onlyInClient()
    function create()