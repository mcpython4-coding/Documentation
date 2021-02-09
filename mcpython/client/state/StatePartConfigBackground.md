***StatePartConfigBackground.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class BackgroundHandler

        variable batch

        variable objects

        variable background_raw: PIL.Image.Image

        variable background_size

        variable background_image

        variable old_win_size

        static
        function recreate(cls, wx, wy)

    @onlyInClient() class StatePartConfigBackground extends mcpython.client.state.StatePart.StatePart

        function activate(self)

        function bind_to_eventbus(self)

        function draw(self)

        function resize(self, x, y)