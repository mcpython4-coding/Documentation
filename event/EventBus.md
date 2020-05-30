***EventBus.py - documentation - last updated on 30.5.2020 by uuk***
___

    class EventBus
        
        An class for bundling event calls to instances of this to make it easy to add/remove big event notations.
        It should be something like an sub-eventhandler


        function __init__(self, args=(), kwargs={}, crash_on_error=True)

            variable self.event_subscriptions - name -> (function, args, kwargs)[

            variable self.extra_arguments

            variable self.crash_on_error

            variable self.sub_buses

            variable self.id

        function subscribe(self, eventname: str, function, *args, info=None, **kwargs)
            
            add an function to the event bus by event name. If event name does NOT exists, it will be created localy
            :param eventname: the event to listen to on this bis
            :param function: the function that should be called when event is sended
            :param args: the args to give
            :param kwargs: the kwargs to give
            :param info: an info to give for the caller


        function subscribe_package_load(self, eventname, package)

        function unsubscribe(self, event_name: str, function)
            
            remove an function from the event bus
            :param event_name: the event name the function was registered to
            :param function: the function itself
            :raise ValueError: when event name is unknown OR function was never assigned


        function call(self, event_name, *args, **kwargs)
            
            call an event on this event bus. also works when deactivated
            :param event_name: the name of the event to call
            :param args: arguments to give
            :param kwargs: kwargs to give
            :return: an list of tuple of (return value, info)


        function call_until(self, event_name, check_function, *args, **kwargs)

        function activate(self)

        function deactivate(self)

        function create_sub_bus(self, *args, activate=True, **kwargs)

        function call_as_stack(self, eventname, *args, amount=1, **kwargs)