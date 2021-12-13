***Buttons.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ImageOverlayButtonRenderer

        function __init__(
                self,
                button_size: typing.Tuple[int, int],
                icon: pyglet.image.AbstractImage,
                on_press: typing.Callable,
                icon_offset=(0, 0),
                ):

            variable self.backgrounds

            variable self.icon

            variable self.icon_offset

            variable self.on_press

            variable self.hovering

            variable self.active

            variable self.position

            variable self.size

            variable self.underlying_event_bus: mcpython.engine.event.EventBus.EventBus

        function on_mouse_move(self, x, y, dx, dy)

        function on_key_press(self, button, mod)

        function on_mouse_press(self, x, y, button, mod)

        function press_button(self)

        function over_button(self, x: int, y: int)

            variable self.hovering

        function draw(self)

    variable ARROW_TEXTURE_SHEET

    variable RIGHT_ARROW

    variable LEFT_ARROW

    function reload()

    function arrow_button_left(position, callback)

    function arrow_button_right(position, callback)