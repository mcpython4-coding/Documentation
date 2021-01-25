***CommandParser.py - documentation - last updated on 25.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class ParsingCommandInfo
        
        info which stores information about the active executed command


        function __init__(self, entity=None, position=None, dimension=None, chat=None)

            variable self.entity

            variable self.position

            variable self.dimension

            variable self.local_variable_stack
                for the future... todo: implement this
                this will hold local variables
                /execute store target-able and /execute set <name> <value> able
                /execute if var <name> defined
                /execute if var <name> >/</>=/<=/==
                /variable <name> store result <expression>
                /variable <name> store position x/y/z [<selector>/<position>]
                /operation target <expression name> <... args>
                /return <value or variable>
                /variable <name> delete
                /variable <name> copy [to/from (default)] <var>
                access-able via something like <var name> in commands (-> custom entry parser!)

        function copy(self)
            
            :return: a copy of itself


        function __str__(self)

    class CommandParser
        
        Main class for parsing an command
        todo: can we pre-parse data into python text and eval it? (If we do, we must make it very secure!)


        function __init__(self)

            variable self.command_parsing - start -> (Command, ParseBridge)

        function add_command(self, command: mcpython.server.command.Command)
            
            register an command
            :param command: the command to add


        function parse(self, command: str, info=None)
            
            Parse an command
            :param command: the command to parse
            :param info: the info to use. can be None if one should be generated
            todo: check permission


        function _convert_to_values(self, command, parse_bridge, info, index=1) -> tuple
            
            parse command into values that can be than executed
            :param command: the command to parse
            :param parse_bridge: the command info to use
            :param info: the info to use
            :param index: the index to start on


    variable shared.command_parser