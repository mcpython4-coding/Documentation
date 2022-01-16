***MixinProcessors.py - documentation - last updated on 16.1.2022 by uuk***
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
                handler,
                function: FunctionPatcher,
                modifier_list: typing.List["AbstractMixinProcessor"],
                ) -> bool:

        function apply(
                self,
                handler,
                target: FunctionPatcher,
                helper: MixinPatchHelper,
                ):
            
            Applies the mixin processor to the target
            :param handler: the handler instance
            :param target: the target FunctionPatcher instance
            :param helper: the helper instance, the method is responsible for invoking store() on it


        function is_breaking(self) -> bool

    class MixinReplacementProcessor extends AbstractMixinProcessor

        function __init__(self, replacement: types.FunctionType)

            variable self.replacement

        function apply(
                self,
                handler,
                target: FunctionPatcher,
                helper: MixinPatchHelper,
                ):

        function is_breaking(self) -> bool

    class MixinConstantReplacer extends AbstractMixinProcessor

        function __init__(
                self,
                before,
                after,
                fail_on_not_found=False,
                matcher: AbstractInstructionMatcher = None,
                ):

            variable matcher: AbstractInstructionMatcher

            variable self.before

            variable self.after

            variable self.fail_on_not_found

            variable self.matcher

        function apply(
                self,
                handler,
                target: FunctionPatcher,
                helper: MixinPatchHelper,
                ):

    class MixinGlobal2ConstReplace extends AbstractMixinProcessor

        function __init__(
                self, global_name: str, after, matcher: AbstractInstructionMatcher = None
                ):

            variable self.global_name

            variable self.after

            variable self.matcher

        function apply(
                self,
                handler,
                target: FunctionPatcher,
                helper: MixinPatchHelper,
                ):

            variable match

                variable helper.instruction_listing[index]

    class MixinLocal2ConstReplace extends AbstractMixinProcessor

        function __init__(
                self, local_name: str, after, matcher: AbstractInstructionMatcher = None
                ):

            variable self.local_name

            variable self.after

            variable self.matcher

        function apply(
                self,
                handler,
                target: FunctionPatcher,
                helper: MixinPatchHelper,
                ):

            variable match

                variable helper.instruction_listing[index]

    class MixinGlobalReTargetProcessor extends AbstractMixinProcessor

        function __init__(
                self,
                previous_global: str,
                new_global: str,
                matcher: AbstractInstructionMatcher = None,
                ):

            variable matcher: AbstractInstructionMatcher

            variable self.previous_global

            variable self.new_global

            variable self.matcher

        function apply(
                self,
                handler,
                target: FunctionPatcher,
                helper: MixinPatchHelper,
                ):

            variable match

                variable helper.instruction_listing[index]

    class InjectFunctionCallAtHeadProcessor extends AbstractMixinProcessor

        function __init__(
                self,
                target_func: typing.Callable,
                *args,
                collected_locals=tuple(),
                inline=False,
                ):

            variable self.target_func

            variable self.args

            variable self.collected_locals

            variable self.inline

        function apply(
                self,
                handler,
                target: FunctionPatcher,
                helper: MixinPatchHelper,
                ):

            variable index

    class InjectFunctionCallAtReturnProcessor extends AbstractMixinProcessor

        function __init__(
                self,
                target_func: typing.Callable,
                *args,
                matcher: AbstractInstructionMatcher = None,
                collected_locals=tuple(),
                add_return_value=False,
                inline=False,
                ):

            variable matcher: AbstractInstructionMatcher

            variable self.target_func

            variable self.args

            variable self.matcher

            variable self.collected_locals

            variable self.add_return_value

            variable self.inline

        function apply(
                self,
                handler,
                target: FunctionPatcher,
                helper: MixinPatchHelper,
                ):

            variable matches

    class InjectFunctionCallAtReturnReplaceValueProcessor extends AbstractMixinProcessor

        function __init__(
                self,
                target_func: typing.Callable,
                *args,
                matcher: AbstractInstructionMatcher = None,
                collected_locals=tuple(),
                add_return_value=False,
                ):

            variable matcher: AbstractInstructionMatcher

            variable self.target_func

            variable self.args

            variable self.matcher

            variable self.collected_locals

            variable self.add_return_value

        function apply(
                self,
                handler,
                target: FunctionPatcher,
                helper: MixinPatchHelper,
                ):

            variable matches

    class InjectFunctionCallAtYieldProcessor extends AbstractMixinProcessor

        function __init__(
                self,
                target_func: typing.Callable,
                *args,
                matcher: AbstractInstructionMatcher = None,
                collected_locals=tuple(),
                add_yield_value=False,
                inline=False,
                ):

            variable matcher: AbstractInstructionMatcher

            variable self.target_func

            variable self.args

            variable self.matcher

            variable self.collected_locals

            variable self.add_yield_value

            variable self.inline

        function apply(
                self,
                handler,
                target: FunctionPatcher,
                helper: MixinPatchHelper,
                ):

            variable matches

    class InjectFunctionCallAtYieldReplaceValueProcessor extends AbstractMixinProcessor

        function __init__(
                self,
                target_func: typing.Callable,
                *args,
                matcher: AbstractInstructionMatcher = None,
                collected_locals=tuple(),
                add_yield_value=False,
                is_yield_from=False,
                ):

            variable matcher: AbstractInstructionMatcher

            variable self.target_func

            variable self.args

            variable self.matcher

            variable self.collected_locals

            variable self.add_yield_value

            variable self.is_yield_from

        function apply(
                self,
                handler,
                target: FunctionPatcher,
                helper: MixinPatchHelper,
                ):

            variable matches

                            variable helper.instruction_listing[index]

                            variable helper.instruction_listing[index]

    class InjectFunctionCallAtTailProcessor extends AbstractMixinProcessor

        function __init__(
                self,
                target_func: typing.Callable,
                *args,
                collected_locals=tuple(),
                add_return_value=False,
                inline=False,
                ):

            variable self.target_func

            variable self.args

            variable self.collected_locals

            variable self.add_return_value

            variable self.inline

        function apply(
                self,
                handler,
                target: FunctionPatcher,
                helper: MixinPatchHelper,
                ):

    class InjectFunctionLocalVariableModifier extends AbstractMixinProcessor

        function __init__(
                self,
                function: typing.Callable,
                local_variables: typing.List[str],
                matcher: AbstractInstructionMatcher,
                *args,
                collected_locals=tuple(),
                ):

            variable self.function

            variable self.local_variables

            variable self.args

            variable self.matcher

            variable self.collected_locals

        function apply(
                self,
                handler,
                target: FunctionPatcher,
                helper: MixinPatchHelper,
                ):

            variable collected_locals

            variable store_locals

    class MethodInlineProcessor extends AbstractMixinProcessor

        function __init__(self, func_name: str, target_accessor: typing.Callable[[], typing.Callable] = None)

            variable self.func_name

            variable self.target_accessor

        function apply(
                self,
                handler,
                target: FunctionPatcher,
                helper: MixinPatchHelper,
                ):

                        variable source