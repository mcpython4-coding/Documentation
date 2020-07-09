***UIPartScrollBar.py - documentation - last updated on 18.6.2020 by uuk***
___

    variable IMAGE

    variable scroll_active

    variable scroll_inactive

    class UIScrollBar extends mcpython.state.ui.UIPart.UIPart
        
        class representing an scroll bar


        function __init__(self, position: tuple, scroll_distance: int, on_scroll=None)

            variable self.selected

            variable self.bar_position

            variable self.bar_sprite

            variable self.scroll_distance

            variable self.on_scroll

            variable self.active

        function move(self, delta: int)

        function bind_to_eventbus(self)

        function on_mouse_press(self, x, y, button, mod)

        function on_mouse_release(self, x, y, button, mod)

        function on_mouse_drag(self, x, y, dx, dy, button, mod)

        function on_draw(self)

        function get_status(self) -> float
            
            will return the status as an float between 0 and 1 where 0 is the downer end and 1 the upper


        function set_status(self, status: float)

        function set_size_respective(self, position: tuple, scroll_distance: int)