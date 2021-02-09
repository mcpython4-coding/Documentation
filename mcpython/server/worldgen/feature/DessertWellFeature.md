***DessertWellFeature.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @shared.registry class DessertWellFeature extends mcpython.server.worldgen.feature.IFeature.IFeature

        variable NAME

        variable SAND_LIKE
            todo: make tag

        variable SANDSTONE

        variable SANDSTONE_SLAB

        variable WATER

        static
        function place_array(
                cls,
                array: mcpython.server.worldgen.WorldGenerationTaskArrays.IWorldGenerationTaskHandlerReference,
                x: int,
                y: int,
                z: int,
                config,
                ):
            
            Code ported from minecraft using minecraft forge dev-environment for version 1.16.4
