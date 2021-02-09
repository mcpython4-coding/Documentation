***GameRule.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class GameRuleFixer extends mcpython.common.world.datafixers.IDataFixer.IPartFixer
        
        Fixer targeting one or more game-rule entries


        variable TARGET_SERIALIZER_NAME

        variable TARGET_GAMERULE_NAME - which game rules to apply to

        static
        function fix(cls, save_file, data) -> dict

    class GameRuleRemovalFixer extends mcpython.common.world.datafixers.IDataFixer.IPartFixer
        
        Fixer targeting the removal of game-rule data from the save files


        variable TARGET_SERIALIZER_NAME

        variable TARGET_GAMERULE_NAME - which game rules to apply to

    @shared.registry class GameRule extends mcpython.common.world.serializer.IDataSerializer.IDataSerializer

        variable PART

        static
        function apply_part_fixer(cls, save_file, fixer)

        static
        function load(cls, save_file)

        static
        function save(cls, data, save_file)