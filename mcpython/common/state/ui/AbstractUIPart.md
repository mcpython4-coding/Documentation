***AbstractUIPart.py - documentation - last updated on 14.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractUIPart extends mcpython.common.state.AbstractStatePart.AbstractStatePart,  ABC

        function __init__(
                self, position, bounding_box_size, anchor_element="WS", anchor_window="WS"
                ):

            variable self.position

            variable self.bounding_box_size

            variable self.anchor_element

            variable self.anchor_window

        function get_real_position(self)