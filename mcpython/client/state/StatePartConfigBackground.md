***StatePartConfigBackground.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
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