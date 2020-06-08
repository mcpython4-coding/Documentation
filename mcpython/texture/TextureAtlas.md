***TextureAtlas.py - documentation - last updated on 8.6.2020 by uuk***
___

    variable MISSING_TEXTURE

    class TextureAtlasGenerator
        
        generator system for an item atlas


        function __init__(self)

            variable self.atlases

        function add_image(self, image: PIL.Image.Image, modname: str) -> tuple

        function add_image_file(self, file: str, modname: str) -> tuple

        function add_images(self, images: list, modname, one_atlased=True) -> list

        function add_image_files(self, files: list, modname: str, one_atlased=True) -> list

        function output(self)

    class TextureAtlas

        function __init__(self, size=(16, 16), image_size=(16, 16), add_missing_texture=True, pyglet_special_pos=True)

            variable self.size

            variable self.image_size

            variable self.pyglet_special_pos

            variable self.texture

            variable self.free_space

            variable self.images

            variable self.imagelocations - an images[-parallel (x, y)-list

            variable self.group

        function add_image(self, image: PIL.Image.Image, ind=None, position=None) -> tuple

        function is_free_for(self, images: list) -> bool

    variable handler