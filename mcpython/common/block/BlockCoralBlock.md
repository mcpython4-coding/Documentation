***BlockCoralBlock.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
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

    @shared.mod_loader("minecraft", "stage:block:load")
    function load()