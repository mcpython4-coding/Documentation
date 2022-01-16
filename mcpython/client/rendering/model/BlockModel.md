***BlockModel.py - documentation - last updated on 16.1.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class Model
        
        Class representing a (block) model from the file system
        Contains the needed API functions to render the model


        variable __slots__

        function __init__(self, name: str, modname: str = None)

            variable self.name

            variable self.modname

            variable self.parent

            variable self.used_textures

            variable self.animated_textures

            variable self.texture_addresses

            variable self.texture_names

            variable self.drawable

            variable self.texture_atlas

            variable self.box_models

            variable self.parent

            variable self.box_models
                prepare the box models from parent
            
            Informs the texture bake system about our new textures we want to be in there
            Prepares the texture_addresses attribute with the location of the texture


            variable to_add

            variable add

                    variable self.texture_addresses[name]

                variable self.texture_atlas

                variable self.parent

                variable self.parent

            variable self.parent

                variable self.used_textures

                variable self.texture_names

                variable self.texture_names[name]

                    variable texture_f

                    variable texture_f

                    variable texture_f

                    variable self.animated_textures[

                variable self.used_textures[name]

                variable self.drawable

                variable self.texture_names[name]

        function prepare_rendering_data_multi_face(
                self,
                instance: IBlockStateRenderingTarget,
                position: typing.Tuple[float, float, float],
                config: dict,
                faces: int,
                previous: typing.Tuple[typing.List[float], typing.List[float]] = None,
                batch: pyglet.graphics.Batch = None,
                scale: float = 1,
                ) -> typing.Tuple[
                typing.Tuple[
                typing.List[float], typing.List[float], typing.List[float], typing.List
                ],
                typing.Any,
                ]:
                """
                Collects the vertex and texture data for a block at the given position with given configuration
                :param instance: the instance to draw
                :param position: the offset position
                :param config: the configuration
                :param faces: the faces
                :param previous: previous collected data, as a tuple of vertices, texture coords
                :param batch: the batch to use
                :param scale: the scale to use
                :return: a tuple of vertices and texture coords, and an underlying BoxModel for some identification stuff
                """
                
                collected_data = ([], [], [], []) if previous is None else previous
                
                # If this is true, we cannot render this model as stuff is not fully linked
                if not self.drawable:
                logger.println(
                f"[BLOCK MODEL][FATAL] can't draw the model '{self.name}' "
                f"(which has not defined textures) at {position}"
                )
                return collected_data, None
                
                if not self.box_models:
                return collected_data, None
                
                # todo: can we parse this beforehand and store as an attribute?
                rotation = config["rotation"]
                if rotation == (90, 90, 0):
            
            Collects the vertex and texture data for a block at the given position with given configuration
            :param instance: the instance to draw
            :param position: the offset position
            :param config: the configuration
            :param faces: the faces
            :param previous: previous collected data, as a tuple of vertices, texture coords
            :param batch: the batch to use
            :param scale: the scale to use
            :return: a tuple of vertices and texture coords, and an underlying BoxModel for some identification stuff


            variable collected_data

            variable rotation
                todo: can we parse this beforehand and store as an attribute?

                variable rotation

        function add_faces_to_batch(
                self,
                instance: IBlockStateRenderingTarget,
                position: typing.Tuple[float, float, float],
                batch: pyglet.graphics.Batch,
                config: dict,
                faces: int,
                scale: float = 1,
                ) -> typing.Iterable[VertexList]:
            
            Adds given faces to the given batch system
            Parameters same as prepare_rendering_data_multi_face


        function draw_face(
                self,
                instance,
                position: typing.Tuple[float, float, float],
                config: dict,
                face: mcpython.util.enums.EnumSide | int,
                scale: float = 1,
                ):
            
            Similar to add_face_to_batch, but does it in-place without a batches
            Use batches wherever possible!


                variable face

        function get_texture_position(
                self, name: str
                ) -> typing.Optional[typing.Tuple[int, int]]:
            
            Helper method resolving a texture name to texture coords
            :param name: the name of the texture
            :return: a tuple of x, y of the texture location, defaults to 0, 0 in case of an error


                variable n

        @deprecation.deprecated()
        function get_prepared_data_for_scaled(
                self,
                instance: IBlockStateRenderingTarget,
                position: typing.Tuple[float, float, float],
                config: dict,
                face: mcpython.util.enums.EnumSide,
                scale: float,
                previous: typing.Tuple[typing.List[float], typing.List[float]] = None,
                batch=None,
                ) -> typing.Tuple[
                typing.Tuple[
                typing.List[float], typing.List[float], typing.List[float], typing.List
                ],
                typing.Any,
                ]:
                return self.prepare_rendering_data_multi_face(
                instance,
                position,
                config,
                face.bitflag,
                scale=scale,
                previous=previous,
                batch=batch,
                )
                
                @deprecation.deprecated()
                def add_face_to_batch(
                self,
                instance: IBlockStateRenderingTarget,
                position: typing.Tuple[float, float, float],
                batch: pyglet.graphics.Batch,
                config: dict,
                face: mcpython.util.enums.EnumSide,
                ):

        @deprecation.deprecated()
        function add_face_to_batch(
                self,
                instance: IBlockStateRenderingTarget,
                position: typing.Tuple[float, float, float],
                batch: pyglet.graphics.Batch,
                config: dict,
                face: mcpython.util.enums.EnumSide,
                ):

        @deprecation.deprecated()
        function get_prepared_data_for(
                self,
                instance: IBlockStateRenderingTarget,
                position: typing.Tuple[float, float, float],
                config: dict,
                face: mcpython.util.enums.EnumSide,
                previous: typing.Tuple[typing.List[float], typing.List[float]] = None,
                batch=None,
                ) -> typing.Tuple[
                typing.Tuple[
                typing.List[float], typing.List[float], typing.List[float], typing.List
                ],
                typing.Any,
                ]:
                return self.prepare_rendering_data_multi_face(
                instance, position, config, face.bitflag, previous=previous, batch=batch
                )
                
                @deprecation.deprecated()
                def draw_face_scaled(
                self,
                instance,
                position: typing.Tuple[float, float, float],
                config: dict,
                face: mcpython.util.enums.EnumSide,
                scale: float,
                ):

        @deprecation.deprecated()
        function draw_face_scaled(
                self,
                instance,
                position: typing.Tuple[float, float, float],
                config: dict,
                face: mcpython.util.enums.EnumSide,
                scale: float,
                ):