***CommandEntry.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class CommandEntry extends mcpython.common.event.Registry.IRegistryContent
        
        A parse-able command entry


        variable TYPE

        static
        function parse(entry_list: list, start: int, info, arguments, kwargs) -> tuple
            
            parse an entry in entry list to an value
            :param entry_list: the entries to parse
            :param start: which entry to start at
            :param info: the command info to use
            :param arguments: handed over creation arguments
            :param kwargs: handed over optional creative arguments
            :return: an (new start, value)-tuple


        static
        function is_valid(entry_list: list, start: int, arguments, kwargs) -> bool
            
            checks if entry is valid
            :param entry_list: the entries to check
            :param start: which entry to start at
            :param arguments: handed over creation arguments
            :param kwargs: handed over optional creation arguments
            :return: if entry is valid, as a bool


    function load()
            
            Entry for definite string


            variable NAME

            static
            function parse(entry_list: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entry_list: list, start: int, arguments, kwargs) -> bool

        @shared.registry class IntEntry extends CommandEntry
            
            Entry for int


            variable NAME

            static
            function parse(entry_list: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entry_list: list, start: int, arguments, kwargs) -> bool

        @shared.registry class StringEntry extends CommandEntry
            
            String entry


            variable NAME

            static
            function parse(entry_list: list, start: int, info, arguments, kwargs) -> tuple

                    variable data

                        variable data

            static
            function is_valid(entry_list: list, start: int, arguments, kwargs) -> bool

        @shared.registry class StringWithoutQuotesEntry extends CommandEntry
            
            string entry


            variable NAME

            static
            function parse(entry_list: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entry_list: list, start: int, arguments, kwargs) -> bool

        @shared.registry class FloatEntry extends CommandEntry
            
            float entry


            variable NAME

            static
            function parse(entry_list: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entry_list: list, start: int, arguments, kwargs) -> bool

        @shared.registry class BlockNameEntry extends CommandEntry
            
            blockname entry


            variable NAME

            static
            function parse(entry_list: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entry_list: list, start: int, arguments, kwargs) -> bool

        @shared.registry class ItemNameEntry extends CommandEntry
            
            Item name entry


            variable NAME

            static
            function parse(entry_list: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entry_list: list, start: int, arguments, kwargs) -> bool

        @shared.registry class DimensionNameEntry extends CommandEntry
            
            Dimension name entry


            variable NAME

            static
            function parse(entry_list: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entry_list: list, start: int, arguments, kwargs) -> bool

        @shared.registry class SelectorEntry extends CommandEntry
            
            Selector entry


            variable NAME

            static
            function parse(entry_list: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entry_list: list, start: int, arguments, kwargs) -> bool

        @shared.registry class PositionEntry extends CommandEntry
            
            Position entry


            variable NAME

            static
            function parse(entry_list: list, start: int, info, arguments, kwargs) -> tuple

            static
            function _parse_coordinate_to_real(r: str, index: int, info) -> float
                
                Parses a coordinate (could be relative) to a valid coordinate
                :param r: the coordinate to use
                :param index: the index in the info position
                :param info: the info to use
                :return: an float value representing this


            static
            function is_valid(entry_list: list, start: int, arguments, kwargs) -> bool

        @shared.registry class SelectDefinedStringEntry extends CommandEntry
            
            Select definite string entry


            variable NAME

            static
            function parse(entry_list: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entry_list: list, start: int, arguments, kwargs) -> bool

        @shared.registry class OpenEndUndefinedStringEntry extends CommandEntry
            
            open end undefined string entry


            variable NAME

            static
            function parse(entry_list: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entry_list: list, start: int, arguments, kwargs) -> bool

        @shared.registry class BooleanEntry extends CommandEntry

            variable TABLE

            variable NAME

            static
            function parse(entry_list: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entry_list: list, start: int, arguments, kwargs) -> bool