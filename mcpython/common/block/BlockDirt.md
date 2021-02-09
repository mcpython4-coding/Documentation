***BlockDirt.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class BlockDirt extends AbstractBlock.AbstractBlock
        
        Base class for dirt
        todo: implement real -> grass convert


        variable NAME: str

        variable HARDNESS

        variable BLAST_RESISTANCE

        variable ASSIGNED_TOOLS

        variable ENABLE_RANDOM_TICKS

        function on_random_update(self)

                            variable position

                            variable instance

    @shared.mod_loader("minecraft", "stage:block:load")
    function load()