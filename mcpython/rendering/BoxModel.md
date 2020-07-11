***BoxModel.py - documentation - last updated on 11.7.2020 by uuk***
___

    variable UV_ORDER

    variable SIDE_ORDER

    variable UV_INDICES - representative for the order of uv insertion

    variable SIMILAR_VERTEX

    class BoxModel

        function __init__(self, data: dict, model)

            variable self.__data - todo: remove
                todo: move most of the code here to the build function

            variable self.model

            variable self.boxposition

            variable self.boxsize

            variable status

                variable self.rotated_vertices

                variable self.rotated_vertices

                variable SIMILAR_VERTEX[status]

            variable self.tex_data

            variable self.deactive

            variable self.raw_vertices

        @deprecation.deprecated(deprecated_in="snapshot dev 1 cycle 1", removed_in="v1.2.0 alpha")
        function get_data(self)

        @deprecation.deprecated(deprecated_in="snapshot dev 1 cycle 1", removed_in="v1.2.0 alpha")
        function set_data(self, data)

        variable data

        function build(self)

        function get_vertex_variant(self, rotation: tuple, position: tuple) -> list
            
            implementation to get the vertex data for an rotated block
            :param rotation: the rotation to use
            :param position: the position of the vertex cube

            
            x, y, z = position
            x += self.boxposition[0] - 0.5 + self.rposition[0]
            y += self.boxposition[1] - 0.5 + self.rposition[1]
            z += self.boxposition[2] - 0.5 + self.rposition[2]
            rotation = (rotation[0] % 360, rotation[1] % 360, rotation[2] % 360)
            if rotation in self.rotated_vertices:  # is there data prepared in this case?
                vertex_r = [[(e[0] + x, e[1] + y, e[2] + z) for e in l] for l in self.rotated_vertices[rotation]]
            else:  # otherwise, create it and store it todo: can we pre-calculate it?
                vertex_r = [[util.math.rotate_point(l[i * 3:i * 3 + 3], (0, 0, 0), rotation) for i in
                            range(len(l)//3)] for l in self.raw_vertices]
                vertex_r = [[util.math.rotate_point(e, self.rotation_core, self.rotation) for e in l] for l in vertex_r]
                self.rotated_vertices[rotation] = vertex_r
                vertex_r = [[(e[0] + x, e[1] + y, e[2] + z) for e in l] for l in vertex_r]


        function add_to_batch(self, position, batch, rotation, active_faces=None)
            
            adds the box model to the batch
            :param position: the position based on
            :param batch: the batches to select from
            :param rotation: the rotation to use
            :param active_faces: which faces to show
            :return: an vertex-list-list
            todo: make active_faces an dict of faces -> state, not an order-defined list


        function draw(self, position, rotation, active_faces=None)
            
            draws the BoxModel direct into the world
            WARNING: use batches for better performance
            :param position: the position to draw on
            :param rotation: the rotation to draw with
            :param active_faces: which faces to draw


        function add_face_to_batch(self, position, batch, rotation, face)

        function draw_face(self, position, rotation, face)

        @deprecation.deprecated(deprecated_in="snapshot dev 1 cycle 1", removed_in="v1.2.0 alpha")
        function copy(self, new_model=None)

    class BaseBoxModel
        
        an non-model-bound boxmodel class


        function __init__(self, relative_position: tuple, size: tuple, texture, texture_region=None, rotation=(0, 0, 0), rotation_center=None)
            
            creates an new renderer for the box-model
            :param relative_position: where to position the box relative to draw position
            :param size: the size of the box
            :param texture: which texture to use. May be str or pyglet.graphics.TextureGroup
            :param texture_region: which tex region to use, from (0, 0) to (1, 1)
            :param rotation: how to rotate the bbox
            :param rotation_center: where to rotate the box around


            variable self.relative_position

            variable self.size

            variable self.texture

        function recalculate_cache(self)

        function get_rotation(self)

        function set_rotation(self, rotation: tuple)

        variable rotation

        function get_texture_region(self)

        function set_texture_region(self, region)

        variable texture_region

        function add_to_batch(self, batch, position, rotation=(0, 0, 0), rotation_center=(0, 0, 0))

        function draw(self, position, rotation=(0, 0, 0), rotation_center=(0, 0, 0))