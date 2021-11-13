***FaceInfo.py - documentation - last updated on 14.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class FaceInfo
        
        Class for face state of the block


        variable DEFAULT_FACE_STATE

        variable DEFAULT_FACE_DATA

        function __init__(self, block)
            
            Block face state, client-sided container holding information for rendering


            variable self.block

            variable self.multi_data

            variable self.multi_faces

        function is_shown(self) -> bool

        function show_face(self, face: EnumSide, force=False)
            
            Shows a face
            :param face: the face of the block
            :param force: force the show, WARNING: internal only


                variable self.face_data

            variable self.faces[face.normal_name]

                    variable self.subscribed_renderer

                    variable self.face_data[face.normal_name]

                    variable self.face_data[face.normal_name]

        function show_faces(self, faces: typing.List[str])
            
            Optimised show_face() for more than one face
            Will do only something optimal when more than one face is passed in


                variable self.face_data

                    variable self.subscribed_renderer

                    variable self.multi_data

                variable self.multi_data

        function _hide_data(self)

            variable self.multi_data

        function hide_face(self, face: EnumSide)
            
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

        function hide_all(self)
            
            Will hide all faces


                    variable self.faces[face.normal_name]

                variable self.face_data