***Biome.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class Biome extends mcpython.common.event.Registry.IRegistryContent,  ABC
        
        Abstract base class for biomes
        Defines the look of the biome
        todo: add factory for it


        variable NAME

        variable PASSIVE_SPAWNS

        variable HOSTILE_SPAWNS

        variable AMBIENT_SPAWNS

        variable GRASS_COLOR

        variable WATER_COLOR

        variable FEATURES

        variable FEATURES_SORTED

        variable CARVERS - for the future...

        static
        function get_landmass(cls) -> str

        static
        function get_weight(cls) -> int

        static
        function get_height_range(cls) -> typing.Tuple[int, int]

        static
        function get_top_layer_height_range(
                cls,
                position: typing.Tuple[int, int],
                dimension: mcpython.common.world.AbstractInterface.IDimension,
                ) -> typing.Tuple[int, int]:

        static
        function get_top_layer_configuration(
                cls,
                height: int,
                position: typing.Tuple[int, int],
                dimension: mcpython.common.world.AbstractInterface.IDimension,
                ) -> typing.List[str]: