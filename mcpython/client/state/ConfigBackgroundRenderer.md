***ConfigBackgroundRenderer.py - documentation - last updated on 19.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ConfigBackgroundRenderer extends AbstractStateRenderer

        variable ASSIGNED_DRAW_STAGE

        function __init__(self)

            variable background_raw: PIL.Image.Image

            variable self.background_image

            variable self.objects

        function recreate(self, wx, wy)

                    variable obj

                    variable obj.position

        function on_activate(self)

        function resize(self, width, height)

        function draw(self)