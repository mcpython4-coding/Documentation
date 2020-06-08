***StateStartMenu.py - documentation - last updated on 8.6.2020 by uuk***
___

    class StateStartMenu extends mcpython.state.State.State

        variable NAME

        variable CONFIG_LOCATION

        function __init__(self):  super().__init__()
                
                def bind_to_eventbus(self):

        function bind_to_eventbus(self)

        static
        function on_new_game_press(x, y)

        static
        function on_quit_game_press(x, y)

        static
        function on_draw_2d_pre(): pyglet.gl.glClearColor(1., 1., 1., 1.)
                
                @staticmethod
                def on_key_press(key, modifier):

        static
        function on_key_press(key, modifier)

    variable startmenu

    function create()