***DefaultStonePlacementLayer.py - documentation - last updated on 14.5.2020 by uuk***
___

    @G.worldgenerationhandler class DefaultStonePlacementLayer extends Layer
        static function normalize_config(config: LayerConfig)

        variable NAME

        static function add_generate_functions_to_chunk(cls, config: LayerConfig, reference)
        static function generate_xz(reference, x, z, config)