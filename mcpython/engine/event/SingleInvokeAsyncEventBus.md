***SingleInvokeAsyncEventBus.py - documentation - last updated on 28.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class SingleInvokeAsyncEventBus
        
        Special async variant of the normal event bus
        Allows by design only one invocation


        function __init__(
                self,
                crash_on_error: bool = True,
                ):

            variable crash_on_error: bool

            variable self.id

            variable self.event_subscriptions

            variable self.popped_event_subscriptions

            variable self.crash_on_error

            variable self.close_on_error

            variable self.sub_buses

        function subscribe(
                self,
                event_name: str,
                function: typing.Awaitable = None,
                info=None,
                ):
            
            Adds a function to the event bus by event name. Dynamically creates underlying data structure for new
            event names
            :param event_name: the event to listen to on this bus
            :param function: the awaitable object to run
            :param info: an info to give for the caller

            
            Call an event on this event bus. Also works when deactivated
            :param event_name: the name of the event to call

        
        #     Will call a cancel able event.
        #     Works the same way as call, but will use call_until() with an CancelAbleEvent as first parameter which is checked after each call
        #     :param event_name: the name to call
        #     :return: if it was canceled or not

        
        #     Will call the event stack until an check_function returns True or all subscriptions where done
        #     :param event_name: the name of the event
        #     :param check_function: the check function to call with
        #     :return: the result in the moment of True or None


        function activate(self)

        function deactivate(self)

        function create_sub_bus(self, *args, activate=True, **kwargs)

            variable result

        function reset_event_stack(self, event_name: str)
            
            Will reset all event subscriptions which where popped from the normal list
            :param event_name: the name of the event to restore
