***CommandParser.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class CommandExecutionEnvironment

        function __init__(
                self,
                position: typing.Tuple[float, float, float] = None,
                dimension: IDimension = None,
                this=None,
                ):

            variable dimension: IDimension

            variable self.position

            variable self.dimension

            variable self.this

            variable self.chat

        function get_dimension(self)

        function get_current_chunk(self)

        function with_dimension(self, dimension)

        function get_position(self)

        function with_position(self, position)

        function get_this(self)

        function with_this(self, this)

        function copy(self)

    class CommandParser

        function __init__(self)

            variable parsed

        function parse(self, string: str)

            variable command

                variable node

        function register_command(self, command: mcpython.server.command.Builder.Command)
            
            Helper method for registering a command into the system
            :param command: the command instance


            variable self.commands[command.name.removeprefix("/")]

                variable instance

                variable instance.following_nodes

    variable shared.command_parser

        variable handler: CommandParser