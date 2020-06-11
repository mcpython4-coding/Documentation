***DataFixer1to2.py - documentation - last updated on 11.6.2020 by uuk***
___

    @G.registry class DataFixer1to2 extends mcpython.storage.datafixers.IDataFixer.IStorageVersionFixer

        variable NAME

        variable FIXES_FROM

        variable FIXES_TO

        static
        function apply(cls, savefile)

    @G.registry class ChunkDataFixer1to2 extends mcpython.storage.serializer.Chunk.ChunkDataFixer

        variable NAME

        variable FIXES_FROM

        variable FIXES_TO

        static
        function fix(cls, savefile, dimension, region, chunk, cdata)