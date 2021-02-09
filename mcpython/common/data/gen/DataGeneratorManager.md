***DataGeneratorManager.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
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