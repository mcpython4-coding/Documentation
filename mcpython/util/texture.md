***texture.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    function colorize(mask: PIL.Image.Image, color: tuple) -> PIL.Image.Image
        
        colorize an image-mask (greyscale) with an color
        :param mask: the mask to base on
        :param color: the color to use
        :return: the colorized image


    function to_pyglet_image(image: PIL.Image.Image) -> pyglet.image.AbstractImage
        
        Will transform the image into an pyglet image
        :param image: the image to transform
        :return: the transformed one
        todo: can we do this in-memory?


    function to_pillow_image(image: pyglet.image.AbstractImage) -> PIL.Image.Image
        
        Will transform the pyglet image into an pillow one
        :param image: the image to transform
        :return: the transformed one
        todo: can we do this in-memory?


    function to_pyglet_sprite(image: PIL.Image.Image) -> pyglet.sprite.Sprite
        
        Will transform the pillow image into an pyglet sprite
        :param image: the image
        :return: the sprite


    function hex_to_color(color: str) -> typing.Tuple[int, int, int]