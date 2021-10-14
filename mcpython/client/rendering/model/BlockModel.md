***BlockModel.py - documentation - last updated on 14.10.2021 by uuk***
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


        function __init__(self, data: dict, name: str, modname: str)

            variable self.data

            variable self.name

            variable self.parent

            variable self.used_textures

            variable self.texture_addresses

            variable self.texture_names

            variable self.drawable

                    variable self.parent

                variable self.parent

                variable self.used_textures

                variable self.texture_names

                    variable texture

                        variable self.used_textures[name]

                        variable self.drawable

                        variable self.texture_names[name]

            variable to_add
                inform the texture bake system about our new textures we want to be in there

            variable add

            variable self.texture_atlas

                variable self.texture_addresses[name]

                variable self.texture_atlas

            variable self.box_models
                prepare the box models from parent

        function get_prepared_data_for(
                self,
                instance: IBlockStateRenderingTarget,
                position: typing.Tuple[float, float, float],
                config: dict,
                face: mcpython.util.enums.EnumSide,
                previous: typing.Tuple[typing.List[float], typing.List[float]] = None,
                ) -> typing.Tuple[
                typing.Tuple[typing.List[float], typing.List[float], typing.List[float]],
                typing.Any,
                ]:
                """
                Collects the vertex and texture data for a block at the given position with given configuration
                :param instance: the instance to draw
                :param position: the offset position
                :param config: the configuration
                :param face: the face
                :param previous: previous collected data, as a tuple of vertices, texture coords
                :return: a tuple of vertices and texture coords, and an underlying BoxModel for some identification stuff
                """
                
                # If this is true, we cannot render this model as stuff is not fully linked
                if not self.drawable:
                logger.println(
                f"[BLOCK MODEL][FATAL] can't draw the model '{self.name}' "
                f"(which has not defined textures) at {position}"
                )
                return ([], [], []) if previous is None else previous, None
                
                rotation = config["rotation"]
                if rotation == (90, 90, 0):
            
            Collects the vertex and texture data for a block at the given position with given configuration
            :param instance: the instance to draw
            :param position: the offset position
            :param config: the configuration
            :param face: the face
            :param previous: previous collected data, as a tuple of vertices, texture coords
            :return: a tuple of vertices and texture coords, and an underlying BoxModel for some identification stuff


            variable rotation

                variable rotation

            variable collected_data

            variable box_model

        function add_face_to_batch(
                self,
                instance: IBlockStateRenderingTarget,
                position: typing.Tuple[float, float, float],
                batch: pyglet.graphics.Batch,
                config: dict,
                face: mcpython.util.enums.EnumSide,
                ) -> typing.Iterable[VertexList]:
            
            Adds a given face to the batch
            Simply wraps a get_prepared_data_for call around the box_model.add_prepared_data_to_batch-call


        function draw_face(
                self,
                position: typing.Tuple[float, float, float],
                config: dict,
                face: mcpython.util.enums.EnumSide,
                ):
            
            Similar to add_face_to_batch, but does it in-place without a batches
            Use batches wherever possible!


        function get_texture_position(
                self, name: str
                ) -> typing.Optional[typing.Tuple[int, int]]:
            
            Helper method resolving a texture name to texture coords
            :param name: the name of the texture
            :return: a tuple of x, y of the texture location, defaults to 0, 0 in case of an error


                variable n