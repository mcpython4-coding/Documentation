***IOre.py - documentation - last updated on 16.5.2020 by uuk***
___

    function place_default(x: int, y: int, z: int, sx: int, sy: int, sz: int, blocks: list, replace

    class OrePlacementMode extends enum.Enum

        variable DEFAULT - args: minh, maxh

        variable MIDDLE_HIGHEST - args: minh, maxh, minchance

    class IOre extends world.gen.feature.IFeature.IFeature

        static function place(dimension, x, y, z, **config)

        static function get_height_range() -> tuple

        static function get_ore_block() -> str or list
            
            :return: an orename or an list of orenames or an {orename: chance} table


        static function get_replacement_blocks(): return ["minecraft

        static function get_size_range() -> tuple

        static function get_chunk_count() -> int

        static function get_ore_height() -> int

    class INormalOre extends IOre

        static function place(cls, dimension, x, y, z, **config)

        static function get_ore_height(cls) -> int

    class CoalOre extends INormalOre

        static function get_size_range() -> tuple

        static function get_chunk_count() -> int

        static function get_height_range() -> tuple

        static function get_ore_block() -> str or list: return "minecraft