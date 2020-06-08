***BlockModelFactory.py - documentation - last updated on 8.6.2020 by uuk***
___

    class BlockModelFactory

        function __init__(self)

            variable self.name

            variable self.parent

            variable self.elements

            variable self.textures

        function setName(self, name: str)

        function setParent(self, parent: str)

        function addElement(self, f: tuple, t: tuple, textures: list, rotation=None, uvs=[(0, 0, 1, 1)]*6, texture_rotation=[0]*6)
            
            will add an visual element to the model
            :param f: coords where to start
            :param t: coords where to end
            :param textures: the textures to use for each face, in order of util.enums.EnumSide.iterate()
            :param rotation: the rotation to use, as (<origin>, <axis>, <angle>, [<rescale>])
            :param uvs: the uv regions for the textures
            :param texture_rotation: the rotation for each texture


        function setTexture(self, key: str, texture: str)

        function finish(self)

        function finish_up(self)

    class NormalBlockStateFactory

        function __init__(self)

            variable self.name

            variable self.variants

        function setName(self, name: str)

        function addVariant(self, variant_descriptor: str, *models)

        function finish(self)

        function finish_up(self)