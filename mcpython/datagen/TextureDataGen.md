***TextureDataGen.py - documentation - last updated on 13.6.2020 by uuk***
___

    class TextureConstructor extends mcpython.datagen.Configuration.IDataGenerator
        
        generator system for generating textures


        function __init__(self, config, name: str, image_size: tuple)
            
            will create an new TextureConstructor-instance
            :param config: the config to use
            :param name: the name of the texture address as "{group}/{path without .png}"
            :param image_size: the size of the image to create


            variable self.name

            variable self.image_size

            variable self.actions

        function add_image_layer_top(self, location_or_image, position=(0, 0), rescale=(1, 1))
            
            will alpha-composite an image ontop of all previous actions
            :param location_or_image: the image to add
            :param position: the position to add on
            :param rescale: rescale of the image


        function add_coloring_layer(self, location_or_image, color: tuple, position=(0, 0), rescale=(1, 1))
            
            will alpha-composite an image (which is colored before) ontop of all previous actions
            :param location_or_image: the image to add
            :param color: the color to colorize with
            :param position: the position to add on
            :param rescale: rescale of the image


        function generate(self)