***Scrollbar.py - documentation - last updated on 13.11.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ScrollbarRenderer

        function __init__(
                self,
                texture,
                position: typing.Tuple[int, int],
                height: int,
                steps: int,
                per_page_button=1,
                on_progress_change=None,
                enable_key_progress_changes=True,
                ):

            variable self.texture

            variable self.position

            variable self.height

            variable self.steps

            variable self.per_page_button

            variable self.current_step

            variable self.on_progress_change

            variable self.enable_key_progress_changes

        function on_activate(self)

        function on_deactivate(self)

        function on_key_press(self, symbol, modifiers)

                    variable self.current_step

                    variable self.current_step

                    variable self.current_step

                    variable self.current_step

                variable self.current_step

                variable self.current_step

        function draw(self, offset: typing.Tuple[int, int])