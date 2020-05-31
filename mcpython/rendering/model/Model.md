***Model.py - documentation - last updated on 6.6.2020 by uuk***
___

    class Model

        function __init__(self, data: dict, name: str, modname: str)

            variable self.data

            variable self.name

            variable self.parent

            variable self.used_textures

            variable self.texture_addresses

            variable self.texturerename

        function add_face_to_batch(self, position, batch, config, face)

        function draw_face(self, position, config, face)

        function get_texture_position(self, name: str) -> tuple