***DefaultHeightMapLayer.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    @shared.world_generation_handler class DefaultHeightMapLayer extends ILayer

        variable NAME

        variable DEPENDS_ON

        variable noise

        variable noise.merger_config

        static
        function normalize_config(config: LayerConfig)

        static
        function add_generate_functions_to_chunk(cls, config: LayerConfig, reference)

        static
        function get_height_at(cls, config, chunk, x, z, v) -> list