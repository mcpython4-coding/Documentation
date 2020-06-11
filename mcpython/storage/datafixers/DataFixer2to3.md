***DataFixer2to3.py - documentation - last updated on 11.6.2020 by uuk***
___

    @G.registry class DataFixer2to3 extends mcpython.storage.datafixers.IDataFixer.IStorageVersionFixer

        variable NAME

        variable FIXES_FROM

        variable FIXES_TO

        static
        function apply(cls, savefile)

    @G.registry class ChunkFixer2to3 extends mcpython.storage.serializer.Chunk.BlockPartFixer

        variable NAME

        variable TARGET_BLOCK_NAME

        static
        function fix(cls, savefile, dimension, region, chunk, palette)