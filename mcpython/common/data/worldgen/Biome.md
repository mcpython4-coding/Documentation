***Biome.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class ITopLayerConfigurator extends ABC

        function __init__(self, config: dict)

            variable self.config

        function get_top_layer_height_range(
                self,
                position: typing.Tuple[int, int],
                dimension: mcpython.common.world.AbstractInterface.IDimension,
                ) -> typing.Tuple[int, int]:

        function get_top_layer_configuration(
                self,
                height: int,
                position: typing.Tuple[int, int],
                dimension: mcpython.common.world.AbstractInterface.IDimension,
                ) -> typing.List[str]:

    class DefaultTopLayerConfiguration extends ITopLayerConfigurator

        variable NAME

        function __init__(self, config: dict)

            variable flag

            variable self.default_block

                variable self.top_extension

                variable self.bottom_extension

        function get_top_layer_height_range(
                self,
                position: typing.Tuple[int, int],
                dimension: mcpython.common.world.AbstractInterface.IDimension,
                ) -> typing.Tuple[int, int]:

        function get_top_layer_configuration(
                self,
                height: int,
                position: typing.Tuple[int, int],
                dimension: mcpython.common.world.AbstractInterface.IDimension,
                ) -> typing.List[str]:

            variable data

                variable data[: self.bottom_extension[1]]

    class BiomeSerializer extends mcpython.common.data.DataSerializerHandler.ISerializer

        variable COLLECTED

        variable TOP_LAYER_CONFIGURATORS

        static
        function register_helper(cls, obj: typing.Type)

        static
        function deserialize(cls, data: dict) -> typing.Type[ISerializeAble]

            variable layer_config: ITopLayerConfigurator

            class Biome extends mcpython.server.worldgen.biome.Biome.Biome

                variable NAME

                variable PASSIVE_SPAWNS
                    name -> weight, group size

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
                        ):

        static
        function decode_feature(cls, data: dict)

        static
        function serialize(cls, obj: typing.Type[ISerializeAble]) -> dict

        static
        function register(cls, obj: ISerializeAble)

        static
        function clear(cls)

    variable instance

    variable instance.on_deserialize

    variable instance.on_clear