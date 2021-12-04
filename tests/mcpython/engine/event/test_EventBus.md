***test_EventBus.py - documentation - last updated on 1.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class TestEventBus extends TestCase

        function test_import(self)

        function test_constructor(self)

            variable shared.NEXT_EVENT_BUS_ID

            variable instance

        function test_subscribe(self)

            function test()

            variable bus

        function test_unsubscribe(self)

            function test()

            variable bus

        function test_call(self)

            variable state

            function test()

            variable bus

        function test_call_args(self)

            variable state

            function test(flag)

            variable bus

        function test_call_with_subscriber_args(self)

            variable state

            function test(flag)

            variable bus

        function test_call_with_args_and_subscriber_args(self)

            variable state

            function test(flag1, flag2)

            variable bus

        function test_call_cancelable(self)

            variable calls

            function test(cancel: CancelAbleEvent)

            variable bus

            variable result

        function test_call_as_stack(self)

            variable invoked

            function test()

            variable bus

        function test_call_as_stack_multi(self)

            variable invoke_times

            function test()

            variable bus

        function test_reset_event_stack(self)

            function test()

            variable bus