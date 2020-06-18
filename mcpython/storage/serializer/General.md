***General.py - documentation - last updated on 18.6.2020 by uuk***
___

    @G.registry class General extends mcpython.storage.serializer.IDataSerializer.IDataSerializer

        variable PART

        static
        function load(cls, savefile)

            variable savefile.version

            variable playername

            variable G.world.active_player

            variable G.world.config

        static
        function save(cls, data, savefile)