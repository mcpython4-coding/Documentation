***GrassBlock.py - documentation - last updated on 13.11.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class GrassBlock extends IFoliageColoredBlock.IFoliageColoredBlock
        
        Class for the grass block


        variable NAME

        variable HARDNESS

        variable ASSIGNED_TOOLS

        variable ENABLE_RANDOM_TICKS

        function get_model_state(self) -> dict

        function on_random_update(self)

                variable instance

                variable instance

        function on_player_interaction(
                self,
                player,
                button: int,
                modifiers: int,
                hit_position: tuple,
                itemstack,
                ):