***Chunk.py - documentation - last updated on 26.7.2020 by uuk***
___

    function chunk2region(cx, cz): return cx >> 5, cz >> 5
            
            
            def access_region_data(savefile, dimension: int, region: tuple):

    function access_region_data(savefile, dimension: int, region: tuple)

    function write_region_data(savefile, dimension, region, data)

    class BlockPartFixer extends mcpython.storage.datafixers.IDataFixer.IPartFixer
        
        Fixer for fixing special block data
        Applied only ONES per block-palette entry, not ones per block. Will change all blocks of the same kind
        in that chunk


        variable TARGET_SERIALIZER_NAME

        variable TARGET_BLOCK_NAME - on which block(s) to apply

        static
        function fix(cls, savefile, dim, region, chunk, data) -> dict
            
            called to apply the fix
            :param savefile: the savefile-instance to use
            :param dim: the dim in
            :param region: the region in
            :param chunk: the chunk in
            :param data: the block data
            :return: the transformed data


    class ChunkDataFixer extends mcpython.storage.datafixers.IDataFixer.IPartFixer
        
        fixer targeting an whole chunk-data dict


        variable TARGET_SERIALIZER_NAME

        static
        function fix(cls, savefile, dim, region, chunk, data) -> dict
            
            will apply the fix
            :param savefile: the savefile to use
            :param dim: the dimension in
            :param region: the region in
            :param chunk: the chunk position
            :param data: the chunk data
            :return: the transformed chunk data


    class RegionDataFixer extends mcpython.storage.datafixers.IDataFixer.IPartFixer
        
        fixer for fixing an whole .region file


        variable TARGET_SERIALIZER_NAME

        static
        function fix(cls, savefile, dim, region, data) -> dict
            
            will apply the fix
            :param savefile: the savefile to use
            :param dim: the dimension in
            :param region: the region in
            :param data: the region data
            :return: the transformed region data


    class BlockRemovalFixer extends mcpython.storage.datafixers.IDataFixer.IPartFixer
        
        Fixer for removing block-data from special blocks from the chunk system
        Will replace the block data with REPLACE (default: air-block)


        variable TARGET_SERIALIZER_NAME

        variable TARGET_BLOCK_NAMES - on which block(s) to apply

        variable REPLACE - the block data to replace with

    class EntityDataFixer extends mcpython.storage.datafixers.IDataFixer.IPartFixer
        
        Fixer for fixing entity data from storage


        variable TARGET_SERIALIZER_NAME

        variable TARGET_ENTITY_NAME - which entity to apply to

        static
        function fix(cls, savefile, dim, region, chunk, data)
            
            will apply the fix
            :param savefile: the savefile to use
            :param dim: the dimension in
            :param region: the region in
            :param chunk: the chunk in
            :param data: the entity data


    class EntityRemovalFixer extends mcpython.storage.datafixers.IDataFixer.IPartFixer
        
        Fixer for removing an entity type from saves


        variable TARGET_SERIALIZER_NAME

        variable TARGET_ENTITY_NAME - which entity to apply to

    class ChunkMapDataFixer extends mcpython.storage.datafixers.IDataFixer.IPartFixer
        
        Fixer for changing the map data of the chunk


        variable TARGET_SERIALIZER_NAME

        static
        function fix(cls, savefile, dim, region, chunk, data)
            
            will apply the fix
            :param savefile: the savefile to use
            :param dim: the dimension in
            :param region: the region in
            :param chunk: the chunk in
            :param data: the map data


    @G.registry class Chunk extends mcpython.storage.serializer.IDataSerializer.IDataSerializer

        variable PART

        static
        function apply_part_fixer(cls, savefile, fixer)

                    variable data

                    variable data

                    variable data

                        variable data[chunk]

                variable blocks

                    variable data

                        variable palette

                                variable palette[i]

                    variable data

                        variable cdata

                    variable data

                        variable cdata

                    variable data

                        variable cdata

        static
        function load(cls, savefile, dimension: int, chunk: tuple, immediate=False)

            variable chunk_instance: mcpython.world.Chunk.Chunk

            variable G.worldgenerationhandler.enable_generation

            variable data

            variable chunk_instance.generated

            variable inv_file

                    variable data["block_palette"][i]

                variable position

                variable d

                function add(blockinstance)

                variable flag

            variable positions

                    variable biome_map

                    variable entity_instance

                variable entity_instance.rotation

                variable entity_instance.harts

            variable chunk_instance.loaded

            variable chunk_instance.is_ready

            variable chunk_instance.visible

            variable G.worldgenerationhandler.enable_generation

        static
        function save(cls, data, savefile, dimension: int, chunk: tuple, override=False)

            variable G.worldgenerationhandler.enable_generation
                when doing stuff, please make sure that nothing fancy happens

            variable palette - list of {"custom": <some stuff>, "name": <name>, "shown": <shown>, ...}
                these section is for dumping block stuff...

            variable inv_file - where to dump inventory stuff

            variable overridden

                variable rel_position

                variable block

                variable block_data

                    variable block_data["inventories"] - create the entry for the data

                            variable overridden

                        variable path - were to locate in the file

                    variable cdata["blocks"][rel_position]

                    variable cdata["blocks"][rel_position]

                variable edata

                variable biome_map - read the biome map ...

                variable positions - an list of all (x, z) in the chunk, for sorting the arrays
                    ... and use it as an template for the following
                    todo: use something else more stable!

                variable landmass_map

                variable cdata["maps"]["minecraft:landmass_map"]

                variable cdata["maps"]["landmass_palette"]

                    variable mass

                        variable index

                        variable index

                variable biome_palette

                variable biomes

                        variable index

                        variable index

                variable cdata["maps"]["biome"]

                variable cdata["maps"]["biome_palette"] - todo: move to global map of biomes

                variable height_map

                variable cdata["maps"]["height"]

            variable data[chunk] - dump the chunk into the region

            variable G.worldgenerationhandler.enable_generation - re-enable world gen as we are finished