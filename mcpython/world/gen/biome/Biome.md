***Biome.py - documentation - last updated on 8.6.2020 by uuk***
___

    class Biome extends mcpython.event.Registry.IRegistryContent

        variable NAME

        static
        function get_temperature() -> float

        static
        function get_landmass() -> str

        static
        function get_weight() -> int

        static
        function get_height_range()

        static
        function get_top_layer_height_range()

        static
        function get_top_layer_configuration(height: int)

        static
        function get_trees() -> list
            
            :return: an (IFeature, chance as n)[


        static
        function get_ores() -> list
            
            :return: an IOre[
