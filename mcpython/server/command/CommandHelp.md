***CommandHelp.py - documentation - last updated on 25.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    @shared.registry class CommandHelp extends mcpython.server.command.Command.Command
        
        class for /help command


        variable NAME

        static
        function insert_parse_bridge(parse_bridge: ParseBridge)

        static
        function parse(values: list, modes: list, info)

        static
        function get_help() -> list

    variable PAGES
        generate help pages  todo: change to an loading stage

        variable h

    variable LINES_PER_PAGE - an internal config, can be changed