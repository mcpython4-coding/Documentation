***FaceInfo.py - documentation - last updated on 16.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class FaceInfo
        
        Class for face state of the block
        todo: merge data into AbstractBlock & make this a static class


        variable DEFAULT_FACE_STATE

        variable DEFAULT_FACE_DATA

        function __init__(self, block)
            
            Block face state


            variable self.block

        function is_shown(self) -> bool

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
