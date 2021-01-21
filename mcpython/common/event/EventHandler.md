***EventHandler.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
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