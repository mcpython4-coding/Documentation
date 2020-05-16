***UIPartImage.py - documentation - last updated on 16.5.2020 by uuk***
___

    class UIPartImage extends UIPart.UIPart

        function __init__(self, image
            
            creates an new UIPartButton
            :param position: the position of the button
            :param press: the EventInfo for mouse buttons and mods, no area
            :param anchor_image: the anchor on the button
            :param anchor_window: the anchor on the window


            variable self.on_press

            variable self.active

        function bind_to_eventbus(self)

        function on_mouse_press(self, x, y, button, modifiers)

        function on_draw_2d(self)