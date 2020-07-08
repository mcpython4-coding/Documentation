***BlockModelFactory.py - documentation - last updated on 10.6.2020 by uuk***
___

    @deprecation.deprecated("dev2-2", "a1.5.0") class BlockModelFactory

        @deprecation.deprecated("dev2-2", "a1.5.0")
        function __init__(self)

            variable self.name

            variable self.parent

            variable self.elements

            variable self.textures

        @deprecation.deprecated("dev2-2", "a1.5.0")
        function setName(self, name: str)

        @deprecation.deprecated("dev2-2", "a1.5.0")
        function setParent(self, parent: str)

        @deprecation.deprecated("dev2-2", "a1.5.0")
        function addElement(self, f: tuple, t: tuple, textures: list, rotation=None, uvs=[(0, 0, 1, 1)]*6, texture_rotation=[0]*6)
            
            will add an visual element to the model
            :param f: coords where to start
            :param t: coords where to end
            :param textures: the textures to use for each face, in order of util.enums.EnumSide.iterate()
            :param rotation: the rotation to use, as (<origin>, <axis>, <angle>, [<rescale>])
            :param uvs: the uv regions for the textures
            :param texture_rotation: the rotation for each texture


        @deprecation.deprecated("dev2-2", "a1.5.0")
        function setTexture(self, key: str, texture: str)

        @deprecation.deprecated("dev2-2", "a1.5.0")
        function finish(self)

        @deprecation.deprecated("dev2-2", "a1.5.0")
        function finish_up(self)

    @deprecation.deprecated("dev2-2", "a1.5.0") class NormalBlockStateFactory

        @deprecation.deprecated("dev2-2", "a1.5.0")
        function __init__(self)

            variable self.name

            variable self.variants

        @deprecation.deprecated("dev2-2", "a1.5.0")
        function setName(self, name: str)

        @deprecation.deprecated("dev2-2", "a1.5.0")
        function addVariant(self, variant_descriptor: str, *models)

        @deprecation.deprecated("dev2-2", "a1.5.0")
        function finish(self)

        @deprecation.deprecated("dev2-2", "a1.5.0")
        function finish_up(self)