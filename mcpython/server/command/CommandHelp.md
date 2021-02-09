***CommandHelp.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @shared.registry class CommandHelp extends mcpython.server.command.Command.Command
        
        class for /help command


        variable NAME

        static
        function insert_command_syntax_holder(command_syntax_holder: CommandSyntaxHolder)

        static
        function parse(values: list, modes: list, info)

        static
        function get_help() -> list

    variable PAGES
        generate help pages  todo: change to an loading stage

        variable h

    variable LINES_PER_PAGE - an internal config, can be changed