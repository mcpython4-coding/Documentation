***DefaultFeatureLayer.py - documentation - last updated on 26.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    @shared.world_generation_handler class DefaultFeatureLayer extends ILayer

        variable DEPENDS_ON

        variable NAME

        static
        function add_generate_functions_to_chunk(config: LayerConfig, reference)

        static
        function generate_position(x, z, reference, config)

            variable treemap
                todo: rename to structure blocking info or something similar

            variable biome
                the various maps

            variable height

                    variable count

                    variable feature_def: mcpython.server.worldgen.feature.IFeature.FeatureDefinition
                        Use one random feature todo: make noise based

                    variable feature