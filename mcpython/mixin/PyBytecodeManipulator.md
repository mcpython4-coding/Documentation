***PyBytecodeManipulator.py - documentation - last updated on 10.1.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable __all__

    function null()

    class FunctionPatcher
        
        Code inspired by https://rushter.com/blog/python-bytecode-patch/
        Wrapped class for handling __code__ objects at runtime,
        and writing the modified code back into the source function
        See https://docs.python.org/3.10/library/inspect.html
        and http://unpyc.sourceforge.net/Opcodes.html
        todo: add different wrapper types for different versions


        function __init__(self, target: FunctionType)

            variable self.target

            variable self.code

            variable self.argument_count
                Number of real arguments, neither positional only nor keyword arguments

            variable self.positional_only_argument_count

            variable self.keyword_only_argument_count

            variable self.number_of_locals

            variable self.max_stack_size

            variable self.flags
                Code flags, see https://docs.python.org/3.10/library/inspect.html#inspect-module-co-flags

            variable self.code_string
                The code string, transformed to a bytearray for manipulation

            variable self.constants
                The constants in the code, use ensureConstant when wanting new ones

            variable self.names
                The local variable name table

            variable self.variable_names

            variable self.filename

            variable self.name

            variable self.first_line_number

            variable self.line_number_table

            variable self.free_vars

            variable self.cell_vars

            variable self.can_be_reattached

                variable self.columntable

                variable self.exceptiontable

                variable self.end_line_table

                variable self.qual_name

            function applyPatches(self)
                
                Writes the data this container holds back to the function


                variable self.target.__code__

            function applyPatches(self)
                
                Writes the data this container holds back to the function


                variable self.target.__code__

        function create_method_from(self)

        function overrideFrom(self, patcher: "FunctionPatcher")
            
            Force-overrides the content of this patcher with the one from another one


        function copy(self)
            
            Creates a copy of this object WITHOUT method binding


        function ensureConstant(self, const) -> int
            
            Makes some constant arrival in the program
            :param const: the constant
            :return: the index into the constant table


        function get_instruction_list(self) -> typing.List[dis.Instruction]

        function instructionList2Code(self, instruction_list: typing.List[dis.Instruction])

            variable new_instructions

            variable skipped

                            variable data

                            variable data

                        variable data

                    variable skipped

        function ensureName(self, name: str) -> int

        function ensureVarName(self, name)

        function ensureFreeVar(self, name: str)

        function ensureCellVar(self, name: str)