***IWorldGenConfig.py - documentation - last updated on 27.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class IBiomeSource

        function get_biome_at(self, x, z, noises, landmass, config, temperature) -> str

        function get_creation_args(self) -> typing.List

    class SingleBiomeSource extends IBiomeSource

        function __init__(self, biome_name: str)

            variable self.biome_name

        function get_biome_at(self, x, z, noises, landmass, config, temperature) -> str

        function get_creation_args(self) -> typing.Tuple

    class DefaultBiomeSource extends IBiomeSource
        
        The default biome source


        static
        function get_biome_at(cls, x, z, noises, landmass, config, temperature) -> str

        static
        function get_creation_args(cls) -> typing.Tuple

    class IWorldGenConfig extends  mcpython.common.data.serializer.DataSerializationManager.ISerializeAble 

        variable SERIALIZER

        variable NAME

        variable DIMENSION

        variable DISPLAY_NAME

        variable BIOMES

        variable BIOME_SOURCE: IBiomeSource

        variable LANDMASSES

        variable LAYERS

        variable GENERATES_START_CHEST

        variable CONFIGURATION_STATE_INSTANCE
            A lazy mcpython.common.state.worldgen.AbstractWorldGeneration.AbstractState for usage for configuration
            todo: use this API and display it correctly
            todo: add serialization config
            todo: store configured object for later usage

        static
        function on_chunk_prepare_generation(
                cls,
                chunk: mcpython.engine.world.AbstractInterface.IChunk,
                array: mcpython.server.worldgen.WorldGenerationTaskArrays.WorldGenerationTaskHandlerReference,
                ):

        static
        function on_chunk_generation_finished(
                cls, chunk: mcpython.engine.world.AbstractInterface.IChunk
                ):