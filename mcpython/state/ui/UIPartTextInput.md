***UIPartTextInput.py - documentation - last updated on 8.6.2020 by uuk***
___

    variable ALL_PATTERN

    variable INT_PATTERN

    variable INT_PATTERN_POSITIVE

    class UIPartTextInput extends UIPart.UIPart

        function __init__(self, size, position, anchor_ti="LD", anchor_window="LD", pattern=ALL_PATTERN, default_text="",
                text_size=10, on_text_update=None, on_enter_press=None, empty_overlay_text=""):

        function update_lable(self)

        function bind_to_eventbus(self)

        function on_draw_2d(self)

        function on_mouse_press(self, x, y, button, modifiers)

        function on_key_press(self, key, mod)

        function on_text(self, text: str)

        function reset(self): self.entered_text = self.default_text
                
                
                class TextInputTabHandler(mcpython.state.StatePart.StatePart):

    class TextInputTabHandler extends mcpython.state.StatePart.StatePart

        function __init__(self, textinputs: list)

            variable self.textinputs

        function bind_to_eventbus(self)

        function on_key_press(self, button, mod)