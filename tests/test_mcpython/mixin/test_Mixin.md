***test_Mixin.py - documentation - last updated on 16.1.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable INVOKER_COUNTER

    variable INVOKED

    function increase_counter()

    function test()

    function test2()

    function test3(a)

    function test4(a)

    function test_global()

    function test_global2()

    function test_global3()

    function reset_test_methods()

        function test()

        function test2()

        function test3(a)

        function test4(a)

        function test_global()

        function test_global2()

        function test_global3()

        variable INVOKED

    class TestMixinHandler extends TestCase

        function setUp(self)

            variable shared.IS_TEST_ENV

            variable MixinHandler.LOCKED

        function test_lock(self)

            variable MixinHandler.LOCKED

            variable MixinHandler.LOCKED

        function test_replace_function_body(self)

            variable handler

            function test()

            @handler.override("test")
            function override()

            variable patcher

            variable handler

            variable coro

            variable patcher

            variable coro

        function test_function_lookup(self)

            variable method

        function test_mixin_override(self)

            variable handler

            @handler.override("tests.test_mcpython.mixin.test_Mixin:test")
            function override()

        function test_mixin_override_twice(self)

            variable handler

            @handler.override("tests.test_mcpython.mixin.test_Mixin:test")
            function override()

            @handler.override("tests.test_mcpython.mixin.test_Mixin:test")
            function override2()

        function test_mixin_by_name_twice_with_priority(self)

            variable handler

            function override()

            @handler.override("tests.test_mcpython.mixin.test_Mixin:test")
            function override2()

        function test_mixin_by_name_twice_with_negative_priority(self)

            variable handler

            @handler.override("tests.test_mcpython.mixin.test_Mixin:test")
            function override()

            function override2()

        function test_mixin_by_name_twice_conflicting(self)

            variable handler

            function override()

            function override2()

        function test_mixin_by_name_twice_non_conflicting_order(self)

            variable handler

            function override()

            @handler.override("tests.test_mcpython.mixin.test_Mixin:test")
            function override2()

        function test_mixin_by_name_twice_conflicting_order(self)

            variable handler

            function override()

            function override2()

        function test_constant_replacement_1(self)

            variable handler

        function test_constant_replacement_2(self)

            variable handler

        function test_constant_replacement_fail_1(self)

            variable handler

        function test_constant_replacement_fail_2(self)

            variable handler

        function test_global_to_global_1(self)

            variable handler

            variable INVOKER_COUNTER

            variable INVOKER_COUNTER

        function test_global_to_const_1(self)

            variable handler

            variable invoked

            function callback()

        function test_global_to_const_2(self)

            variable handler

            variable invoked

            function callback()

        function test_global_to_const_3(self)

            variable handler

            variable invoked

            function callback()

        function test_global_to_const_4(self)

            variable handler

            variable invoked

            function callback()

        function test_global_to_const_5(self)

            variable handler

            variable invoked

            function callback()

        function test_global_to_const_6(self)

            variable handler

            variable invoked

            function callback()

        function test_mixin_inject_at_head_1(self)

            variable handler

            variable invoked

            @handler.inject_at_head("tests.test_mcpython.mixin.test_Mixin:test", args=(3,))
            function inject(c)

        function test_mixin_inject_at_head_2(self)

            variable handler

            variable invoked

            @handler.inject_at_head("tests.test_mcpython.mixin.test_Mixin:test", args=(3,))
            function inject(c)

            @handler.inject_at_head("tests.test_mcpython.mixin.test_Mixin:test", args=(5,))
            function inject2(c)

        function test_mixin_inject_at_head_inline_1(self)

            function target()

            variable handler

            @handler.inject_at_head("test", inline=True)
            function inject()

            variable INVOKED

            variable INVOKED

            variable INVOKED

        function test_mixin_inject_at_return_1(self)

            variable handler

            variable invoked

            function inject(c)

        function test_mixin_inject_at_return_2(self)

            variable handler

            variable invoked

            function inject(c)

            function inject2(c)

        function test_mixin_inject_at_return_3(self)

            variable handler

            variable invoked

            function inject(c)

        function test_mixin_inject_at_return_4(self)

            variable handler

            variable invoked

            function inject(c)

            function inject2(c)

        function test_mixin_inject_at_return_5(self)

            function target()

            variable handler

            variable invoked

            @handler.inject_at_return("test", add_return_value=True)
            function inject(c)

        function test_mixin_inject_at_return_inline_1(self)

            variable handler

            function inject(c)

            variable INVOKED

            variable INVOKED

        function test_mixin_inject_at_return_value_1(self)

            variable handler

            variable invoked

            function inject(c)

        function test_mixin_inject_at_return_value_2(self)

            variable handler

            variable invoked

            function inject(c)

            function inject2(c)

        function test_mixin_inject_at_return_value_3(self)

            variable handler

            variable invoked

            function inject(c)

        function test_mixin_inject_at_return_value_4(self)

            variable handler

            variable invoked

            function inject(c)

            function inject2(c)

        function test_mixin_inject_at_yield_1(self)

            variable handler

            variable invoked

            function inject(c, _)

        function test_mixin_inject_at_yield_2(self)

            variable handler

            variable invoked

            function inject(c, _)

            function inject2(c, _)

        function test_mixin_inject_at_yield_3(self)

            variable handler

            variable invoked

            function inject(_, c)

        function test_mixin_inject_at_yield_4(self)

            variable handler

            variable invoked

            function inject(_, c)

            function inject2(_, c)

        function test_mixin_inject_at_yield_5(self)

            function target()

            variable handler

            variable invoked

            @handler.inject_at_yield("test", add_yield_value=True)
            function inject(v, _)

        function test_mixin_inject_at_yield_6(self)

            function target(c)

            variable handler

            variable invoked

            @handler.inject_at_yield("test", add_yield_value=True)
            function inject(v, _)

        function test_mixin_inject_at_yield_inline_1(self)

            variable handler

            function inject(_)

        function test_mixin_inject_at_yield_value_1(self)

            variable handler

            variable invoked

            function inject(c, _)

        function test_mixin_inject_at_yield_value_2(self)

            variable handler

            variable invoked

            function inject(c, _)

            function inject2(c, _)

        function test_mixin_inject_at_tail_1(self)

            function target(flag)

            variable handler

            variable invoked

            @handler.inject_at_tail("test", add_return_value=True)
            function inject(c)

        function test_mixin_inject_at_tail_inline_1(self)

            variable invoked

            function target(flag)

            variable handler

            @handler.inject_at_tail("test", inline=True)
            function inject()

        function test_mixin_given_method_call_inject_1(self)

            variable INVOKED

            function localtest()

            function inject(c: int)

            variable helper

        function test_mixin_given_method_call_inject_2(self)

            variable INVOKED

            function localtest()

            function inject(c: int)

            variable helper

        function test_mixin_given_method_call_inject_3(self)

            variable INVOKED

            function localtest()

            function inject(c: int)

            variable helper

        function test_local2constant_transformer_1(self)

            variable handler

            function func(c)

        function test_local_var_modifier_1(self)

            variable handler

            function func(c)

            @handler.inject_local_variable_modifier_at("test", CounterMatcher(0), ["c"])
            function inject(c)

        function test_local_var_modifier_2(self)

            variable handler

            function func(c)

            @handler.inject_local_variable_modifier_at("test", CounterMatcher(0), ["c"])
            function inject(c)

        function test_local_var_modifier_3(self)

            variable handler

            function func(c)

            function inject(c, d)