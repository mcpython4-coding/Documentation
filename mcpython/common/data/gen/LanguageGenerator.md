***LanguageGenerator.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class LanguageGenerator extends IDataGenerator

        function __init__(self, lang_name: str)

            variable self.lang_name

            variable self.table

        function add_key(self, key: str, value: str)

        function dump(self, generator: DataGeneratorInstance)

        function get_default_location(self, generator: DataGeneratorInstance, name: str)