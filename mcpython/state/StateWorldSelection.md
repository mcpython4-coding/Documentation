***StateWorldSelection.py - documentation - last updated on 18.6.2020 by uuk***
___

    variable MISSING_TEXTURE

    variable WORLD_SELECTION

    variable WORLD_SELECTION_SELECT

    class StateWorldSelection extends State.State

        variable NAME

        function __init__(self)

            variable self.world_data - the data representing the world list; first goes first in list from above

            variable self.selected_world

            variable self.selection_sprite

        function bind_to_eventbus(self)

        function on_resize(self, wx, wy)

        function get_parts(self) -> list

        function on_mouse_press(self, x, y, button, modifiers)

        function on_scroll(self, x, y, dx, dy, button, mod, status)

        function on_mouse_scroll(self, x, y, dx, dy)

        function recalculate_sprite_position(self)

                variable self.parts[4].active

        function on_key_press(self, symbol, modifiers)

        function on_draw_2d_post(self)

        function activate(self)

        function reload_world_icons(self)

        function on_back_press(self, *_)

        function on_new_world_press(self, *_)

        function on_world_load_press(self, *_)

        function enter_world(self, number: int)

    variable worldselection

    function create()