***General.py - documentation - last updated on 20.6.2020 by uuk***
___

    class WorldConfigFixer extends mcpython.storage.datafixers.IDataFixer.IPartFixer
        
        Class representing an fix for the config-entry


        variable TARGET_SERIALIZER_NAME

        static
        function fix(cls, savefile, data: dict) -> dict

    @G.registry class General extends mcpython.storage.serializer.IDataSerializer.IDataSerializer

        variable PART

        static
        function apply_part_fixer(cls, savefile, fixer)

            variable data

            variable data["config"]

        static
        function load(cls, savefile)

            variable savefile.version

            variable playername

            variable G.world.active_player

            variable G.world.config

        static
        function save(cls, data, savefile)