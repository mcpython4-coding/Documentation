***UIPartLabel.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class UIPartLabel extends UIPart.UIPart

        function __init__(
                self,
                text,
                position,
                press=mcpython.common.event.EventInfo.MousePressEventInfo(
                pyglet.window.mouse.LEFT
                ),
                anchor_lable="WS",
                anchor_window="WS",
                on_press=None,
                color=(0, 0, 0, 255),
                text_size=20,
                ):
            
            creates an new UIPartButton
            :param text: the text of the lable
            :param position: the position of the lable
            :param press: the EventInfo for mouse lables and mods, no area
            :param anchor_lable: the anchor on the lable
            :param anchor_window: the anchor on the window
            :param on_press: called when the mouse presses on the lable together with x and y
            :param color: the color of the text to use
            :param text_size: the size of the text


            variable self.text

            variable self.press: mcpython.common.event.EventInfo.MousePressEventInfo

            variable self.color

            variable self.text_size

            variable self.on_press

            variable self.lable

            variable self.active

        function bind_to_eventbus(self)

        function get_real_position(self)

        function on_mouse_press(self, x, y, button, modifiers)

        function on_draw_2d(self)