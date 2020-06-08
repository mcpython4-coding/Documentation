***RenderingHelper.py - documentation - last updated on 8.6.2020 by uuk***
___

    class RenderingHelper
        
        class for helping storing an gl status and exchanging it, rolling back, ...


        function __init__(self)
            
            creates an new rendering helper.
            WARNING: multiple instances may work NOT well together as they are based on the same gl backend


            variable self.status_table

            variable self.saved

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
