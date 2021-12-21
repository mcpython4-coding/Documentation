***EventBus.py - documentation - last updated on 20.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class CancelAbleEvent
        
        Tracker class for a cancelable event


        function __init__(self)

            variable self.canceled

        function cancel(self)

    class EventBus
        
        An class for bundling event calls to instances of this to make it easy to add/remove big event notations.
        It should be something like an sub-event-handler
        todo: make thread-safe


        function __init__(
                self,
                crash_on_error: bool = True,
                ):

            variable crash_on_error: bool
            
            Creates a new EventBus instance
            :param crash_on_error: if an crash should be triggered on an exception of a function


            variable self.id

            variable self.event_subscriptions

            variable self.popped_event_subscriptions

            variable self.crash_on_error

            variable self.close_on_error

            variable self.sub_buses

        function subscribe(
                self,
                event_name: str,
                function: typing.Callable | typing.Awaitable = None,
                *args,
                info=None,
                **kwargs,
                ):
            
            Adds a function to the event bus by event name. Dynamically creates underlying data structure for new
            event names
            :param event_name: the event to listen to on this bus
            :param function: the function that should be called when event is sent
            :param args: the args to give
            :param kwargs: the kwargs to give
            :param info: an info to give for the caller


        function unsubscribe(
                self, event_name: str, function: typing.Callable | typing.Awaitable
                ):
            
            Remove a function from the event bus from a given event
            :param event_name: the event name the function was registered to
            :param function: the function itself
            :raise ValueError: when event name is unknown OR function was never assigned


            variable any_found

                    variable any_found

            variable exception_occ

                        variable result

                    variable exception_occ

        function call(self, event_name: str, *args, **kwargs)

            variable handler

        function call_cancelable(self, event_name: str, *args, **kwargs)

                        variable result

                        variable result

                            variable result

        function call_until(
                self,
                event_name: str,
                check_function: typing.Callable[[typing.Any], bool],
                *args,
                **kwargs,
                ):

        function activate(self)

        function deactivate(self)

        function create_sub_bus(self, *args, activate=True, **kwargs)

        function call_as_stack(
                self, event_name: str, *args, amount=1, store_stuff=True, **kwargs
                ):

            variable result

                        variable function

                        variable ex

        function call_as_stack_no_result(
                self, event_name: str, *args, amount=1, store_stuff=True, **kwargs
                ):

                        variable result

            variable result

                        variable r

                            variable r

                        variable r

                            variable r

        function reset_event_stack(self, event_name: str)
            
            Will reset all event subscriptions which where popped from the normal list
            :param event_name: the name of the event to restore
