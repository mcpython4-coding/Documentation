***ISlab.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable BBOX_DICT

    class ISlab extends mcpython.common.block.AbstractBlock.AbstractBlock
        
        base class for slabs


        variable DEFAULT_FACE_SOLID

        function __init__(self)

            variable self.type

        function on_block_added(self)

        function get_model_state(self)

        function set_model_state(self, state: dict)

        variable DEBUG_WORLD_BLOCK_STATES

        function on_player_interact(
                self, player, itemstack, button, modifiers, exact_hit
                ) -> bool:

        function get_view_bbox(self)