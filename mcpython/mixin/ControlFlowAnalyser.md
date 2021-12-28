***ControlFlowAnalyser.py - documentation - last updated on 28.12.2021 by uuk***
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

    variable FLOW_JUMP_CONDITIONAL_OFFSET
        SETUP_WITH, FOR_ITER, SETUP_FINALLY

    variable FLOW_JUMP_CONDITIONAL_DIRECT
        POP_JUMP_IF_TRUE, POP_JUMP_IF_FALSE, JUMP_IF_NOT_EXC_MATCH, JUMP_IF_TRUE_OR_POP
        JUMP_IF_FALSE_OR_POP

    class Branch

        function __init__(self, container: "ControlFlowAnalyser")

            variable self.container

            variable self.following_branches

            variable self.instructions: typing.List[dis.Instruction]

            variable self.dataflow_for_instructions

            variable self.batch

            variable self.rendering_objects

        function add_instruction(self, instr: dis.Instruction)

        function prepare_rendering(self)

        function draw(self)

        function prepare_dataflow(self, tracker: "StackAnalyserTracker")

                        variable a

                        variable b

                        variable a

                        variable b

                        variable c

                        variable a

                        variable b

                        variable c

                        variable d

                        variable a

                        variable a

                        variable b

    class IDataFlowDataSource

    class StackAnalyserTracker

        function __init__(self)

            variable self.stack_data_flow: typing.List[IDataFlowDataSource]

        function pop(self)

        function push(self, value: IDataFlowDataSource)

    class ConstantDataSource extends IDataFlowDataSource

        function __init__(self)

            variable self.value

    class InvokeResultSource extends IDataFlowDataSource

        function __init__(self)

            variable self.body_ref: str

            variable self.arg_sources: typing.List[IDataFlowDataSource]

    class IterItemSource extends IDataFlowDataSource

        function __init__(self)

            variable self.iter_source: IDataFlowDataSource

    class IterUnpackSource extends IDataFlowDataSource

        function __init__(self)

            variable self.iter_source: IDataFlowDataSource

            variable self.iter_item

    class AttributSource extends IDataFlowDataSource

        function __init__(self)

            variable self.name: str

            variable self.target: IDataFlowDataSource

    class ModuleImportSource extends IDataFlowDataSource

        function __init__(self)

            variable self.module_name: str

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

        function calculate_data_flow(self)

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