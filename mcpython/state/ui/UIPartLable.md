***UIPartLable.py - documentation - last updated on 8.6.2020 by uuk***
___

    class UIPartLable extends UIPart.UIPart

        function __init__(self, text, position, press=mcpython.event.EventInfo.MousePressEventInfo(pyglet.window.mouse.LEFT),
                anchor_lable="WS", anchor_window="WS", on_press=None, color=(0, 0, 0, 255), text_size=20):
            
            creates an new UIPartButton
            :param text: the text of the lable
            :param position: the position of the lable
            :param press: the EventInfo for mouse lables and mods, no area
            :param anchor_lable: the anchor on the lable
            :param anchor_window: the anchor on the window
            :param on_press: called when the mouse presses on the lable together with x and y
            :param color: the color of the text to use
            :param text_size: the size of the text


            variable self.on_press

            variable self.lable

            variable self.active

        function bind_to_eventbus(self)

        function get_real_position(self)

        function on_mouse_press(self, x, y, button, modifiers)

        function on_draw_2d(self)