***LandMassMap.py - documentation - last updated on 16.1.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class LandMassMap extends mcpython.server.worldgen.map.AbstractChunkInfoMap.AbstractMap
        
        Class storing which land mass we are in
        todo: migrate to biome map


        variable NAME

        function __init__(self, chunk: IChunk)

            variable self.land_mass_table

            variable self.reference_table

            variable self.land_mass_table[:]

            variable self.reference_table[:]

        function get_at_xz(self, x: int, z: int) -> str

        function set_at_xz(self, x: int, z: int, mass: str)

        function dump_debug_info(self, file: str)