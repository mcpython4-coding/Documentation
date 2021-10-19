***GameViewStatePart.py - documentation - last updated on 19.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    function get_block_break_time(block, itemstack)

        variable hardness

        variable is_tool

        variable tool_level

    class GameView extends AbstractStatePart.AbstractStatePart

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
                gl_color_3d=(1.0, 1.0, 1.0),
                activate_crosshair=True,
                activate_label=True,
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

            variable self.active_label

            variable self.color_3d

            variable self.clear_color

            variable self.active_hotkeys

        function set_mouse_active(self, active: bool)

        function get_mouse_active(self)

        variable activate_mouse

        function create_state_renderer(self) -> typing.Any

        function bind_to_eventbus(self)

        function on_update(self, dt: float)

                    variable vector

                            variable self.block_looking_at

                            variable self.mouse_press_time

        function on_physics_update(self, dt: float)

            variable m

            variable dt

                variable player

        function on_left_click_interaction_update(self, dt: float)

                variable player

                variable vector

                    variable chunk

                        variable selected_itemstack: mcpython.common.container.ResourceStack.ItemStack

                        variable block

                                variable items

        function on_right_click_interaction_update(self, dt: float)

            variable player

            variable slot

            variable active_itemstack

                    variable food

                        variable self.set_cooldown

                variable vector

                        variable py

                            variable chunk

                                variable self.mouse_press_time

                            variable instance

                            variable self.mouse_press_time

        function on_middle_click_interaction_update(self, dt: float)

                    variable chunk

                    variable self.mouse_press_time

                    variable block

                    variable itemstack

                    variable block

                    variable selected_slot

                        variable slots

                                    variable ref_itemstack

                        variable old_itemstack

        function physics_update_internal(self, dt: float, player)
            
            Internal implementation of the `update()` method. This is where most
            of the motion logic lives, along with gravity and collision detection.
            todo: on server, do for all players
            Parameters
            ----------
            dt : float
                The change in time since the last call.


            variable before

                variable player.fallen_since_y

            variable player.position

                variable self.void_damage_cooldown

        function calculate_player_hearts(self, dt, player)

        function update_player_chunks(self, before, player)

        function calculate_motion(self, dt: float, player) -> typing.Tuple[float, float, float]

            variable speed

                variable block_inst

            variable d - distance covered this tick.

                variable shared.window.dy

                variable dy

        function on_mouse_press(self, x: int, y: int, button: int, modifiers: int)

            variable slot

            variable vector

            variable block

            variable cancel

                    variable cancel

                    variable cancel

                variable self.set_cooldown

                variable shared.window.mouse_pressing[button]

        function on_mouse_motion(self, x: int, y: int, dx: int, dy: int)

        function on_key_press(self, symbol: int, modifiers: int)

                variable player.strafe[0]

                variable player.strafe[0]

                variable player.strafe[1]

                variable player.strafe[1]

                    variable player.flying

                    variable self.double_space_cooldown

                        variable shared.window.dy

                variable index

        function on_key_release(self, symbol: int, modifiers: int)

            variable player

                variable player.strafe[0]

                variable player.strafe[0]

                variable player.strafe[1]

                variable player.strafe[1]

                variable self.double_space_cooldown

        function on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int)

                variable player.active_inventory_slot