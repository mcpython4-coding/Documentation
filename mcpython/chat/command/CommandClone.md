***CommandClone.py - documentation - last updated on 24.6.2020 by uuk***
___

    @G.registry class CommandClone extends mcpython.chat.command.Command.Command
        
        Class for the /clone command
        events:
            - command:clone:block_map(ParsingCommandInfo, dict): called when data is collected together with the data table


        variable NAME

        static
        function insert_parse_bridge(parsebridge: ParseBridge)

        static
        function parse(values: list, modes: list, info)

            variable block_map - the map holding the blocks to clone

            variable dimension

                        variable chunk

                        variable block - and get the real block

                variable chunk

                    variable block

        static
        function get_help() -> list