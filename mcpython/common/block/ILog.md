***ILog.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class ILog extends mcpython.common.block.AbstractBlock.AbstractBlock
        
        base class for logs


        function __init__(self)

            variable self.axis

        function get_model_state(self)

        function set_model_state(self, state: dict)

        variable DEBUG_WORLD_BLOCK_STATES