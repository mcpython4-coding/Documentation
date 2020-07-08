***texture.py - documentation - last updated on 4.7.2020 by uuk***
___

    function colorize(mask: PIL.Image.Image, color: tuple) -> PIL.Image.Image
        
        colorize an imagemask with an color
        :param mask: the mask to base on
        :param color: the color to use
        :return: the colorized image


    function to_pyglet_image(image: PIL.Image.Image) -> pyglet.image.AbstractImage
        
        Will transform the image into an pyglet image
        :param image: the image to transform
        :return: the transformed one


    function to_pillow_image(image: pyglet.image.AbstractImage) -> PIL.Image.Image
        
        Will transform the pyglet image into an pillow one
        :param image: the image to transform
        :return: the transformed one


    function to_pyglet_sprite(image: PIL.Image.Image) -> pyglet.sprite.Sprite
        
        Will transform the pillow image into an pyglet sprite
        :param image: the image
        :return: the sprite
