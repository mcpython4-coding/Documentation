***TagGenerator.py - documentation - last updated on 10.6.2020 by uuk***
___

    class TagGenerator extends mcpython.datagen.Configuration.IDataGenerator

        function __init__(self, config, group: str, name: str, override=False)

            variable self.group

            variable self.name

            variable self.override

            variable self.affected

        function add_affected(self, *affected)

        function generate(self)