***pyglet_binding.py - documentation - last updated on 23.8.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class PygletDataManager
        
        Binding manager for a pyglet backend with support for async stuff handling


        function __init__(self, side: mcpython.engine.asyncm.Manager.SpawnedProcessInfo)

            variable self.side

            variable self.windows

            variable self.event_loop

            variable self.platform_event_loop

            variable self.event_loop.has_exit

            variable self.event_loop.is_running

            variable self.side.call_regular

            variable win

            @win.event
            function on_close()

            @win.event
            function on_draw()

            variable module

            variable win_class

            variable win

            variable win.async_manager

            variable timeout
                todo: can we do some stuff async?

                variable self.event_loop.is_running

    function spawn_in(process_manager: mcpython.engine.asyncm.Manager.AsyncProcessManager)

            variable side.pyglet_manager