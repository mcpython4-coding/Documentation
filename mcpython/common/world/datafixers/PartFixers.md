***PartFixers.py - documentation - last updated on 16.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class GameRuleFixer extends IPartFixer
        
        Fixer targeting one or more game-rule entries


        variable TARGET_SERIALIZER_NAME

        variable TARGET_GAMERULE_NAME - which game rules to apply to

        static
        function fix(cls, save_file, data) -> dict

        static
        function apply(cls, save_file, *args)

    class GameRuleRemovalFixer extends IPartFixer
        
        Fixer targeting the removal of game-rule data from the save files


        variable TARGET_SERIALIZER_NAME

        variable TARGET_GAMERULE_NAME - which game rules to apply to

        static
        function apply(cls, save_file, *args)

    class WorldConfigFixer extends IPartFixer
        
        Class representing an fix for the config-entry


        variable TARGET_SERIALIZER_NAME

        static
        function fix(cls, save_file, data: dict) -> dict

        static
        function apply(cls, save_file, *args)

    class WorldGeneralFixer extends IPartFixer
        
        Class representing an fix for the config-entry


        variable TARGET_SERIALIZER_NAME

        static
        function fix(cls, save_file, data: dict) -> dict

        static
        function apply(cls, save_file, *args)

    class PlayerDataFixer extends IPartFixer
        
        fixer for fixing player data


        variable TARGET_SERIALIZER_NAME

        static
        function fix(cls, savefile, player, data) -> dict
            
            will apply the fix
            :param savefile: the savefile to use
            :param player: the player used or None if not provided
            :param data: the data used
            :return: the fixed data


        static
        function apply(cls, save_file, *args)