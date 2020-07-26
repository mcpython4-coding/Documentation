***LanguageGenerator.py - documentation - last updated on 26.7.2020 by uuk***
___

    class LanguageGenerator extends mcpython.datagen.Configuration.IDataGenerator

        function __init__(self, config: mcpython.datagen.Configuration.DataGeneratorConfig, lang_name: str)

            variable self.lang_name

            variable self.table

        function add_key(self, key: str, value: str)

        function generate(self)