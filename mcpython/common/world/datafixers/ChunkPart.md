***ChunkPart.py - documentation - last updated on 16.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class BlockPartFixer extends IPartFixer
        
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


        static
        function apply(cls, save_file, *args, **kwargs)

    class ChunkDataFixer extends IPartFixer
        
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


        static
        function apply(cls, save_file, *args)

    class RegionDataFixer extends IPartFixer
        
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


        static
        function apply(cls, save_file, *args)

    class BlockRemovalFixer extends IPartFixer
        
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

        static
        function apply(cls, save_file, *args)

    class EntityDataFixer extends IPartFixer
        
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


        static
        function apply(cls, save_file, *args)

    class EntityRemovalFixer extends IPartFixer
        
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

        static
        function apply(cls, save_file, *args)

    class ChunkMapDataFixer extends IPartFixer
        
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


        static
        function apply(cls, save_file, *args)