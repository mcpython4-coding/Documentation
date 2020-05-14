***UIPartTextInput.py - documentation - last updated on 14.5.2020 by uuk***
___

    variable ALL_PATTERN


    variable INT_PATTERN


    variable INT_PATTERN_POSITIVE


    class UIPartTextInput extends UIPart.UIPart
        function update_lable(self)
        function bind_to_eventbus(self)
        function on_draw_2d(self)
        function on_mouse_press(self, x, y, button, modifiers)
        function on_key_press(self, key, mod)
        function on_text(self, text: str)
        function reset(self)

    class TextInputTabHandler extends state.StatePart.StatePart
        function __init__(self, textinputs: list)
        function bind_to_eventbus(self)
        function on_key_press(self, button, mod)