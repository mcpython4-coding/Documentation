***ModelFactory.py - documentation - last updated on 30.5.2020 by uuk***
___

    class ModelFactory

        function __init__(self, name: str, parent="block/block")

            variable self.name

            variable self.parent

            variable self.elements

            variable self.textures

        function add_drawing_box(self, position, size, texturenames)

        function set_texture(self, name, texturefile)

        function finish(self)