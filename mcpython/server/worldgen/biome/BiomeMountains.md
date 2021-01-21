***BiomeMountains.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class Plains extends Biome.Biome

        variable NAME

        variable PASSIVE_SPAWNS

        variable HOSTILE_SPAWNS

        variable AMBIENT_SPAWNS

        variable FEATURES

        static
        function get_weight() -> int

        static
        function get_height_range() -> typing.Tuple[int, int]