***BlockFaceState.py - documentation - last updated on 14.5.2020 by uuk***
___

    class BlockFaceState

        function __init__(self, block)

            variable self.block

            variable self.faces

            variable self.face_data

            variable self.custom_renderer - holds an custom block renderer

            variable self.subscribed_renderer

        function show_face(self, face: util.enums.EnumSide)

            variable self.faces[face]

                    variable self.face_data[face]

                        variable self.subscribed_renderer

        function hide_face(self, face: util.enums.EnumSide)

            variable self.faces[face]

                        variable self.subscribed_renderer

        function _draw_custom_render(self)

        function update(self, redraw_complete=False)

            variable state

        function hide_all(self)

                variable self.subscribed_renderer

        function __del__(self)