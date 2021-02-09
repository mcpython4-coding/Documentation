***PlantFeature.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
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