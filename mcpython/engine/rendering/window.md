***window.py - documentation - last updated on 5.2.2022 by uuk***
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

    @onlyInClient() class Window extends  pyglet.window.Window if not shared.NO_WINDOW and shared.IS_CLIENT else NoWindow 
        
        Class representing the game window.
        Interacts with the pyglet backend.
        todo: move the pyglet-engine-calls to here to make it possible to exchange the backend


        function __init__(self, *args, **kwargs)
            
            Creates a new window-instance
            :param args: args send to pyglet.window.Window-constructor
            :param kwargs: kwargs send to pyglet.window.Window-constructor


            variable shared.window
                write window instance to globals.py for sharing

            variable self.exclusive
                Whether the window exclusively captures the mouse.

            variable self.sector - todo: move to player
                Which sector the player is currently in.

            variable self.dy - todo: move to player
                Velocity in the y (upward) direction.

                variable self.num_keys
                    Convenience list of num keys, todo: move to config.py

                variable self.keys - key handler from pyglet

                variable self.mouse_pressing
                    storing mouse information todo: use pyglet's mouse handler

                variable self.mouse_position

                variable self.label
                    The label that is displayed in the top left of the canvas.  todo: move to separated class

                variable self.label2

                variable self.label3

            variable self.cpu_usage
                todo: move both to separated class

            variable self.cpu_usage_timer

            variable self.CROSSHAIRS_TEXTURE
                todo: move to separated class

        function load(self)

                variable self.CROSSHAIRS_TEXTURE

        function reset_caption(self)
            
            Will set the caption of the window to the default one


        function set_exclusive_mouse(self, exclusive: bool)
            
            If `exclusive` is True, the game will capture the mouse and not display it. Otherwise,
            the mouse is free to move


        static
        function get_sight_vector(cls)
            
            Returns the current line of sight vector indicating the direction
            the player is looking.
            todo: move to player or some util system


        function update(self, dt: float)
            
            This method is scheduled to be called repeatedly by the pyglet clock.
            :param dt: The change in time since the last call.


                variable self.cpu_usage

                variable self.cpu_usage_timer

        @onlyInClient()
        function on_mouse_press(self, x: int, y: int, button: int, modifiers: int)
            
            Called when a mouse button is pressed. See pyglet docs for button amd modifier mappings.
            :param x, y: The coordinates of the mouse click. Always center of the screen if the mouse is captured.
            :param button: Number representing mouse button that was clicked. 1 = left button, 4 = right button.
                [access via pyglet.window.mouse]
            :param modifiers : Number representing any modifying keys that were pressed when the mouse button was clicked.
                [access via pyglet.window.key.MOD_[...]]


            variable self.mouse_pressing[button]

        @onlyInClient()
        function on_mouse_release(self, x, y, button, modifiers)
            
            Called when an button is released with the same argument as on_mouse_press


        @onlyInClient()
        function on_mouse_drag(
                self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int
                ):
            
            Called when the mouse moves over the screen while one or more buttons are pressed
            :param x: the new x position
            :param y: the new y position
            :param dx: the delta x
            :param dy: the delta y
            :param buttons: the buttons pressed
            :param modifiers: the modifiers pressed


            variable self.mouse_position

        @onlyInClient()
        function on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int)
            
            Called by pyglet when the mouse wheel is spun
            :param x: the new x scroll
            :param y: the new y scroll
            :param scroll_x: the delta x
            :param scroll_y: the delta y


        @onlyInClient()
        function on_mouse_motion(self, x: int, y: int, dx: float, dy: float)
            
            Called when the player moves the mouse.
            :param x y: The coordinates of the mouse click. Always center of the screen if the mouse is captured.
            :param dx dy: The movement of the mouse.
            todo: use pyglet's MouseHandler for tracking the mouse position and buttons


            variable self.mouse_position

        @onlyInClient()
        function on_key_press(self, symbol: int, modifiers: int)
            
            Called when the player presses a key. See pyglet docs for key mappings.
            :param symbol: Number representing the key that was pressed.
            :param modifiers: Number representing any modifying keys that were pressed.


                    variable shared.profiler

                    variable shared.profiler
                        os.makedirs(shared.build+"/profiles", exist_ok=True)
                        shared.profiler.dump_stats(shared.build+"/profiles/"+str(time.time())+".txt")

        @onlyInClient()
        function on_key_release(self, symbol, modifiers)
            
            Called when the player releases a key. See pyglet docs for key mappings.
            :param symbol: Number representing the key that was pressed.
            :param modifiers: Number representing any modifying keys that were pressed.


        @onlyInClient()
        function on_resize(self, width: int, height: int)
            
            Called when the window is resized to a new `width` and `height`.


            @onlyInClient()
            @name_is_static("pyglet", lambda: pyglet)
            function set_2d(self)

            @onlyInClient()
            @name_is_static("pyglet", lambda: pyglet)
            function set_3d(self, position=None, rotation=None)

                    variable shared.rendering_helper.default_3d_stack

            @onlyInClient()
            @name_is_static("pyglet", lambda: pyglet)
            function on_draw(self)
                
                Called by pyglet to draw the canvas.
                todo: move to separated configurable rendering pipeline


        @onlyInClient()
        function draw_focused_block(self)
            
            Draw black edges around the block that is currently under the crosshairs.
            todo: move to special helper class


        @onlyInClient()
        function draw_label(self)
            
            Draw the label in the top left of the screen.
            todo: move to special helper class


            variable vector

                variable blockname

                    variable blockname

                variable self.label2.text

                variable self.label3.y

                variable self.label3.y

                variable biomemap

                variable biome

            variable process

            variable mem_info

            variable used_m

            variable total_m

                variable self.label3.text

        function get_block_entity_info(self)
            
            used by hotkey for copying entity data to the clipboard
            todo: move to special helper class


            variable vector

                variable blockname

                    variable blockname

        @onlyInClient()
        function draw_reticle(self)
            
            Draw the crosshairs in the center of the screen.
            todo: move to special helper class


        function on_text(self, text: str)
            
            Called by pyglet with decoded key values when an text is entered
            :param text: the text entered


        function on_close(self)
            
            Called when the window tries to close itself
            cleans up some stuff before closing
