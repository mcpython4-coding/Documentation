***DataSerializerHandler.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class ISerializeAble extends ABC

        variable SERIALIZER: typing.Type["ISerializer"]

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

    class DatapackSerializationHelper

        function __init__(
                self,
                name: str,
                path_group: str,
                data_formatter=None,
                data_un_formatter=None,
                re_run_on_reload=False,
                load_on_stage: str = None,
                on_bake=None,
                on_dedicated_server=True,
                ):

            variable load_on_stage: str

            variable self.name

            variable self.path_group

            variable self.serializer: typing.List[typing.Type[ISerializer]]

            variable self.on_deserialize

            variable self.on_clear

            variable self.data_formatter

            variable self.data_un_formatter

            variable self.re_run_on_reload

            variable self.load_on_stage

            variable self.on_bake

        function register_serializer(self, serializer: typing.Type[ISerializer])

        function map_pack(self, modname: str, pathname: str)

        function load_file(self, file: str)

                    variable data

                        variable obj

        function clear(self)

        function bake(self)