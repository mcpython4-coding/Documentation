***StateWorldSelection.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    variable MISSING_TEXTURE

    variable WORLD_SELECTION

    variable WORLD_SELECTION_SELECT

    @onlyInClient() class StateWorldSelection extends State.State

        variable NAME

        function __init__(self)

            variable self.world_data

        function bind_to_eventbus(self)

        function on_resize(self, wx, wy)

        function get_parts(self) -> list

        function on_mouse_press(self, x, y, button, modifiers)

        function on_scroll(self, x, y, dx, dy, button, mod, status)

        function on_mouse_scroll(self, x, y, dx, dy)

        function recalculate_sprite_position(self)

                variable self.parts[-1].active

        function on_key_press(self, symbol, modifiers)

        function on_draw_2d_post(self)

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