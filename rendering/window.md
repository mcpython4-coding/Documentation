***window.py - documentation - last updated on 30.5.2020 by uuk***
___

    class Window extends pyglet.window.Window

        function __init__(self, *args, **kwargs)

            variable G.window

            variable self.exclusive
                Whether or not the window exclusively captures the mouse.

            variable self.flying
                When flying gravity has no effect and speed is increased.

            variable self.strafe
                Strafing is moving lateral to the direction you are facing,
                e.g. moving to the left or right while continuing to face forward.
                
                First element is -1 when moving forward, 1 when moving back, and 0
                otherwise. The second element is -1 when moving left, 1 when moving
                right, and 0 otherwise.

            variable self.sector
                Which sector the player is currently in.

            variable self.dy
                Velocity in the y (upward) direction.

            variable self.num_keys
                Convenience list of num keys, todo: move to config.py

            variable self.world
                Instance of the model that handles the world.

            variable self.label
                The label that is displayed in the top left of the canvas.

            variable self.label2

            variable self.label3

            variable self.cpu_usage

            variable self.cpu_usage_timer

            variable self.mouse_pressing
                storing mouse information

            variable self.mouse_position

            variable self.keys

            variable self.CROSSHAIRS_TEXTURE

        function reset_caption(self)

        function set_exclusive_mouse(self, exclusive)
            
            the game will ignore the mouse.


            variable self.exclusive

        function get_sight_vector(self)
            
            the player is looking.


            variable m
                y ranges from -90 to 90, or -pi/2 to pi/2, so m ranges from 0 to 1 and
                is 1 when looking ahead parallel to the ground and 0 when looking
                straight up or down.

            variable dy
                dy ranges from -1 to 1 and is -1 when looking straight down and 1 when
                looking straight up.

            variable dx

            variable dz

        function get_motion_vector(self)
            
            player.
            Returns
            -------
            vector : tuple of len 3
                Tuple containing the velocity in x, y, and z respectively.


                variable strafe

                variable y_angle

                variable x_angle

                variable dy

                variable dx

                variable dz

                variable dy

                variable dx

                variable dz

        function update(self, dt)
            
            clock.
            Parameters
            ----------
            dt : float
                The change in time since the last call.


                variable self.cpu_usage

                variable self.cpu_usage_timer

            variable sector

                variable self.sector

        function collide(self, position, height)
            
            is colliding with any blocks in the world.
            Parameters
            ----------
            position : tuple of len 3
                The (x, y, z) position to check for collisions at.
            height : int or float
                The height of the player.
            Returns
            -------
            position : tuple of len 3
                The new position of the player taking into account collisions.


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

                        variable blockstate

                                variable blockstate

                            variable self.dy
                                You are colliding with the ground or ceiling, so stop
                                falling / rising.

                            variable G.window.flying

                                variable dy

                                variable G.world.get_active_player().fallen_since_y

        function on_mouse_press(self, x, y, button, modifiers)
            
            amd modifier mappings.
            Parameters
            ----------
            x, y : int
                The coordinates of the mouse click. Always center of the screen if
                the mouse is captured.
            button : int
                Number representing mouse button that was clicked. 1 = left button,
                4 = right button.
            modifiers : int
                Number representing any modifying keys that were pressed when the
                mouse button was clicked.


            variable self.mouse_pressing[button]

        function on_mouse_release(self, x, y, button, modifiers)

        function on_mouse_drag(self, x, y, dx, dy, buttons, modifiers)

        function on_mouse_scroll(self, x, y, scroll_x, scroll_y)

        function on_mouse_motion(self, x, y, dx, dy)
            
            Parameters
            ----------
            x, y : int
                The coordinates of the mouse click. Always center of the screen if
                the mouse is captured.
            dx, dy : float
                The movement of the mouse.


            variable self.mouse_position

        function on_key_press(self, symbol, modifiers)
            
            mappings.
            Parameters
            ----------
            symbol : int
                Number representing the key that was pressed.
            modifiers : int
                Number representing any modifying keys that were pressed.


        function on_key_release(self, symbol, modifiers)
            
            mappings.
            Parameters
            ----------
            symbol : int
                Number representing the key that was pressed.
            modifiers : int
                Number representing any modifying keys that were pressed.


        function on_resize(self, width, height)
            


            variable self.label.y
                label

            variable self.label2.y

            variable self.label3.x

            variable self.label3.y

        function set_2d(self)
            


            variable viewport

        function set_3d(self, position=None, rotation=None)
            


            variable viewport

        function on_draw(self)
            


        function draw_focused_block(self)
            
            crosshairs.


            variable vector

            variable block

                variable block

        function draw_label(self)
            


                variable x

            variable chunk

            variable self.label.text

            variable vector

                variable blockname

                variable self.label2.text

                variable self.label3.y

                variable self.label3.y

                variable biomemap

            variable process

            variable mem_info

            variable used_m

            variable total_m

                variable self.label3.text

        function get_block_entity_info(self)

        function draw_reticle(self)
            


        function on_text(self, text)

        function on_close(self)