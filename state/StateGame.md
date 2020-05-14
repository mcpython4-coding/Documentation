***StateGame.py - documentation - last updated on 14.5.2020 by uuk***
___

    class StateGame extends State.State

        variable NAME

        static function is_mouse_exclusive()

        function __init__(self)

        function get_parts(self) -> list

        function on_activate(self)

            variable G.worldgenerationhandler.enable_auto_gen

        function on_deactivate(self)

            variable G.worldgenerationhandler.enable_auto_gen

            variable G.window.mouse_pressing

        function bind_to_eventbus(self)

        function on_key_press(self, symbol, modifiers)

                        variable self.parts[0].activate_mouse

        static function open_chat(enter="")

            variable G.chat.text

        static function on_draw_2d_pre()

    variable game

    function create()

        variable game