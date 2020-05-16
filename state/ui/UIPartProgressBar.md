***UIPartProgressBar.py - documentation - last updated on 16.5.2020 by uuk***
___

    class UIPartProgressBar extends UIPart.UIPart
            
            creates an new UIPartProgressBar
            :param position: the position to create on
            :param size: the size of the progressbar
            :param color: the color to use for the progress
            :param progress_items: the amount of items that the progressbar holds. default: size[0]-6
            :param status: how far we are at the moment
            :param text: the text to draw ontop of the progress bar
            :param anchor_pgb: the anchor on the progress bar
            :param anchor_window: the anchor on the window


            variable self.lable

            variable self.active

        function bind_to_eventbus(self)

        function on_draw_2d(self)

            variable sx

            variable self.lable.text

            variable self.lable.font_size

            variable self.lable.x

            variable self.lable.y