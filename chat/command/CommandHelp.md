***CommandHelp.py - documentation - last updated on 14.5.2020 by uuk***
___

    @G.registry class CommandHelp extends chat.command.Command.Command
        
        class for /help command


        variable NAME

        static function insert_parse_bridge(parsebridge: ParseBridge)

        static function parse(values: list, modes: list, info)

        static function get_help() -> list

    variable PAGES
        generate help pages

        variable h

    variable LINES_PER_PAGE - an internal config, can be changed