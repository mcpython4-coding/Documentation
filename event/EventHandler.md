***EventHandler.py - documentation - last updated on 30.5.2020 by uuk***
___

    class EventHandler

        function __init__(self)

            variable self.buses

            variable self.active_buses

        function create_bus(self, *args, active=True, **kwargs) -> event.EventBus.EventBus

        function activate_bus(self, bus: event.EventBus.EventBus)

        function deactivate_bus(self, bus: event.EventBus.EventBus)

        function call(self, eventname, *args, **kwargs)

    variable G.eventhandler

    variable PUBLIC_EVENT_BUS

    variable LOADING_EVENT_BUS