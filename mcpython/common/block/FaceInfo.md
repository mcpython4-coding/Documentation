***FaceInfo.py - documentation - last updated on 13.12.2021 by uuk***
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
                A reference to the super block

            variable self.faces
                Holds which faces are visible

            variable self.subscribed_renderer: bool
                If the custom_renderer was bound to a rendering event or not

            variable self.bound_rendering_info

            variable self.multi_data
                The data from the normal add_to_batch() calls, should be a list of VertexList's

        function is_shown(self) -> bool

        function show_faces(self, faces: int)
            
            Shows the faces indicating by the bit flag (See EnumSide.bitflag)


                    variable self.subscribed_renderer

                    variable self.multi_data

                variable self.multi_data

        function _hide_data(self)

            variable self.multi_data

        function hide_faces(self, faces: int)
            
            Will hide the faces indicated by the face
            :param faces: the faces to hide
            Will hide all faces and re-render the still visible ones


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