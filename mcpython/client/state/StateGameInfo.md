***StateGameInfo.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable sprite
        todo: use pyglet.image.Image.get_region(area)

    @onlyInClient() class StateGameInfo extends mcpython.client.state.State.State

        variable NAME

        static
        function is_mouse_exclusive()

        function get_parts(self) -> list

        function bind_to_eventbus(self)

        static
        function on_key_press(symbol, modifiers)

        static
        function on_mouse_press(x, y, button, modifiers)

    variable game_info

    @onlyInClient()
    function create()