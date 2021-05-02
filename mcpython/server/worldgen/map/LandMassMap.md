***LandMassMap.py - documentation - last updated on 2.5.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @shared.world_generation_handler class LandMassMap extends mcpython.server.worldgen.map.AbstractChunkInfoMap.AbstractMap

        variable NAME

        function __init__(self, chunk)

        function load_from_saves(self, data)

            variable previous_mass

                    variable index

                        variable previous_mass

        function dump_for_saves(self)

            variable previous_mass

                    variable mass

        function get_at_xz(self, x: int, z: int) -> str

        function set_at_xz(self, x: int, z: int, mass: str)

        function dump_debug_info(self, file: str)