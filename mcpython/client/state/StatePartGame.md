***StatePartGame.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class HotKeys extends enum.Enum

        variable RELOAD_CHUNKS

        variable GAME_CRASH

        variable GET_PLAYER_POSITION

        variable CLEAR_CHAT

        variable COPY_BLOCK_OR_ENTITY_DATA

        variable TOGGLE_GAMEMODE_1_3

        variable RELOAD_TEXTURES

        function __init__(self, keys, event, min_press=0)

            variable self.keys

            variable self.event

            variable self.active

            variable self.min_press

            variable self.press_start

        function check(self)

        function blocks(self, symbol, mods) -> bool

    variable ALL_KEY_COMBOS

    @onlyInClient() class StatePartGame extends StatePart.StatePart

        variable NAME

        variable mouse_press_time

        variable block_looking_at

        variable double_space_cooldown

        variable set_cooldown

        variable void_damage_cooldown

        variable regenerate_cooldown

        variable hunger_heart_cooldown

        variable break_time

        static
        function calculate_new_break_time(cls)

        function __init__(
                self,
                activate_physics=True,
                activate_mouse=True,
                activate_keyboard=True,
                activate_3d_draw=True,
                activate_focused_block=True,
                glcolor3d=(1.0, 1.0, 1.0),
                activate_crosshair=True,
                activate_lable=True,
                clear_color=(0.5, 0.69, 1.0, 1),
                active_hotkeys=None,
                ):

                variable active_hotkeys

            variable self.activate_physics

            variable self.__activate_mouse

            variable self.activate_keyboard

            variable self.activate_3d_draw

            variable self.activate_focused_block_draw

            variable self.activate_crosshair

            variable self.active_lable

            variable self.color_3d

            variable self.clear_color

            variable self.active_hotkeys

        function set_mouse_active(self, active: bool)

        function get_mouse_active(self)

        variable activate_mouse

        function bind_to_eventbus(self)

        function on_update(self, dt: float)

                variable vector

                        variable self.block_looking_at

                        variable self.mouse_press_time

        function on_physics_update(self, dt: float)

        function on_left_click_interaction_update(self, dt: float)

            variable player

            variable selected_itemstack: mcpython.common.container.ItemStack.ItemStack

                variable vector

                    variable block

                    variable chunk

                                variable items

        function on_right_click_interaction_update(self, dt: float)

                                    variable self.mouse_press_time

                                variable instance

                                variable self.mouse_press_time

        function on_middle_click_interaction_update(self, dt: float)

                        variable slots: list

                                    variable ref_itemstack

                        variable old_itemstack

        function _update(self, dt: float)
            
            of the motion logic lives, along with gravity and collision detection.
            Parameters
            ----------
            dt : float
                The change in time since the last call.


            variable player

            variable speed

                variable block_inst

            variable d - distance covered this tick.

                variable shared.window.dy

                variable dy

            variable before

                variable player.fallen_since_y

            variable player.position

                variable self.void_damage_cooldown

            variable after

                variable self.regenerate_cooldown

                variable self.hunger_heart_cooldown

            variable ny

        function on_mouse_press(self, x: int, y: int, button: int, modifiers: int)

        function on_mouse_motion(self, x: int, y: int, dx: int, dy: int)

        function on_key_press(self, symbol: int, modifiers: int)

                variable shared.window.strafe[0]

                variable shared.window.strafe[0]

                variable shared.window.strafe[1]

                variable shared.window.strafe[1]

                    variable shared.world.get_active_player().flying

                    variable self.double_space_cooldown

                        variable shared.window.dy

                variable index

        function on_key_release(self, symbol: int, modifiers: int)

                variable shared.window.strafe[0]

                variable shared.window.strafe[0]

                variable shared.window.strafe[1]

                variable shared.window.strafe[1]

                variable self.double_space_cooldown

        function on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int)

        function on_draw_3d(self)

        function on_draw_2d(self)