***BlockState.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class BlockStateNotNeeded extends Exception

    class IBlockStateDecoder extends mcpython.common.event.Registry.IRegistryContent
        
        Abstract base class for block state decoders
        Identification of files to decode:
            bool(is_valid(data)) == True, where data is the loaded json data
            for developers of mods: add an entry called "mod_marker" storing the mod name the loader is implemented in and
                check for it here
        Loading:
            __init__(data, BlockStateDefinition) -> Instance
        Baking:
            bake() is called to bake references and do similar stuff, returning success or not
        Drawing:
            add_face_to_batch() should add the given face to the batches given
            add_raw_face_to_batch() should add a face to the batch without the block instance, but instead the position
            draw() should draw the block in-place
        todo: add draw variant for raw
        todo: add data getter functions for better performance
        todo: cache non-offset data from models per state for faster drawing
        todo: can we do something rendering wise which will make it efficient to draw multiple same blocks
        todo: block batches should be selected before, based on a property on block class


        variable TYPE

        static
        function is_valid(cls, data: dict) -> bool

        function __init__(self, data: dict, block_state: "BlockStateDefinition")

            variable self.data

            variable self.block_state

        function bake(self) -> bool

        function add_face_to_batch(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                batch: pyglet.graphics.Batch,
                face: mcpython.util.enums.EnumSide,
                ) -> list:

        function add_raw_face_to_batch(self, position, state, batches, faces)

        function draw_face(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                face: mcpython.util.enums.EnumSide,
                ):  # optional: draws the BlockState direct without an batch
                pass
                
                def transform_to_hitbox(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                ):  # optional: transforms the BlockState into an BoundingBox-like objects
                pass
                
                
                blockstate_decoder_registry = mcpython.common.event.Registry.Registry(
                "minecraft:blockstates",
                ["minecraft:blockstate"],
                "stage:blockstate:register_loaders",
                )
                
                
                @shared.registry
                class MultiPartDecoder(IBlockStateDecoder):

        function transform_to_hitbox(
                self,
                instance: mcpython.client.rendering.model.api.IBlockStateRenderingTarget,
                ):  # optional: transforms the BlockState into an BoundingBox-like objects
                pass
                
                
                blockstate_decoder_registry = mcpython.common.event.Registry.Registry(
                "minecraft:blockstates",
                ["minecraft:blockstate"],
                "stage:blockstate:register_loaders",
                )
                
                
                @shared.registry
                class MultiPartDecoder(IBlockStateDecoder):

    variable blockstate_decoder_registry

    @shared.registry class MultiPartDecoder extends IBlockStateDecoder
        
        Decoder for mc multipart state files.
        WARNING: the following decoder has some extended features:
        entry parent: An parent DefaultDecoded blockstate from which states and model aliases should be copied
        entry alias: An dict of original -> aliased model to transform any model name of this kind in the system with the given model. Alias names MUST start with alias:
        todo: can we optimize it by pre-doing some stuff?
        todo: fix alias system


        variable NAME

        static
        function is_valid(cls, data: dict) -> bool

        function __init__(self, data: dict, block_state)

            variable self.model_alias

                variable self.parent

                variable self.model_alias

        function bake(self)

                variable self.parent

                variable data

                        variable data["model"]

                            variable data[i]["model"]

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
        function get_or_load(cls, name: str) -> "BlockStateDefinition"

            variable file

            variable data

        function __init__(self, data: dict, name: str, immediate=False, force=False)

            variable self.name

            variable shared.model_handler.blockstates[name]

            variable self.loader

                    variable self.loader

            variable self.baked

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