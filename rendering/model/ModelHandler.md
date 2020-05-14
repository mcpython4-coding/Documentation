***ModelHandler.py - documentation - last updated on 14.5.2020 by uuk***
___

    class ModelHandler
        function __init__(self)
        function add_from_mod(self, modname)
        function search(self)
        function add_from_data(self, name, data)
        function build(self)
        function __let_subscribe_to_build(self, model)
        function special_build(self, used)
        function process_models(self)
        function load_model(self, name: str)
        function add_face_to_batch(self, block, face, batches) -> list
        function draw_face(self, block, face)
        function draw_block(self, block)
        function get_bbox(self, block)

    variable G.modelhandler
