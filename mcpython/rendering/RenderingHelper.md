***RenderingHelper.py - documentation - last updated on 8.7.2020 by uuk***
___

    class RenderingHelper
        
        class for helping storing an gl status and exchanging it, rolling back, ...
        todo: add setup functions for various systems


        function __init__(self)
            
            creates an new rendering helper.
            WARNING: multiple instances may work NOT well together as they are based on the same gl backend


            variable self.status_table

            variable self.saved

            variable self.default_3d_stack

        function save_status(self, add_to_stack=True)
            
            will save the current status to later revert back to it
            :param add_to_stack: if the current status should be added to the internal collections.deque for using
                pop_status with these element
            :return: the copy of the status, injectable into apply()


        function pop_status(self)
            
            Will pop the current status and will revert it to the one before the save_status()-call
            WARNING: when no status found, an exception will be raised


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


        function get_default_3d_matrix_stack(self, base=None) -> mcpython.rendering.MatrixStack.MatrixStack
            
            will create an MatrixStack-instance with the active transformation for the active player
            Will set up perspective for 3d rendering with these stack
            :param base: the MatrixStack-instance to set into
            :return: the MatrixStack instance
            WARNING: all transformations will be applied ON TOP of the base-MatrixStack if its provided


        function get_dynamic_3d_matrix_stack(self, base=None) -> mcpython.rendering.MatrixStack.LinkedMatrixStack
            
            same as get_default_3d_matrix_stack, but the matrix stack is an LinkedMatrixStack with links to player position,
                etc.
            [see above]


        function setup2d(self, anchor=(0, 0), z_buffer=0)

        static
        function enableAlpha(cls)

        static
        function disableAlpha(cls)