***DefaultTopLayerLayer.py - documentation - last updated on 10.1.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @shared.world_generation_handler class DefaultTopLayerLayer extends ILayer

        variable NAME

        variable DEPENDS_ON

        variable noise

            variable chunk

            variable noise_map

            variable height_map

            variable biome_map

                    variable biome

        static
        function generate_xz(reference, x, z, config, noise_value, world_height, biome)

            variable r

            variable height

            variable decorators

                variable y

                variable block