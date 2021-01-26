***DefaultTopLayerLayer.py - documentation - last updated on 26.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    @shared.world_generation_handler class DefaultTopLayerLayer extends ILayer

        variable NAME

        variable DEPENDS_ON

        variable noise

        static
        function add_generate_functions_to_chunk(cls, config: LayerConfig, reference)

            variable heightmap

            variable biome_map

                variable world_height

                variable biome

        static
        function generate_xz(reference, x, z, config, noise_value, world_height, biome)

            variable r

            variable height

            variable decorators

                variable y

                variable block