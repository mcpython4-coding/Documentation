***CommandClear.py - documentation - last updated on 14.5.2020 by uuk***
___

    @G.registry class CommandClear extends chat.command.Command.Command
        
        command /clear
        


        variable NAME


        variable CANCEL_CLEAR - cancel the clear-execute

        static function insert_parse_bridge(parsebridge: ParseBridge)
        static function parse(cls, values: list, modes: list, info)
        static function get_help() -> list