***factory.py - documentation - last updated on 6.6.2020 by uuk***
___

    class ITextureChange extends mcpython.event.Registry.IRegistryContent

        variable TYPE

        static
        function convert(images: list, image: PIL.Image.Image, *args, **kwargs) -> PIL.Image.Image: raise NotImplementedError()
                
                
                class TextureFactory:
                def __init__(self):

    class TextureFactory

        function __init__(self)

            variable self.changer

        static
        function add_transform(registry, obj: ITextureChange)

        function transform(self, images: list, image, mode, *args, **kwargs)

        function apply_from_file(self, file)

        function apply_from_data(self, data: dict)

        function load(self)

    variable G.texturefactoryhandler

    variable texturechanges

    @G.registry class TextureResize extends ITextureChange

        variable NAME

        static
        function convert(images: list, image: PIL.Image.Image, size=None) -> PIL.Image.Image

    @G.registry class TextureColorize extends ITextureChange

        variable NAME

        static
        function convert(images: list, image: PIL.Image.Image, color=None) -> PIL.Image.Image

    @G.registry class TextureCut extends ITextureChange

        variable NAME

        static
        function convert(images: list, image: PIL.Image.Image, area=None) -> PIL.Image.Image

    @G.registry class TextureRebase extends ITextureChange

        variable NAME

        static
        function convert(images: list, image: PIL.Image.Image, size=None, position=(0, 0)) -> PIL.Image.Image

    @G.registry class TextureCombine extends ITextureChange

        variable NAME

        static
        function convert(images: list, image: PIL.Image.Image, base=None, position=(0, 0)) -> PIL.Image.Image