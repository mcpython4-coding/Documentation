***WorldGenerationModeModifier.py - documentation - last updated on 23.8.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class WorldGenerationModeModifier extends  mcpython.common.data.serializer.DataSerializationManager.ISerializer 

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

    variable instance.on_unload