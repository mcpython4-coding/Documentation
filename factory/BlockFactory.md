***BlockFactory.py - documentation - last updated on 16.5.2020 by uuk***
___

    class BlockFactory

        function __init__(self)

            variable self.name

            variable self.breakable

            variable self.modelstates

            variable self.solid_faces

            variable self.create_callback

            variable self.delete_callback

            variable self.randomupdate_callback

            variable self.update_callback

            variable self.interaction_callback

            variable self.hardness

            variable self.minmum_toollevel

            variable self.besttools

            variable self.speed_multiplier

            variable self.block_item_generator_state

            variable self.face_name

            variable self.customsolidsidefunction

            variable self.custommodelstatefunction

            variable self.customitemstackmodifcationfunction

            variable self.customblockitemmodificationfunction

            variable self.islog

            variable self.baseclass

        function copy(self)

        function finish(self, register=True)

        function _finish(self, register)

            class baseclass extends object

                class baseclass extends baseclass,  cls

            variable master

            class ConstructedBlock extends baseclass

                variable CUSTOM_WALING_SPEED_MULTIPLIER

                variable NAME

                variable BLOCK_ITEM_GENERATOR_STATE

                variable BREAKABLE

                static function get_all_model_states()

                function __init__(self, *args, **kwargs)

                function on_remove(self)

                variable HARDNESS

                variable MINIMUM_TOOL_LEVEL

                variable BEST_TOOLS_TO_BREAK

                function set_model_state(self, state)

                function get_model_state(self)

                class ConstructedBlock extends ConstructedBlock

                    variable self.face_solid

                class ConstructedBlock extends ConstructedBlock

                    function on_random_update(self)

                class ConstructedBlock extends ConstructedBlock

                    function on_block_update(self)

                class ConstructedBlock extends ConstructedBlock

                    function get_model_state(self) -> dict

                class ConstructedBlock extends ConstructedBlock

                    function on_player_interact(self, player, itemstack, button, modifiers, exact_hit) -> bool

                class ConstructedBlock extends ConstructedBlock

                    function on_request_item_for_block(self, itemstack)

                class ConstructedBlock extends ConstructedBlock

                    static function modify_block_item(cls, itemconstructor)

                class ConstructedBlock extends ConstructedBlock

                    variable MODEL_FACE_NAME

        function setName(self, name: str)

        function setCreateCallback(self, function)

        function setDeleteCallback(self, function)

        function setBrakeAbleFlag(self, state: bool)

        function setRandomUpdateCallback(self, function)

        function setUpdateCallback(self, function)

        function setCustomSolidSideFunction(self, function)

        function setSolidSideTableEntry(self, side, state: bool)

        function setCustomModelStateFunction(self, function)

        function setDefaultModelState(self, state: dict)

        function setAllModelStateInfo(self, modelstates)

        function setInteractionCallback(self, function)

        function setFallable(self)

        function setAllSideSolid(self, state)

        function setLog(self)

        function setSlab(self)

        function setHardness(self, value: float)

        function setMinimumToolLevel(self, value: int)

        function setBestTools(self, tools)

        function setCustomItemstackModificationFunction(self, function)

        function setCustomBlockItemModification(self, function)

        function setSpeedMultiplier(self, factor)

        function setBlockItemGeneratorState(self, state: dict)

        function setHorizontalOrientable(self, face_name="facing")