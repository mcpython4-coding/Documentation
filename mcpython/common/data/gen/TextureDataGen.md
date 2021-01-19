***TextureDataGen.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class TextureConstructor extends IDataGenerator
        
        generator system for generating textures


        function __init__(self, name: str, image_size: tuple = None)
            
            will create an new TextureConstructor-instance
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


        function add_coloring_layer(
                self, location_or_image, color: tuple, position=(0, 0), rescale=(1, 1)
                ):
            
            will alpha-composite an image (which is colored before) ontop of all previous actions
            :param location_or_image: the image to add
            :param color: the color to colorize with
            :param position: the position to add on
            :param rescale: rescale of the image


                    variable location_or_image

        function scaled(self, scale: tuple)

        function crop(self, region: tuple)

        function add_alpha_composite_layer(self, location_or_image, position=(0, 0))

        function write(self, generator: "DataGeneratorInstance", name: str)

                        variable self.image_size

            variable image

                    variable i

                    variable size

                    variable scale

                    variable image

                    variable size

                    variable region

                    variable image