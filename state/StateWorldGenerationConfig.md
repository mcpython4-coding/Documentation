***StateWorldGenerationConfig.py - documentation - last updated on 14.5.2020 by uuk***
___

    class StateWorldGenerationConfig extends State.State

        variable NAME

        function __init__(self)

        function get_parts(self) -> list

            variable parts - gui.back*#", (-320, 20), anchor_window="MD",

            variable text

        function on_back_press(self, x, y)

        function on_generate_press(self, x, y)

        function generate(self)

        function bind_to_eventbus(self)

        function on_key_press(self, symbol, modifiers)

        static function on_draw_2d_pre()

        function on_activate(self)

            variable self.parts[2].index

            variable self.parts[2].text

            variable self.parts[3].index

            variable self.parts[3].text

    variable worldgenerationconfig

    function create()

        variable worldgenerationconfig