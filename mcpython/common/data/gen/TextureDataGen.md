***TextureDataGen.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
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