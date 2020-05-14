***StatePartGame.py - documentation - last updated on 14.5.2020 by uuk***
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

            variable status

                variable self.active

                variable self.active

                variable self.press_start

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

        static function calculate_new_braketime(cls)

            variable vector

            variable blockpos

            variable block

                variable cls.braketime - no braketime because no block

                variable hardness

                variable itemstack

                variable istool

                variable toollevel

                    variable cls.braketime

                    variable cls.braketime

            variable self.activate_physics

            variable self.__activate_mouse

            variable self.activate_keyboard

            variable self.activate_3d_draw

            variable self.activate_focused_block_draw

            variable self.activate_crosshair

            variable self.active_lable

            variable self.glcolor3d

            variable self.clearcolor

            variable self.active_hotkeys

        function set_mouse_active(self, active: bool)

            variable self.__activate_mouse

        function get_mouse_active(self)

        variable activate_mouse

        function bind_to_eventbus(self)

            variable state

        function on_update(self, dt)

                variable vector

                        variable self.block_looking_at

                        variable self.mouse_press_time

        function on_physics_update(self, dt)

            variable m

            variable dt

        function on_left_click_interaction_update(self, dt)

                variable vector

                    variable block

                    variable chunk

                                variable items

        function on_right_click_interaction_update(self, dt)

                    variable itemfood

                        variable self.set_cooldown

                variable vector

                        variable slot

                            variable py

                                variable chunk

                                variable self.mouse_press_time

        function on_middle_click_interaction_update(self, dt)

                variable vector

                    variable chunk

                    variable self.mouse_press_time

                    variable block

                    variable itemstack

                    variable block

                    variable selected_slot

                        variable inventory

                        variable slots: list

                                    variable sslot

                        variable old_itemstack

        function _update(self, dt)
            
            of the motion logic lives, along with gravity and collision detection.
            Parameters
            ----------
            dt : float
                The change in time since the last call.


            variable speed

                variable block_inst

            variable d - distance covered this tick.

                variable G.window.dy

                variable dy

            variable before

                variable G.world.get_active_player().fallen_since_y

            variable G.world.get_active_player().position

                variable self.void_damage_cooldown

            variable after

                variable self.regenerate_cooldown

                variable self.hunger_heart_cooldown

            variable ny

        function on_mouse_press(self, x, y, button, modifiers)

            variable slot

            variable vector

            variable block

            variable cancel

                    variable cancel

                    variable cancel

                variable self.set_cooldown

                variable G.window.mouse_pressing[button]

        function on_mouse_motion(self, x, y, dx, dy)

                variable m

                variable y

                variable G.world.get_active_player().rotation

        function on_key_press(self, symbol, modifiers)

                variable G.window.strafe[0]

                variable G.window.strafe[0]

                variable G.window.strafe[1]

                variable G.window.strafe[1]

                    variable G.window.flying

                    variable self.double_space_cooldown

                        variable G.window.dy

                variable index

        function on_key_release(self, symbol, modifiers)

                variable G.window.strafe[0]

                variable G.window.strafe[0]

                variable G.window.strafe[1]

                variable G.window.strafe[1]

                variable self.double_space_cooldown

        function on_mouse_scroll(self, x, y, scroll_x, scroll_y)

                variable G.world.get_active_player().active_inventory_slot

        function on_draw_3d(self)

        function on_draw_2d(self)