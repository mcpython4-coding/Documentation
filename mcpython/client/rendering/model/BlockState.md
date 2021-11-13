***BlockState.py - documentation - last updated on 13.11.2021 by uuk***
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


        variable NAME

        static
        function is_valid(cls, data: dict) -> bool

        function __init__(self, block_state)

            variable self.parent

            variable self.model_alias

        function parse_data(self, data: dict)

                variable self.parent

                variable self.model_alias

        function bake(self)

                    variable self.parent

                    variable self.model_alias

                variable data

                        variable data["model"]

                            variable data[i]["model"]

        function add_face_to_batch(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                batch: pyglet.graphics.Batch,
                face: mcpython.util.enums.EnumSide,
                previous=None,
                ):

            variable state

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
        entry alias: An dict of original -> aliased model to transform any model name of this kind in the system with the given model. Alias names MUST start with alias:


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

        function bake(self)

                variable self.parent

                        variable state.models[i]

                        variable model

        function add_face_to_batch(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                batch: pyglet.graphics.Batch,
                face: mcpython.util.enums.EnumSide,
                ):

            variable data

        function add_raw_face_to_batch(
                self, instance: IBlockStateRenderingTarget, position, state, batches, face
                ):

            variable state

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

        static
        function from_directory(cls, directory: str, modname: str, immediate=False)

        static
        function from_file(cls, file: str, modname: str, immediate=False)

        static
        function unsafe_from_file(cls, file: str)

        static
        function from_data(
                cls,
                name: str,
                data: typing.Dict[str, typing.Any],
                immediate=False,
                store=True,
                force=False,
                ):

        static
        function unsafe_from_data(
                cls, name: str, data: typing.Dict[str, typing.Any], immediate=False, force=False
                ):

                variable instance

        static
        function get_or_load(cls, name: str) -> "BlockStateContainer"

            variable file

            variable data

        function __init__(self, name: str, immediate=False, force=False)

            variable self.name

            variable shared.model_handler.blockstates[name]

            variable self.loader

            variable self.baked

        function parse_data(self, data: dict)

        function bake(self)

        function add_face_to_batch(
                self,
                block: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                batch: pyglet.graphics.Batch,
                face: mcpython.util.enums.EnumSide,
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

        function __init__(self)

            variable self.data

            variable self.models - (model, config, weight)

        function parse_data(self, data: dict)

                variable models

        function copy(self)

        function add_face_to_batch(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                batch: pyglet.graphics.Batch,
                face: mcpython.util.enums.EnumSide,
                ):

                variable instance.block_state

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