***IOre.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    function place_default(
            x: int,
            y: int,
            z: int,
            sx: int,
            sy: int,
            sz: int,
            blocks: list,
            replace: list,
            dimension: mcpython.common.world.AbstractInterface.IDimension,
            ):

                        variable block

                        variable name

    class OrePlacementMode extends enum.Enum

        variable DEFAULT - args: minh, maxh

        variable MIDDLE_HIGHEST - args: minh, maxh, minchance

    class IOre extends mcpython.server.worldgen.feature.IFeature.IFeature

        static
        function place(dimension, x, y, z, **config)

        static
        function get_height_range() -> tuple

        static
        function get_ore_block() -> str or list
            
            :return: an orename or an list of orenames or an {orename: chance} table


        static
        function get_replacement_blocks()

        static
        function get_size_range() -> tuple

        static
        function get_chunk_count() -> int

        static
        function get_ore_height() -> int

    class INormalOre extends IOre,  ABC

        static
        function place(cls, dimension, x, y, z, **config)

        static
        function get_ore_height(cls) -> int

    class CoalOre extends INormalOre

        static
        function get_size_range() -> tuple

        static
        function get_chunk_count() -> int

        static
        function get_height_range() -> tuple

        static
        function get_ore_block() -> str or list

    @shared.registry class DefaultOreFeature extends mcpython.server.worldgen.feature.IFeature.IFeature

        variable NAME

    @shared.registry class DefaultEmeraldFeature extends mcpython.server.worldgen.feature.IFeature.IFeature

        variable NAME

    @shared.registry class DefaultInfestedStoneFeature extends mcpython.server.worldgen.feature.IFeature.IFeature

        variable NAME