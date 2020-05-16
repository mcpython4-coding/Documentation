***ISlab.py - documentation - last updated on 16.5.2020 by uuk***
___

    variable BBOX_DICT

    class ISlab extends block.Block.Block
        
        base class for slabs


        function __init__(self, *args, **kwargs)

                variable self.type

        function get_model_state(self)

        function set_model_state(self, state: dict)

        static function get_all_model_states() -> list

        function on_player_interact(self, player, itemstack, button, modifiers, exact_hit) -> bool

        function get_view_bbox(self)