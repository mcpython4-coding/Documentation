***AbstractDamageBarItem.py - documentation - last updated on 28.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ToolTipRendererForDamage extends DefaultHoveringItemBoxDefinition

        function getAdditionalText(self, itemstack: ItemStack) -> typing.List[str]

    class AbstractDamageBarItem extends mcpython.common.item.AbstractItem.AbstractItem,  ABC

        variable TOOL_TIP_RENDERER

        function __init__(self)

            variable self.unbreakable

        function get_tooltip_provider(self)

            variable self.unbreakable

        function get_damage_info(
                self,
                itemstack,
                ) -> typing.Optional[typing.Tuple[float, typing.Tuple[int, int, int]]]:

        function getDamageBarInfo(self, itemstack: ItemStack) -> str

        function draw_in_inventory(
                self, itemstack, position: typing.Tuple[int, int], scale: float
                ):

            variable width

            variable height

            variable d

    class DefaultDamageBarItem extends AbstractDamageBarItem,  ABC

        function get_damage_info(
                self,
                itemstack,
                ) -> typing.Optional[typing.Tuple[float, typing.Tuple[int, int, int]]]:

            variable damage

        function get_damage(self, itemstack) -> float

    class DamageOnUseItem extends DefaultDamageBarItem,  ABC

        variable DURABILITY: int

        function __init__(self)

            variable self.damage

        function get_damage(self, itemstack) -> float

        function getDamageBarInfo(self, itemstack: ItemStack) -> str