***Model.py - documentation - last updated on 14.5.2020 by uuk***
___

    class Model

        function __init__(self, data: dict, name: str, modname: str)

            variable self.data

            variable self.name

            variable self.parent

            variable self.used_textures

            variable self.texture_addresses

            variable self.texturerename

                variable self.parent

                variable self.used_textures

                variable self.texturerename

            variable self.drawable

                    variable texture

                        variable self.used_textures[name]

                        variable self.drawable

                        variable self.texturerename[name]

            variable toadd

            variable add

            variable self.texture_atlas

                variable self.texture_addresses[name]

                variable self.texture_atlas

            variable self.boxmodels

        function add_face_to_batch(self, position, batch, config, face)

            variable data

        function draw_face(self, position, config, face)

        function get_texture_position(self, name: str) -> tuple

                variable fname