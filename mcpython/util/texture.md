***texture.py - documentation - last updated on 23.8.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    function colorize(
            mask: PIL.Image.Image,
            color: tuple,
            colorizer=lambda color, mask: tuple(c * mask // 255 for c in color[:3])
            + (tuple() if len(color) == 3 else (color[-1])),
            ) -> PIL.Image.Image:
        
        Colorize an image-mask with a color using colorizer as the operator
        :param mask: the mask to base on
        :param color: the color to use
        :param colorizer: the colorizer method to use, defaults to a simple channel-based multiplication
        :return: the colorized image


        variable color

        variable mask: PIL.Image.Image

        variable new_image: PIL.Image.Image

                variable color_alpha

                    variable pixel_color

    function layer_with_alpha(base: PIL.Image.Image, top: PIL.Image.Image)

    function to_pyglet_image(image: PIL.Image.Image)
        
        Will transform the image into an pyglet image
        :param image: the image to transform
        :return: the transformed one
        todo: can we do this in-memory? (less time consumed)


    function to_pyglet_sprite(image: PIL.Image.Image)
        
        Will transform the pillow image into an pyglet sprite
        :param image: the image
        :return: the sprite


    function to_pillow_image(image) -> PIL.Image.Image
        
        Will transform the pyglet image into an pillow one
        :param image: the image to transform
        :return: the transformed one
        todo: can we do this in-memory? (less time consumed)


    function hex_to_color(color: str) -> typing.Tuple[int, int, int]
        
        Helper method for transforming a hex string encoding a color into a tuple of color entries


    function int_hex_to_color(color: int) -> typing.Tuple[int, int, int]

    function resize_image_pyglet(image, size: typing.Tuple[int, int])