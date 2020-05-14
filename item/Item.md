***Item.py - documentation - last updated on 14.5.2020 by uuk***
___

    class Item extends event.Registry.IRegistryContent

        variable TYPE


        variable STACK_SIZE


        variable HAS_BLOCK

        static function get_used_texture_files(cls):  # WARNING: will be removed during item rendering update; todo
        static function get_default_item_image_location() -> str:  # WARNING
        function __init__(self)
        function __eq__(self, other)
        function get_active_image_location(self):  # WARNING
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
        function get_data(self): return "no
        function set_data(self, data)