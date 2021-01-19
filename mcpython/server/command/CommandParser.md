***CommandParser.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class ParsingCommandInfo
        
        info which stores information about the active executed command


        function __init__(self, entity=None, position=None, dimension=None, chat=None)

            variable self.entity

            variable self.position

            variable self.dimension

        function copy(self)
            
            :return: a copy of itself


        function __str__(self)

    class CommandParser
        
        main class for parsing an command


        function __init__(self)

            variable self.commandparsing - start -> (Command, ParseBridge)

        function add_command(self, command: mcpython.server.command.Command)
            
            register an command
            :param command: the command to add


        function parse(self, command: str, info=None)
            
            pase an command
            :param command: the command to parse
            :param info: the info to use. can be None if one should be generated
            todo: check permission


        function _convert_to_values(self, command, parsebridge, info, index=1) -> tuple
            
            parse command into values that can be than executed
            :param command: the command to parse
            :param parsebridge: the command info to use
            :param info: the info to use
            :param index: the index to start on


    variable shared.command_parser