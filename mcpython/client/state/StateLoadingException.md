***StateLoadingException.py - documentation - last updated on 23.8.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class StateLoadingException extends State.State

        variable NAME

        function __init__(self)

            variable self.labels

            variable self.label_batch

        function set_text(self, text: str)

        function create_state_parts(self) -> list

        function resume(self, *_)

        function bind_to_eventbus(self)

        function on_resize(self, w, h)

            variable self.parts[1].position

                variable label.x

        function on_draw_2d_pre(self)

            variable self.parts[1].text

        function on_update(self, dt)

        function deactivate(self)

        function activate(self)

    variable loadingexception

    function error_occur(text: str)