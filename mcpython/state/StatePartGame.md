***StatePartGame.py - documentation - last updated on 13.6.2020 by uuk***
___

    class HotKeys extends enum.Enum

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

    class StatePartGame extends StatePart.StatePart

        variable NAME

        variable mouse_press_time

        variable block_looking_at

        variable double_space_cooldown

        variable set_cooldown

        variable void_damage_cooldown

        variable regenerate_cooldown

        variable hunger_heart_cooldown

        variable braketime

        static
        function calculate_new_braketime(cls)

        function __init__(self, activate_physics=True, activate_mouse=True, activate_keyboard=True, activate_3d_draw=True,
                activate_focused_block=True, glcolor3d=(1., 1., 1.), activate_crosshair=True, activate_lable=True,
                clearcolor=(0.5, 0.69, 1.0, 1), active_hotkeys=ALL_KEY_COMBOS):

        function set_mouse_active(self, active: bool)

        function get_mouse_active(self): return self.__activate_mouse
                
                activate_mouse = property(get_mouse_active, set_mouse_active)
                
                def bind_to_eventbus(self):

        variable activate_mouse

        function bind_to_eventbus(self)

        function on_update(self, dt)

                variable vector

                        variable self.block_looking_at

                        variable self.mouse_press_time

        function on_physics_update(self, dt)

        function on_left_click_interaction_update(self, dt)

        function on_right_click_interaction_update(self, dt)

        function on_middle_click_interaction_update(self, dt)

        function _update(self, dt)
            
            of the motion logic lives, along with gravity and collision detection.
            Parameters
            ----------
            dt : float
                The change in time since the last call.


            variable player

            variable speed

                variable block_inst

            variable d - distance covered this tick.

                variable G.window.dy

                variable dy

            variable before

                variable player.fallen_since_y

            variable player.position

                variable self.void_damage_cooldown

            variable after

                variable self.regenerate_cooldown

                variable self.hunger_heart_cooldown

            variable ny

        function on_mouse_press(self, x, y, button, modifiers)

        function on_mouse_motion(self, x, y, dx, dy)

        function on_key_press(self, symbol, modifiers)

                variable G.window.strafe[0]

                variable G.window.strafe[0]

                variable G.window.strafe[1]

                variable G.window.strafe[1]

                    variable G.world.get_active_player().flying

                    variable self.double_space_cooldown

                        variable G.window.dy

                variable index

        function on_key_release(self, symbol, modifiers)

        function on_mouse_scroll(self, x, y, scroll_x, scroll_y)

        function on_draw_3d(self)

        function on_draw_2d(self)