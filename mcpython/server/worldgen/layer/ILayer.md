***ILayer.py - documentation - last updated on 26.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class LayerConfig

        function __init__(self, *config, **attr_config)

            variable self.config

            variable self.layer: typing.Optional["ILayer"]

            variable self.bedrock_chance

            variable self.max_height_factor

            variable self.masses

            variable self.temperature_max

            variable self.temperature_min

        function apply_config(self, attr_config: dict)

    class ILayer extends mcpython.common.event.Registry.IRegistryContent
        
        Implementation for each layer in generation code.
        An layer is an step in the generation code
        DEPENDS_ON should be an list of other layer names this layer depends on,
        currently not used, but later for parallel world gen


        variable DEPENDS_ON

        static
        function normalize_config(config: LayerConfig)

        variable NAME

        static
        function add_generate_functions_to_chunk(config: LayerConfig, reference)