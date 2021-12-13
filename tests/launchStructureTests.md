***launchStructureTests.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable launch

    variable test_mod

    class AbstractStructureTestAction extends ABC

        variable TYPE_NAME: str

        function setup(self, test: "StructureTest")

        function get_comparable_identifier(self)

    class AbstractStructureTestValidator extends ABC

        variable TYPE_NAME: str

        function validate(self, test: "StructureTest") -> bool

    class EndOfTestAction extends AbstractStructureTestValidator

        function validate(self, test: "StructureTest") -> bool

    class StructureTest

        class StructureTestStage

            function __init__(self, test: "StructureTest")

                variable self.test

                variable self.actions

                variable self.validators

                variable self.delay_after

            function clean(self)

            function run_actions(self)

            function validate(self)

            function add_action(self, action: AbstractStructureTestAction)

            function add_validator(self, validator: AbstractStructureTestValidator)

        function __init__(self)

            variable self.env_variables

            variable self.stages: typing.List["StructureTest.StructureTestStage"]

            variable self.current_stage

            variable self.requirements

        function set_env_variable(self, variable: str, value)

        function get_env_variable(self, variable: str)

        function decode_from_data(self, data: dict)

        function begin(self)

            variable setup

            variable end

        function next_stage(self, dt=None)

            variable stage

    class StructureTestManager

        function __init__(self)

            variable self.tests: typing.List[StructureTest]

            variable self.current_test

            variable self.validators

        function register_requirement_loader(
                self, name: str, loader: typing.Callable[[StructureTest], None]
                ):

            variable self.requirements[name]

        function register_test_action(self, part: typing.Type[AbstractStructureTestAction])

        function register_test_validator(
                self, validator: typing.Type[AbstractStructureTestValidator]
                ):

            variable self.validators[validator.TYPE_NAME]

        function register_test(self, test: StructureTest)

        function start_tests(self)

        function next_test(self)

        function look_for_empty_chunk(self) -> typing.Tuple[int, int]

        function get_free_player(self) -> str

        function enforce_requirement(self, test: StructureTest, req: str)

    class PlayerController

        function __init__(self, test: StructureTest)

            variable self.test

        function prepareInventory(self)

    variable manager

    function intercept_loading(handler)

        variable world_config_state

        @PUBLIC_EVENT_BUS.subscribe("on_game_enter")
        function on_game_enter()