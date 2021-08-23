***TextureAtlas.py - documentation - last updated on 23.8.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable MISSING_TEXTURE

    @onlyInClient() class TextureAtlasGenerator
        
        Generator system for a multiple underlying ItemAtlas'
        Based on some identifier


        function __init__(self)

        function add_image(
                self, image: PIL.Image.Image, identifier: typing.Hashable
                ) -> typing.Tuple[typing.Tuple[int, int], "TextureAtlas"]:
            
            Adds a single pillow image to the underlying atlas system


            variable image

        function add_image_file(
                self, file: str, identifier: str
                ) -> typing.Tuple[typing.Tuple[int, int], "TextureAtlas"]:
            
            Adds a single image by file name (loadable by resource system!)


        function add_images(
                self, images: typing.List[PIL.Image.Image], identifier: str, single_atlas=True
                ) -> typing.List[typing.Tuple[typing.Tuple[int, int], "TextureAtlas"]]:

            variable images

            variable m_size

            variable atlas

        function add_image_files(
                self, files: list, identifier: str, single_atlas=True
                ) -> typing.List[typing.Tuple[typing.Tuple[int, int], "TextureAtlas"]]:

        function output(self)

                    variable location

                    variable atlas.group

    @onlyInClient() class TextureAtlas
        
        One-texture atlas
        Contains a single underlying texture, dynamically resized when needed


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
                The underlying texture

            variable self.free_space
                Where is space for images?

            variable self.images: typing.List[PIL.Image.Image]

            variable self.group: typing.Optional[pyglet.graphics.TextureGroup]
                The pyglet texture group, only for storage reasons

        function add_image(
                self, image: PIL.Image.Image, position=None
                ) -> typing.Tuple[int, int]:
            
            Adds an image to the atlas and returns the position of it in the atlas


                variable self.image_size

                variable self.texture

                variable image

                variable old
                    todo: export to separate function

                variable self.size

                variable self.texture

        function is_free_for(self, images: list) -> bool

        function is_free_for_slow(self, images: list) -> bool

    variable handler