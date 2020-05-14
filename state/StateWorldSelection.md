***StateWorldSelection.py - documentation - last updated on 14.5.2020 by uuk***
___

    class StateWorldSelection extends State.State

        variable NAME

        function __init__(self)

        function get_parts(self) -> list

        function on_back_press(self, *_)

        function on_new_world_press(self, *_)

            variable worldname

        function on_world_load_press(self, *_)

            variable worldname

        function bind_to_eventbus(self)

        function on_key_press(self, symbol, modifiers)

        static function on_draw_2d_pre()

        function on_activate(self)

    variable worldselection

    function create()

        variable worldselection