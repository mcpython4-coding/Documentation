***BlockFaceState.py - documentation - last updated on 16.5.2020 by uuk***
___

    class BlockFaceState
        
        class for face state of the block


        function __init__(self, block)
            
            block face state


            variable self.block

            variable self.faces

            variable self.face_data

            variable self.custom_renderer - holds an custom block renderer

            variable self.subscribed_renderer: bool

        function show_face(self, face: util.enums.EnumSide)
            
            shows an face
            :param face: the face of the block


        function hide_face(self, face: util.enums.EnumSide)
            
            will hide an face
            :param face: the face to hide


        function _draw_custom_render(self)
            
            will inherit the custom renderer


        function update(self, redraw_complete=False)
            
            updates the block face state
            :param redraw_complete: if all sides should be re-drawn
            todo: make redraw-complete always True or default to True


        function hide_all(self)
            
            will hide all faces


        function __del__(self)
            
            will delete references to various parts for gc
