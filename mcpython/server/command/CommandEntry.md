***CommandEntry.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class CommandEntry extends mcpython.common.event.Registry.IRegistryContent
        
        an parseable command entry


        variable TYPE

        static
        function parse(entrylist: list, start: int, info, arguments, kwargs) -> tuple
            
            parse an entry in entrylist to an value
            :param entrylist: the entrys to parse
            :param start: which entry to start at
            :param info: the command info to use
            :param arguments: overgiven creation arguments
            :param kwargs: overgiven optional creative arguments
            :return: an (new start, value)-tuple


        static
        function is_valid(entrylist: list, start: int, arguments, kwargs) -> bool
            
            checks if entry is valid
            :param entrylist: the entrys to check
            :param start: which entry to start at
            :param arguments: overgiven creation arguments
            :param kwargs: overgiven optional creation arguments
            :return: if entry is valid


    function load()
            
            Entry for definite string


            variable NAME

            static
            function parse(entrylist: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entrylist: list, start: int, arguments, kwargs) -> bool

        @shared.registry class IntEntry extends CommandEntry
            
            entry for int


            variable NAME

            static
            function parse(entrylist: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entrylist: list, start: int, arguments, kwargs) -> bool

        @shared.registry class StringEntry extends CommandEntry
            
            string entry


            variable NAME

            static
            function parse(entrylist: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entrylist: list, start: int, arguments, kwargs) -> bool

        @shared.registry class StringWithoutQuotesEntry extends CommandEntry
            
            string entry


            variable NAME

            static
            function parse(entrylist: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entrylist: list, start: int, arguments, kwargs) -> bool

        @shared.registry class FloatEntry extends CommandEntry
            
            float entry


            variable NAME

            static
            function parse(entrylist: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entrylist: list, start: int, arguments, kwargs) -> bool

        @shared.registry class BlockNameEntry extends CommandEntry
            
            blockname entry


            variable NAME

            static
            function parse(entrylist: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entrylist: list, start: int, arguments, kwargs) -> bool

        @shared.registry class ItemNameEntry extends CommandEntry
            
            itemname entry


            variable NAME

            static
            function parse(entrylist: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entrylist: list, start: int, arguments, kwargs) -> bool

        @shared.registry class SelectorEntry extends CommandEntry
            
            Selector entry


            variable NAME

            static
            function parse(entrylist: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entrylist: list, start: int, arguments, kwargs) -> bool

        @shared.registry class PositionEntry extends CommandEntry
            
            position entry


            variable NAME

            static
            function parse(entrylist: list, start: int, info, arguments, kwargs) -> tuple

            static
            function _parse_coordinate_to_real(r: str, index: int, info) -> float
                
                parse an coordinate (could be relative) to an valid coordinate
                :param r: the coordinate to use
                :param index: the index in the info position
                :param info: the info to use
                :return: an float value representing this


            static
            function is_valid(entrylist: list, start: int, arguments, kwargs) -> bool

        @shared.registry class SelectDefinitedStringEntry extends CommandEntry
            
            select definite string entry


            variable NAME

            static
            function parse(entrylist: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entrylist: list, start: int, arguments, kwargs) -> bool

        @shared.registry class OpenEndUndefinedStringEntry extends CommandEntry
            
            open end undefined string entry


            variable NAME

            static
            function parse(entrylist: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entrylist: list, start: int, arguments, kwargs) -> bool

        @shared.registry class BooleanEntry extends CommandEntry

            variable TABLE

            variable NAME

            static
            function parse(entrylist: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entrylist: list, start: int, arguments, kwargs) -> bool