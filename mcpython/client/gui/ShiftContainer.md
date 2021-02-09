***ShiftContainer.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ShiftContainer
        
        Container class holding information on which inventory parts can be shift-clicked
        todo: is their no better way of doing this?
        todo: maybe add more than two sides?


        function __init__(self)

            variable self.container_A

            variable self.container_B

        function get_opposite_item_list_for(self, slot)

        function move_to_opposite(self, slot, count=None) -> bool

                variable count

            variable opposite

                    variable delta