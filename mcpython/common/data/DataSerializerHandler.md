***DataSerializerHandler.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
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

        function map_pack(self, modname: str, pathname: str, immediate=False)

        function load_file(self, file: str)

                    variable data

                        variable obj

        function clear(self)

        function on_bake(self)