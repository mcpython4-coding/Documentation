***IWorldGenConfig.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
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

        static
        function get_biome_at(cls, x, z, noises, landmass, config, temperature) -> str

        static
        function get_creation_args(cls) -> typing.Tuple

    class IWorldGenConfig extends mcpython.common.data.DataSerializerHandler.ISerializeAble

        variable SERIALIZER

        variable NAME

        variable DIMENSION

        variable DISPLAY_NAME

        variable BIOMES

        variable BIOME_SOURCE: typing.Type[IBiomeSource]

        variable LANDMASSES

        variable LAYERS

        variable GENERATES_START_CHEST

        variable CONFIGURATION_STATE_INSTANCE
            A lazy mcpython.client.state.worldgen.AbstractWorldGeneration.AbstractState for usage for configuration
            todo: use this API and display it correctly
            todo: add serialization config
            todo: store configured object for later usage

        static
        function on_chunk_prepare_generation(
                cls,
                chunk: mcpython.common.world.AbstractInterface.IChunk,
                array: mcpython.server.worldgen.WorldGenerationTaskArrays.WorldGenerationTaskHandlerReference,
                ):

        static
        function on_chunk_generation_finished(
                cls, chunk: mcpython.common.world.AbstractInterface.IChunk
                ):