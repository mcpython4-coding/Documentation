***ShiftContainer.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class ShiftContainer
        
        container class holding information on which inventory parts can be shift-clicked


        function __init__(self)

            variable self.container_A

            variable self.container_B

        function get_opposite_item_list_for(self, slot)

        function move_to_opposite(self, slot, count=None) -> bool