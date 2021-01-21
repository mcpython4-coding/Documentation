***math.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    function cube_vertices_better(
            x: float,
            y: float,
            z: float,
            nx: float,
            ny: float,
            nz: float,
            faces=(True, True, True, True, True, True),
            ):
        
        Similar to cube_vertices, but will return it per-face instead of an whole array of data
        :param x: the x position
        :param y: the y position
        :param z: the z position
        :param nx: the size in x direction
        :param ny: the size in y direction
        :param nz: the size in z direction
        :param faces: which faces to generate
        :return: an tuple of length 6 representing each face


        variable top

        variable bottom

        variable left

        variable right

        variable front

        variable back

    function tex_coordinates(x, y, size=(32, 32), region=(0, 0, 1, 1), rot=0) -> tuple
        
        Return the bounding vertices of the texture square.
        :param x: the texture atlas entry to use
        :param y: the texture atlas entry to use
        :param size: the size of the texture atlas used
        :param region: the texture region to use. (0, 0, 1, 1) is full texture atlas texture size
        :param rot: in steps of 90: how much to rotate the vertices
        :return: an tuple representing the texture coordinates


    function tex_coordinates_better(
            *args, size=(32, 32), tex_region=None, rotation=(0, 0, 0, 0, 0, 0)
            ) -> list:
        
        this is an better implementation of above tex_coords function. It will return an list of coords instead
        of an list where you have to manually find entries
        :param args: every face to calculate
        :param size: the size of the texture group
        :param tex_region: the region in the texture, where 0 is one end and 1 the other
        :param rotation: the rotation of the whole thing
        :return: an list of lists of texture coords


            variable tex_region

    function tex_coordinates_factor(fx, fy, tx, ty)

    function normalize(position)
        
        Accepts `position` of arbitrary precision and returns the block
        containing that position.
        :param position: the position
        :return block_position: the rounded position


    function normalize_ceil(position)
        
        Same as normalize(position), but with math.ceil() instead of round()
        :param position: the position
        :return: the ceil-ed position


    function position_to_chunk(position)
        
        Returns a tuple representing the chunk for the given `position`.
        :param position: the position
        :return: the chunk


    function position_to_chunk_unsafe(position)
        
        Returns a tuple representing the chunk for the given `position`.
        :param position: the position
        :return: the chunk


    function topological_sort(items)
        
        'items' is an iterable of (item, dependencies) pairs, where 'dependencies'
        is an iterable of the same type as 'items'.
        If 'items' is a generator rather than a data structure, it should not be
        empty. Passing an empty generator for 'items' (zero yields before return)
        will cause topological_sort() to raise TopologicalSortFailure.
        An empty iterable (e.g. list, tuple, set, ...) produces no items but
        raises no exception.


        variable provided

        variable items

        variable missing

        variable previous_missing

        variable result

                variable previous_missing

    function rotate_point(point, origin, rotation)
        
        Helper function for rotating an point around another one
        :param point: the point to rotate
        :param origin: the origin to rotate around
        :param rotation: the rotation angle
        :return: the rotated point


        variable nx

        variable ny

        variable nx

        variable nz

        variable ny

        variable nz

    function product(iterable: typing.List[float])