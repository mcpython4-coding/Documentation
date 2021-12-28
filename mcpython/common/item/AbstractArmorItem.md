***AbstractArmorItem.py - documentation - last updated on 28.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractArmorItem extends  mcpython.common.item.AbstractDamageBarItem.DefaultDamageBarItem,  ABC 
        
        Base class for armor
        Provides the properties specific to an armor item


        variable DURABILITY

        variable DEFENSE_POINTS

        variable STACK_SIZE

        variable TOOL_TIP_RENDERER

        function __init__(self)

            variable self.damage

            variable self.damage

        function get_damage(self, itemstack) -> float

        function get_tooltip_provider(self)

        function getDamageBarInfo(self, itemstack: ItemStack) -> str

        function get_data(self)

        function set_data(self, data)