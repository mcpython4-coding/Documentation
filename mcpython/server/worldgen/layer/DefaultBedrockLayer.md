***DefaultBedrockLayer.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    @shared.world_generation_handler class DefaultBedrockLayer extends ILayer
        
        Class for generating the bedrock layer


        variable NAME

        variable noise

        static
        function normalize_config(config: LayerConfig)

        static
        function add_generate_functions_to_chunk(cls, config: LayerConfig, reference)