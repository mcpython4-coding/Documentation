***PartFixers.py - documentation - last updated on 13.11.2021 by uuk***
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

            variable data

                    variable data[name]

    class GameRuleRemovalFixer extends IPartFixer
        
        Fixer targeting the removal of game-rule data from the save files


        variable TARGET_SERIALIZER_NAME

        variable TARGET_GAMERULE_NAME - which game rules to apply to

            variable data

    class WorldConfigFixer extends IPartFixer
        
        Class representing an fix for the config-entry


        variable TARGET_SERIALIZER_NAME

            variable data

            variable data["config"]

    class WorldGeneralFixer extends IPartFixer
        
        Class representing an fix for the config-entry


        variable TARGET_SERIALIZER_NAME

            variable data

            variable data

    class PlayerDataFixer extends IPartFixer
        
        fixer for fixing player data


        variable TARGET_SERIALIZER_NAME
            
            will apply the fix
            :param savefile: the savefile to use
            :param player: the player used or None if not provided
            :param data: the data used
            :return: the fixed data


            variable data

                variable player_data

                variable player

                variable player_data

                variable data[name]