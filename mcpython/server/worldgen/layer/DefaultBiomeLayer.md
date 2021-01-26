***DefaultBiomeLayer.py - documentation - last updated on 26.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    @shared.world_generation_handler class DefaultBiomeMapLayer extends ILayer
        
        Layer for calculating which biomes to generate


        variable NAME

        variable DEPENDS_ON

        variable ]

        static
        function add_generate_functions_to_chunk(cls, config: LayerConfig, reference)

            variable biome_map
                The various chunk maps needed

            variable land_map

            variable temperature_map

                    variable biome_map[