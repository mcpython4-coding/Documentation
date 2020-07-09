***Item.py - documentation - last updated on 9.7.2020 by uuk***
___

    class Item extends mcpython.event.Registry.IRegistryContent

        variable TYPE

        variable STACK_SIZE

        variable HAS_BLOCK

        variable ITEM_NAME_COLOR

        static
        function get_default_item_image_location() -> str:  # WARNING: will be removed during item rendering update
                raise NotImplementedError()
                
                def __init__(self):

        function __init__(self)

            variable self.uuid

        function __eq__(self, other)

        function get_active_image_location(self):  # WARNING: will be removed during item rendering update
                return self.get_default_item_image_location()
                
                def get_block(self) -> str:

        function get_block(self) -> str

        function on_player_interact(self, player, block, button, modifiers) -> bool
            
            called when the player tries to use the item
            :param player: the player interacting
            :param block: the block in focus, may be None
            :param button: the button used
            :param modifiers: the modifiers used
            :return: if default logic should be interrupted
            todo: add an exact_hit-parameter


        function on_set_from_item(self, block)

        function get_data(self): return "no:data"
                
                def set_data(self, data):

        function set_data(self, data)

        function get_tooltip_provider(self)

        function getAdditionalTooltipText(self, stack, renderer) -> list