***Model.py - documentation - last updated on 14.5.2020 by uuk***
___

    class Model
        function __init__(self, data: dict, name: str, modname: str)
        function add_face_to_batch(self, position, batch, config, face)
        function draw_face(self, position, config, face)
        function get_texture_position(self, name: str) -> tuple