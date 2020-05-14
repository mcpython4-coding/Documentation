***BlockState.py - documentation - last updated on 14.5.2020 by uuk***
___

    class BlockStateNotNeeded extends Exception

    class IBlockStateDecoder extends event.Registry.IRegistryContent

        variable TYPE

        static function is_valid(cls, data: dict) -> bool

        function __init__(self, data: dict, block_state)

            variable self.data

            variable self.block_state

        function add_face_to_batch(self, block, batch, face) -> list

        function transform_to_hitbox(self, block):  # optional

        function draw_face(self, block, face):  # optional

    variable blockstatedecoderregistry

    @G.registry class MultiPartDecoder extends IBlockStateDecoder

        variable NAME

        static function is_valid(cls, data: dict) -> bool

        function __init__(self, data: dict, block_state)

        function add_face_to_batch(self, block, batch, face)

            variable state

            variable result

                    variable data

                            variable entries

                            variable block.block_state

        static function _test_for(cls, state, part, use_or=False)

                        variable condition

                        variable condition

                        variable condition

                        variable condition

        function transform_to_hitbox(self, blockinstance)

            variable state

            variable bbox

                    variable data

                        variable model

                            variable entries

                            variable block.block_state

                        variable model

        function draw_face(self, block, face)

            variable state

                    variable data

                            variable entries

                            variable block.block_state

    @G.registry class DefaultDecoder extends IBlockStateDecoder

        variable NAME

        static function is_valid(cls, data: dict) -> bool

        function __init__(self, data: dict, block_state)

            variable self.states

                    variable keymap

                        variable keymap[e.split("=")[0]]

                    variable keymap

        function add_face_to_batch(self, block, batch, face)

            variable data

        function transform_to_hitbox(self, blockinstance)

            variable data

            variable bbox

                    variable model

                        variable rotation

        function draw_face(self, block, face)

            variable data
        
    @G.registry
    class ForgeVersionDecoder(IBlockStateDecoder):
        @classmethod
        def is_valid(cls, data: dict) -> bool:
            return "forge_marker" in data and data["forge_marker"] == 1 and "mod_marker" not in data
        def __init__(self, data: dict, block_state):
            super().__init__(data, block_state)
        def add_face_to_batch(self, block, batch, face):
            return []


    class BlockStateDefinition

        variable TO_CREATE

        static function from_directory(directory: str, modname: str)

        static function from_file(cls, file: str, modname: str)

        static function _from_file(cls, file: str)

                variable s

                variable modname

        static function from_data(cls, name, data)

        static function _from_data(cls, name, data)

        function __init__(self, data: dict, name: str)

            variable G.modelhandler.blockstates[name]

            variable self.loader

                    variable self.loader

        function add_face_to_batch(self, block, batch, face)

        function draw_face(self, block, face)

    class BlockState

        function __init__(self, data)

            variable self.models - (model, config)

                variable models

        static function decode_entry(data: dict)

            variable model

            variable rotations

        function add_face_to_batch(self, block, batch, face)

                variable block.block_state

            variable result

        function draw_face(self, block, face)

                variable block.block_state