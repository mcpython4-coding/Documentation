***DefaultHeightMapLayer.py - documentation - last updated on 13.11.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @shared.world_generation_handler class DefaultHeightMapLayer extends ILayer

        variable NAME

        variable DEPENDS_ON

        variable noise

        variable noise.merger_config

        static
        function normalize_config(config: LayerConfig)

            variable chunk

            variable height_map

            variable biome_map

            variable noise_map

        static
        function get_height_at(cls, config, chunk, x, z, v, biome_map) -> list