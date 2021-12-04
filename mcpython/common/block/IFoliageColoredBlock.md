***IFoliageColoredBlock.py - documentation - last updated on 13.11.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class IFoliageColoredBlock extends mcpython.common.block.AbstractBlock.AbstractBlock
        
        Base class for foliage colored blocks


        function get_tint_for_index(
                self, index: int
                ) -> typing.Tuple[float, float, float, float]:

            variable biome_map

            variable biome_name

            variable biome