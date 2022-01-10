***DefaultHeightMapLayer.py - documentation - last updated on 10.1.2022 by uuk***
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

        variable base_noise

        variable base_noise.merger_config

        variable inter_noise_1

        variable inter_noise_2

        static
        function normalize_config(config: LayerConfig)

            variable chunk

            variable height_map

            variable base_noise_map
                todo: can we optimize this preparation by sending prepared noise values directly to the async part

            variable inter_noise_map_1

            variable inter_noise_map_2

            variable height

                variable total_height

                    variable info

                    variable inter

                    variable info

                variable info