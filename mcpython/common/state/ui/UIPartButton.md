***UIPartButton.py - documentation - last updated on 14.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable image

    variable IMAGES

    function load_images()

        variable image

        variable disabled

        variable enabled

        variable hovering

    function draw_button(position, size, mode)

            variable i

                variable ii

    class UIPartButton extends AbstractUIPart.AbstractUIPart

        function __init__(
                self,
                size,
                text,
                position,
                press=mcpython.engine.event.EventInfo.MousePressEventInfo(
                pyglet.window.mouse.LEFT
                ),
                anchor_button="WS",
                anchor_window="WS",
                on_press=None,
                on_hover=None,
                on_try_press=None,
                enable=True,
                has_hovering_state=True,
                ):
            
            Creates a new UIPartButton
            :param size: the size of the button
            :param text: the text of the button
            :param position: the position of the button
            :param press: the EventInfo for mouse buttons and mods, no area
            :param anchor_button: the anchor on the button
            :param anchor_window: the anchor on the window
            :param on_press: called together with x and y on press on the button  todo: change to include button
            :param on_hover: called on every mouse move on the button with the mouse x and y
            :param on_try_press: called when the button is pressed during an in-active phase of the button with x and y
            :param enable: if the button should be enabled from the start
            :param has_hovering_state: if the button has an state different from normal when the mouse is over it


            variable self.text

            variable self.press: mcpython.engine.event.EventInfo.MousePressEventInfo

            variable self.on_press

            variable self.on_hover

            variable self.on_try_press

            variable self.enabled

            variable self.has_hovering_state

            variable self.hovering

            variable self.lable

            variable self.active

        function bind_to_eventbus(self)

        function deactivate(self)

        function on_mouse_press(self, x, y, button, modifiers)

        function on_mouse_motion(self, x, y, dx, dy)

        function on_draw_2d(self)

            variable self.lable.text
                todo: reconsider language only on reload & text change

            variable self.lable.x

            variable self.lable.y

            variable self.lable.font_size

    class UIPartToggleButton extends UIPartButton

        function __init__(
                self,
                size,
                text_possibilities,
                position,
                toggle=mcpython.engine.event.EventInfo.MousePressEventInfo(
                pyglet.window.mouse.LEFT
                ),
                toggle_back=mcpython.engine.event.EventInfo.MousePressEventInfo(
                pyglet.window.mouse.RIGHT
                ),
                anchor_button="WS",
                anchor_window="WS",
                on_toggle=None,
                on_hover=None,
                on_try_press=None,
                enable=True,
                has_hovering_state=True,
                text_constructor="{}",
                start=0,
                ):
            
            creates an new UIPartButton
            :param size: the size of the button
            :param text_possibilities: the texts of the button
            :param position: the position of the button
            :param toggle: the EventInfo for mouse buttons and mods, no area to define, toggle forward
            :param toggle_back: the EventInfo for mouse buttons and mods, no area to define, toggle backwards
            :param anchor_button: the anchor on the button
            :param anchor_window: the anchor on the window
            :param on_toggle: called when the button toggles, parameters: (from: str, to: str, direction: int, position:tuple)
            :param on_hover: called when the mouse is over the button
            :param on_try_press: called when button is disabled and the user presses the button
            :param enable: button should be clickable?
            :param has_hovering_state: if the button gets blue when mouse is over it
            :param text_constructor: an string.format(item) or an function(item: str) -> str entry
            :param start: where in the array to start from


            variable self.text_pages

            variable self.text_constructor

            variable self.index

            variable self.text

            variable self.toggle: mcpython.engine.event.EventInfo.MousePressEventInfo

            variable self.toggle_back: mcpython.engine.event.EventInfo.MousePressEventInfo

            variable self.on_toggle

            variable self.on_hover

            variable self.on_try_press

            variable self.event_functions

            variable self.enabled

            variable self.has_hovering_state

            variable self.hovering

            variable self.lable

            variable self.active

        function update_text(self)

        function on_mouse_press(self, x, y, button, modifiers)

        function on_draw_2d(self)