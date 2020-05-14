***BlockState.py - documentation - last updated on 14.5.2020 by uuk***
___

    class BlockStateNotNeeded extends Exception

    class IBlockStateDecoder extends event.Registry.IRegistryContent

        variable TYPE

        static function is_valid(cls, data: dict) -> bool
        function __init__(self, data: dict, block_state)
        function add_face_to_batch(self, block, batch, face) -> list
        function transform_to_hitbox(self, block):  # optional
        function draw_face(self, block, face):  # optional

    variable blockstatedecoderregistry


    @G.registry class MultiPartDecoder extends IBlockStateDecoder

        variable NAME

        static function is_valid(cls, data: dict) -> bool
        function __init__(self, data: dict, block_state)
        function add_face_to_batch(self, block, batch, face)
        static function _test_for(cls, state, part, use_or=False)
        function transform_to_hitbox(self, blockinstance)
        function draw_face(self, block, face)

    @G.registry class DefaultDecoder extends IBlockStateDecoder

        variable NAME

        static function is_valid(cls, data: dict) -> bool
        function __init__(self, data: dict, block_state)
        function add_face_to_batch(self, block, batch, face)
        function transform_to_hitbox(self, blockinstance)
        function draw_face(self, block, face)
        
    @G.registry
    class ForgeVersionDecoder(IBlockStateDecoder):
        @classmethod
        def is_valid(cls, data: dict) -> bool:
            return "forge_marker" in data and data["forge_marker"] == 1 and "mod_marker" not in data
    
        def __init__(self, data: dict, block_state):
            super().__init__(data, block_state)
    
        def add_face_to_batch(self, block, batch, face):
            return []
    
        def transform_to_hitbox(self, block): raise NotImplementedError()


    class BlockStateDefinition

        variable TO_CREATE

        static function from_directory(directory: str, modname: str)
        static function from_file(cls, file: str, modname: str)
        static function _from_file(cls, file: str)
        static function from_data(cls, name, data)
        static function _from_data(cls, name, data)
        function __init__(self, data: dict, name: str)
        function add_face_to_batch(self, block, batch, face)
        function draw_face(self, block, face)

    class BlockState
        function __init__(self, data)
        static function decode_entry(data: dict)
        function add_face_to_batch(self, block, batch, face)
        function draw_face(self, block, face)