***TextureAtlas.py - documentation - last updated on 14.5.2020 by uuk***
___

    variable MISSING_TEXTURE


    class TextureAtlasGenerator
        function __init__(self)
        function add_image(self, image: PIL.Image.Image, modname: str) -> tuple
        function add_image_file(self, file: str, modname: str) -> tuple
        function add_images(self, images: list, modname, one_atlased=True) -> list
        function add_image_files(self, files: list, modname: str, one_atlased=True) -> list
        function output(self)

    class TextureAtlas
        function __init__(self, size=(16, 16), image_size=(16, 16), add_missing_texture=True, pyglet_special_pos=True)
        function add_image(self, image: PIL.Image.Image, ind=None, position=None) -> tuple
        function is_free_for(self, images: list) -> bool

    variable handler
