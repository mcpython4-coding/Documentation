***TextureAtlas.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    variable MISSING_TEXTURE

    @onlyInClient() class TextureAtlasGenerator
        
        generator system for an item atlas


        function __init__(self)

            variable self.atlases

        function add_image(self, image: PIL.Image.Image, modname: str) -> tuple

        function add_image_file(self, file: str, modname: str) -> tuple

        function add_images(self, images: list, modname, one_atlased=True) -> list

        function add_image_files(self, files: list, modname: str, one_atlased=True) -> list

        function output(self)

    @onlyInClient() class TextureAtlas

        function __init__(
                self,
                size=(16, 16),
                image_size=(16, 16),
                add_missing_texture=True,
                pyglet_special_pos=True,
                ):

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