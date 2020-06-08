***BlockModelGenerator.py - documentation - last updated on 10.6.2020 by uuk***
___

    function encode_model_key(key)

    class ModelRepresentation
        
        Class for representing an model in an block-state definition generator.
        Rendering is implemented by the respective rendering backend


        function __init__(self, model: str, r_x=0, r_y=0, uvlock=False, weight=None)
            
            will create an new entry
            :param model: the model to use as e.g. minecraft:block/stone
            :param r_x: the rotation in x direction
            :param r_y: the rotation in y direction
            :param uvlock: if uv's should be not affected by rotation
            :param weight: the weight, when in an list of multiple models


            variable self.model

            variable self.r_x

            variable self.r_y

            variable self.uvlock

            variable self.weight

            variable self.wrap_cache - holding the data when calling wrap() to make later re-use possible

        function wrap(self) -> dict
            
            will encode your data to an json-able dict


    class SingleFaceConfiguration
        
        class for the configuration of one face of an element in an BlockModel


        function __init__(self, face: typing.Union[str, mcpython.util.enums.EnumSide], texture: str, uv=(0, 0, 1, 1),
                cullface: typing.Union[str, mcpython.util.enums.EnumSide]=None, rotation=0):
            
            will create an new config
            :param face: the face to configure, as str for face in mcpython.util.enums.EnumSide or an entry of that enum
            :param texture: the texture variable name to use, "#" in front optional (auto-added when not provided)
            :param uv: the uv indexes. when out of the 0-1 bound, behaviour is undefined
            :param cullface: the cull face of the face. Same parsing as face
            :param rotation: the rotation of the texture as an multiple of 90


            variable self.wrap_cache

        function wrap(self) -> dict
            
            will encode the data into an dict-like object
            :return:


            variable self.wrap_cache

    class BlockStateGenerator extends mcpython.datagen.Configuration.IDataGenerator
        
        generator class for an block state


        function __init__(self, config, name: str)

            variable self.name

            variable self.states

        function add_state(self, state: typing.Any[str, dict, list], *models: typing.List[typing.Any[str, ModelRepresentation]])
            
            will add an new possible state into the block state file
            :param state: the state as an str, an dict or an list of states
            :param models: the models to use in this case


        function generate(self)

    class MultiPartBlockStateGenerator extends mcpython.datagen.Configuration.IDataGenerator
        
        Generator class for an multipart model


        function __init__(self, config, name: str)

            variable self.name

            variable self.states

        function add_state(self, state: typing.Any[None, str, dict, list],
                *models: typing.List[typing.Any[str, ModelRepresentation]]):
            
            will add an entry
            :param state: the case in which this should be active.
                None: always
                str: represents an list of "<name>=<state>" separated by "," as state
                dict: represents same as str, but not packed
                list: represents an OR over an list of state-like-entries
            :param models: the models to apply
            :return:


        function generate(self)

        static
        function _encode_condition(cls, state)

    class ModelDisplay
        
        class holding an display configuration for the block


        function __init__(self, rotation: tuple = None, translation: tuple = None, scale: tuple = None)
            
            creates an new config for an display
            :param rotation: the rotation to use
            :param translation: the translation to use
            :param scale: the scale to use


            variable self.rotation

            variable self.translation

            variable self.scale

        function wrap(self) -> dict

    class BlockModelGenerator extends mcpython.datagen.Configuration.IDataGenerator
        
        Generator for an block model


        function __init__(self, config, name: str, parent: str = "minecraft:block/block", ambientocclusion=True)

            variable self.name

            variable self.parent

            variable self.ambientocclusion

            variable self.textures

            variable self.elements

            variable self.display

        function set_texture_variable(self, name: str, texture: str)

        function add_element(self, f: tuple, t: tuple, *faces: typing.List[SingleFaceConfiguration], rotation_center=None,
                rotation_axis=None, rotation_angle=None, rotation_rescale=False, shade=True):

        function set_display_mode(self, key: str, config: ModelDisplay)

        function generate(self)