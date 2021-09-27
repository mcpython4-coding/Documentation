***util.py - documentation - last updated on 27.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class BlockSource
        
        Helper class for working with blocks
        Contains a list of blocks
        Used for getting and matching blocks
        todo: something global for defining states for block creation


        static
        function from_any(cls, block: typing.Union[str, "BlockSource"]) -> "BlockSource"

        function __init__(self)

            variable self.blocks

        function with_block(self, block: typing.Optional[str])

        function get(self)

        function contains(self, instance) -> bool

        function copy(self)

    class AnyBlock extends BlockSource
        
        Matcher matching any block


        variable INSTANCE: typing.Optional["AnyBlock"]

        function __init__(self, excludes=None)

            variable self.excludes

        function get(self)

        function contains(self, instance) -> bool

        function with_block(self, block: str)

        function copy(self)

    variable AnyBlock.INSTANCE

    function filter_values(
            data: typing.Dict, matcher: BlockSource, inverted=False, to="minecraft:air"
            ):
        
        In-place dict value filter using a block source matcher
        :param data: the data, as a dict of any -> matchable
        :param matcher: the BlockSource instance
        :param inverted: if inverted or not
        :param to: what to filter to, so which block to replace with


                variable data[key]

    function filter_list(
            data: typing.List, matcher: BlockSource, inverted=False, to="minecraft:air"
            ):
        
        Filters a list-like structure of block-like elements
        :param data: the list-like
        :param matcher: the matcher
        :param inverted: if inverted
        :param to: filter to


                variable data[i]

    function area_iterator(start: typing.Tuple[int, int, int], end: typing.Tuple[int, int, int])

    function fill_area(
            access: mcpython.engine.world.AbstractInterface.ISupportWorldInterface,
            start: typing.Tuple[int, int, int],
            end: typing.Tuple[int, int, int],
            block: typing.Union[str, BlockSource],
            ):

        variable block

    function fill_area_replacing(
            access: mcpython.engine.world.AbstractInterface.ISupportWorldInterface,
            start: typing.Tuple[int, int, int],
            end: typing.Tuple[int, int, int],
            block: typing.Union[str, BlockSource],
            replacing: typing.Union[str, BlockSource],
            ):

        variable block

        variable replacing

            variable previous

    function get_content(
            access: mcpython.engine.world.AbstractInterface.ISupportWorldInterface,
            start: typing.Tuple[int, int, int],
            end: typing.Tuple[int, int, int],
            ) -> typing.Dict[typing.Tuple[int, int, int], typing.Any]:

        variable data

            variable b

                variable b

            variable data[

    function get_content_list(
            access: mcpython.engine.world.AbstractInterface.ISupportWorldInterface,
            start: typing.Tuple[int, int, int],
            end: typing.Tuple[int, int, int],
            ) -> typing.Iterable:

            variable b

                variable b

    function paste_content(
            access: mcpython.engine.world.AbstractInterface.ISupportWorldInterface,
            start: typing.Tuple[int, int, int],
            data: typing.Dict[typing.Tuple[int, int, int], typing.Any],
            insert_air=True,
            replaces=AnyBlock.INSTANCE,
            ):

        variable replaces

        variable start

            variable p2

    function paste_content_list(
            access: mcpython.engine.world.AbstractInterface.ISupportWorldInterface,
            start: typing.Tuple[int, int, int],
            end: typing.Tuple[int, int, int],
            data: typing.List[typing.Any],
            insert_air=True,
            replaces=AnyBlock.INSTANCE,
            ):

        variable replaces

            variable p2

    function clone(
            access: mcpython.engine.world.AbstractInterface.ISupportWorldInterface,
            start: typing.Tuple[int, int, int],
            end: typing.Tuple[int, int, int],
            to: typing.Tuple[int, int, int],
            block_filter=AnyBlock.INSTANCE,
            replaces=AnyBlock.INSTANCE,
            insert_air=True,
            remove_start=False,
            ):

        variable replaces

        variable block_filter

        variable block_list

        variable block_list

    function create_hollow_structure(
            access: mcpython.engine.world.AbstractInterface.ISupportWorldInterface,
            start: typing.Tuple[int, int, int],
            end: typing.Tuple[int, int, int],
            block: typing.Union[str, BlockSource],
            outline_size=1,
            fill_center=False,
            fill_center_with=None,
            ):
        
        Creates a hollow structure
        :param access: the world-like object
        :param start: the start
        :param end: the end
        :param block: the block
        :param outline_size: the width of the structure
        :param fill_center: if the center should be filled
        :param fill_center_with: with this block


        variable block

        variable fill_center_with