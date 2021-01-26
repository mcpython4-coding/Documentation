***BiomeHandler.py - documentation - last updated on 26.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class BiomeHandler
        
        The main handler for biomes
        Stores needed maps for the lookup during biome generation
        todo: make proper registry for biomes as everything is now data-driven-able, and as such depends not on a custom
            register function
        todo: maybe use instances for dynamic constructed biomes?


        function __init__(self)

            variable self.registry_list

            variable self.biomes

        function register(self, biome: typing.Type[mcpython.server.worldgen.biome.Biome.Biome])

        static
        function setup_biome_feature_list(
                cls, biome: typing.Type[mcpython.server.worldgen.biome.Biome.Biome], force=False
                ):
            
            Helper function for recalculating the internal biome feature sorted array
            :param biome: the biome
            :param force: force-recalculate?


                variable biome.FEATURES_SORTED

                    variable data

                    variable biome.FEATURES_SORTED[feature_def.group]

                    variable data

                    variable biome.FEATURES_SORTED[group]

        function __call__(self, biome: typing.Type[mcpython.server.worldgen.biome.Biome.Biome])
            
            Registers a biome to the internal system
            Will setup the FEATURES_SORTED system for later lookup
            :param biome: the biome to register
            :return: the biome, for @BiomeHandler-ing


            variable self.biomes[biome.NAME]

        function unregister(
                self, biome: typing.Type[mcpython.server.worldgen.biome.Biome.Biome]
                ):

        static
        function get_biomes_for_dimension(
                cls, biomes: typing.Dict[int, str], weighted=False, temperature=None
                ) -> list:

                variable biomes

                variable biomes

        function get_sum_weight_count(self, biomes, temperature=None) -> int

        function get_biome_at(
                self,
                landmass: str,
                select_value: float,
                temperature: float,
                biomes: typing.Dict[str, typing.Dict[int, str]],
                ) -> str:
            
            Gets an biome with given info
            :param landmass: the landmass to chose from
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