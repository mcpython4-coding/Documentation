***Configuration.py - documentation - last updated on 8.6.2020 by uuk***
___

    class IDataGenerator
        
        base class for every data generator


        function __init__(self, config)

            variable self.config

        function generate(self)

    class DataGeneratorConfig
        
        configuration class for the data generators.
        Used to store some global stuff


        function __init__(self, modname: str, output_folder: str, file_scheme: str = "{group}/{namespace}/{sub-group}/{path}")

            variable self.output_folder

            variable self.modname

            variable self.file_scheme

            variable self.elements

        function add_element(self, element: IDataGenerator)

        function shaped_recipe(self, name: str)

        function shapeless_recipe(self, name: str)

        function smelting_recipe(self, *args, **kwargs)

        function __build(self)

        function write(self, data, *args)

        function write_json(self, data, *args)