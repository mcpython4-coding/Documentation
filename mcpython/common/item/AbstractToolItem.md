***AbstractToolItem.py - documentation - last updated on 30.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractToolItem extends mcpython.common.item.AbstractDamageBarItem.DamageOnUseItem,  ABC

        variable HAS_BLOCK

        variable STACK_SIZE

        variable TOOL_LEVEL

        variable TOOL_TYPE

        function __init__(self)

        function __eq__(self, other)

        function get_tool_level(self):  # todo: remove
                return self.TOOL_LEVEL
                
                def get_tool_type(self):  # todo: remove
                return self.TOOL_TYPE
                
                def get_speed_multiplyer(self, itemstack):

        function get_tool_type(self):  # todo: remove
                return self.TOOL_TYPE
                
                def get_speed_multiplyer(self, itemstack):

        function get_speed_multiplyer(self, itemstack)

        function get_data(self)

        function set_data(self, data)

        function add_damage(self, damage: int) -> bool