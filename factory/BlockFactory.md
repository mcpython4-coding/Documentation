***BlockFactory.py - documentation - last updated on 14.5.2020 by uuk***
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

            variable block

            variable block.__dict__

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

                    variable states

                function __init__(self, *args, **kwargs)

                function on_remove(self)

                variable HARDNESS

                variable MINIMUM_TOOL_LEVEL

                variable BEST_TOOLS_TO_BREAK

                function set_model_state(self, state)

                function get_model_state(self)

                    variable state

                        variable state

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

            variable self.name

        function setCreateCallback(self, function)

            variable self.create_callback

        function setDeleteCallback(self, function)

            variable self.delete_callback

        function setBrakeAbleFlag(self, state: bool)

            variable self.breakable

        function setRandomUpdateCallback(self, function)

            variable self.randomupdate_callback

        function setUpdateCallback(self, function)

            variable self.update_callback

        function setCustomSolidSideFunction(self, function)

            variable self.customsolidsidefunction

        function setSolidSideTableEntry(self, side, state: bool)

            variable self.solid_faces[side]

        function setCustomModelStateFunction(self, function)

            variable self.custommodelstatefunction

        function setDefaultModelState(self, state: dict)

                variable state

            function get_state(*_)

        function setAllModelStateInfo(self, modelstates)

            variable self.modelstates

        function setInteractionCallback(self, function)

            variable self.interaction_callback

        function setFallable(self)

        function setAllSideSolid(self, state)

        function setLog(self)

            variable self.islog

        function setSlab(self)

        function setHardness(self, value: float)

            variable self.hardness

        function setMinimumToolLevel(self, value: int)

            variable self.minmum_toollevel

        function setBestTools(self, tools)

            variable self.besttools

        function setCustomItemstackModificationFunction(self, function)

            variable self.customitemstackmodifcationfunction

        function setCustomBlockItemModification(self, function)

            variable self.customblockitemmodificationfunction

        function setSpeedMultiplier(self, factor)

            variable self.speed_multiplier

        function setBlockItemGeneratorState(self, state: dict)

            variable self.block_item_generator_state

        function setHorizontalOrientable(self, face_name="facing")

            variable self.face_name