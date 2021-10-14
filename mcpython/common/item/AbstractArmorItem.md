***AbstractArmorItem.py - documentation - last updated on 14.10.2021 by uuk***
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

        variable DURABILITY

        function __init__(self)

            variable self.damage

        function write_to_network_buffer(self, buffer: WriteBuffer)

        function read_from_network_buffer(self, buffer: ReadBuffer)

        variable DEFENSE_POINTS

        function get_defense_points(self)

        variable STACK_SIZE

        function get_damage(self) -> float

        function get_data(self)

        function set_data(self, data)