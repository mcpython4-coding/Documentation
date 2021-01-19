***CommandExecute.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    @shared.registry class CommandExecute extends mcpython.server.command.Command.Command
        
        class for /execute command


        variable NAME

        static
        function insert_parse_bridge(parsebridge: ParseBridge)

        static
        function parse(values: list, modes: list, info)

        static
        function _parse_subcommand(index, command, values, info)
            
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

                variable info.dimension

        static
        function get_help() -> list