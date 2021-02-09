***DefaultFeatureLayer.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
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