***BlockState.py - documentation - last updated on 5.2.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable blockstate_decoder_registry

    class MultiPartDecoder extends IBlockStateDecoder
        
        Decoder for mc multipart state files.
        WARNING: the following decoder has some extended features:
        entry parent: An parent DefaultDecoded blockstate from which states and model aliases should be copied
        entry alias: An dict of original -> aliased model to transform any model name of this kind in the system with the given model. Alias names MUST start with alias:
        todo: can we optimize it by pre-doing some stuff?
        todo: fix alias system


        variable __slots__

        variable NAME

        @forced_arg_type("data", lambda: dict, may_subclass=False)
        static
        function is_valid(cls, data: dict) -> bool

        function __init__(self, block_state)

            variable self.parent

            variable self.model_alias

        @forced_arg_type("data", lambda: dict, may_subclass=False)
        @builtins_are_static()
        function parse_data(self, data: dict)

                variable self.parent

                variable self.model_alias

                    variable parent: BlockStateContainer

                    variable self.parent

                        variable self.parent

                    variable self.parent

                    variable self.model_alias

                variable data

                        variable data["model"]

                            variable data[i]["model"]

        @deprecation.deprecated()
        function add_face_to_batch(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                batch: pyglet.graphics.Batch,
                face: mcpython.util.enums.EnumSide,
                previous=None,
                ):

            variable state

            variable box_model

            variable box_model

        function add_faces_to_batch(
                self,
                instance: IBlockStateRenderingTarget,
                batch: pyglet.graphics.Batch,
                faces: int,
                previous=None,
                ) -> typing.Iterable:

            variable state

            variable box_model

            variable box_model

        static
        function _test_for(cls, state, part, use_or=False)

        function transform_to_bounding_box(
                self, instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget
                ):

            variable state

            variable bbox

                    variable data

                        variable model

                        variable model

        function draw_face(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                face: mcpython.util.enums.EnumSide,
                previous=None,
                ):

            variable state

            variable box_model

        function draw_face_scaled(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                face: mcpython.util.enums.EnumSide,
                scale: float,
                previous=None,
                ):

            variable state

            variable box_model

        function prepare_rendering_data(
                self,
                box_model,
                face,
                instance: IBlockStateRenderingTarget,
                prepared_texture,
                prepared_vertex,
                prepared_tint,
                state,
                ):

                    variable data

        function prepare_rendering_data_multi_face(
                self,
                box_model,
                faces: int,
                instance: IBlockStateRenderingTarget,
                prepared_texture,
                prepared_vertex,
                prepared_tint,
                prepare_vertex_elements,
                state,
                batch: pyglet.graphics.Batch = None,
                ):

                    variable data

        function prepare_rendering_data_scaled(
                self,
                box_model,
                face,
                instance: IBlockStateRenderingTarget,
                prepared_texture,
                prepared_vertex,
                prepared_tint,
                state,
                scale: float,
                ):

                    variable data

    class DefaultDecoder extends IBlockStateDecoder
        
        Decoder for mc block state files.
        WARNING: the following decoder has some extended features:
        entry parent: An parent DefaultDecoded blockstate from which states and model aliases should be copied
        entry alias: An dict of original -> aliased model to transform any model name of this kind in the system with the given model.
        Alias names MUST start with "alias:"
        todo: add better lookup system for variants


        variable __slots__

        variable NAME

        static
        function is_valid(cls, data: dict) -> bool

        function __init__(self, block_state)

            variable self.parent

            variable self.model_alias

            variable self.states

        function parse_data(self, data: dict)

                    variable keymap

                        variable keymap[e.split("=")[0]]

                    variable keymap

            variable self.model_alias

            variable self.parent

                variable self.parent

                variable self.model_alias

                variable parent: BlockStateContainer

                variable self.parent

                        variable state.models[i]

                        variable model

        @deprecation.deprecated()
        function add_face_to_batch(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                batch: pyglet.graphics.Batch,
                face: mcpython.util.enums.EnumSide,
                ):

            variable data

        function add_faces_to_batch(
                self,
                instance: IBlockStateRenderingTarget,
                batch: pyglet.graphics.Batch,
                faces: int,
                ) -> typing.Iterable:

            variable data

        function add_raw_face_to_batch(
                self, instance: IBlockStateRenderingTarget, position, state, batches, face
                ):

        function transform_to_bounding_box(
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

        function draw_face_scaled(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                face: mcpython.util.enums.EnumSide,
                scale: float,
                ):

            variable data

    class BlockStateContainer

        variable TO_CREATE

        variable LOOKUP_DIRECTORIES

        variable RAW_DATA

        variable NEEDED - for parent <-> child connection

                variable s

                variable modname

                variable instance

            variable file

            variable data

        variable __slots__

        function __init__(self, name: str, immediate=False, force=False)

            variable self.name

            variable shared.model_handler.blockstates[name]

            variable self.loader

            variable self.baked

                    variable self.loader: IBlockStateDecoder

                    variable self.baked

                variable self.baked

        @deprecation.deprecated()
        function add_face_to_batch(self, block, batch, face)

        function add_faces_to_batch(
                self,
                block: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                batch: pyglet.graphics.Batch,
                faces: int,
                ):

        function add_raw_face_to_batch(
                self,
                instance: IBlockStateRenderingTarget,
                position: tuple,
                state,
                batches,
                face,
                ):

        function draw_face(
                self,
                block: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                face: mcpython.util.enums.EnumSide,
                ):

        function draw_face_scaled(
                self,
                block: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                face: mcpython.util.enums.EnumSide,
                scale: float,
                ):

    class BlockState
        
        Container holding a single block state link
        todo: don't store the raw data


        variable __slots__

        function __init__(self)

            variable self.data

            variable self.models - (model, config, weight)

        function parse_data(self, data: dict)

                variable models

        function copy(self)

        @deprecation.deprecated()
        function add_face_to_batch(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                batch: pyglet.graphics.Batch,
                face: mcpython.util.enums.EnumSide,
                ):

        function add_faces_to_batch(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                batch: pyglet.graphics.Batch,
                faces: int,
                ):

                variable instance.block_state

            variable m

            variable result

        function add_raw_face_to_batch(
                self, instance: IBlockStateRenderingTarget, position, batches, face
                ):

            variable block_state

            variable result

        function draw_face(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                face: mcpython.util.enums.EnumSide,
                ):

                variable instance.block_state

        function draw_face_scaled(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                face: mcpython.util.enums.EnumSide,
                scale: float,
                ):

                variable instance.block_state