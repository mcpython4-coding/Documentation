***BoxModel.py - documentation - last updated on 5.2.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class BoxModel extends AbstractBoxModel

        static
        function new(cls, data: dict, model=None) -> "BoxModel"

        function __init__(self, flip_y=True)

            variable self.flip_y

            variable self.vertex_provider: typing.Optional[VertexProvider]

            variable self.atlas

            variable self.model

            variable self.data

            variable self.tex_data

            variable self.inactive

            variable self.box_position

            variable self.box_size

            variable self.faces

            variable self.animated_texture_coords

            variable self.face_tint_index

            variable self.texture_region_rotate: typing.List[float]

            variable self.enable_alpha

        function parse_mc_data(self, data: dict, model=None)
            
            Parses the default "elements" tag from a vanilla model file
            :param data: one element of the "elements" tag
            :param model: the assigned model, or None if not arrival


            variable self.model

            variable self.data

            variable self.box_position

            variable self.box_size

                    variable self.rotation_center

                variable rot
                    todo: add a way to rotate around more than one axis

                variable rot["xyz".index(data["rotation"]["axis"])]

                variable self.rotation

            variable self.vertex_provider

            variable UD

            variable NS

            variable EW

            variable self.texture_region[:]

                variable name: str

        function _parse_face(self, f: dict, face: EnumSide)

                variable self.animated_faces[face.index]

                variable self.faces[face.index]

            variable index

                variable uvs

                variable uvs

                    variable self.texture_region[index]

                    variable self.texture_region[index]

                variable self.texture_region_rotate[index]

                variable self.face_tint_index[index]

        function build(self, atlas=None)
            
            "Builds" the model by preparing internal data like preparing the texture atlas, the texture coordinates, etc.


                variable atlas

            variable data

                    variable data[i]

                    variable coords

                    variable size

                    variable self.animated_texture_coords[i]

            variable self.tex_data

            variable self.inactive

            variable self.atlas

            variable self.enable_alpha

        function get_vertex_variant(
                self, rotation: tuple, position: tuple, scale: float = 1
                ) -> list:
            
            Implementation to get the vertex data for a rotated block
            :param rotation: the rotation to use
            :param position: the position of the vertex cube
            :param scale: the scale to use


            variable vertices

        @deprecation.deprecated()
        function get_prepared_box_data(
                self,
                instance,
                position,
                rotation=(0, 0, 0),
                active_faces=None,
                uv_lock=False,
                previous=None,
                ) -> typing.Tuple[typing.List[float], typing.List[float], typing.List[float], list]:

                variable active_faces

                variable active_faces

                variable active_faces

                variable active_faces

        function prepare_rendering_data_multi_face(
                self,
                instance: IBlockStateRenderingTarget,
                position: typing.Tuple[float, float, float],
                rotation: typing.Tuple[float, float, float] = (0, 0, 0),
                faces: int = 0,
                uv_lock=False,
                previous: typing.Tuple[
                typing.List[float], typing.List[float], typing.List[float]
                ] = None,
                batch: pyglet.graphics.Batch | typing.List[pyglet.graphics.Batch] = None,
                scale: float = 1,
                ) -> typing.Tuple[typing.List[float], typing.List[float], typing.List[float], list]:
            
            Util method for getting the box data for a block (vertices and uv's)
            :param instance: the instance to get information from to render
            :param position: the position of the block
            :param rotation: the rotation
            :param faces: the faces to get data for, None means all
            :param uv_lock: ?
            :param previous: previous data to add the new to, or None to create new
            :param batch: the batch to use
            :param scale: a scale to use, passed to VertexProvider


            variable vertex

            variable collected_data

                variable batch

            variable enable_animated

            variable faces

                    variable face

                variable i

                variable i2

                            variable group

        @deprecation.deprecated()
        function get_prepared_box_data_scaled(
                self,
                instance: IBlockStateRenderingTarget,
                position: typing.Tuple[float, float, float],
                rotation: typing.Tuple[float, float, float] = (0, 0, 0),
                scale: float = 1,
                active_faces=None,
                uv_lock=False,
                previous: typing.Tuple[
                typing.List[float], typing.List[float], typing.List[float]
                ] = None,
                batch=None,
                ) -> typing.Tuple[typing.List[float], typing.List[float], typing.List[float], list]:

                variable active_faces

                variable active_faces

        function add_prepared_data_to_batch(
                self,
                collected_data: typing.Tuple[
                typing.List[float], typing.List[float], typing.List[float], list
                ],
                batch: typing.Union[pyglet.graphics.Batch, typing.List[pyglet.graphics.Batch]],
                ) -> typing.Iterable[VertexList]:
            
            Adds the data from get_prepared_box_data to a given batch
            :param collected_data: the collected data
            :param batch: the batch to add in


                variable batch

        function add_to_batch(
                self,
                instance: IBlockStateRenderingTarget,
                position: typing.Tuple[float, float, float],
                batch: typing.Union[pyglet.graphics.Batch, typing.List[pyglet.graphics.Batch]],
                rotation: typing.Tuple[float, float, float],
                active_faces=None,
                uv_lock=False,
                ):
            
            Adds the box model to the batch
            Internally wraps a get_prepared_box_data call around the add_prepared_data_to_batch method
            Use combined data where possible
            :param instance: the instance to use for rendering
            :param position: the position based on
            :param batch: the batches to select from
            :param rotation: the rotation to use
            :param active_faces: which faces to show
            :param uv_lock: if the uv's should be locked in place or not
            :return: an vertex-list-list
            todo: make active_faces an dict of faces -> state, not an order-defined list


            variable collected_data

        function draw_prepared_data(
                self,
                collected_data: typing.Tuple[
                typing.List[float], typing.List[float], typing.List[float], list
                ],
                ):
            
            Draws prepared data to the screen
            WARNING: the invoker is required to set up OpenGL for rendering the stuff, including linking the textures
            Use batches when possible
            :param collected_data: the data


        function draw(
                self,
                instance: IBlockStateRenderingTarget,
                position: typing.Tuple[float, float, float],
                rotation: typing.Tuple[float, float, float],
                active_faces: typing.List[bool] = None,
                uv_lock: bool = False,
                ):
            
            Draws the BoxModel direct into the world
            WARNING: use batches for better performance
            :param instance: the instance to ues for rendering
            :param position: the position to draw on
            :param rotation: the rotation to draw with
            :param uv_lock: if the uv's should be locked in place or not
            :param active_faces: which faces to draw


            variable collected_data

        function draw_scaled(
                self,
                instance: IBlockStateRenderingTarget,
                position: typing.Tuple[float, float, float],
                rotation: typing.Tuple[float, float, float],
                scale: float,
                active_faces: typing.List[bool] = None,
                uv_lock: bool = False,
                ):
            
            Draws the BoxModel direct into the world
            WARNING: use batches for better performance
            :param instance: the instance to ues for rendering
            :param position: the position to draw on
            :param rotation: the rotation to draw with
            :param scale: the scale to draw in
            :param uv_lock: if the uv's should be locked in place or not
            :param active_faces: which faces to draw


            variable collected_data

        function add_face_to_batch(
                self,
                instance: IBlockStateRenderingTarget,
                position: typing.Tuple[float, float, float],
                batch,
                rotation: typing.Tuple[float, float, float],
                face: EnumSide,
                uv_lock=False,
                ):

                variable rotation

            variable face

        function draw_face(
                self,
                instance: IBlockStateRenderingTarget,
                position: typing.Tuple[float, float, float],
                rotation: typing.Tuple[float, float, float],
                face: EnumSide,
                uv_lock=False,
                ):

                variable rotation

            variable face

        function draw_face_scaled(
                self,
                instance: IBlockStateRenderingTarget,
                position: typing.Tuple[float, float, float],
                rotation: typing.Tuple[float, float, float],
                face: EnumSide,
                scale: float,
                uv_lock=False,
                ):

                variable rotation

            variable face

        function copy(self, new_model=None)

    @onlyInClient() class RawBoxModel extends AbstractBoxModel
        
        A non-model-bound BoxModel class


        function copy(self) -> "AbstractBoxModel"

        function __init__(
                self,
                relative_position: typing.Tuple[float, float, float],
                size: typing.Tuple[float, float, float],
                texture: typing.Union[str, pyglet.graphics.TextureGroup],
                texture_region: typing.List[typing.Tuple[float, float, float, float]] = None,
                rotation: typing.Tuple[float, float, float] = (0, 0, 0),
                rotation_center: typing.Tuple[float, float, float] = None,
                ):
            
            Creates a new renderer for the box-model
            :param relative_position: where to draw the box, used in calculations of vertex coordinates
            :param size: the size of the box
            :param texture: which texture to use. May be str or pyglet.graphics.TextureGroup
            :param texture_region: which tex region to use, from (0, 0) to (1, 1)
            :param rotation: how to rotate the box around rotation_center
            :param rotation_center: where to rotate the box around


                variable texture_region

            variable self.relative_position

            variable self.size

            variable self.raw_texture

            variable self.texture_source

            variable self.texture

            variable self.__texture_region

            variable self.__rotation

            variable self.vertex_cache

            variable self.rotated_vertex_cache

            variable self.texture_cache

            variable self.rotation_center

            variable self.vertex_provider: typing.Optional[VertexProvider]

            variable self.texture

        function auto_value_region(
                self,
                texture_start: typing.Tuple[float, float],
                texture_dimensions: typing.Tuple[float, float, float],
                ):
            
            Helper function for calculating the texture region in the default layout
            :param texture_start: the top left coordinates of the texture
            :param texture_dimensions: how big the texture is


            variable self.texture_region

        function recalculate_cache(self)

            variable self.texture_cache
                todo: this seems odd

        function get_rotation(self)

        function set_rotation(self, rotation: tuple)

        variable rotation

        function get_texture_region(self)

        function set_texture_region(self, region)

        variable texture_region

        function get_vertices(self, position, rotation, rotation_center)

        function add_to_batch(
                self,
                batch: pyglet.graphics.Batch,
                position: typing.Tuple[float, float, float],
                rotation=(0, 0, 0),
                rotation_center=(0, 0, 0),
                ):

            variable vertices

        @deprecation.deprecated()
        function add_face_to_batch(
                self,
                batch: pyglet.graphics.Batch,
                position: typing.Tuple[float, float, float],
                face: typing.Optional[typing.Union[typing.Iterable[int], EnumSide]],
                rotation=(0, 0, 0),
                rotation_center=(0, 0, 0),
                ):

            variable vertices

            variable result

                variable t

                variable v

        function add_faces_to_batch(
                self,
                batch: pyglet.graphics.Batch,
                position: typing.Tuple[float, float, float],
                faces: int,
                rotation=(0, 0, 0),
                rotation_center=(0, 0, 0),
                ):

            variable vertices

            variable result

                variable t

                variable v

        function draw(
                self,
                position: typing.Tuple[float, float, float],
                rotation=(0, 0, 0),
                rotation_center=(0, 0, 0),
                ):

            variable vertices

    @onlyInClient() class MutableRawBoxModel extends RawBoxModel

        function add_to_batch(
                self,
                batch: pyglet.graphics.Batch,
                position: typing.Tuple[float, float, float],
                rotation=(0, 0, 0),
                rotation_center=(0, 0, 0),
                ):

            variable vertices

        function mutate_add_to_batch(
                self,
                previous: pyglet.graphics.vertexdomain.VertexList,
                position: typing.Tuple[float, float, float],
                rotation=(0, 0, 0),
                rotation_center=(0, 0, 0),
                ):

            variable vertices

            variable previous.vertices[:]

        @deprecation.deprecated()
        function add_face_to_batch(
                self,
                batch: pyglet.graphics.Batch,
                position: typing.Tuple[float, float, float],
                face: typing.Optional[typing.Union[typing.Iterable[int], EnumSide]],
                rotation=(0, 0, 0),
                rotation_center=(0, 0, 0),
                ):

            variable vertices

            variable result

                variable t

                variable v

        function add_faces_to_batch(
                self,
                batch: pyglet.graphics.Batch,
                position: typing.Tuple[float, float, float],
                faces: int,
                rotation=(0, 0, 0),
                rotation_center=(0, 0, 0),
                ):

            variable vertices

            variable result

                variable t

                variable v

        function mutate_add_face_to_batch(
                self,
                previous: typing.List[pyglet.graphics.vertexdomain.VertexList],
                position: typing.Tuple[float, float, float],
                face: typing.Optional[typing.Union[typing.Iterable[int], EnumSide]],
                rotation=(0, 0, 0),
                rotation_center=(0, 0, 0),
                ):

            variable vertices

                variable v

                variable previous.pop(0).vertices[:]

    @onlyInClient() class ColoredRawBoxModel extends RawBoxModel

        function add_to_batch(
                self,
                batch: pyglet.graphics.Batch,
                position: typing.Tuple[float, float, float],
                rotation=(0, 0, 0),
                rotation_center=(0, 0, 0),
                color=(1, 1, 1, 1),
                ):

            variable vertices

        @deprecation.deprecated()
        function add_face_to_batch(
                self,
                batch: pyglet.graphics.Batch,
                position: typing.Tuple[float, float, float],
                face: typing.Union[typing.Iterable[int], EnumSide],
                rotation=(0, 0, 0),
                rotation_center=(0, 0, 0),
                color=(1, 1, 1, 1),
                ):

            variable vertices

            variable result

                variable t

                variable v

        function add_faces_to_batch(
                self,
                batch: pyglet.graphics.Batch,
                position: typing.Tuple[float, float, float],
                faces: int,
                rotation=(0, 0, 0),
                rotation_center=(0, 0, 0),
                color=(1, 1, 1, 1),
                ):

            variable vertices

            variable result

                variable t

                variable v

        function draw(
                self,
                position: typing.Tuple[float, float, float],
                rotation=(0, 0, 0),
                rotation_center=(0, 0, 0),
                color=(1, 1, 1, 1),
                ):

            variable vertices