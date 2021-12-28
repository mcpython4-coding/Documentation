***util.py - documentation - last updated on 28.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable TAB_TEXTURE

    function getTabTexture()

        variable TAB_TEXTURE

    class CreativeTabScrollbar
        
        Creative tab scrollbar
        Feel free to re-use for other stuff
        todo: use batches


        variable SCROLLBAR_SIZE

        variable NON_SELECTED_SCROLLBAR

        variable SELECTED_SCROLLBAR

            variable cls.NON_SELECTED_SCROLLBAR

            variable cls.SELECTED_SCROLLBAR

        function __init__(self, callback: typing.Callable[[int], None], scroll_until: int = 1)

            variable self.callback

            variable self.scroll_until

            variable self.currently_scrolling

            variable self.underlying_event_bus: mcpython.engine.event.EventBus.EventBus

            variable self.position

            variable self.height

            variable self.is_hovered

        function on_mouse_drag(self, x, y, dx, dy, buttons, modifiers)

        function on_mouse_move(self, x, y, dx, dy)

        function on_mouse_scroll(self, x, y, sx, sy)

        function on_key_press(self, symbol, modifiers)

        function get_scrollbar_position(self)

        function draw_at(self, lower_left: typing.Tuple[int, int], height: int)

        function activate(self)

        function deactivate(self)

        function set_max_value(self, value: int)

            variable self.scroll_until

            variable self.currently_scrolling