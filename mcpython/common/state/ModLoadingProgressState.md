***ModLoadingProgressState.py - documentation - last updated on 19.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class ModLoadingProgress extends AbstractState.AbstractState

        variable NAME

        function __init__(self)

            variable self.stage_bar

            variable self.mod_bar

            variable self.item_bar

            variable self.memory_bar

        function create_state_parts(self) -> list

        function bind_to_eventbus(self)

        function on_resize(self, w, h)

            variable self.parts[3].position

        function on_draw_2d_pre(self)

        function on_update(self, dt)

        function deactivate(self)

    variable mod_loading