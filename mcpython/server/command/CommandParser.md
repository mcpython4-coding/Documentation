***CommandParser.py - documentation - last updated on 27.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class ParsingCommandInfo
        
        Info which stores information about the active executed command
        Shared across commands wherever possible
        todo: add reset system, so we don't need to copy every time


        function __init__(self, entity=None, position=None, dimension=None, chat=None)

            variable self.entity

            variable self.position

            variable self.dimension

            variable self.local_variable_stack
                for the future... todo: implement this
                this will hold local variables
                /execute store target-able and /execute set <name> <value> able
                /execute if/unless var <name> defined
                /execute if/unless var <name> >/</>=/<=/==
                /execute with <name> copied <var name>
                /execute with <name> static <value>
                /variable <name> store result <expression>
                /variable <name> store position x/y/z [<selector>/<position>]
                /variable operate <target var> <expression name> <... args>
                /return <value or variable>
                /variable <name> delete
                /variable <name> copy [to/from (default)] <var>
                /function <name> [store <var name>] ...: <param name> copied <var name> / static <value>
                access-able via something like <var name> in commands (-> custom entry parser!)

        function copy(self, include_variables=False) -> "ParsingCommandInfo"
            
            :param include_variables: if the local variable table should be copied
            :return: a copy of itself


                variable instance.local_variable_stack

        function __str__(self)

    class CommandParser
        
        Main class for parsing an command
        todo: can we pre-parse data into python text and eval it? (If we do, we must make it very secure!)


        function __init__(self)

            variable self.command_parsing - start -> (Command, ParseBridge)

        function add_command(self, command: mcpython.server.command.Command)
            
            register an command
            :param command: the command to add


                variable self.command_parsing[entry]

        function parse(self, command: str, info=None)
            
            Parse an command
            :param command: the command to parse
            :param info: the info to use. can be None if one should be generated
            todo: check permission


        function _convert_to_values(
                self, command, syntax, info, index=1
                ) -> typing.Tuple[
                typing.Optional[typing.List],
                typing.Optional[typing.List[typing.Tuple[typing.Any, int]]],
                ]:
                """
                Parse command into values that can be than executed
                :param command: the command to parse
                :param syntax: the command info to use
                :param info: the info to use
                :param index: the index to start on
                :return: a tuple of the parsed values and the nodes iterated over, as (Node, node index)
                """
                if len(command) == 1 and not any(
                [
                subcommand.mode
                == mcpython.server.command.Command.CommandArgumentMode.OPTIONAL
                for subcommand in syntax.nodes
                ]
                ):
            
            Parse command into values that can be than executed
            :param command: the command to parse
            :param syntax: the command info to use
            :param info: the info to use
            :param index: the index to start on
            :return: a tuple of the parsed values and the nodes iterated over, as (Node, node index)


            variable active_entry

            variable values

            variable array

            variable command_registry

                        variable active_entry

    variable shared.command_parser