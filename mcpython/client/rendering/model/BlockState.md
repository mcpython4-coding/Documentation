***BlockState.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class BlockStateNotNeeded extends Exception

    class IBlockStateDecoder extends mcpython.common.event.Registry.IRegistryContent

        variable TYPE

        static
        function is_valid(cls, data: dict) -> bool

        function __init__(self, data: dict, block_state)

            variable self.data

            variable self.block_state

        function add_face_to_batch(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                batch: pyglet.graphics.Batch,
                face: mcpython.util.enums.EnumSide,
                ) -> list:

        function add_raw_face_to_batch(self, position, state, batches, faces)

        function transform_to_hitbox(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                ):  # optional: transforms the BlockState into an BoundingBox-like objects
                pass
                
                def draw_face(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                face: mcpython.util.enums.EnumSide,
                ):  # optional: draws the BlockState direct without an batch
                pass
                
                def bake(self) -> bool:

        function draw_face(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                face: mcpython.util.enums.EnumSide,
                ):  # optional: draws the BlockState direct without an batch
                pass
                
                def bake(self) -> bool:

        function bake(self) -> bool
            
            Called when it is time to bake it
            :return: if it was successful or not


    variable blockstate_decoder_registry

    @shared.registry class MultiPartDecoder extends IBlockStateDecoder
        
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

        function add_face_to_batch(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                batch: pyglet.graphics.Batch,
                face: mcpython.util.enums.EnumSide,
                ):

            variable state

                    variable data

                            variable entries

                            variable instance.block_state

        static
        function _test_for(cls, state, part, use_or=False)

        function transform_to_hitbox(
                self, instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget
                ):

            variable state

            variable bbox

                    variable data

                        variable model

                            variable entries

                            variable instance.block_state

                        variable model

        function draw_face(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                face: mcpython.util.enums.EnumSide,
                ):

            variable state

                    variable data

                            variable entries

                            variable instance.block_state

    @shared.registry class DefaultDecoder extends IBlockStateDecoder
        
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

                variable parent: BlockStateDefinition

                variable self.parent

                        variable state.models[i]

        function add_face_to_batch(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                batch: pyglet.graphics.Batch,
                face: mcpython.util.enums.EnumSide,
                ):

            variable data

        function add_raw_face_to_batch(self, position, state, batches, face)

        function transform_to_hitbox(
                self, instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget
                ):

                variable instance.block_state

            variable data

            variable bbox

                    variable model

                        variable rotation

        function draw_face(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                face: mcpython.util.enums.EnumSide,
                ):

            variable data

    class BlockStateDefinition

        variable TO_CREATE

        variable LOOKUP_DIRECTORIES

        variable NEEDED - for parent <-> child connection

        static
        function from_directory(cls, directory: str, modname: str, immediate=False)

        static
        function from_file(cls, file: str, modname: str, immediate=False)

        static
        function unsafe_from_file(cls, file: str)

        static
        function from_data(cls, name: str, data: typing.Dict[str, typing.Any], immediate=False)

        static
        function unsafe_from_data(cls, name: str, data: typing.Dict[str, typing.Any])

        function __init__(self, data: dict, name: str)

            variable self.name

        function bake(self)

        function add_face_to_batch(
                self,
                block: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                batch: pyglet.graphics.Batch,
                face: mcpython.util.enums.EnumSide,
                ):

        function add_raw_face_to_batch(self, position: tuple, state, batches, face)

        function draw_face(
                self,
                block: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                face: mcpython.util.enums.EnumSide,
                ):

    class BlockState

        static
        function decode_entry(data: typing.Dict[str, typing.Any])

        function __init__(self, data: dict)

            variable self.data

            variable self.models - (model, config, weight)

        function copy(self)

        function add_face_to_batch(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                batch: pyglet.graphics.Batch,
                face: mcpython.util.enums.EnumSide,
                ):

                variable instance.block_state

            variable result

        function add_raw_face_to_batch(self, position, batches, face)

        function draw_face(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                face: mcpython.util.enums.EnumSide,
                ):

                variable instance.block_state