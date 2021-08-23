***ButtonBackgroundBuilder.py - documentation - last updated on 23.8.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ButtonState extends enum.Enum

        variable ACTIVE

        variable HOVERING

        variable DISABLED

    class ButtonBackgroundBuilder

        function __init__(
                self,
                texture_default: PIL.Image.Image,
                texture_hovering: PIL.Image.Image,
                texture_disabled: PIL.Image.Image,
                ):

            variable self.texture_default

            variable self.texture_hovering

            variable self.texture_disabled

        function get_texture_for_state(self, state: ButtonState) -> PIL.Image.Image

        function get_texture_for_size(
                self, sx: int, sy: int, state: ButtonState
                ) -> PIL.Image.Image:

            variable texture

            variable new

        function get_pyglet_texture(
                self, sx: int, sy: int, state: ButtonState
                ) -> pyglet.image.AbstractImage:

    variable WIDGETS

    variable DefaultButtonTexture

    function reload()

        variable WIDGETS

        variable DefaultButtonTexture