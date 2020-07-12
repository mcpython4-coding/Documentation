***EntityModelGenerator.py - documentation - last updated on 12.7.2020 by uuk***
___

    class EntityModelGenerator extends mcpython.datagen.Configuration.IDataGenerator
        
        Data generator for creating an entity model file


        function __init__(self, config, name)

            variable self.name

            variable self.boxes

            variable self.states

            variable self.y_inverted

        function setInvertedY(self, state=True)
            
            will set all y indexes to their other values
            :param state: the state to set to, default is True


        function add_box(self, name: str, texture: str, tex_size: tuple, position: tuple, rotation: tuple, size: tuple,
                center: tuple, uv=None):
            
            will add one new box to the entity model
            :param name: the name of the box
            :param texture: the texture of the box as an ResourceLocation-string
            :param tex_size: the size of the texture, needed for all subsequent calculations
            :param position: the position of the box relative to the entity origin
            :param rotation: the rotation of the box in degrees
            :param size: the size of the box, in 16 units = 1 block length
            :param center: the center of the rotation
            :param uv: the uv's to use


        function addBox(self, name: str, texture: str, tex_size: tuple, position: tuple, size: tuple, uv: tuple, rotation_center=(0, 0, 0), rotation=(0, 0, 0))

        function add_state(self, name: str, *boxes)
            
            adds an state for rendering the entity
            :param name: the name of the state
            :param boxes: the boxes to include


        function generate(self)

                        variable uv[i]

                variable data["boxes"][key]

                variable boxes

                        variable e

                        variable e

                variable data["states"][key]