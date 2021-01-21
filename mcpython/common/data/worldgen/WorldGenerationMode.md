***WorldGenerationMode.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class WorldGenerationModeSerializer extends  mcpython.common.data.DataSerializerHandler.ISerializer 

        variable COLLECTED

        static
        function deserialize(cls, data: dict) -> typing.Type[ISerializeAble]

            class WorldGenMode extends  mcpython.server.worldgen.mode.IWorldGenConfig.IWorldGenConfig 

                variable NAME

                variable DIMENSION

                variable DISPLAY_NAME

                variable biome_data

                variable BIOMES

                variable biome_config

                variable BIOME_SOURCE

                variable LANDMASSES

                variable LAYERS

                variable GENERATES_START_CHEST

        static
        function serialize(cls, obj: typing.Type[ISerializeAble]) -> dict

                variable biome_data

                variable BIOMES

                variable data["biomes"]

                variable data["landmasses"]

                variable data["layers"]

                variable data["generates_start_chest"]

        static
        function register(cls, obj: ISerializeAble)

        static
        function clear(cls)

    variable instance

    variable instance.on_deserialize

    variable instance.on_clear