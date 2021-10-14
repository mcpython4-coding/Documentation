***MixinMethodWrapper.py - documentation - last updated on 14.10.2021 by uuk***
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


    variable OFFSET_JUMPS

    variable REAL_JUMPS

    class MixinPatchHelper
        
        See https://docs.python.org/3/library/dis.html#python-bytecode-instructions for a detailed instruction listing
        Contains helper methods for working with bytecode outside the basic wrapper


        function __init__(self, patcher: FunctionPatcher)

            variable self.patcher

            variable self.instruction_listing

        function walk(self) -> typing.Iterable[typing.Tuple[int, dis.Instruction]]

        function store(self)

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

        static
        function prepare_method_for_insert(method: FunctionPatcher) -> FunctionPatcher
            
            Prepares a FunctionPatcher for being inserted into another method
            Does the stuff around the control flow control methods
            Will work on a copy of the method, not the method itself


            variable i

            variable helper

                variable instr