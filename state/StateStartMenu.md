***StateStartMenu.py - documentation - last updated on 14.5.2020 by uuk***
___

    class StateStartMenu extends state.State.State

        variable NAME

        function __init__(self)

        function get_parts(self) -> list

        function bind_to_eventbus(self)

        static function on_new_game_press(x, y)

        static function on_quit_game_press(x, y)

        static function on_draw_2d_pre()

        static function on_key_press(key, modifier)

    variable startmenu

    function create()

        variable startmenu