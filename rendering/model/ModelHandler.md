***ModelHandler.py - documentation - last updated on 14.5.2020 by uuk***
___

    class ModelHandler

        function __init__(self)

            variable self.models

            variable self.used_models

            variable self.found_models

            variable self.blockstates

            variable self.lookup_locations

            variable self.dependence_list

        function add_from_mod(self, modname)

        function search(self)

                variable found_models

                    variable s

                    variable mod_fix

                    variable address_fix

                    variable name

                    variable self.found_models[name]

        function add_from_data(self, name, data)

            variable self.found_models[name]

        function build(self)

        function __let_subscribe_to_build(self, model)

            variable modname

        function special_build(self, used)

            variable file

                variable data

                variable data

                variable depend

                variable depend

        function process_models(self)

            variable sorted_models

            variable sorted_models

            variable self.dependence_list - decrease memory usage

                variable modname

        function load_model(self, name: str)

            variable location

                    variable modeldata

                    variable self.models[name]

                    variable self.models[name]

        function add_face_to_batch(self, block, face, batches) -> list

            variable blockstate

        function draw_face(self, block, face)

            variable blockstate

        function draw_block(self, block)

        function get_bbox(self, block)

    variable G.modelhandler