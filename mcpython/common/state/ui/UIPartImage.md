***UIPartImage.py - documentation - last updated on 19.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class UIPartImage extends AbstractUIPart.AbstractUIPart

        function __init__(
                self,
                image: pyglet.sprite.Sprite,
                position,
                anchor_window="WS",
                on_press=None,
                press=mcpython.engine.event.EventInfo.MousePressEventInfo(
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

            variable self.press: mcpython.engine.event.EventInfo.MousePressEventInfo

            variable self.on_press

            variable self.active

        function bind_to_eventbus(self)

        function on_mouse_press(self, x, y, button, modifiers)

        function on_draw_2d(self)