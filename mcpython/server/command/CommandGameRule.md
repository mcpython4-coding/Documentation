***CommandGameRule.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    @shared.registry class CommandGamerule extends mcpython.server.command.Command.Command
        
        class for /gamerule command


        variable NAME

        variable CANCEL_GIVE

        static
        function insert_parse_bridge(parsebridge: ParseBridge)

        static
        function parse(cls, values: list, modes: list, info)

        static
        function get_help() -> list