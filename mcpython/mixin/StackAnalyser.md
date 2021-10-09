***StackAnalyser.py - documentation - last updated on 9.10.2021 by uuk***
___

    class StackAnalyser
        
        Code for statically analyzing the stack of a MixinPatchHelper wrapper object


        function __init__(self, patcher: MixinPatchHelper)

            variable self.patcher

            variable self.possible_return_values

            variable self.possible_yielded_values

        function prepareSimpleStack(self)

            variable self.opcode2stack

            variable visited_nodes

        function visitCp(self, cp: int, visited: typing.Set[int], stack: list, local: list, named_locals: dict)

            variable instr: dis.Instruction

                variable a

                variable a

                variable named_locals[instr.argval]

                variable keys

                variable local[instr.arg]

                variable local[instr.arg]
                
                index = instr.arg
                if index < len(self.patcher.patcher.cell_vars):
                    stack.append(self.patcher.patcher.cell_vars[index])
                else:
                    stack.append(self.patcher.patcher.free_vars[index-len(self.patcher.patcher.cell_vars)])
