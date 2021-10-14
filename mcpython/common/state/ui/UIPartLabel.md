***UIPartLabel.py - documentation - last updated on 14.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class UIPartLabel extends AbstractUIPart.AbstractUIPart

        function __init__(
                self,
                text,
                position,
                press=mcpython.engine.event.EventInfo.MousePressEventInfo(
                pyglet.window.mouse.LEFT
                ),
                anchor_lable="WS",
                anchor_window="WS",
                on_press=None,
                color=(0, 0, 0, 255),
                text_size=20,
                ):
            
            Creates a new label
            :param text: the text of the label
            :param position: the position of the label
            :param press: the EventInfo for mouse labels and mods, no area
            :param anchor_label: the anchor on the label
            :param anchor_window: the anchor on the window
            :param on_press: called when the mouse presses on the label together with x and y
            :param color: the color of the text to use
            :param text_size: the size of the text


            variable self.text

            variable self.press: mcpython.engine.event.EventInfo.MousePressEventInfo

            variable self.color

            variable self.text_size

            variable self.on_press

            variable self.lable

            variable self.active

        function bind_to_eventbus(self)

        function get_real_position(self)

        function on_mouse_press(self, x, y, button, modifiers)

        function on_draw_2d(self)