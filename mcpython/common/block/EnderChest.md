***EnderChest.py - documentation - last updated on 27.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class EnderChest extends IHorizontalOrientableBlock.IHorizontalOrientableBlock
        
        class for the ender chest
        todo: check if it can be opened like in chests
        todo: fix renderer


        variable NAME

        variable DEFAULT_FACE_SOLID

        variable HARDNESS

        variable MINIMUM_TOOL_LEVEL

        variable ASSIGNED_TOOLS

        variable DEBUG_WORLD_BLOCK_STATES

        function on_player_interaction(
                self, player, button: int, modifiers: int, hit_position: tuple
                ):

        function set_model_state(self, state: dict)

                    variable self.face

                    variable self.face

        function get_model_state(self) -> dict

        function get_view_bbox(self)

        function on_block_remove(self, reason)