***ModelHandler.py - documentation - last updated on 23.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class ModelHandler

        function __init__(self)

            variable self.models

            variable self.used_models

            variable self.found_models

            variable self.blockstates

            variable self.lookup_locations

            variable self.dependence_list

            variable self.hide_blockstate_errors

            variable self.raw_models

        function add_from_mod(self, modname: str)
            
            will add locations for an given mod name
            :param modname: the mod to use


        function search(self)
            
            Will search all locations for new stuff
            todo: add datapack locations


                    variable self.found_models[name]

        function add_from_data(self, name: str, data: dict, store=True)
            
            will inject data as an block-model file
            :param name: the name to use
            :param data: the data to inject
            :param store: if it should be stored and re-loaded on reload event


        function build(self, immediate=False)

        function let_subscribe_to_build(self, model, immediate=False)

        function special_build(self, used: str)

        function process_models(self, immediate=False)

        function load_model(self, name: str)

        function add_face_to_batch(self, block, face, batches) -> list

            variable blockstate

                variable vertex

                variable vertex

        function add_raw_face_to_batch(
                self, position, state, block_state_name: str, batches, face
                ):

                variable vertex

                variable blockstate

                variable vertex

        function draw_face(self, block, face)

            variable blockstate

        function draw_block(self, block)

        function get_bbox(self, block)

        function reload_models(self)

    variable shared.model_handler