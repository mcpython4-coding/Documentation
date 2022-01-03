***AbstractChunkInfoMap.py - documentation - last updated on 3.1.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractMap extends IBufferSerializeAble,  ABC
        
        Abstract map class holding information about a Chunk, in map-like formats
        Contains code for writing to save, by default, does nothing


        variable NAME

        variable VERSION

        static
        function init_on(cls, chunk) -> "AbstractMap"

        function __init__(self, chunk)

            variable self.chunk

            variable version

                    variable fixer

                    variable target

                        variable buffer.stream

                    variable buffer.stream

                    variable version

        function dump_debug_info(self, file: str)