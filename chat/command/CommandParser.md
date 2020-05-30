***CommandParser.py - documentation - last updated on 30.5.2020 by uuk***
___

    class ParsingCommandInfo
        
        info which stores information about the active executed command


        function __init__(self, entity=None, position=None, dimension=None)

            variable self.entity

            variable self.position

            variable self.dimension

        function copy(self)
            
            :return: a copy of itself


    class CommandParser
        
        main class for parsing an command


        function __init__(self)

            variable self.commandparsing - start -> (Command, ParseBridge)

            variable self.CANCEL_REGISTER

            variable self.CANCEL_COMMAND_EXECUTE

        function add_command(self, command: chat.command.Command)
            
            register an command
            :param command: the command to add


        function parse(self, command: str, info=None)
            
            pase an command
            :param command: the command to parse
            :param info: the info to use. can be None if one should be generated


        function _convert_to_values(self, command, parsebridge, info, index=1) -> tuple
            
            parse command into values that can be than executed
            :param command: the command to parse
            :param parsebridge: the command info to use
            :param info: the info to use
            :param index: the index to start on


    variable G.commandparser