***BlockDirt.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
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