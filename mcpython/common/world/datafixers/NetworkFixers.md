***NetworkFixers.py - documentation - last updated on 16.1.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractNetworkFixer extends ABC

        variable BEFORE_VERSION: int

        variable AFTER_VERSION: int
            
            Applies this data fixer to a specific object with data
            :param target: the target obj
            :param source_buffer: the source buffer to read from
            :param target_buffer: the buffer to write into, if you want to
            :return: if all data was loaded directly into the block, otherwise, the target_buffer must contain the needed
                    data


    class BlockDataFixer extends AbstractNetworkFixer,  ABC
        
        Handler for fixing block data using network buffers for blocks
        When subclassing and setting BLOCK_NAME to a good block name (a block name found in registry),
        the fixer will be automatically bound to the block class
        Use the Block.NETWORK_BUFFER_DATA_FIXERS for manual registration
        WARNING: returning True from apply2stream() will intercept any further buffer loading, so also the stuff
                you don't need to do yourself, but instead you use await super().read_from_network_buffer(...)


        static
        function __init_subclass__(cls, **kwargs)

    class ItemDataFixer extends AbstractNetworkFixer,  ABC
        
        Handler for fixing item data using network buffers for items
        When subclassing and setting ITEM_NAME to a good item name (a item name found in registry),
        the fixer will be automatically bound to the block class
        Use the Block.NETWORK_BUFFER_DATA_FIXERS for manual registration
        WARNING: returning True from apply2stream() will intercept any further buffer loading, so also the stuff
                you don't need to do yourself, but instead you use await super().read_from_network_buffer(...)


        static
        function __init_subclass__(cls, **kwargs)

    class EntityDataFixer extends AbstractNetworkFixer,  ABC

        static
        function bind(cls, entity_cls)

    class ChunkInfoMapFixer extends AbstractNetworkFixer,  ABC
        
        Handler for fixing chunk data maps


        variable MAP_NAME: str

        static
        function __init_subclass__(cls, **kwargs)

                variable target

                variable target.DATA_FIXERS[cls.BEFORE_VERSION]

    class ContainerDataFixer extends AbstractNetworkFixer,  ABC

        static
        function bind(cls, inventory)

    class ChunkDataFixer extends AbstractNetworkFixer,  ABC

        static
        function __init_subclass__(cls, **kwargs)

            variable Chunk.DATA_FIXERS[cls.BEFORE_VERSION]