***MixinMethodWrapper.py - documentation - last updated on 10.1.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    function reconstruct_instruction(
            instr: dis.Instruction,
            arg=None,
            arg_value=None,
            arg_repr=None,
            offset=None,
            jump_target=None,
            ):

    function mixin_return(value=None)
        
        Invoke before a normal return in a mixin injected to return the method injected into
        This method call and the return will be combined into a regular return statement
        Use from <...>.MixinMethodWrapper import mixin_return outside the method in a global scope when possible,
        it makes it easier to detect inside the bytecode
        todo: use this for real!


    variable OFFSET_JUMPS

    variable REAL_JUMPS

    class MixinPatchHelper
        
        See https://docs.python.org/3/library/dis.html#python-bytecode-instructions for a detailed instruction listing
        Contains helper methods for working with bytecode outside the basic wrapper container
        Can save-ly exchange code regions with others, and redirect jump instructions correctly.
        Also contains code to inline whole methods into the code


        function __init__(self, patcher: FunctionPatcher | types.FunctionType)

            variable self.patcher

        function walk(self) -> typing.Iterable[typing.Tuple[int, dis.Instruction]]

        function store(self)

        function re_eval_instructions(self)

        function deleteRegion(self, start: int, end: int, safety=True)
            
            Deletes a region from start (including) to end (excluding) of the code, rebinding jumps and similar calls
            outside the region
            If safety is True, will ensure no direct jumps occur into this region
            (This is done during code walking for jump resolving)
            WARNING: the user is required to make sure that stack & variable constraints still hold


            variable i

            variable size

            function rebind_offset(o: int) -> int

            function rebind_real(o: int) -> int

                    variable offset

                    variable self.instruction_listing[i]

                    variable self.instruction_listing[i]

        function insertRegion(self, start: int, instructions: typing.List[dis.Instruction])
            
            Inserts a list of instructions into the opcode list, resolving the jumps in code correctly
            WARNING: the user is required to make sure that stack & variable constraints still hold


            variable size

            function rebind_offset(o: int) -> int

            function rebind_real(o: int) -> int

                    variable offset

                    variable self.instruction_listing[i]

                    variable self.instruction_listing[i]

            variable self.instruction_listing

        function replaceConstant(
                self,
                previous,
                new,
                matcher: typing.Callable[["MixinPatchHelper", int, int], bool] = None,
                ):
            
            Replaces a constant with another one
            :param previous: the old constant
            :param new: the new constant
            :param matcher: the matcher for instructions, or None


                variable const_index

                variable self.patcher.constants[const_index]

                variable const_index

            variable match

                        variable self.instruction_listing[index]

        function getLoadGlobalsLoading(
                self, global_name: str
                ) -> typing.Iterable[typing.Tuple[int, dis.Instruction]]:

        function insertMethodAt(self, start: int, method: FunctionPatcher, force_inline=True)
            
            Inserts a method body at the given position
            Does some magic for linking the code
            Use mixin_return or capture_local for advance control flow
            Will not modify the passed method. Will copy that object


        function insertMethodMultipleTimesAt(
                self,
                start: typing.List[int],
                method: FunctionPatcher,
                force_multiple_inlines=False,
                ):
            
            Similar to insertMethodAt(), but is able to do some more optimisations in how to inject the method.
            Works best when used with multiple injection targets
            :param start: the start to inject at
            :param method: the method to inject
            :param force_multiple_inlines: if we should force multiple inlines for each method call, or if we can
                optimise stuff


        function makeMethodAsync(self)
            
            Simply makes this method async, like it was declared by "async def"


            variable self.is_async

        function makeMethodSync(self)
            
            Simply makes this method sync, like it was declared without "async def"


            variable self.is_async

        function insertGivenMethodCallAt(
                self,
                offset: int,
                method: typing.Callable,
                *args,
                collected_locals=tuple(),
                pop_result=True,
                include_stack_top_copy=False,
                special_args_collectors: typing.Iterable[dis.Instruction] = tuple(),
                insert_after=tuple(),
                ):
            
            Injects the given method as a constant call into the bytecode of that function
            :param offset: the offset to inject at
            :param method: the method to inject
            :param collected_locals: what locals to send to the method call
            :param pop_result: if to pop the result
            :param include_stack_top_copy: if to add the stack top as the last parameter
            :param special_args_collectors: args collecting instructions for some stuff,
                the entry count represents the arg count added here
            :param insert_after: an iterable of instructions to insert after the method call


        function insertStaticMethodCallAt(self, offset: int, method: str, *args)
            
            Injects a static method call into another method
            :param offset: the offset to inject at, from function head
            :param method: the method address to inject, by module:path
            :param args: the args to invoke with
            WARNING: due to the need of a dynamic import instruction, the method to inject into cannot lie in the same
                package as the method call to inject
            todo: add option to load the method beforehand and inject as constant


            variable real_name

                variable real_module

                variable real_module

            variable instructions

        function insertAsyncStaticMethodCallAt(self, offset: int, method: str, *args)
            
            Injects a static method call to an async method into another method
            :param offset: the offset to inject at, from function head
            :param method: the method address to inject, by module:path
            :param args: the args to invoke with
            WARNING: due to the need of a dynamic import instruction, the method to inject into cannot lie in the same
                package as the method call to inject
            todo: add option to load the method beforehand and inject as constant


            variable real_name

                variable real_module

                variable real_module

            variable instructions

        static
        function prepare_method_for_insert(method: FunctionPatcher) -> FunctionPatcher
            
            Prepares a FunctionPatcher for being inserted into another method
            Does the stuff around the control flow control methods
            Will work on a copy of the method, not the method itself


            variable i

            variable helper

                variable instr

        function print_stats(self)