***ModelHandler.py - documentation - last updated on 9.2.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @forced_attribute_type("break_stages", list) @forced_attribute_type("raw_models", list) @forced_attribute_type("hide_blockstate_errors", lambda: bool) @forced_attribute_type("dependence_list", lambda: list) @forced_attribute_type("lookup_locations", lambda: set) @forced_attribute_type("blockstates", lambda: dict) @forced_attribute_type("found_models", lambda: dict) @forced_attribute_type("used_models", lambda: set) @forced_attribute_type("models", lambda: dict) class ModelHandler

        function __init__(self)

            variable self.used_models: typing.Set[str]

            variable self.lookup_locations: typing.Set[str]

            variable self.dependence_list

            variable self.hide_blockstate_errors

            variable self.raw_models

            variable SIZE

            variable self.break_stages
                todo: reload these textures on normal reload
            
            Will add locations for a given mod name
            :param modname: the mod to use

            
            Will search all locations for new stuff
            todo: add datapack locations


                variable found_models

                    variable s

                    variable mod_fix

                    variable address_fix

                    variable name

                    variable self.found_models[name]

                    variable self.found_models[name]

        function add_from_data(self, name: str, data: dict, store=True)
            
            Will inject data as a block-model file
            :param name: the name to use
            :param data: the data to inject
            :param store: if it should be stored and re-loaded on reload event


            variable modname

                variable modname

                variable used

            variable file

                    variable data

                    variable data

                variable data

                variable depend

                variable depend

                variable sorted_models

                variable name

            variable location

                        variable model_data

                        variable self.models[name]

                            variable self.models[

                            variable self.models[name]

                        variable self.models[

                        variable self.models[name]

        @deprecation.deprecated()
        function add_face_to_batch(
                self, block: IBlockStateRenderingTarget, face: EnumSide, batches
                ) -> typing.Iterable:

            variable blockstate

        function add_faces_to_batch(
                self, block, faces: int, batches: typing.List
                ) -> typing.Iterable:
            
            Adds a collection of faces to a batch
            :param block: the thing to get rendering information from
            :param faces: n bitmap describing the faces
            :param batches: the batches to render into  todo: make single-atlas able
            :return: a list of vertex lists


            variable blockstate

        function add_raw_face_to_batch(
                self,
                instance: IBlockStateRenderingTarget,
                position,
                state,
                block_state_name: str,
                batches,
                face,
                ):

                variable vertex_list

                variable blockstate

                variable vertex_list

        function draw_face(self, block, face)

            variable blockstate

        function draw_face_scaled(self, block, face, scale: float)

            variable blockstate

        function draw_block(self, block)

        function draw_block_scaled(self, block, scale: float)

        function get_bbox(self, block)

        function draw_block_break_overlay(
                self, position: typing.Tuple[float, float, float], progress: float
                ):

            variable stage

            variable model

    variable shared.model_handler