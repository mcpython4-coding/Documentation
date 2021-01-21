***UIPartProgressBar.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class UIPartProgressBar extends UIPart.UIPart

        function __init__(
                self,
                position,
                size,
                color=(1.0, 0.0, 0.0),
                progress_items=None,
                status=0,
                text="",
                anchor_pgb="WS",
                anchor_window="WS",
                text_color=(0, 0, 0, 255),
                ):
            
            creates an new UIPartProgressBar
            :param position: the position to create on
            :param size: the size of the progressbar
            :param color: the color to use for the progress
            :param progress_items: the amount of items that the progressbar holds. default: size[0]-6
            :param status: how far we are at the moment
            :param text: the text to draw ontop of the progress bar
            :param anchor_pgb: the anchor on the progress bar
            :param anchor_window: the anchor on the window


            variable self.color

            variable self.progress_max

            variable self.progress

            variable self.text

            variable self.lable

            variable self.active

        function bind_to_eventbus(self)

        function on_draw_2d(self)

                variable self.progress

            variable sx

            variable self.lable.text

            variable self.lable.font_size

            variable self.lable.x

            variable self.lable.y