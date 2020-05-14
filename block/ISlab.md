***ISlab.py - documentation - last updated on 14.5.2020 by uuk***
___

    variable BBOX_DICT

    class ISlab extends block.Block.Block
        
        base class for slabs


        function __init__(self, *args, **kwargs)

                variable self.type

                variable self.type

            variable self.face_solid

        function get_model_state(self)

        function set_model_state(self, state: dict)

                variable self.type

        static function get_all_model_states() -> list

        function on_player_interact(self, player, itemstack, button, modifiers, exact_hit) -> bool

        function get_view_bbox(self)