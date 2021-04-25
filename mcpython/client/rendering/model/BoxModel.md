***BoxModel.py - documentation - last updated on 25.4.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable UV_ORDER

    variable SIDE_ORDER

    variable UV_INDICES

    variable SIMILAR_VERTEX

    @onlyInClient() class BoxModel

        static
        function new(cls, data: dict, model=None)

        function __init__(self, data: dict, model=None, flip_y=True)

            variable self.atlas
                todo: move most of the code here to the build function / decode function

            variable self.model

            variable self.data

            variable self.box_position

            variable self.box_size

            variable self.relative_position

            variable self.faces

            variable UD

            variable NS

            variable EW

            variable self.texture_region

            variable self.texture_region_rotate

                variable name: str

                    variable f

                    variable var

                    variable self.faces[face]

                    variable index

                        variable uvs

                        variable uvs

                            variable self.texture_region[index]

                            variable self.texture_region[index]

                        variable self.texture_region_rotate[index]

            variable self.rotation

            variable self.rotation_center

                    variable self.rotation_center

                variable rot

                variable rot["xyz".index(data["rotation"]["axis"])]

                variable self.rotation

            variable status

                variable self.rotated_vertices

                variable self.rotated_vertices

                variable SIMILAR_VERTEX[status]

            variable self.tex_data

            variable self.un_active

            variable self.raw_vertices

        function build(self, atlas=None)
            
            "Builds" the model by preparing internal data like preparing the texture atlas, the texture coordinates


                variable atlas

            variable self.tex_data

            variable self.un_active

            variable self.atlas

        function get_vertex_variant(self, rotation: tuple, position: tuple) -> list
            
            Implementation to get the vertex data for a rotated block
            :param rotation: the rotation to use
            :param position: the position of the vertex cube


                variable vertex_r

                variable vertex

                variable vertex_r

                    variable face_r

                        variable v

                        variable v

                variable self.rotated_vertices[rotation]

        function get_prepared_box_data(
                self, position, rotation, active_faces=None, uv_lock=False
                ):

            variable vertex

            variable collected_data

                    variable face

                variable i

                variable i2

        function add_prepared_data_to_batch(self, collected_data, batch)

                variable batch

        function add_to_batch(
                self,
                position: typing.Tuple[float, float, float],
                batch,
                rotation,
                active_faces=None,
                uv_lock=False,
                ):
            
            Adds the box model to the batch
            :param position: the position based on
            :param batch: the batches to select from
            :param rotation: the rotation to use
            :param active_faces: which faces to show
            :param uv_lock: if the uv's should be locked in place or not
            :return: an vertex-list-list
            todo: make active_faces an dict of faces -> state, not an order-defined list


            variable collected_data

        function draw_prepared_data(self, collected_data)

        function draw(
                self,
                position: typing.Tuple[float, float, float],
                rotation,
                active_faces=None,
                uv_lock=False,
                ):
            
            draws the BoxModel direct into the world
            WARNING: use batches for better performance
            :param position: the position to draw on
            :param rotation: the rotation to draw with
            :param uv_lock: if the uv's should be locked in place or not
            :param active_faces: which faces to draw


            variable collected_data

        function add_face_to_batch(self, position, batch, rotation, face, uv_lock=False)

        function draw_face(self, position, rotation, face, uv_lock=False)

        function copy(self, new_model=None)

    @onlyInClient() class BaseBoxModel
        
        An non-model-bound boxmodel class


        function __init__(
                self,
                relative_position: tuple,
                size: tuple,
                texture,
                texture_region=None,
                rotation=(0, 0, 0),
                rotation_center=None,
                ):
            
            Creates an new renderer for the box-model
            :param relative_position: where to position the box relative to draw position
            :param size: the size of the box
            :param texture: which texture to use. May be str or pyglet.graphics.TextureGroup
            :param texture_region: which tex region to use, from (0, 0) to (1, 1)
            :param rotation: how to rotate the bbox
            :param rotation_center: where to rotate the box around


                variable texture_region

            variable self.relative_position

            variable self.size

            variable self.raw_texture

            variable self.texture

            variable self.__texture_region

            variable self.__rotation

            variable self.vertex_cache

            variable self.rotated_vertex_cache

            variable self.texture_cache

            variable self.rotation_center

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

        function get_rotation(self)

        function set_rotation(self, rotation: tuple)

        variable rotation

        function get_texture_region(self)

        function set_texture_region(self, region)

        variable texture_region

        function add_to_batch(
                self, batch, position, rotation=(0, 0, 0), rotation_center=(0, 0, 0)
                ):

            variable vertex

                variable vertex

                variable self.rotated_vertex_cache[rotation]

            variable result

                variable t

                variable v

        function add_face_to_batch(
                self, batch, position, face, rotation=(0, 0, 0), rotation_center=(0, 0, 0)
                ):

            variable vertex

                variable vertex

                variable self.rotated_vertex_cache[rotation]

            variable result

                variable t

                variable v

        function draw(self, position, rotation=(0, 0, 0), rotation_center=(0, 0, 0))