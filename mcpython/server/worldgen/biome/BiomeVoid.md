***BiomeVoid.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class Void extends Biome.Biome

        variable NAME

        static
        function get_weight() -> int

        static
        function get_height_range() -> typing.Tuple[int, int]

        static
        function get_top_layer_height_range(
                position: typing.Tuple[int, int],
                dimension: mcpython.common.world.AbstractInterface.IDimension,
                ) -> typing.Tuple[int, int]:

        static
        function get_top_layer_configuration(
                height: int,
                position: typing.Tuple[int, int],
                dimension: mcpython.common.world.AbstractInterface.IDimension,
                ) -> typing.List[str]: