***ILayer.py - documentation - last updated on 18.11.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class LayerConfig
        
        The configuration object for world generation layers.
        Should be read / written to by the Layers,


        function __init__(self, *config, **attr_config)

            variable self.config

            variable self.layer: typing.Optional["ILayer"]

            variable self.bedrock_chance

            variable self.max_height_factor

            variable self.masses

            variable self.temperature_max

            variable self.temperature_min

        function apply_config(self, attr_config: dict)

    class ILayer extends mcpython.common.event.api.IRegistryContent
        
        Implementation for each layer in generation code.
        A layer is a step in the generation code
        DEPENDS_ON should be a list of other layer names this layer depends on,
        currently not used, but later for parallel world gen (You see that the generation function itself is async)


        variable TYPE

        variable NAME

        variable DEPENDS_ON

        static
        function normalize_config(config: LayerConfig)