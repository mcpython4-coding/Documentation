***EventHandler.py - documentation - last updated on 14.5.2020 by uuk***
___

    class EventHandler
        function __init__(self)
        function create_bus(self, *args, active=True, **kwargs) -> event.EventBus.EventBus
        function activate_bus(self, bus: event.EventBus.EventBus)
        function deactivate_bus(self, bus: event.EventBus.EventBus)
        function call(self, eventname, *args, **kwargs)
        function __call__(self, *args, **kwargs)

    variable G.eventhandler


    variable PUBLIC_EVENT_BUS


    variable LOADING_EVENT_BUS
