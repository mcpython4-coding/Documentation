***StateGameInfo.py - documentation - last updated on 8.6.2020 by uuk***
___

    variable sprite
        todo: use pyglet.image.Image.get_region(area)

    class StateGameInfo extends mcpython.state.State.State

        variable NAME

        static
        function is_mouse_exclusive(): return False
                
                def get_parts(self) -> list:

        function get_parts(self) -> list

        function bind_to_eventbus(self)

        static
        function on_key_press(symbol, modifiers)

        static
        function on_mouse_press(x, y, button, modifiers)

    variable gameinfo

    function create()