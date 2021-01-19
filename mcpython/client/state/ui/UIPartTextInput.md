***UIPartTextInput.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    variable ALL_PATTERN

    variable INT_PATTERN

    variable INT_PATTERN_POSITIVE

    @onlyInClient() class UIPartTextInput extends UIPart.UIPart

        function __init__(
                self,
                size,
                position,
                anchor_ti="LD",
                anchor_window="LD",
                pattern=ALL_PATTERN,
                default_text="",
                text_size=10,
                on_text_update=None,
                on_enter_press=None,
                empty_overlay_text="",
                ):

            variable self.pattern

            variable self.default_text

            variable self.text_size

            variable self.selected

            variable self.on_text_update

            variable self.on_enter_press

            variable self.lable

            variable self.empty_overlay_text

        function update_lable(self)

        function bind_to_eventbus(self)

        function on_draw_2d(self)

        function on_mouse_press(self, x, y, button, modifiers)

        function on_key_press(self, key, mod)

        function on_text(self, text: str)

        function reset(self)

    @onlyInClient() class TextInputTabHandler extends mcpython.client.state.StatePart.StatePart

        function __init__(self, textinputs: list)

            variable self.textinputs

        function bind_to_eventbus(self)

        function on_key_press(self, button, mod)