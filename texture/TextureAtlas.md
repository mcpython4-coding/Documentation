***TextureAtlas.py - documentation - last updated on 14.5.2020 by uuk***
___

    variable MISSING_TEXTURE

    class TextureAtlasGenerator

        function __init__(self)

            variable self.atlases

        function add_image(self, image: PIL.Image.Image, modname: str) -> tuple

            variable image

        function add_image_file(self, file: str, modname: str) -> tuple

        function add_images(self, images: list, modname, one_atlased=True) -> list

            variable images

            variable m_size

            variable atlas

        function add_image_files(self, files: list, modname: str, one_atlased=True) -> list

        function output(self)

                    variable location

                    variable atlas.group

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

                variable self.image_size

                variable self.texture

                variable image

                variable old

                variable self.size

                variable self.texture

            variable pos

        function is_free_for(self, images: list) -> bool

            variable count

    variable handler