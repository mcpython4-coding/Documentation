***Candle.py - documentation - last updated on 3.1.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ICandleGroup extends AbstractBlock.AbstractBlock
        
        Base class for the candle block system


        variable IS_SOLID

        variable DEFAULT_FACE_SOLID

        variable DEBUG_WORLD_BLOCK_STATES

        function __init__(self)

            variable self.count

            variable self.lit

        function get_model_state(self)

                variable self.count

                variable self.lit

    class ICandleCake extends FlowerLikeBlock

        variable SUPPORT_BLOCK_TAG

        variable IS_SOLID

        variable DEFAULT_FACE_SOLID

        variable DEBUG_WORLD_BLOCK_STATES

        function __init__(self)

            variable self.lit

        function get_model_state(self)

                variable self.lit

                variable player.hunger