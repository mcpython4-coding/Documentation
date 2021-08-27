***ModelHandler.py - documentation - last updated on 27.8.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ModelHandler

        function __init__(self)

            variable self.used_models: typing.Set[str]

            variable self.lookup_locations: typing.Set[str]

            variable self.dependence_list

            variable self.hide_blockstate_errors

            variable self.raw_models

        function add_from_mod(self, modname: str)
            
            Will add locations for a given mod name
            :param modname: the mod to use


        function search(self)
            
            Will search all locations for new stuff
            todo: add datapack locations


                    variable self.found_models[name]

        function add_from_data(self, name: str, data: dict, store=True)
            
            Will inject data as a block-model file
            :param name: the name to use
            :param data: the data to inject
            :param store: if it should be stored and re-loaded on reload event


        function build(self, immediate=False)

        function let_subscribe_to_build(self, model, immediate=False)

                variable modname

        function special_build(self, used: str)

            variable file

                    variable data

                    variable data

                variable data

                variable depend

                variable depend

        function process_models(self, immediate=False)

                variable modname

        function load_model(self, name: str)

            variable location

                    variable model_data

                        variable self.models[

                        variable self.models[name]

                        variable self.models[

                        variable self.models[name]

        function add_face_to_batch(self, block, face, batches) -> typing.Iterable

            variable blockstate

                variable vertex_list

                variable vertex_list

        function add_raw_face_to_batch(
                self, position, state, block_state_name: str, batches, face
                ):

                variable vertex_list

                variable blockstate

                variable vertex_list

        function draw_face(self, block, face)

            variable blockstate

        function draw_block(self, block)

        function get_bbox(self, block)

        function reload_models(self)

    variable shared.model_handler