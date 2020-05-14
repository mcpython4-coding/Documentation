***BiomeHandler.py - documentation - last updated on 14.5.2020 by uuk***
___

    class BiomeHandler

        function __init__(self)

            variable self.registrylist

            variable self.biomes

            variable self.biometable - {dim: int -> {landmass: str -> {temperature: int -> [biomename with weights]}}}}

        function register(self, biome, dimensions=[])

        function __call__(self, biome)

            variable self.biomes[biome.NAME]

        function add_biome_to_dim(self, dim: int, biomename: str)

            variable biome

                variable self.biometable[dim][biome.get_landmass()][biome.get_temperature()]

        function remove_biome_from_dim(self, dim: int, biomename: str)

            variable biome

        function is_biome_in_dim(self, dim: int, biomename: str)

        function get_biomes_for_dimension(self, dim: int, landmass: str, weighted=False, temperature=None) -> list

                variable l

                variable l

        function get_sum_weight_count(self, dim: int, landmass: str, temperature=None) -> int

        function get_biome_at(self, landmass: str, dim: int, selectvalue: float, temperature: float) -> str
            
            gets an biome with given info
            :param landmass: the landmass to choise from
            :param dim: the dimension we were in
            :param selectvalue: an value with which the system decides which biome to select, value from 0. - 1.
            :param temperature: the temperature to use
            :return: the biome which was selected


            variable temperatures

            variable temperature

            variable biomes

            variable selectvalue

    variable G.biomehandler

    function load()