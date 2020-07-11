***EventBus.py - documentation - last updated on 11.7.2020 by uuk***
___

    class CancelAbleEvent

        function __init__(self)

            variable self.canceled

        function cancel(self)

    class EventBus
        
        An class for bundling event calls to instances of this to make it easy to add/remove big event notations.
        It should be something like an sub-eventhandler
        todo: make thread-safe


        function __init__(self, args: typing.Iterable = (), kwargs: dict = None, crash_on_error: bool = True)
            
            Creates an new EventBus instance
            :param args: the args to send to every function call
            :param kwargs: the kwargs to send to every function call
            :param crash_on_error: if an crash should be triggered on an exception of an func


            variable self.event_subscriptions - name -> (function, args, kwargs)[

            variable self.popped_event_subscriptions

            variable self.extra_arguments

            variable self.crash_on_error

            variable self.sub_buses

            variable self.id

        function subscribe(self, eventname: str, function: typing.Callable, *args, info=None, **kwargs)
            
            add an function to the event bus by event name. If event name does NOT exists, it will be created localy
            :param eventname: the event to listen to on this bis
            :param function: the function that should be called when event is sended
            :param args: the args to give
            :param kwargs: the kwargs to give
            :param info: an info to give for the caller


        @deprecation.deprecated("dev4-3", "a1.3.0")
        function subscribe_package_load(self, eventname, package)

        function unsubscribe(self, event_name: str, function)
            
            remove an function from the event bus
            :param event_name: the event name the function was registered to
            :param function: the function itself
            :raise ValueError: when event name is unknown OR function was never assigned


        function call(self, event_name: str, *args, **kwargs)
            
            call an event on this event bus. also works when deactivated
            :param event_name: the name of the event to call
            :param args: arguments to give
            :param kwargs: kwargs to give
            :return: an list of tuple of (return value, info)


        function call_cancelable(self, event_name: str, *args, **kwargs)
            
            Will call an cancel able event.
            Works the same way as call, but will use call_until() with an CancelAbleEvent as first parameter which is checked after each call
            :param event_name: the name to call
            :param args: args to call with
            :param kwargs:  kwargs to call with
            :return: if it was canceled or not


        function call_until(self, event_name: str, check_function: typing.Callable[[typing.Any], bool], *args, **kwargs)
            
            Will call the event stack until an check_function returns True or all subscriptions where done
            :param event_name: the name of the event
            :param check_function: the check function to call with
            :param args: the args to call with
            :param kwargs: the kwargs to call with
            :return: the result in the moment of True or None


        function activate(self)

        function deactivate(self)

        function create_sub_bus(self, *args, activate=True, **kwargs)

        function call_as_stack(self, eventname, *args, amount=1, **kwargs)

        function resetEventStack(self, eventname: str)
            
            Will reset all event subscriptions which where popped from the normal list
            :param eventname: the name of the event to restore
