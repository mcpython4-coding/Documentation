***CommandRecipeView.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @shared.registry class CommandRecipeView extends mcpython.server.command.Command.Command
        
        Class for the /recipeview command


        variable NAME

        variable INVENTORY

        static
        function insert_command_syntax_holder(command_syntax_holder: CommandSyntaxHolder)

        static
        function parse(cls, values: list, modes: list, info)

            variable recipe

        static
        function get_help() -> list