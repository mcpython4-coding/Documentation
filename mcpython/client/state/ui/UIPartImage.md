***UIPartImage.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class UIPartImage extends UIPart.UIPart

        function __init__(
                self,
                image: pyglet.sprite.Sprite,
                position,
                anchor_window="WS",
                on_press=None,
                press=mcpython.common.event.EventInfo.MousePressEventInfo(
                pyglet.window.mouse.LEFT
                ),
                anchor_image="WS",
                ):
            
            creates an new UIPartButton
            :param position: the position of the button
            :param press: the EventInfo for mouse buttons and mods, no area
            :param anchor_image: the anchor on the button
            :param anchor_window: the anchor on the window


            variable self.image

            variable self.press: mcpython.common.event.EventInfo.MousePressEventInfo

            variable self.on_press

            variable self.active

        function bind_to_eventbus(self)

        function on_mouse_press(self, x, y, button, modifiers)

        function on_draw_2d(self)