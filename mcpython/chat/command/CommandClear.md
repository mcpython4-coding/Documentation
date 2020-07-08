***CommandClear.py - documentation - last updated on 24.6.2020 by uuk***
___

    @G.registry class CommandClear extends mcpython.chat.command.Command.Command
        
        Class for the /clear command
        events:
            - command:clear(CancelAbleEvent, ParsingCommandInfo): called when /clear is executed
            - command:clear:entity(CancelAbleEvent, ParsingCommandInfo, Entity): called for every entity affected by /clear.
                Will cancel /clear only for THIS entity
            - command:clear:finish(ParsingCommandInfo): called by command "/clear" on end of clearing inventory
            removed:
            - command:clear:start & command:clear:end


        variable NAME

        static
        function insert_parse_bridge(parsebridge: ParseBridge)

        static
        function parse(cls, values: list, modes: list, info)

        static
        function get_help() -> list