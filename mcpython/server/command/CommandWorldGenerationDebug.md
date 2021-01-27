***CommandWorldGenerationDebug.py - documentation - last updated on 27.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    @shared.registry class CommandWorldGenDebug extends mcpython.server.command.Command.Command
        
        Class for the /worldgendebug command


        variable NAME

        static
        function insert_command_syntax_holder(command_syntax_holder: CommandSyntaxHolder)

        static
        function parse(cls, values: list, modes: list, info)

                function ping(context)

        static
        function get_help() -> list