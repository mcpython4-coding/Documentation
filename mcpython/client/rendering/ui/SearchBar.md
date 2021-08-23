***SearchBar.py - documentation - last updated on 23.8.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class SearchBar

        function __init__(
                self,
                change_callback=None,
                enter_callback=None,
                exit_callback=None,
                enable_mouse_to_enter=False,
                ):

            variable self.change_callback

            variable self.enter_callback

            variable self.exit_callback

            variable self.position

            variable self.entry_size

            variable self.underlying_event_bus: mcpython.engine.event.EventBus.EventBus

            variable self.enable_mouse_to_enter

            variable self.inner_text

            variable self.enabled

            variable self.label

        function close(self)

        function on_key_press(self, symbol, mod)

        function on_text(self, text: str)

        function on_mouse_press(self, x, y, button, mod)

        function enable(self)

        function disable(self)

        function draw(self)

        function is_position_in_field(self, x: int, y: int)