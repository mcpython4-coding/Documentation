***EventBus.py - documentation - last updated on 23.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class CancelAbleEvent

        function __init__(self)

            variable self.canceled

        function cancel(self)

    class EventBus
        
        An class for bundling event calls to instances of this to make it easy to add/remove big event notations.
        It should be something like an sub-event-handler
        todo: make thread-safe


        function __init__(
                self,
                args: typing.Iterable = (),
                kwargs: dict = None,
                crash_on_error: bool = True,
                ):

            variable args: typing.Iterable

            variable kwargs: dict

            variable crash_on_error: bool
            
            Creates an new EventBus instance
            :param args: the args to send to every function call
            :param kwargs: the kwargs to send to every function call
            :param crash_on_error: if an crash should be triggered on an exception of an func


                variable kwargs

            variable self.event_subscriptions - name -> (function, args, kwargs)[

            variable self.popped_event_subscriptions

            variable self.extra_arguments

            variable self.crash_on_error

            variable self.sub_buses

            variable self.id

        function subscribe(
                self, event_name: str, function: typing.Callable, *args, info=None, **kwargs
                ):
            
            Add an function to the event bus by event name. If event name does NOT exists, it will be created locally
            :param event_name: the event to listen to on this bis
            :param function: the function that should be called when event is send
            :param args: the args to give
            :param kwargs: the kwargs to give
            :param info: an info to give for the caller


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


        function call_until(
                self,
                event_name: str,
                check_function: typing.Callable[[typing.Any], bool],
                *args,
                **kwargs
                ):
            
            Will call the event stack until an check_function returns True or all subscriptions where done
            :param event_name: the name of the event
            :param check_function: the check function to call with
            :param args: the args to call with
            :param kwargs: the kwargs to call with
            :return: the result in the moment of True or None


                variable start

                    variable result

                    variable dif

        function activate(self)

        function deactivate(self)

        function create_sub_bus(self, *args, activate=True, **kwargs)

        function call_as_stack(self, event_name, *args, amount=1, **kwargs)

        function resetEventStack(self, event_name: str)
            
            Will reset all event subscriptions which where popped from the normal list
            :param event_name: the name of the event to restore
