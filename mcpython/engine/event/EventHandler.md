***EventHandler.py - documentation - last updated on 23.8.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class EventHandler

        function __init__(self)

            variable self.buses

            variable self.active_buses

        function create_bus(self, *args, active=True, **kwargs) -> EventBus

        function activate_bus(self, bus: EventBus)

        function deactivate_bus(self, bus: EventBus)

        function call(self, event_name, *args, **kwargs)

        function call_cancelable(self, event_name, *args, **kwargs)

        function __call__(self, *args, **kwargs)

    variable shared.event_handler

    variable PUBLIC_EVENT_BUS

    variable LOADING_EVENT_BUS