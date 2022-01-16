***util.py - documentation - last updated on 16.1.2022 by uuk***
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

    variable UINT

    variable LONG

    variable ULONG

    variable FLOAT

    variable BYTE

    class TableIndexedOffsetTable

        function __init__(self, data: typing.Dict[str, bytes] = None, handling: typing.Callable = _to_bin)

            variable self.data

            variable self.handling

            variable self.override_data

            variable buffer

        function writeData(self, name: str, data: typing.Any)

            variable order

                variable b

                variable r

            variable data

            variable head

            variable c

                variable e[1]

    class ReadBuffer

        variable __slots__

        function __init__(self, stream: typing.Union[typing.BinaryIO, bytes])

            variable self.stream

        function read_bool(self)

        function read_bool_group(self, count: int)

        function read_struct(self, structure: struct.Struct)

        function read_byte(self)

        function read_int(self)

        function read_uint(self)

        function read_long(self)

        function read_ulong(self)

        function read_big_long(self, size_size=2)

        function read_float(self)

        function read_string(self, size_size=2, encoding="utf-8") -> str

        function read_nullable_string(self, size_size=2, encoding="utf-8") -> str | None

            variable size

                variable result

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

            variable head

            variable entries

            variable head

                    variable info

            variable data

            variable result

            variable head

            variable keys

                    variable data

                    variable result

        function read_sub_buffer_dynamic_size(self, size_size=2) -> "ReadBuffer"

        class SkipableIterator

            function __init__(self, handler: typing.Callable[["ReadBuffer"], typing.Awaitable | typing.Any], parts: typing.List[bytes])

                variable self.handler

                variable self.parts

                variable self.pointer

                variable r

                variable data

            function skip(self, count: int = 1)

            function __getitem__(self, item: int) -> typing.Coroutine

            variable data

        class CachedLookupList extends SkipableIterator

            variable entry_size

            variable data

            variable entry_size

            variable size

            variable data

            variable r

            variable entry_size

            variable size

            variable data

                variable d

                    variable r

            variable sort

    class WriteBuffer

        variable __slots__

        function __init__(self)

        function get_data(self) -> bytes

        function write_bool(self, state: bool)

        function write_bool_group(self, bools: typing.List[bool])

                variable bits

        function write_struct(self, structure: struct.Struct, *data)

        function write_byte(self, value: int)

        function write_int(self, value: int)

        function write_uint(self, value: int)

        function write_long(self, value: int)

        function write_ulong(self, value: int)

        function write_big_long(self, value: int, size_size=2)

            variable length
                todo: can we optimize this calculation (one byte more is a lot bigger than we need!)?

            variable data

        function write_float(self, value: float)

        function write_string(self, value: str, size_size=2, encoding="utf-8")

        function write_nullable_string(self, value: str, size_size=2, encoding="utf-8")

                variable data

            variable data

                variable result

                variable result

                variable k

                variable v

        function write_bytes(self, data: bytes, size_size=2)

        function write_const_bytes(self, data: bytes)

        function write_uuid(self, uid: uuid.UUID)

            variable cls

        function write_sub_buffer(self, buffer: "WriteBuffer")

        function write_sub_buffer_dynamic_size(self, buffer: "WriteBuffer", size_size=2)
            
            Writes a container structure allowing to skip elements
            Internally creates a header for the table with indices


                variable buffer

                variable r

            variable encoded
            
            Writes a list of arbitrary data of similar size (with padding)
            Optimal when storing multiple items of the same size, fast access times,
            lazy decoding and skip-able container when reading


                variable buffer

                variable r

            variable encoded

                variable entry_size

            variable encoded

    class IBufferSerializeAble extends ABC

        static
        function create_new(cls) -> "IBufferSerializeAble"