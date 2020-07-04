***Configuration.py - documentation - last updated on 4.7.2020 by uuk***
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
            
            creates an new configuration object for an data generation
            :param modname: the mod-name to use
            :param output_folder: the folder to put data to, MUST be full-path, not local path
            :param file_scheme: an schema how to store the data. formatted with .format().
                group is "assets" or "data", namespace is the namespace, sub-group is e.g. recipes or textures and path is
                the path to store under, like in "minecraft:block/example" it is block/example.<what file ending ever>


        function setDefaultNamespace(self, namespace: str)
            
            will set the default namespace when not specified for namespace-needed items [like items, blocks, ...]
            :param namespace: the namespace to use


        function add_element(self, element: IDataGenerator)
            
            will insert an generator into the config for later generation
            :param element: the element to insert


        function shaped_recipe(self, name: str)
            
            will create an new mcpython.datagen.RecipeGenerator.ShapedRecipeGenerator create with these config object
            :param name: the name to generate under; used for the path-formatter


        function shapeless_recipe(self, name: str)
            
            will create an new mcpython.datagen.RecipeGenerator.ShapelessRecipeGenerator create with these config object
            :param name: the name to generate under; used for the path-formatter


        function one_to_one(self, name: str, i, o)
            
            simple way to create an shapeless recipe with only one input and one output
            :param name: the name to generate under; used for the path-formatter
            :param i: the input
            :param o: the output


        function smelting_recipe(self, *args, **kwargs)
            
            will create an new mcpython.datagen.RecipeGenerator.SmeltingGenerator create with these config object
            :param args: [0]: the name to generate under; used for the path-formatter
                        ... send to constructor of class


        function __build(self)
            
            Internal function to build the config
            Will decide if the system should data-gen or not


        function write(self, data, *args)
            
            writes certain data into the file system
            :param data: the data to write, possible: str, bytes or pickle-able
            :param args: the formatting args, must be 3 or 4 long
            :return:


        function write_json(self, data, *args)
            
            Will write data in human-readable json mode (with \n in place and right indent) via the simple json format
            It will sort the keys
            :param data: the data to save
            :param args: the args to pass to self.write()
