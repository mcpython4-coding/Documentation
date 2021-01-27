***CommandExecute.py - documentation - last updated on 27.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    @shared.registry class CommandExecute extends mcpython.server.command.Command.Command
        
        Class for /execute command


        variable EXECUTE_NODES

        variable EXECUTE_END_NODES

        variable SPECIAL_NODE_PARSING

        variable NAME

        static
        function insert_command_syntax_holder(cls, command_syntax_holder: CommandSyntaxHolder)

            variable command_syntax_holder.main_entry

            variable followed

            variable old

            variable cls.EXECUTE_NODES["unless"].nodes

        static
        function parse(values: list, modes: list, info)

        static
        function _parse_subcommand(cls, index: int, command: str, values: typing.List, info)
            
            Execute an entry in the parsed command
            :param index: the index to start
            :param command: the parsed active command
            :param values: the values that where parsed
            :param info: the command info which was used
            Mods adding custom entries should use the SPECIAL_NODE_PARSING extension point for parsing their entries


                    variable info.entity

                    variable info.position

                variable subcommand: str

                variable flag

                        variable block

                        variable flag

                        variable flag

                    variable selector

                    variable flag

                        variable flag

                        variable flag
                            todo: make more safe

                variable info.dimension

        static
        function get_help() -> list