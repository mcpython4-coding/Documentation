***abstract.py - documentation - last updated on 16.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ISerializeAble extends IBufferSerializeAble,  ABC

        variable SERIALIZER: typing.Optional[typing.Type["ISerializer"]]

        static
        function deserialize(cls, data: bytes) -> "ISerializeAble"

        function serialize(self) -> bytes

    class ISerializer

        static
        function check(cls, data: bytes) -> bool

        static
        function deserialize(cls, data: bytes) -> ISerializeAble

        static
        function serialize(cls, obj: ISerializeAble) -> bytes