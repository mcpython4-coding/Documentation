***window.py - documentation - last updated on 13.5.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class NoWindow
        
        Class simulating an window for the no-window mode
        todo: add some more functions here


        function __init__(self, *args, **kwargs)

            variable self.width

        function get_size(self)

        function push_handlers(self, handler)

        function close(self)

        function set_caption(self, caption: str)

        function set_icon(self, *args)

        function set_fullscreen(self, state: bool)

        function set_size(self, width, height)

        function set_minimum_size(self, width, height)

        function set_maximum_size(self, width, height)

    @onlyInClient() class Window extends pyglet.window.Window if not shared.NO_WINDOW else NoWindow
        
        Class representing the game window.
        Interacts with the pyglet backend.
        todo: move the pyglet-engine-calls to here to make it possible to exchange the backend


        function __init__(self, *args, **kwargs)
            
            creates an new window-instance
            :param args: args send to pyglet.window.Window-constructor
            :param kwargs: kwargs send to pyglet.window.Window-constructor


            variable shared.window - write window instance to globals.py for sharing

            variable self.exclusive
                Whether or not the window exclusively captures the mouse.

            variable self.strafe
                Strafing is moving lateral to the direction you are facing,
                e.g. moving to the left or right while continuing to face forward.
                
                First element is -1 when moving forward, 1 when moving back, and 0
                otherwise. The second element is -1 when moving left, 1 when moving
                right, and 0 otherwise. todo: move to player's movement-attribute

            variable self.sector - todo: move to player
                Which sector the player is currently in.

            variable self.dy - todo: move to player
                Velocity in the y (upward) direction.

            variable self.num_keys
                Convenience list of num keys, todo: move to config.py

            variable self.label
                The label that is displayed in the top left of the canvas.  todo: move to separated class

            variable self.label2

            variable self.label3

            variable self.cpu_usage
                todo: move to separated class

            variable self.cpu_usage_timer - todo: move to separated class

            variable self.mouse_pressing
                storing mouse information todo: use pyglet's mouse handler

            variable self.mouse_position

            variable self.draw_profiler - todo: move to separated class

            variable self.tick_profiler - todo: move to separated class

            variable self.keys - key handler from pyglet

            variable self.CROSSHAIRS_TEXTURE
                todo: move to separated class

        function load(self)

            variable self.CROSSHAIRS_TEXTURE

        function print_profiler(self, dt=None)
            
            Will print the enabled profiler(s)
            todo: move to separated Profiler class


        function reset_caption(self)
            
            Will set the caption of the window to the default one


        function set_exclusive_mouse(self, exclusive)
            
            If `exclusive` is True, the game will capture the mouse and not display it. Otherwise,
            the mouse is free to move


        static
        function get_sight_vector(cls)
            
            Returns the current line of sight vector indicating the direction
            the player is looking.
            todo: move to player


        function get_motion_vector(self) -> tuple
            
            Returns the current motion vector indicating the velocity of the
            player.
            :return: vector: Tuple containing the velocity in x, y, and z respectively.
            todo: integrate into player movement


        function update(self, dt: float)
            
            This method is scheduled to be called repeatedly by the pyglet clock.
            :param dt: The change in time since the last call.
            todo: move to TickHandler


                variable self.cpu_usage

                variable self.cpu_usage_timer

            variable sector

                variable self.sector

        function collide(self, position: tuple, height: int, previous=None)
            
            Checks to see if the player at the given `position` and `height`
            is colliding with any blocks in the world.
            :param position: The (x, y, z) position to check for collisions at.
            :param height: The height of the player.
            :param previous: the previous position the player was, for the block collision API, optional
            :return The new position of the player taking into account collisions.
            todo: move to physic package
            todo: make player based
            todo: make account player & block hit box


            variable previous_positions

            variable pad
                How much overlap with a dimension of a surrounding block you need to
                have to count as a collision. If 0, touching terrain at all counts as
                a collision. If .49, you sink into the ground, as if walking through
                tall grass. If >= .5, you'll fall through the ground.

            variable p

            variable np

                    variable d
                        How much overlap you have with this dimension.

                        variable op

                        variable chunk

                        variable block

                        variable blockstate

                                variable blockstate

                            variable self.dy
                                You are colliding with the ground or ceiling, so stop
                                falling / rising.

                            variable shared.world.get_active_player().flying

                                variable dy

                                variable shared.world.get_active_player().fallen_since_y

        function get_colliding_blocks(self, position: tuple, height: int) -> tuple
            
            Similar to collide(), but will simply return an list of block-positions the player collides with and an list of blocks the player is in, but should not collide
            :param position: the position to use as center
            :param height: the height of the player
            :return: an tuple of colliding full blocks and colliding no collision blocks


        function on_mouse_press(self, x: int, y: int, button: int, modifiers: int)
            
            Called when a mouse button is pressed. See pyglet docs for button amd modifier mappings.
            :param x, y: The coordinates of the mouse click. Always center of the screen if the mouse is captured.
            :param button: Number representing mouse button that was clicked. 1 = left button, 4 = right button.
                [access via pyglet.window.mouse]
            :param modifiers : Number representing any modifying keys that were pressed when the mouse button was clicked.
                [access via pyglet.window.key.MOD_[...]]


            variable self.mouse_pressing[button]

        function on_mouse_release(self, x, y, button, modifiers)
            
            called when an button is released with the same argument as on_mouse_press


        function on_mouse_drag(
                self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int
                ):
            
            called when the mouse moves over the screen while one or more buttons are pressed
            :param x: the new x position
            :param y: the new y position
            :param dx: the delta x
            :param dy: the delta y
            :param buttons: the buttons pressed
            :param modifiers: the modifiers pressed


            variable self.mouse_position

        function on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int)
            
            called by pyglet when the mouse wheel is spinned
            :param x: the new x scroll
            :param y: the new y scroll
            :param scroll_x: the delta x
            :param scroll_y: the detla y


        function on_mouse_motion(self, x: int, y: int, dx: float, dy: float)
            
            Called when the player moves the mouse.
            :param x, y: The coordinates of the mouse click. Always center of the screen if the mouse is captured.
            :param dx, dy : The movement of the mouse.
            todo: use pyglet's MouseHandler for tracking the mouse position and buttons


            variable self.mouse_position

        function on_key_press(self, symbol: int, modifiers: int)
            
            Called when the player presses a key. See pyglet docs for key mappings.
            :param symbol: Number representing the key that was pressed.
            :param modifiers: Number representing any modifying keys that were pressed.


        function on_key_release(self, symbol, modifiers)
            
            Called when the player releases a key. See pyglet docs for key mappings.
            :param symbol: Number representing the key that was pressed.
            :param modifiers: Number representing any modifying keys that were pressed.


        function on_resize(self, width: int, height: int)
            
            Called when the window is resized to a new `width` and `height`.


        function set_2d(self)

        function set_3d(self, position=None, rotation=None)

        function on_draw(self)
            
            Called by pyglet to draw the canvas.
            todo: move to separated configurable rendering pipeline


        function draw_focused_block(self)
            
            Draw black edges around the block that is currently under the crosshairs.
            todo: move to special helper class


        function draw_label(self)
            
            Draw the label in the top left of the screen.
            todo: move to special helper class


        function get_block_entity_info(self)
            
            used by hotkey for copying entity data to the clipboard
            todo: move to special helper class


            variable vector

                variable blockname

                    variable blockname

        function draw_reticle(self)
            
            Draw the crosshairs in the center of the screen.
            todo: move to special helper class


        function on_text(self, text: str)
            
            Called by pyglet with decoded key values when an text is entered
            :param text: the text entered


        function on_close(self)
            
            Called when the window tries to close itself
            cleans up some stuff before closing
