***BlockFaceState.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class BlockFaceState
        
        Class for face state of the block
        todo: merge into AbstractBlock


        variable DEFAULT_FACE_STATE

        variable DEFAULT_FACE_DATA

        function __init__(self, block)
            
            Block face state


            variable self.block

        function show_face(self, face: mcpython.util.enums.EnumSide)
            
            Shows an face
            :param face: the face of the block


                variable self.face_data

            variable self.faces[face.normal_name]

                    variable self.face_data[face.normal_name]

                        variable self.subscribed_renderer

                    variable self.face_data[face.normal_name]

        function hide_face(self, face: mcpython.util.enums.EnumSide)
            
            Will hide an face
            :param face: the face to hide


            variable self.faces[face.normal_name]

                        variable self.subscribed_renderer

            variable self.face_data[face.normal_name]

                variable self.face_data

        function _draw_custom_render(self)
            
            Will inherit the custom renderer


        function update(self, redraw_complete=True)
            
            Updates the block face state
            :param redraw_complete: if all sides should be re-drawn


            variable dimension

            variable chunk

            variable state

                variable face

        function hide_all(self)
            
            Will hide all faces
            todo: can we optimize it
