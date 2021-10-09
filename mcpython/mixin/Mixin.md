***Mixin.py - documentation - last updated on 9.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractMixinProcessor
        
        Mixin processor class
        Stuff that works on methods on a high level


        function canBeAppliedOnModified(
                self,
                handler: "MixinHandler",
                function: types.FunctionType,
                modifier_list: typing.List["AbstractMixinProcessor"],
                ) -> bool:

        function canBeFurtherModified(
                self, handler: "MixinHandler", function: types.FunctionType
                ) -> bool:

        function apply(
                self,
                handler: "MixinHandler",
                target: mcpython.mixin.PyBytecodeManipulator.FunctionPatcher,
                ):

    class MixinReplacementProcessor extends AbstractMixinProcessor

        function __init__(self, replacement: types.FunctionType)

            variable self.replacement

        function canBeFurtherModified(
                self, handler: "MixinHandler", function: types.FunctionType
                ) -> bool:

        function apply(
                self,
                handler: "MixinHandler",
                target: mcpython.mixin.PyBytecodeManipulator.FunctionPatcher,
                ):

    class MixinHandler
        
        Handler for mixing into some functions
        Create one of this object per mixin group
        This is than an annotation holder, working the following way:
        @<instance>.<some modifier>(<target address>, <...args>)
        def <some override>(...):
            ...
        Please make sure that the signatures match up, when not other specified
        By default, control flow with "return"'s is only arrival in the specified section.
        Use mixin_return() followed by a normal return to exit the method injected into


        function __init__(self, processor_name: str, skip_on_fail=False, priority=0)

            variable self.processor_name

            variable self.skip_on_fail

            variable self.priority

        function applyMixins(self)

                variable patcher

        static
        function lookup_method(method: str)

                variable module

        function replace_function_body(
                self, access_str: str
                ) -> typing.Callable[[types.FunctionType], types.FunctionType]:

            function annotate(function)

        function inline_method_calls(self, access_str: str, method_call_target: str)
            
            Inlines all method calls to a defined function
            Does not work like the normal inline-keyword, as we cannot find all method calls
            WARNING: method must be looked up for it to work
            WARNING: when someone mixes into the method to inline AFTER this mixin applies,
                the change will not be affecting this method
            This is not a real mixin, but a self-modifier


        function inject_at_head(self, access_str: str)
            
            Injects some code at the function head
            Can be used for e.g. parameter manipulation


        function inject_at_return(
                self,
                access: str,
                return_sampler=lambda *_: True,
                include_previous_mixed_ins=False,
                ):
            
            Injects code at specific return statements
            :param access: the method
            :param return_sampler: a method checking a return statement, signature not defined by now
            :param include_previous_mixed_ins: if return statements from other mixins should be included in the search


        function inject_replace_method_invoke(
                self, access: str, target_method: str, sampler=lambda *_: True, inline=True
                ):
            
            Modifies method calls to call another method
            :param access: the method
            :param target_method: the method to replace
            :param sampler: optionally, some checker for invoke call
            :param inline: when True, will inline this annotated method into the target
