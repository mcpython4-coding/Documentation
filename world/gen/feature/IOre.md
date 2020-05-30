***IOre.py - documentation - last updated on 30.5.2020 by uuk***
___

    function place_default(x: int, y: int, z: int, sx: int, sy: int, sz: int, blocks: list, replace: list,
            dimension: world.Dimension.Dimension):

    class OrePlacementMode extends enum.Enum

        variable DEFAULT - args: minh, maxh

        variable MIDDLE_HIGHEST - args: minh, maxh, minchance

    class IOre extends world.gen.feature.IFeature.IFeature

        static
        function place(dimension, x, y, z, **config)

        static
        function get_height_range() -> tuple: raise NotImplementedError()
                
                @staticmethod
                def get_ore_block() -> str or list:

        static
        function get_ore_block() -> str or list
            
            :return: an orename or an list of orenames or an {orename: chance} table


        static
        function get_ore_height() -> int: raise NotImplementedError()
                
                
                class INormalOre(IOre):

    class INormalOre extends IOre

        static
        function place(cls, dimension, x, y, z, **config)

        static
        function get_ore_height(cls) -> int

    class CoalOre extends INormalOre

        static
        function get_height_range() -> tuple: return 0, 127
                
                @staticmethod
                def get_ore_block() -> str or list: return "minecraft:coal_ore"
                
                

        static
        function get_ore_block() -> str or list: return "minecraft:coal_ore"
                
                