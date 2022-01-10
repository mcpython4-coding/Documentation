***InstructionMatchers.py - documentation - last updated on 10.1.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractInstructionMatcher

        function matches(self, function: MixinPatchHelper, index: int, match_count: int) -> bool

        function __and__(self, other)

        function __or__(self, other)

        function __invert__(self)

    class AndMatcher extends AbstractInstructionMatcher

        function __init__(self, *matchers: AbstractInstructionMatcher)

            variable self.matchers

        function matches(self, function: MixinPatchHelper, index: int, match_count: int) -> bool

        function __and__(self, other)

    class OrMatcher extends AbstractInstructionMatcher

        function __init__(self, *matchers: AbstractInstructionMatcher)

            variable self.matchers

        function matches(self, function: MixinPatchHelper, index: int, match_count: int) -> bool

        function __or__(self, other)

    class NotMatcher extends AbstractInstructionMatcher

        function __init__(self, matcher: AbstractInstructionMatcher)

            variable self.matcher

        function matches(self, function: MixinPatchHelper, index: int, match_count: int) -> bool

        function __invert__(self)

    class AnyByInstructionNameMatcher extends AbstractInstructionMatcher

        function __init__(self, opname: str)

            variable self.opname

        function matches(self, function: MixinPatchHelper, index: int, match_count: int) -> bool

    class IndexBasedMatcher extends AbstractInstructionMatcher

        function __init__(
                self,
                start: int,
                end: int = None,
                sub_matcher: AbstractInstructionMatcher = None,
                ):

            variable end: int

            variable sub_matcher: AbstractInstructionMatcher

            variable self.start

            variable self.end

            variable self.sub_matcher

        function matches(self, function: MixinPatchHelper, index: int, match_count: int) -> bool

    class SurroundingBasedMatcher extends AbstractInstructionMatcher

        function __init__(self, this_matcher: AbstractInstructionMatcher = None)

            variable self.this_matcher

            variable self.size

        function set_offset_matcher(self, offset: int, matcher: AbstractInstructionMatcher)

        function matches(self, function: MixinPatchHelper, index: int, match_count: int) -> bool

                variable dx

    class LoadConstantValueMatcher extends AbstractInstructionMatcher

        function __init__(self, value)

            variable self.value

        function matches(self, function: MixinPatchHelper, index: int, match_count: int) -> bool

    class LoadGlobalMatcher extends AbstractInstructionMatcher

        function __init__(self, global_name: str)

            variable self.global_name

        function matches(self, function: MixinPatchHelper, index: int, match_count: int) -> bool

    class CounterMatcher extends AbstractInstructionMatcher

        function __init__(self, count_start: int, count_end: int = None)

            variable self.count_start

            variable self.count_end

        function matches(self, function: MixinPatchHelper, index: int, match_count: int) -> bool