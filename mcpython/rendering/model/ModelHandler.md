***ModelHandler.py - documentation - last updated on 24.6.2020 by uuk***
___

    class ModelHandler

        function __init__(self)

            variable self.models

            variable self.used_models - todo: change to set

            variable self.found_models - todo: clear when not needed

            variable self.blockstates

            variable self.lookup_locations - todo: change to set

            variable self.dependence_list - todo: clear when not needed

        function add_from_mod(self, modname: str)
            
            will add locations for an given mod name
            :param modname: the mod to use


        function search(self)
            
            will search all locations for new stuff
            todo: add datapack locations


        function add_from_data(self, name: str, data: dict)
            
            will inject data as an block-model file
            :param name: the name to use
            :param data: the data to inject


        function build(self)

        function let_subscribe_to_build(self, model)

        function special_build(self, used)

        function process_models(self)

        function load_model(self, name: str)

        function add_face_to_batch(self, block, face, batches) -> list

        function draw_face(self, block, face)

        function draw_block(self, block)

        function get_bbox(self, block)

    variable G.modelhandler