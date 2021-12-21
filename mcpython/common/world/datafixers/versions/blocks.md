***blocks.py - documentation - last updated on 20.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class Furnace0_1Fixer extends BlockDataFixer
        
        Fixes the migration of the "progress" attribute and others of the Furnace block from int to float
        Below are the two classes for the blast furnace and smoker blocks, as they are delivered from the
        furnace block


        variable BLOCK_NAME

        variable BEFORE_VERSION: int

        variable AFTER_VERSION: int

    class BlastFurnace0_1Fixer extends Furnace0_1Fixer

        variable BLOCK_NAME

    class Smoker0_1Fixer extends Furnace0_1Fixer

        variable BLOCK_NAME