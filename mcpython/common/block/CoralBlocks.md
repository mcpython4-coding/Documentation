***CoralBlocks.py - documentation - last updated on 25.4.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ICoralBlock extends mcpython.common.block.AbstractBlock.AbstractBlock
        
        base class for every coral block


        variable ENABLE_RANDOM_TICKS

        function on_random_update(self)

    class BrainCoralBlock extends ICoralBlock
        
        class for brain coral block


        variable NAME: str

    class BubbleCoralBlock extends ICoralBlock
        
        class for bubble coral block


        variable NAME: str

    class FireCoralBlock extends ICoralBlock
        
        class for fire coral block


        variable NAME: str

    class HornCoralBlock extends ICoralBlock
        
        class for horn coral block


        variable NAME: str

    class TubeCoralBlock extends ICoralBlock
        
        class for tube coral block


        variable NAME: str

    function load()