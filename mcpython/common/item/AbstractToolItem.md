***AbstractToolItem.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
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