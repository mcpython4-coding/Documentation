***GameRule.py - documentation - last updated on 11.6.2020 by uuk***
___

    class GameRuleFixer extends mcpython.storage.datafixers.IDataFixer.IPartFixer
        
        Fixer targeting one or more game-rule entries


        variable TARGET_SERIALIZER_NAME

        variable TARGET_GAMERULE_NAME - which game rules to apply to

        static
        function fix(cls, savefile, data) -> dict

    class GameRuleRemovalFixer extends mcpython.storage.datafixers.IDataFixer.IPartFixer
        
        Fixer targeting the removal of game-rule data from the save files


        variable TARGET_SERIALIZER_NAME

        variable TARGET_GAMERULE_NAME - which game rules to apply to

    @G.registry class GameRule extends mcpython.storage.serializer.IDataSerializer.IDataSerializer

        variable PART

        static
        function apply_part_fixer(cls, savefile, fixer)

        static
        function load(cls, savefile)

        static
        function save(cls, data, savefile)