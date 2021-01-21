***UIPart.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class UIPart extends mcpython.client.state.StatePart.StatePart

        function __init__(self, position, bboxsize, anchor_element="WS", anchor_window="WS")

            variable self.position

            variable self.bboxsize

            variable self.anchor_element

            variable self.anchor_window

        function get_real_position(self)