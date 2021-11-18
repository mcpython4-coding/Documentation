***FaceInfo.py - documentation - last updated on 18.11.2021 by uuk***
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


        variable __slots__

        function __init__(self, block)
            
            Block face state, client-sided container holding information for rendering


            variable self.block

            variable self.faces

            variable self.custom_renderer - holds a custom block renderer

            variable self.subscribed_renderer: bool

            variable self.bound_rendering_info

            variable self.multi_data

        function is_shown(self) -> bool

        function show_faces(self, faces: int)
            
            Optimised show_face() for more than one face
            Will do only something optimal when more than one face is passed in


                    variable self.subscribed_renderer

                    variable self.multi_data

                variable self.multi_data

        function _hide_data(self)

            variable self.multi_data

        function hide_faces(self, faces: int)
            
            Will hide a face
            :param faces: the faces to hide


            variable faces

                    variable self.subscribed_renderer

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


            variable self.faces