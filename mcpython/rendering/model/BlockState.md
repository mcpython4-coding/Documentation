***BlockState.py - documentation - last updated on 29.7.2020 by uuk***
___

    class BlockStateNotNeeded extends Exception

    class IBlockStateDecoder extends mcpython.event.Registry.IRegistryContent

        variable TYPE

        static
        function is_valid(cls, data: dict) -> bool: raise NotImplementedError()
                
                def __init__(self, data: dict, block_state):

        function __init__(self, data: dict, block_state)

            variable self.data

            variable self.block_state

        function add_face_to_batch(self, block, batch, face) -> list

        function draw_face(self, block, face):  # optional: draws the BlockState direct without an batch
                pass
                
                def bake(self) -> bool:

        function bake(self) -> bool
            
            Called when it is time to bake it
            :return: if it was successful or not


    variable blockstatedecoderregistry

    @G.registry class MultiPartDecoder extends IBlockStateDecoder
        
        Decoder for mc multipart state files.
        WARNING: the following decoder has some extended features:
        entry parent: An parent DefaultDecoded blockstate from which states and model aliases should be copied
        entry alias: An dict of original -> aliased model to transform any model name of this kind in the system with the given model. Alias names MUST start with alias:
        todo: can we optimize it by pre-doing some stuff?


        variable NAME

        static
        function is_valid(cls, data: dict) -> bool

        function __init__(self, data: dict, block_state)

        function bake(self)

        function add_face_to_batch(self, block, batch, face)

        static
        function _test_for(cls, state, part, use_or=False)

        function transform_to_hitbox(self, blockinstance)

        function draw_face(self, block, face)

    @G.registry class DefaultDecoder extends IBlockStateDecoder
        
        Decoder for mc block state files.
        WARNING: the following decoder has some extended features:
        entry parent: An parent DefaultDecoded blockstate from which states and model aliases should be copied
        entry alias: An dict of original -> aliased model to transform any model name of this kind in the system with the given model. Alias names MUST start with alias:


        variable NAME

        static
        function is_valid(cls, data: dict) -> bool

        function __init__(self, data: dict, block_state)

            variable self.states

                    variable keymap

                        variable keymap[e.split("=")[0]]

        function bake(self)

        function add_face_to_batch(self, block, batch, face)

        function transform_to_hitbox(self, blockinstance)

        function draw_face(self, block, face)

    class BlockStateDefinition

        variable TO_CREATE

        variable LOOKUP_DIRECTORIES

        variable NEEDED - for parent <-> child connection

        static
        function from_directory(cls, directory: str, modname: str, immediate=False)

        static
        function from_file(cls, file: str, modname: str, immediate=False)

        static
        function _from_file(cls, file: str)

        static
        function from_data(cls, name, data)

        static
        function _from_data(cls, name, data)

        function __init__(self, data: dict, name: str)

            variable self.name

            variable G.modelhandler.blockstates[name]

            variable self.loader

                    variable self.loader

        function bake(self)

        function add_face_to_batch(self, block, batch, face)

        function draw_face(self, block, face)

    class BlockState

        function __init__(self, data)

            variable self.data

            variable self.models - (model, config, weight)

        function copy(self)

        static
        function decode_entry(data: dict)

        function add_face_to_batch(self, block, batch, face)

        function draw_face(self, block, face)