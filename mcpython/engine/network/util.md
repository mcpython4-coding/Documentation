***util.py - documentation - last updated on 28.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable INT

    variable LONG

    variable FLOAT

    variable BYTE

    class ReadBuffer

        function __init__(self, stream: typing.Union[typing.BinaryIO, bytes])

            variable self.stream

        function read_bool(self)

        function read_bool_group(self, count: int)

        function read_struct(self, structure: struct.Struct)

        function read_byte(self)

        function read_int(self)

        function read_long(self)

        function read_big_long(self, size_size=2)

        function read_float(self)

        function read_string(self, size_size=2, encoding="utf-8")

            variable size

                variable result

            variable size

        function read_bytes(self, size_size=2)

        function read_const_bytes(self, count: int)

        function read_uuid(self)

            variable module

            variable name

                variable module

                variable cls: "IBufferSerializeAble"

                variable container_instance

            variable tag

    class WriteBuffer

        function __init__(self)

            variable self.data: typing.List[bytes]

        function get_data(self)

        function write_bool(self, state: bool)

        function write_bool_group(self, bools: typing.List[bool])

        function write_struct(self, structure: struct.Struct, *data)

        function write_byte(self, value: int)

        function write_int(self, value: int)

        function write_long(self, value: int)

        function write_big_long(self, value: int, size_size=2)

        function write_float(self, value: float)

        function write_string(self, value: str, size_size=2, encoding="utf-8")

            variable data

                variable result

                variable k

                variable v

        function write_bytes(self, data: bytes, size_size=2)

        function write_const_bytes(self, data: bytes)

        function write_uuid(self, uid: uuid.UUID)

            variable cls

    class IBufferSerializeAble extends ABC

        static
        function create_new(cls) -> "IBufferSerializeAble"