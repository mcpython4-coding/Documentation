***CommandExecute.py - documentation - last updated on 14.5.2020 by uuk***
___

    @G.registry class CommandExecute extends chat.command.Command.Command
        
        class for /execute command
        


        variable NAME

        static function insert_parse_bridge(parsebridge: ParseBridge)
        static function parse(values: list, modes: list, info)
        static function _parse_subcommand(index, command, values, info)
            
            execute an entry in the parsed command
            :param index: the index to start
            :param command: the parsed active command
            :param values: the values that where parsed
            :param info: the command info which was used
            


                    variable info.entity


                    variable info.position


                variable subcommand: str


                variable flag


                        variable block


                        variable flag


                        variable flag


                    variable selector


                    variable flag

        static function get_help() -> list