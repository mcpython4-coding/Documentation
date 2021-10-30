***BlockModelGenerator.py - documentation - last updated on 30.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    function encode_model_key(key)

    class ModelRepr extends IDataGenerator
        
        Class for representing an model in an block-state definition generator.
        Rendering is implemented by the respective rendering backend


        static
        function for_model(cls, model: "BlockModel") -> "ModelRepr"

        function __init__(
                self,
                model: typing.Union[str, "BlockModel"],
                r_x=0,
                r_y=0,
                uv_lock=False,
                weight=None,
                ):
            
            will create an new entry
            :param model: the model to use as e.g. minecraft:block/stone
            :param r_x: the rotation in x direction
            :param r_y: the rotation in y direction
            :param uv_lock: if uv's should be not affected by rotation
            :param weight: the weight, when in an list of multiple models


            variable self.model

            variable self.r_x

            variable self.r_y

            variable self.uv_lock

            variable self.weight

            variable self.generated_cache

        function dump(self, generator: DataGeneratorInstance) -> dict
            
            Will encode your data to an json-able dict


    class SingleFaceConfiguration extends IDataGenerator
        
        Class for the configuration of one face of an element in an BlockModel


        function __init__(
                self,
                face: typing.Union[str, mcpython.util.enums.EnumSide],
                texture: str,
                uv=(0, 0, 1, 1),
                cull_face: typing.Union[str, mcpython.util.enums.EnumSide] = None,
                rotation=0,
                ):
            
            Will create an new config
            :param face: the face to configure, as str for face in mcpython.util.enums.EnumSide or an entry of that enum
            :param texture: the texture variable name to use, "#" in front optional (auto-added when not provided)
            :param uv: the uv indexes. when out of the 0-1 bound, behaviour is undefined
            :param cull_face: the cull face of the face. Same parsing as face
            :param rotation: the rotation of the texture as an multiple of 90


            variable self.face

            variable self.texture - ) else "#" + texture

            variable self.uv

                variable cull_face

            variable self.cull_face

            variable self.rotation

            variable self.generated_cache

        function dump(self, generator: DataGeneratorInstance) -> dict
            
            Will encode the data into an dict-like object


            variable self.generated_cache

    class BlockState extends IDataGenerator
        
        generator class for an block state


        function __init__(self, name: str, parent=None, generate_alias=2)

            variable self.name

            variable self.states

            variable self.parent

            variable self.alias

            variable self.generate_alias

        function add_state(
                self, state: typing.Union[None, str, dict, list, "BlockModel"], *models
                ):
            
            will add an new possible state into the block state file
            :param state: the state as an str, an dict or an list of states or None for default
            :param models: the models to use in this case


            variable model_copy

                    variable model_copy[i]

                    variable model_copy[i]

        function addAliasName(self, name: str, target: str)

        function generateBestAlias(self, limit=2)
            
            Helper function for generating aliases where possible
            :param limit: when an model alias should be created


        function dump(self, generator: DataGeneratorInstance) -> dict

                variable data["parent"]

                variable data["alias"]

        function get_default_location(self, generator: DataGeneratorInstance, name: str)

    class MultiPartBlockState extends IDataGenerator
        
        Generator class for an multipart model


        function __init__(self, name: str, parent=None, optimize=True)

            variable self.name

            variable self.states

            variable self.parent

            variable self.alias

            variable self.optimize

        function add_state(self, state: typing.Union[None, str, dict, list], *models)
            
            will add an entry
            :param state: the case in which this should be active.
                None: always
                str: represents an list of "<name>=<state>" separated by "," as state
                dict: represents same as str, but not packed
                list: represents an OR over an list of state-like-entries
            :param models: the models to apply
            :return:


        function addAliasName(self, name: str, target: str)

        function generateBestAlias(self, limit=2)
            
            Helper function for generating aliases where possible
            :param limit: when an model alias should be created


        function dump(self, generator: DataGeneratorInstance) -> dict

        static
        function _encode_condition(cls, state)

        function get_default_location(self, generator: DataGeneratorInstance, name: str)

    class ModelDisplay extends IDataGenerator
        
        class holding an display configuration for the block


        function __init__(
                self, rotation: tuple = None, translation: tuple = None, scale: tuple = None
                ):
            
            creates an new config for an display
            :param rotation: the rotation to use
            :param translation: the translation to use
            :param scale: the scale to use


            variable self.rotation

            variable self.translation

            variable self.scale

        function dump(self, generator: DataGeneratorInstance) -> dict

    class BlockModel extends IDataGenerator
        
        Generator for a block model


        function __init__(
                self,
                name: str,
                parent: str = "minecraft:block/block",
                ambient_occlusion=True,
                ):

            variable parent: str

            variable self.name

            variable self.parent

            variable self.ambient_occlusion

            variable self.textures

            variable self.elements

            variable self.display

        function set_texture_variable(self, name: str, texture: str)

        function set_texture_variables(self, texture: str, *names)

        function add_element(
                self,
                f: tuple,
                t: tuple,
                *faces,
                rotation_center=None,
                rotation_axis=None,
                rotation_angle=None,
                rotation_rescale=False,
                shade=True
                ):

        function set_display_mode(self, key: str, config: ModelDisplay)

        function dump(self, generator: DataGeneratorInstance) -> dict

        function get_default_location(self, generator: DataGeneratorInstance, name: str)