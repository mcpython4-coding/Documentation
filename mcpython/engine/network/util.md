***util.py - documentation - last updated on 14.10.2021 by uuk***
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

    class ReadBuffer

        function __init__(self, stream: typing.Union[typing.BinaryIO, bytes])

            variable self.stream

        function read_bool(self)

        function read_bool_group(self, count: int)

        function read_struct(self, structure: struct.Struct)

        function read_int(self)

        function read_long(self)

        function read_big_long(self, size_size=2)

        function read_float(self)

        function read_string(self, size_size=2, encoding="utf-8")

        function read_list(self, handling: typing.Callable[[], typing.Any])

        function read_bytes(self, size_size=2)

        function read_const_bytes(self, count: int)

        function read_uuid(self)

    class WriteBuffer

        function __init__(self)

            variable self.data: typing.List[bytes]

        function get_data(self)

        function write_bool(self, state: bool)

        function write_bool_group(self, bools: typing.List[bool])

        function write_struct(self, structure: struct.Struct, *data)

        function write_int(self, value: int)

        function write_long(self, value: int)

        function write_big_long(self, value: int, size_size=2)

        function write_float(self, value: float)

        function write_string(self, value: str, size_size=2, encoding="utf-8")

        function write_list(
                self, data: typing.List, handling: typing.Callable[[typing.Any], typing.Any]
                ):

        function write_bytes(self, data: bytes, size_size=2)

        function write_const_bytes(self, data: bytes)

        function write_uuid(self, uid: uuid.UUID)

    class IBufferSerializeAble extends ABC

        function write_to_network_buffer(self, buffer: WriteBuffer)

        function read_from_network_buffer(self, buffer: ReadBuffer)