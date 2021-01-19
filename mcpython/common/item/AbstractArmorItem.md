***AbstractArmorItem.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class AbstractArmorItem extends  mcpython.common.item.AbstractDamageBarItem.DefaultDamageBarItem 

        variable DURABILITY

        function __init__(self)

            variable self.damage

        variable DEFENSE_POINTS

        function get_defense_points(self)

        variable STACK_SIZE

        function get_damage(self) -> float

        function get_data(self)

        function set_data(self, data)