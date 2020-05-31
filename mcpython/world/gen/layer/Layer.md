***Layer.py - documentation - last updated on 6.6.2020 by uuk***
___

    class LayerConfig

        function __init__(self, *config, **cconfig)

            variable self.config

            variable self.layer

    class Layer extends mcpython.event.Registry.Registry

        static
        function normalize_config(config: LayerConfig)

        variable NAME

        static
        function add_generate_functions_to_chunk(config: LayerConfig, reference)