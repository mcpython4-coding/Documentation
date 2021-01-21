***AbstractDamageBarItem.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class AbstractDamageBarItem extends mcpython.common.item.AbstractItem.AbstractItem,  ABC

        function __init__(self)

            variable self.unbreakable

        function get_damage_info(
                self,
                ) -> typing.Optional[typing.Tuple[float, typing.Tuple[int, int, int]]]:

    class DefaultDamageBarItem extends AbstractDamageBarItem,  ABC

        function get_damage_info(
                self,
                ) -> typing.Optional[typing.Tuple[float, typing.Tuple[int, int, int]]]:

            variable damage

        function get_damage(self) -> float

    class DamageOnUseItem extends DefaultDamageBarItem,  ABC

        variable DURABILITY: int

        function __init__(self)

            variable self.damage

        function get_damage(self) -> float

        function on_block_broken_with(self, itemstack, player, block)