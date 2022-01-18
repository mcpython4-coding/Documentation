***Mixin.py - documentation - last updated on 16.1.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


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
        Consuming no locals needs no performance at runtime, the instructions fetching the locals are not added to
        the bytecode!
        WARNING:
        - capturing locals costs performance, use it only when needed
        - use optional=False only when needed, mods can declare compatible code
        - override a method only when really needed, it breaks anything touching the code, and
            is applied with low priority
        - use local variable changer not much, at it costs performance every time to pack / unpack them
            (and capture only what you need)
        - mixins into big functions are costly at "compile time", and may fail also at compile time,
            use with guard
            (due to some internal changes when certain limits are exceeded)
        You can "inline" certain functions when applying mixins, they support less fancy stuff,
        but your bytecode will be faster as the JIT can make use of more optimisation code
        WARNING: inline() will delete a lot of meta-information (including line numbers), so when debugging,
            it will be harder to do what you want


        variable LOCKED

        function __init__(self, do_code_optimisation=True)

            variable self.do_code_optimisation

            variable self.bound_mixin_processors

            variable self.special_functions

            variable self.affected

        function makeFunctionArrival(self, name: str, func)

        function applyMixins(self)

                variable method_target

                variable patcher

                variable helper

                variable order

                variable non_optionals

                variable optionals

                variable to_delete

                    variable previous

        function lookup_method(self, method: str)

            variable module

                variable module

        function replace_method_constant(
                self,
                access_str: str,
                constant_value,
                new_value,
                priority=0,
                optional=True,
                fail_on_not_found=True,
                matcher: AbstractInstructionMatcher = None,
                ):
            
            Replaces a given constant (globally) in the method based on instructions matched by the matcher
            :param access_str: the access_str for the target
            :param constant_value: the original value
            :param new_value: the new value
            :param priority: the mixin priority
            :param optional: optional mixin?
            :param fail_on_not_found: if mixin applying failed if the constant was not found in the constant table
            :param matcher: a custom instruction matcher, optional, when None, matches all instructions using that constant


        function replace_global_ref(
                self,
                access_str: str,
                previous_name: str,
                new_name: str,
                priority=0,
                optional=True,
                matcher: AbstractInstructionMatcher = None,
                ):
            
            Replaces all LOAD_GLOBAL <global name> instructions with a LOAD GLOBAL <new name> instructions
            (all matched by the matcher instance)
            :param access_str: the access str of the method
            :param previous_name: the global name
            :param new_name: the new global name
            :param priority: the mixin priority
            :param optional: optional mixin?
            :param matcher: the instruction matcher object


        function replace_global_with_constant(
                self,
                access_str: str,
                global_name: str,
                new_value,
                priority=0,
                optional=True,
                matcher: AbstractInstructionMatcher = None,
                ):
            
            Replaces all LOAD_GLOBAL <global name> instructions with a LOAD_CONST(new value) instructions
            (matching the matcher)
            :param access_str: the access str of the method
            :param global_name: the global name
            :param new_value: the new value
            :param priority: the mixin priority
            :param optional: optional mixin?
            :param matcher: the instruction matcher object


        function replace_attribute_with_constant(
                self,
                access_str: str,
                attr_name: str,
                new_value,
                load_from_local_hint: str = None,
                priority=0,
                optional=True,
                matcher: AbstractInstructionMatcher = None,
                ):
            
            Replaces an attribute access to an object with a constant value
            (LOAD_CONST) instruction (matching the matcher)
            :param access_str: the method to mix into
            :param attr_name: the attr name
            :param new_value: the constant value to replace with
            :param load_from_local_hint: optional, a local name which is accessed before it
            :param priority: the mixin priority
            :param optional: optional mixin?
            :param matcher: the instruction matcher object


        function replace_attribute_with_function_call(
                self,
                access_str: str,
                attr_name: str,
                load_from_local_hint: str = None,
                priority=0,
                optional=True,
                matcher: AbstractInstructionMatcher = None,
                args=tuple(),
                collected_locals=tuple(),
                ):
            
            Replaces an attribute access with a method call to a constant method
            given by annotation.
            Passes the object the attribute is accessed on as last argument
            :param access_str: the access string for the method to mix into
            :param attr_name: the attribute name access to look for
            :param load_from_local_hint: optional, a local name which is accessed before it
            :param priority: the mixin priority
            :param optional: optional mixin?
            :param matcher: the instruction matcher object
            :param args: args to add to the function
            :param collected_locals: what locals to add as args


        function replace_local_var_with_const(
                self,
                access_str: str,
                local_name: str,
                constant_value,
                priority=0,
                optional=True,
                matcher: AbstractInstructionMatcher = None,
                ):
            
            Replaces a local variable lookup (LOAD_FAST) with a constant value
            All LOAD_FAST instructions accessing the given attribute matching the matcher
            will be replaced
            :param access_str: the method access string
            :param local_name: the local variable name
            :param constant_value: the constant value to replace with
            :param priority: the mixin priority
            :param optional: optional mixin?
            :param matcher: the instruction matcher object


        function replace_function_call_with_constant(
                self,
                access_str: str,
                func_name: str,
                constant_value,
                is_object_bound=False,
                object_source_hint: str = None,
                priority=0,
                optional=True,
                matcher: AbstractInstructionMatcher = None,
                ):
            
            Replaces a function invocation with a constant value
            Should internal do some cleanup in the bytecode
            :param access_str: the method to mix into
            :param func_name: the function name
            :param constant_value: the value to replace with
            :param is_object_bound: if it is a method of an object (look for GET_ATTR instruction)
                or a global function (look for LOAD_GLOBAL or similar)
            :param object_source_hint: when object bound, a local variable name where the object is stored,
                or None for any source
            :param priority: the mixin priority
            :param optional: optional mixin?
            :param matcher: the instruction matcher object


        function override(
                self, access_str: str, priority=0, optional=True
                ) -> typing.Callable[[types.FunctionType], types.FunctionType]:
            
            Replaces a function with another one.
            Signatures should match (or the new one should be a super set)


            function annotate(function)

        function inject_at_head(
                self,
                access_str: str,
                priority=0,
                optional=True,
                args=tuple(),
                collected_locals=tuple(),
                inline=False,
                ):
            
            Injects some code at the function head
            Can be used for e.g. parameter manipulation
            :param access_str: the access str for the method
            :param priority: the mixin priority
            :param optional: optional mixin?
            :param args: args to add to the function
            :param collected_locals: what locals to add as args
            :param inline: if to inline the target method; requires collected_locals to be empty
                use the capture_local() in that case!


            function annotate(function)

        function inject_at_return(
                self,
                access_str: str,
                include_previous_mixed_ins=False,
                priority=0,
                optional=True,
                args=tuple(),
                matcher: AbstractInstructionMatcher = None,
                collected_locals=tuple(),
                add_return_value=False,
                inline=False,
                ):
            
            Injects code at specific return statements
            :param access_str: the method
            :param include_previous_mixed_ins: if return statements from other mixins should be included in the search (not implemented)
            :param priority: the mixin priority
            :param optional: optional mixin?
            :param args: the args to give to the method
            :param matcher: optional a return statement matcher
            :param collected_locals: what locals to add to the method call
            :param add_return_value: if to add as last parameter the value the function tries to return or not
            :param inline: if to inline the target method; requires collected_locals to be empty
                use the capture_local() in that case; add_return_value has no effect
            todo: add support for add_return_value (copy and store into locals)


            function annotate(function)

        function inject_at_return_replacing_return_value(
                self,
                access_str: str,
                include_previous_mixed_ins=False,
                priority=0,
                optional=True,
                args=tuple(),
                matcher: AbstractInstructionMatcher = None,
                collected_locals=tuple(),
                add_return_value=False,
                ):
            
            Injects the given method at selected return statements, passing all args, and as last argument
            the previous return value, and returning the result of the injected method
            Arguments as above
            todo: make inline-able


            function annotate(function)

        function inject_at_yield(
                self,
                access_str: str,
                include_previous_mixed_ins=False,
                priority=0,
                optional=True,
                args=tuple(),
                matcher: AbstractInstructionMatcher = None,
                collected_locals=tuple(),
                add_yield_value=False,
                inline=False,
                ):
            
            Injects code at specific yield statements
            The function will be invoked with a bool flag indicating if it is a YIELD_VALUE or YIELD_FROM
            instruction, followed by 'args'.
            :param access_str: the method
            :param include_previous_mixed_ins: if yield statements from other mixins should be included in the search (not implemented)
            :param priority: the mixin priority
            :param optional: optional mixin?
            :param args: the args to give to the method
            :param matcher: optional a yield statement matcher
            :param collected_locals: which locals to add as args
            :param add_yield_value: if to add the value yielded as last value
            :param inline: if to inline the target method; requires collected_locals to be empty
                use the capture_local() in that case; add_yield_value has no effect


            function annotate(function)

        function inject_at_yield_replacing_yield_value(
                self,
                access_str: str,
                include_previous_mixed_ins=False,
                priority=0,
                optional=True,
                args=tuple(),
                matcher: AbstractInstructionMatcher = None,
                collected_locals=tuple(),
                add_yield_value=False,
                is_yield_from=None,
                ):
            
            Injects the given method at selected yield statements, passing a bool flag indicating if it is a YIELD_VALUE or
            YIELD_FROM, followed by all args, and as last argument the previous yield value, and yielding the result of the
            injected method.
            Arguments as above
            is_yield_from can change the yield instruction type if needed, set to None (default) for not changing
            todo: add ability to inline this


            function annotate(function)

        function inject_at_tail(
                self,
                access_str: str,
                priority=0,
                optional=True,
                args=tuple(),
                collected_locals=tuple(),
                add_return_value=False,
                inline=False,
                ):
            
            Injects code before the final return statement
            :param access_str: the method
            :param priority: the mixin priority
            :param optional: optional mixin?
            :param args: the args to give to the method
            :param collected_locals: which locals to add as args
            :param add_return_value: if to add the return value at the tail as an argument or not
            :param inline: if to inline the target method; requires collected_locals to be empty
                use the capture_local() in that case; add_return_value has no effect
            todo: add support for add_return_value (copy and store into locals)


            function annotate(function)

        function inject_local_variable_modifier_at(
                self,
                access_str: str,
                matcher: AbstractInstructionMatcher,
                local_variables: typing.List[str],
                priority=0,
                optional=True,
                args=tuple(),
                collected_locals=tuple(),
                ):
            
            Injects a local variable modifying method into the target using specified matcher
            to find places to inject into.
            The function will be invoked with args, followed by the local variable values
            in the order specified in local_variables.
            It is expected to return a tuple of the size of local_variables, to be written back
            into the local variable table.
            WARNING: normally, you want a single-match matcher object,
            as you want only one target in the method!
            This method is not for inlining, as inlined functions can simply
            capture_local() the names they need and than work with them
            :param access_str: the method to inject into
            :param matcher: the instruction matcher where to inject your change function
            :param local_variables: which locals to modify
            :param priority: the mixin priority
            :param optional: optional mixin?
            :param args: args to give the function
            :param collected_locals: what locals to also add, but not write back


            function annotate(function)

        function inject_replace_global_method_invoke(
                self,
                access_str: str,
                target_method: str,
                inline=True,
                priority=0,
                optional=True,
                matcher: AbstractInstructionMatcher = None,
                ):
            
            Modifies method calls to call another method, loaded via LOAD_GLOBAL
            :param access_str: the method
            :param target_method: the method to replace
            :param inline: when True, will inline this annotated method into the target
            :param priority: the mixin priority
            :param optional: optional mixin?
            :param matcher: optional, a matcher object for the "invoke" instruction


        function inject_replace_object_method_invoke(
                self,
                access_str: str,
                target_method: str,
                inline=True,
                priority=0,
                optional=True,
                matcher: AbstractInstructionMatcher = None,
                ):
            
            Modifies method calls to call another method, loaded via LOAD_ATTR
            :param access_str: the method
            :param target_method: the method to replace
            :param inline: when True, will inline this annotated method into the target
            :param priority: the mixin priority
            :param optional: optional mixin?
            :param matcher: optional, a matcher object for the "invoke" instruction


        function inject_replace_builtin_method_invoke(
                self,
                access_str: str,
                target_method: str,
                inline=True,
                priority=0,
                optional=True,
                matcher: AbstractInstructionMatcher = None,
                ):
            
            Modifies method calls to call another method, loaded via the builtin system
            :param access_str: the method
            :param target_method: the method to replace
            :param inline: when True, will inline this annotated method into the target
            :param priority: the mixin priority
            :param optional: optional mixin?
            :param matcher: optional, a matcher object for the "invoke" instruction


        function inject_replace_local_space_method_invoke(
                self,
                access_str: str,
                target_method: str,
                inline=True,
                priority=0,
                optional=True,
                matcher: AbstractInstructionMatcher = None,
                ):
            
            Modifies method calls to call another method, stored in the local variable table
            For parameter function and imported functions in the method body
            :param access_str: the method
            :param target_method: the method to replace
            :param inline: when True, will inline this annotated method into the target
            :param priority: the mixin priority
            :param optional: optional mixin?
            :param matcher: optional, a matcher object for the "invoke" instruction


        function redirect_module_import(
                self,
                access_str: str,
                target_module: str,
                new_module: str,
                priority=0,
                optional=True,
                matcher: AbstractInstructionMatcher = None,
                ):
            
            Redirects a module import in an function to another module
            :param access_str: the method to mixin into
            :param target_module: the module to target
            :param new_module: the new module
            :param priority: the mixin priority
            :param optional: optional mixin?
            :param matcher: optional, an import instruction matcher (only useful when multiple imports
                to the same module exist)


        function cover_with_try_except_block(
                self,
                access_str: str,
                exception_type: Exception,
                start: int = 0,
                end: int = -1,
                priority=0,
                optional=True,
                include_handler=True,
                inline_handler=False,
                ):
            
            Covers the function body with a try-except block of the given exception type.
            Use as an annotation on the handler function
            todo: maybe we want matchers for start/end
            :param access_str: the method to cover
            :param exception_type: the exception type
            :param start: where to start it
            :param end: where to end it
            :param priority: the mixin priority
            :param optional: optional mixin?
            :param include_handler: when False, this is not an annotation, and the exception will be simply ignored
            :param inline_handler: when True, will inline the target method


        function replace_explicit_raise(
                self,
                access_str: str,
                exception_matcher: AbstractInstructionMatcher = None,
                priority=0,
                optional=True,
                remaining_mode="return_result",
                args=tuple(),
                collected_locals=tuple(),
                inline=False,
                ):
            
            Replaces an explicit 'raise' with custom code.
            The custom code decides what should happen next.
            The method gets a nullable exception as the first parameter (depending on re-raise or not)
            :param access_str: the method access str
            :param exception_matcher: the raise instruction matcher, or None
            :param priority: the mixin priority
            :param optional: optional mixin?
            :param remaining_mode: what to do with the raise instruction, can be
                "return" for returning None in any case, "return_result" for returning the result of the function,
                "yield_result" for yielding the result of the function, "yield_from_result" for yielding from
                the function result and "raise" for raising the original exception
            :param args: the args to give to the method
            :param collected_locals: which locals to add as args
            :param inline: when True, will inline the target method; the remaining_mode argument will be ignored


        function remove_flow_branch(
                self,
                access_str: str,
                matcher: AbstractInstructionMatcher,
                priority=0,
                optional=True,
                target_jumped_branch=True,
                ):
            
            Removes a branch introduced by a conditional or non-conditional jump instruction.
            Can optimise the code following that branch away.
            When target_jumped_branch is False, the branch followed by the instruction is removed
            (for conditional branches only), and the conditional will be replaced by a non-conditional jump.
            :param access_str: the method access str
            :param matcher: the matcher object, for the conditional branch instructions
            :param priority: the mixin priority
            :param optional: optional mixin?
            :param target_jumped_branch: see above


        function add_flow_branch(
                self,
                access_str: str,
                matcher: AbstractInstructionMatcher,
                condition_handler: typing.Callable[[...], bool] = None,
                capture_local_variables_for_condition: typing.Iterable[str] = tuple(),
                capture_local_variables_for_branch: typing.Iterable[str] = tuple(),
                priority=0,
                optional=True,
                continue_at: typing.Callable[[MixinPatchHelper, int, int], int] | int = 0,
                inline=False,
                inline_condition=False,
                ):
            
            Adds a (conditional) branch into the code.
            Returns an annotation for the branch code.
            For conditional branches, use the condition_handler and give it a method for decision.
            Use continue_at when you want to continue somewhere else after execution.
            Use the local captures when you need local variable access.
            :param access_str: the function access str
            :param matcher: the matcher object, to decide where the branch is injected
            :param condition_handler: the function returning True / False for the condition, or None
                for a non-conditional branch
            :param capture_local_variables_for_condition: local variable names to send to the condition handler
            :param capture_local_variables_for_branch: local variable names to send to the branch handler
            :param priority: the mixin priority
            :param optional: optional mixin?
            :param continue_at: where to continue execution at, either int (offset) or callable with the helper, the branch index,
                and the instruction index
            :param inline: when True, will inline the target method
            :param inline_condition: when True, will inline the condition method


        function change_iterator(
                self,
                access_str: str,
                matcher: AbstractInstructionMatcher = None,
                priority=0,
                optional=True,
                capture_locals: typing.Iterable[str] = tuple(),
                inline=False,
                ):
            
            Exchanges the used iterator for e.g. for loop
            The attached expression should return the new iterator.
            It gets the previous iterator as an argument
            :param access_str: the function access str
            :param matcher: the matcher object, to decide which iterator instruction to use
            :param priority: the mixin priority
            :param optional: optional mixin?
            :param capture_locals: the local variables to capture for the iterator getter
            :param inline: when True, will inline the target method


    variable mixin_handler

    variable MixinHandler.LOCKED