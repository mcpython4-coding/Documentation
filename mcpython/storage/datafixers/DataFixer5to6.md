***DataFixer5to6.py - documentation - last updated on 11.6.2020 by uuk***
___

    @G.registry class DataFixer5to6 extends mcpython.storage.datafixers.IDataFixer.IStorageVersionFixer

        variable NAME

        variable FIXES_FROM

        variable FIXES_TO

        static
        function apply(cls, savefile)

    @G.registry class RegionDataFixer5to6 extends mcpython.storage.serializer.Chunk.RegionDataFixer

        variable NAME

        static
        function fix(cls, savefile, dimension, region, data)