***factory.py - documentation - last updated on 14.5.2020 by uuk***
___

    class ITextureChange extends event.Registry.IRegistryContent

        variable TYPE

        static function convert(images: list, image: PIL.Image.Image, *args, **kwargs) -> PIL.Image.Image

    class TextureFactory

        function __init__(self)

            variable self.changer

        static function add_transform(registry, obj: ITextureChange)

            variable G.texturefactoryhandler.changer[obj.NAME]

        function transform(self, images: list, image, mode, *args, **kwargs)

            variable texturechange: ITextureChange

        function apply_from_file(self, file)

        function apply_from_data(self, data: dict)

            variable images

                variable image

                variable out

                variable mode

                        variable images[out[i]]

                    variable images[out]

                variable f

                variable d

        function load(self)

            variable entries

    variable G.texturefactoryhandler

    variable texturechanges

    @G.registry class TextureResize extends ITextureChange

        variable NAME

        static function convert(images: list, image: PIL.Image.Image, size=None) -> PIL.Image.Image

    @G.registry class TextureColorize extends ITextureChange

        variable NAME

        static function convert(images: list, image: PIL.Image.Image, color=None) -> PIL.Image.Image

    @G.registry class TextureCut extends ITextureChange

        variable NAME

        static function convert(images: list, image: PIL.Image.Image, area=None) -> PIL.Image.Image

    @G.registry class TextureRebase extends ITextureChange

        variable NAME

        static function convert(images: list, image: PIL.Image.Image, size=None, position=(0, 0)) -> PIL.Image.Image

            variable base

    @G.registry class TextureCombine extends ITextureChange

        variable NAME

        static function convert(images: list, image: PIL.Image.Image, base=None, position=(0, 0)) -> PIL.Image.Image

            variable imageb: PIL.Image.Image