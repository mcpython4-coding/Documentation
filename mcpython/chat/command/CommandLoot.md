***CommandLoot.py - documentation - last updated on 8.6.2020 by uuk***
___

    @G.registry class CommandLoot extends mcpython.chat.command.Command.Command
        
        command /loot


        variable NAME

        variable CANCEL_CLEAR - cancel the clear-execute

        static
        function insert_parse_bridge(parsebridge: ParseBridge)

        static
        function parse(cls, values: list, modes: list, info)

        static
        function get_help() -> list