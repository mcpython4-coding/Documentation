***UIPartLable.py - documentation - last updated on 16.5.2020 by uuk***
___

    class UIPartLable extends UIPart.UIPart
            
            creates an new UIPartButton
            :param text: the text of the lable
            :param position: the position of the lable
            :param press: the EventInfo for mouse lables and mods, no area
            :param anchor_lable: the anchor on the lable
            :param anchor_window: the anchor on the window


            variable self.on_press

            variable self.lable

            variable self.active

        function bind_to_eventbus(self)

        function get_real_position(self)

        function on_mouse_press(self, x, y, button, modifiers)

        function on_draw_2d(self)