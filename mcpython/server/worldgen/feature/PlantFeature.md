***PlantFeature.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    @shared.registry class PlantFeature extends mcpython.server.worldgen.feature.IFeature.IFeature

        variable NAME

        function __init__(self)

            variable self.plants

        function add_plant(self, plant: str, weight: int)

        static
        function as_feature_definition_with_custom_config(
                cls,
                weight: int,
                group: str,
                custom_config: dict,
                group_spawn_count: typing.Union[int, typing.Tuple[int, int]] = 1,
                point: typing.Type[
                mcpython.server.worldgen.feature.IFeature.IFeatureSpawnPoint
                ] = mcpython.server.worldgen.feature.IFeature.TopLayerSpawnPoint,
                config=None,
                ) -> mcpython.server.worldgen.feature.IFeature.FeatureDefinition:

            variable instance