***WorldGenerationModeModifier.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class WorldGenerationModeModifier extends  mcpython.common.data.DataSerializerHandler.ISerializer 

        static
        function deserialize(cls, data: dict) -> dict

        static
        function serialize(cls, obj: typing.Type[ISerializeAble]) -> dict

        static
        function register(cls, data: dict)

                        variable mass

                            variable layer

        static
        function clear(cls)

    variable instance

    variable instance.on_deserialize

    variable instance.on_clear