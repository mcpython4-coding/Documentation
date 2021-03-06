***CommandEntry.py - documentation - last updated on 8.6.2020 by uuk***
___

    class CommandEntry extends mcpython.event.Registry.IRegistryContent
        
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
            function is_valid(entrylist: list, start: int, arguments, kwargs) -> bool: return entrylist[start] == arguments[0]
                    
                    @G.registry
                    class IntEntry(CommandEntry):

        @G.registry class IntEntry extends CommandEntry
            
            entry for int


            variable NAME

            static
            function parse(entrylist: list, start: int, info, arguments, kwargs) -> tuple: return start + 1, int(entrylist[start])
                    
                    @staticmethod
                    def is_valid(entrylist: list, start: int, arguments, kwargs) -> bool:

            static
            function is_valid(entrylist: list, start: int, arguments, kwargs) -> bool

        @G.registry class StringEntry extends CommandEntry
            
            string entry


            variable NAME

            static
            function parse(entrylist: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entrylist: list, start: int, arguments, kwargs) -> bool

        @G.registry class StringWithoutQuotesEntry extends CommandEntry
            
            string entry


            variable NAME

            static
            function parse(entrylist: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entrylist: list, start: int, arguments, kwargs) -> bool: return True
                    
                    @G.registry
                    class FloatEntry(CommandEntry):

        @G.registry class FloatEntry extends CommandEntry
            
            float entry


            variable NAME

            static
            function parse(entrylist: list, start: int, info, arguments, kwargs) -> tuple: return start + 1, float(entrylist[start])
                    
                    @staticmethod
                    def is_valid(entrylist: list, start: int, arguments, kwargs) -> bool:

            static
            function is_valid(entrylist: list, start: int, arguments, kwargs) -> bool

        @G.registry class BlockNameEntry extends CommandEntry
            
            blockname entry


            variable NAME

            static
            function parse(entrylist: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entrylist: list, start: int, arguments, kwargs) -> bool

        @G.registry class ItemNameEntry extends CommandEntry
            
            itemname entry


            variable NAME

            static
            function parse(entrylist: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entrylist: list, start: int, arguments, kwargs) -> bool

        @G.registry class SelectorEntry extends CommandEntry
            
            Selector entry


            variable NAME

            static
            function parse(entrylist: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entrylist: list, start: int, arguments, kwargs) -> bool

        @G.registry class PositionEntry extends CommandEntry
            
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

        @G.registry class SelectDefinitedStringEntry extends CommandEntry
            
            select definite string entry


            variable NAME

            static
            function parse(entrylist: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entrylist: list, start: int, arguments, kwargs) -> bool

        @G.registry class OpenEndUndefinedStringEntry extends CommandEntry
            
            open end undefined string entry


            variable NAME

            static
            function parse(entrylist: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entrylist: list, start: int, arguments, kwargs) -> bool

        @G.registry class BooleanEntry extends CommandEntry

            variable TABLE

            variable NAME

            static
            function parse(entrylist: list, start: int, info, arguments, kwargs) -> tuple

            static
            function is_valid(entrylist: list, start: int, arguments, kwargs) -> bool