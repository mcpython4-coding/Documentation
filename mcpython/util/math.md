***math.py - documentation - last updated on 11.7.2020 by uuk***
___

    @deprecation.deprecated("dev3-2", "a1.3.0")
    function get_max_y(pos)

    @deprecation.deprecated(deprecated_in="dev1-1", removed_in="v1.2.0 alpha")
    function cube_vertices(x, y, z, nx, ny, nz, faces=(True, True, True, True, True, True))
        
        Same as cube_vertices_better, but will return all summed up instead of separated lists


    function cube_vertices_better(x: float, y: float, z: float, nx: float, ny: float, nz: float, faces=(True, True, True, True, True, True))
        
        Similar to cube_vertices, but will return it per-face instead of an whole array of data
        :param x: the x position
        :param y: the y position
        :param z: the z position
        :param nx: the size in x direction
        :param ny: the size in y direction
        :param nz: the size in z direction
        :param faces: which faces to generate
        :return: an tuple of length 6 representing each face


    function tex_coord(x, y, size=(32, 32), region=(0, 0, 1, 1), rot=0) -> tuple
        
        Return the bounding vertices of the texture square.
        :param x: the texture atlas entry to use
        :param y: the texture atlas entry to use
        :param size: the size of the texture atlas used
        :param region: the texture region to use. (0, 0, 1, 1) is full texture atlas texture size
        :param rot: in steps of 90: how much to rotate the vertices
        :return: an tuple representing the texture coordinates


    @deprecation.deprecated(deprecated_in="dev1-1", removed_in="v1.2.0 alpha")
    function tex_coords(*args, size=(32, 32), tex_region=None, rotation=(0, 0, 0, 0, 0, 0))
        
        same as tex_coords_better, but returns everything in an single list instead of an list of tuples
        todo: when removed, rename later the new one to this


    function tex_coords_better(*args, size=(32, 32), tex_region=None, rotation=(0, 0, 0, 0, 0, 0)) -> list
        
        this is an better implementation of above tex_coords function. It will return an list of coords instead
        of an list where you have to manually find entries
        :param args: every face to calculate
        :param size: the size of the texture group
        :param tex_region: the region in the texture, where 0 is one end and 1 the other
        :param rotation: the rotation of the whole thing
        :return: an list of lists of texture coords


    function tex_coord_factor(fx, fy, tx, ty): return fx, fy, tx, fy, tx, ty, fx, ty
            
            
            def normalize(position):

    function normalize(position)
        
        Accepts `position` of arbitrary precision and returns the block
        containing that position.
        :param position: the position
        :return block_position: the rounded position


    function normalize_ceil(position)
        
        Same as normalize(position), but with math.ceil() instead of round()
        :param position: the position
        :return: the ceil-ed position


    @deprecation.deprecated("dev5-1", "a1.5.0")
    function sectorize(position): return positionToChunk(position)
            
            
            def positionToChunk(position):

    function positionToChunk(position)
        
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