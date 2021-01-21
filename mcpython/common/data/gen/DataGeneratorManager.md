***DataGeneratorManager.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class UnsupportedIndirectDumpException extends Exception

    class IDataGenerator

        function dump(self, generator: "DataGeneratorInstance")

        function write(self, generator: "DataGeneratorInstance", name: str)

        function get_default_location(
                self, generator: "DataGeneratorInstance", name: str
                ) -> str:

    class DataGeneratorInstance

        function __init__(self, location: str)

            variable self.default_namespace

            variable self.to_generate

            variable self.location

        function write(self, data: bytes, file: str)

        function get_full_path(self, file: str) -> str

        function annotate(self, generator: IDataGenerator, name: str)

        function generate(self)