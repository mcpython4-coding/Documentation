***PlayerData.py - documentation - last updated on 11.7.2020 by uuk***
___

    class PlayerDataFixer extends mcpython.storage.datafixers.IDataFixer.IPartFixer
        
        fixer for fixing player data


        variable TARGET_SERIALIZER_NAME

        static
        function fix(cls, savefile, player, data) -> dict
            
            will apply the fix
            :param savefile: the savefile to use
            :param player: the player used or None if not provided
            :param data: the data used
            :return: the fixed data


    @G.registry class PlayerData extends mcpython.storage.serializer.IDataSerializer.IDataSerializer

        variable PART

        static
        function apply_part_fixer(cls, savefile, fixer)

        static
        function load(cls, savefile)

        static
        function save(cls, data, savefile)