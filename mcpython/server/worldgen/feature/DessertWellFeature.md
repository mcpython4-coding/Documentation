***DessertWellFeature.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    @shared.registry class DessertWellFeature extends mcpython.server.worldgen.feature.IFeature.IFeature

        variable NAME

        variable SAND_LIKE

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
