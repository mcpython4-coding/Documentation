***StateStartMenu.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
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