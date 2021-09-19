***WorldListState.py - documentation - last updated on 19.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable MISSING_TEXTURE

    variable WORLD_SELECTION

    variable WORLD_SELECTION_SELECT

    @onlyInClient() class WorldList extends AbstractState.AbstractState

        variable NAME

        function __init__(self)

            variable self.world_data

        function create_state_renderer(self) -> typing.Any

        function bind_to_eventbus(self)

        function on_resize(self, wx, wy)

        function create_state_parts(self) -> list

        function on_mouse_press(self, x, y, button, modifiers)

        function on_scroll(self, x, y, dx, dy, button, mod, status)

        function on_mouse_scroll(self, x, y, dx, dy)

        function recalculate_sprite_position(self)

                variable self.parts[-1].active

        function on_key_press(self, symbol, modifiers)

        function activate(self)

        function reload_world_icons(self)

        function on_back_press(self, *_)

        function on_new_world_press(self, *_)

        function on_delete_press(self, *_)

        function on_world_load_press(self, *_)

        function enter_world(self, number: int)

    variable world_selection

    @onlyInClient()
    function create()