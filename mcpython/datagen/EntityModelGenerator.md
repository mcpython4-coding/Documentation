***EntityModelGenerator.py - documentation - last updated on 10.6.2020 by uuk***
___

    class EntityModelGenerator extends mcpython.datagen.Configuration.IDataGenerator

        function __init__(self, config, name)

            variable self.name

            variable self.boxes

            variable self.states

        function add_box(self, name: str, texture: str, tex_size: tuple, position: tuple, rotation: tuple, size: tuple,
                center: tuple, uv=None):

        function add_state(self, name: str, *boxes)

        function generate(self)

                variable data["boxes"][key]

                variable d

                        variable e

                        variable e