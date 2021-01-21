***AbstractFoodItem.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class AbstractFoodItem extends mcpython.common.item.AbstractItem.AbstractItem,  ABC

        variable HUNGER_ADDITION

        function on_eat(self)
            
            called when the player eats the item
            :return: if the item was eaten or not


        function get_eat_hunger_addition(self) -> int