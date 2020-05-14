***Layer.py - documentation - last updated on 14.5.2020 by uuk***
___

    class LayerConfig
        function __init__(self, *config, **cconfig)

    class Layer extends event.Registry.Registry
        static function normalize_config(config: LayerConfig)

        variable NAME

        static function add_generate_functions_to_chunk(config: LayerConfig, reference)