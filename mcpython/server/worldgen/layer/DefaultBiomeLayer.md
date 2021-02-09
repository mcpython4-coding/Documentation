***DefaultBiomeLayer.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
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