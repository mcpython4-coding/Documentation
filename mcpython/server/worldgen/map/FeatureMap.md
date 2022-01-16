***FeatureMap.py - documentation - last updated on 16.1.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class FeatureMap extends mcpython.server.worldgen.map.AbstractChunkInfoMap.AbstractMap

        variable NAME

        variable VERSION

        function __init__(self, chunk)

            variable self.feature_map

            variable self.feature_data

        function reserve_region(
                self,
                start: typing.Tuple[int, int, int],
                end: typing.Tuple[int, int, int],
                name: str,
                ):

        function overlaps_with_region(
                self, start: typing.Tuple[int, int, int], end: typing.Tuple[int, int, int]
                ) -> bool: