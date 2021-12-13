***ControlFlowAnalyser.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable FLOW_INTERRUPT
        RETURN_VALUE, RAISE_VARARGS

    variable FLOW_JUMP_CONDITIONAL_OFFSET
        SETUP_WITH, FOR_ITER, SETUP_FINALLY

    variable FLOW_JUMP_CONDITIONAL_DIRECT
        POP_JUMP_IF_TRUE, POP_JUMP_IF_FALSE, JUMP_IF_NOT_EXC_MATCH, JUMP_IF_TRUE_OR_POP
        JUMP_IF_FALSE_OR_POP

    class Branch

        function __init__(self, container: "ControlFlowAnalyser")

            variable self.container

            variable self.following_branches

            variable self.instructions

            variable self.batch

            variable self.rendering_objects

        function add_instruction(self, instr: dis.Instruction)

        function prepare_rendering(self)

        function draw(self)

    class ControlFlowAnalyser

        function __init__(
                self,
                target: typing.Union[types.FunctionType, FunctionPatcher, MixinPatchHelper],
                ):

                variable self.helper

                variable self.helper

                variable self.helper

            variable self.entry_branch

            variable self.offset2branch

        function calculate_branches(self)

                variable op

                variable branch

                    variable instr: dis.Instruction

                        variable branch

                        variable new

                        variable new

                        variable new

                        variable new

            variable self.entry_branch

        variable obj