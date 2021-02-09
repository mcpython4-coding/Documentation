***IFeature.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class IFeatureSpawnPoint

        static
        function select(cls, x, z, gen_height, biome) -> int

    class TopLayerSpawnPoint extends IFeatureSpawnPoint

        static
        function select(cls, x, z, gen_height, biome) -> int

    class FeatureDefinition
        
        Class holding generation rules and config for an IFeature-class.


        function __init__(
                self,
                feature: typing.Type["IFeature"],
                weight: int,
                group: str,
                group_spawn_count: typing.Union[int, typing.Tuple[int, int]] = 1,
                point: typing.Type[IFeatureSpawnPoint] = TopLayerSpawnPoint,
                config=None,
                ):

            variable point: typing.Type[IFeatureSpawnPoint]

            variable self.feature

            variable self.weight

            variable self.group

            variable self.group_spawn_count

            variable self.spawn_point

            variable self.config

    class IFeature extends mcpython.common.event.Registry.IRegistryContent

        variable TYPE

        static
        function place(cls, dimension, x: int, y: int, z: int, config)

        static
        function place_array(
                cls,
                array: mcpython.server.worldgen.WorldGenerationTaskArrays.IWorldGenerationTaskHandlerReference,
                x: int,
                y: int,
                z: int,
                config,
                ):

        static
        function as_feature_definition(
                cls,
                weight: int,
                group: str,
                group_spawn_count: typing.Union[int, typing.Tuple[int, int]] = 1,
                point: typing.Type[IFeatureSpawnPoint] = TopLayerSpawnPoint,
                config=None,
                ) -> FeatureDefinition:

        static
        function as_feature_definition_with_custom_config(
                cls,
                weight: int,
                group: str,
                custom_config: dict,
                group_spawn_count: typing.Union[int, typing.Tuple[int, int]] = 1,
                point: typing.Type[IFeatureSpawnPoint] = TopLayerSpawnPoint,
                config=None,
                ) -> FeatureDefinition: