***RenderingHelper.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class RenderingHelper
        
        class for helping storing an gl status and exchanging it, rolling back, ...
        todo: add setup functions for various systems
        todo: add checks if this is the rendering process


        function __init__(self)
            
            creates an new rendering helper.
            WARNING: multiple instances may work NOT well together as they are based on the same gl backend
                -> todo: make shared


        function save_status(self, add_to_stack=True)
            
            will save the current status to later revert back to it
            :param add_to_stack: if the current status should be added to the internal collections.deque for using
                pop_status with these element
            :return: the copy of the status, injectable into apply()


        function pop_status(self)
            
            Will pop the current status and will revert it to the one before the save_status()-call
            WARNING: when no status found, an exception will be raised


        function deleteSavedStates(self)

        function glEnable(self, flag: int)
            
            enables an gl flag via glEnable(flag) and will mark it in the status table as True
            :param flag: the flag to set


        function glDisable(self, flag: int)
            
            disables an gl flag via glDisable(flag) and will mark it in the status table as False
            :param flag: the flag to set


        function set_flag(self, flag: int, status: bool)
            
            will set the enabled status via an boolean
            :param flag: the gl-enum-int to use
            :param status: the status to set


        function apply(self, data=None)
            
            will apply an status
            :param data: the data to apply or None to use the active one (to make sure everything is set correctly)


        function get_default_3d_matrix_stack(
                self, base=None
                ) -> mcpython.client.rendering.MatrixStack.MatrixStack:
            
            will create an MatrixStack-instance with the active transformation for the active player
            Will set up perspective for 3d rendering with these stack
            :param base: the MatrixStack-instance to set into
            :return: the MatrixStack instance
            WARNING: all transformations will be applied ON TOP of the base-MatrixStack if its provided
            Use get_dynamic_3d_matrix_stack() where possible & reuse


                variable base

            variable viewport

        function get_dynamic_3d_matrix_stack(
                self, base=None
                ) -> mcpython.client.rendering.MatrixStack.LinkedMatrixStack:
            
            same as get_default_3d_matrix_stack, but the matrix stack is an LinkedMatrixStack with links to player position,
                etc. (so it dynamically updates itself when the player changes the parameters)
            [see above]


                variable base

        function setup2d(self, anchor=(0, 0), z_buffer=0)
            
            will setup an 2d environment
            :param anchor: the anchor in the window as an tuple of two floats representing an move as factors to the window size
            :param z_buffer: the layer in which to render


        function enableAlpha(self)
            
            will enable alpha blending


        function disableAlpha(self)
            
            will disable alpha rendering
