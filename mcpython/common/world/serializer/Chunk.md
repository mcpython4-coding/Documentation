***Chunk.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    function chunk2region(cx, cz)

    function access_region_data(
            save_file,
            dimension: int,
            region: tuple,
            ):

    function write_region_data(
            save_file,
            dimension: int,
            region,
            data,
            ):

    class BlockPartFixer extends mcpython.common.world.datafixers.IDataFixer.IPartFixer
        
        Fixer for fixing special block data
        Applied only ONES per block-palette entry, not ones per block. Will change all blocks of the same kind
        in that chunk


        variable TARGET_SERIALIZER_NAME

        variable TARGET_BLOCK_NAME - on which block(s) to apply

        static
        function fix(
                cls,
                save_file,
                dimension: int,
                region,
                chunk: typing.Tuple[int, int],
                data,
                ) -> dict:
            
            called to apply the fix
            :param save_file: the save-file-instance to use
            :param dimension: the dim in
            :param region: the region in
            :param chunk: the chunk in
            :param data: the block data
            :return: the transformed data


    class ChunkDataFixer extends mcpython.common.world.datafixers.IDataFixer.IPartFixer
        
        Fixer targeting an whole chunk-data dict


        variable TARGET_SERIALIZER_NAME

        static
        function fix(
                cls,
                save_file,
                dimension: int,
                region,
                chunk: typing.Tuple[int, int],
                data,
                ) -> dict:
            
            will apply the fix
            :param save_file: the save-file to use
            :param dimension: the dimension in
            :param region: the region in
            :param chunk: the chunk position
            :param data: the chunk data
            :return: the transformed chunk data


    class RegionDataFixer extends mcpython.common.world.datafixers.IDataFixer.IPartFixer
        
        Fixer for fixing an whole .region file


        variable TARGET_SERIALIZER_NAME

        static
        function fix(
                cls,
                save_file,
                dimension: int,
                region,
                data,
                ) -> dict:
            
            will apply the fix
            :param save_file: the save-file to use
            :param dimension: the dimension in
            :param region: the region in
            :param data: the region data
            :return: the transformed region data


    class BlockRemovalFixer extends mcpython.common.world.datafixers.IDataFixer.IPartFixer
        
        Fixer for removing block-data from special blocks from the chunk system
        Will replace the block data with REPLACE (default: air-block)


        variable TARGET_SERIALIZER_NAME

        variable TARGET_BLOCK_NAMES - on which block(s) to apply

        variable REPLACE

        static
        function on_replace(
                cls,
                save_file,
                dimension: int,
                chunk: typing.Tuple[int, int],
                source,
                target,
                ):

    class EntityDataFixer extends mcpython.common.world.datafixers.IDataFixer.IPartFixer
        
        Fixer for fixing entity data from storage


        variable TARGET_SERIALIZER_NAME

        variable TARGET_ENTITY_NAME - which entity to apply to

        static
        function fix(
                cls,
                save_file,
                dimension: int,
                region,
                chunk: typing.Tuple[int, int],
                data,
                ):
            
            will apply the fix
            :param save_file: the save-file to use
            :param dimension: the dimension in
            :param region: the region in
            :param chunk: the chunk in
            :param data: the entity data


    class EntityRemovalFixer extends mcpython.common.world.datafixers.IDataFixer.IPartFixer
        
        Fixer for removing an entity type from saves


        variable TARGET_SERIALIZER_NAME

        variable TARGET_ENTITY_NAME - which entity to apply to

        static
        function on_replace(
                cls,
                save_file,
                dimension: int,
                chunk: typing.Tuple[int, int],
                previous,
                chunk_data,
                ):

    class ChunkMapDataFixer extends mcpython.common.world.datafixers.IDataFixer.IPartFixer
        
        Fixer for changing the map data of the chunk


        variable TARGET_SERIALIZER_NAME

        static
        function fix(
                cls,
                save_file,
                dimension: int,
                region,
                chunk: typing.Tuple[int, int],
                data,
                ):
            
            will apply the fix
            :param save_file: the save-file to use
            :param dimension: the dimension in
            :param region: the region in
            :param chunk: the chunk in
            :param data: the map data


    @shared.registry class Chunk extends mcpython.common.world.serializer.IDataSerializer.IDataSerializer

        variable PART

        static
        function apply_part_fixer(
                cls,
                save_file,
                fixer: typing.Type[mcpython.common.world.datafixers.IDataFixer.IPartFixer],
                ):

                variable blocks

                    variable data

                        variable palette

                                variable palette[i]

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
        function load(
                cls, save_file, dimension: int, chunk: typing.Tuple[int, int], immediate=False
                ):

            variable region

                variable data

            variable chunk_instance: mcpython.common.world.AbstractInterface.IChunk

            variable shared.world_generation_handler.enable_generation

            variable data

            variable chunk_instance.generated

            variable inv_file

                    variable data["block_palette"][i]

                variable position

                variable d

                function add(instance)

                variable flag

            variable positions

                    variable biome_map

                    variable entity_instance

                variable entity_instance.rotation

                variable entity_instance.harts

            variable chunk_instance.loaded

            variable chunk_instance.is_ready

            variable chunk_instance.visible

            variable shared.world_generation_handler.enable_generation

        static
        function save(cls, data, save_file, dimension: int, chunk: tuple, override=False)

            variable shared.world_generation_handler.enable_generation
                when doing stuff, please make sure that nothing fancy happens

            variable palette
                these section is for dumping block stuff...

            variable inv_file

            variable overridden

                variable rel_position

                variable block

                variable block_data

                    variable block_data["inventories"] - create the entry for the data

                            variable overridden

                        variable path

                    variable cdata["blocks"][rel_position]

                    variable cdata["blocks"][rel_position]

                variable edata

                variable biome_map

                variable positions
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

                variable cdata["maps"][ - todo: move to global map of biomes

                variable height_map

                variable cdata["maps"]["height"]

            variable data[chunk] - dump the chunk into the region

            variable shared.world_generation_handler.enable_generation