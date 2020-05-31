***EventHandler.py - documentation - last updated on 6.6.2020 by uuk***
___

    class EventHandler

        function __init__(self)

            variable self.buses

            variable self.active_buses

        function create_bus(self, *args, active=True, **kwargs) -> mcpython.event.EventBus.EventBus

        function activate_bus(self, bus: mcpython.event.EventBus.EventBus)

        function deactivate_bus(self, bus: mcpython.event.EventBus.EventBus)

        function call(self, eventname, *args, **kwargs)

    variable G.eventhandler

    variable PUBLIC_EVENT_BUS

    variable LOADING_EVENT_BUS