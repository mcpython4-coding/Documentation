***ShulkerBox.py - documentation - last updated on 25.4.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    function create_shulker_box(name)

                variable self.inventory

            variable NAME

            variable DEFAULT_FACE_SOLID

            function on_player_interaction(
                    self, player, button: int, modifiers: int, hit_position: tuple
                    ):

            function get_inventories(self)

            variable HARDNESS

            variable MINIMUM_TOOL_LEVEL

            variable ASSIGNED_TOOLS

            function get_provided_slot_lists(self, side)

            static
            function modify_block_item(
                    cls, item_constructor: mcpython.common.factory.ItemFactory.ItemFactory
                    ):

            static
            function set_block_data(cls, item_instance, block)

            function on_request_item_for_block(self, itemstack)

            function on_block_remove(self, reason)

    function load()