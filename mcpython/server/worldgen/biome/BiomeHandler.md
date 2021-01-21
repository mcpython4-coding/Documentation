***BiomeHandler.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class BiomeHandler

        function __init__(self)

            variable self.registry_list

            variable self.biomes

        function register(self, biome: typing.Type[mcpython.server.worldgen.biome.Biome.Biome])

        function __call__(self, biome)

        function unregister(
                self, biome: typing.Type[mcpython.server.worldgen.biome.Biome.Biome]
                ):

        function get_biomes_for_dimension(
                self, biomes: typing.Dict[int, str], weighted=False, temperature=None
                ) -> list:

                variable l

                variable l

        function get_sum_weight_count(self, biomes, temperature=None) -> int

        function get_biome_at(
                self,
                landmass: str,
                select_value: float,
                temperature: float,
                biomes: typing.Dict[str, typing.Dict[int, str]],
                ) -> str:
            
            gets an biome with given info
            :param landmass: the landmass to choise from
            :param select_value: an value with which the system decides which biome to select, value from 0. - 1.
            :param temperature: the temperature to use
            :param biomes: the biomes to select from
            :return: the biome which was selected


            variable temperatures

            variable temperature

            variable biomes

            variable select_value

                variable select_value

    variable shared.biome_handler

    function load()