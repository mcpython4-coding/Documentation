***ItemTool.py - documentation - last updated on 6.6.2020 by uuk***
___

    class ItemTool extends mcpython.item.Item.Item

        variable NAME

        variable HAS_BLOCK

        variable STACK_SIZE

        variable TOOL_LEVEL

        variable TOOL_TYPE

        function __init__(self)

        function __eq__(self, other)

        function get_tool_type(self):  # todo: remove
                return self.TOOL_TYPE
                
                def get_speed_multiplyer(self, itemstack):

        function get_speed_multiplyer(self, itemstack)