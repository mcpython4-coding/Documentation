***math.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @deprecation.deprecated()
    function cube_vertices_better(
            x: float,
            y: float,
            z: float,
            nx: float,
            ny: float,
            nz: float,
            faces=(True, True, True, True, True, True),
            ) -> typing.Iterable[typing.List[float]]:

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
        :return: a tuple representing the texture coordinates


            variable reindex

            variable _positions

            variable positions

    function tex_coordinates_better(
            *args: typing.Tuple[int, int],
            size=(32, 32),
            tex_region=None,
            rotation=(0, 0, 0, 0, 0, 0)
            ) -> list:
        
        This is a better implementation of above tex_coords function. It will return a list of coords instead
            of a list where you have to manually find entries for drawing
        :param args: for each face to calculate, the uv's as a tuple of size 2
        :param size: the size of the texture group, as specified by the texture atlas
        :param tex_region: the region in the texture, where 0 is one end and 1 the other
        :param rotation: the rotation of the whole thing
        :return: a list of lists of texture coords


            variable tex_region

    function normalize(position: typing.Tuple[float, float, float])
        
        Accepts `position` of arbitrary precision and returns the block
        containing that position
        Uses simply rounding on all components
        :param position: the position
        :return: the rounded position


    function position_to_chunk(
            position: typing.Union[
            typing.Tuple[float, float, float], typing.Tuple[float, float]
            ]
            ) -> typing.Tuple[int, int]:
        
        Returns a tuple representing the chunk for the given `position`.
        :param position: the position, as a two-tuple (x, z) or three-tuple (x, y, z)
        :return: the chunk position, as (x, z)


    @deprecation.deprecated()
    function topological_sort(items)
        
        'items' is an iterable of (item, dependencies) pairs, where 'dependencies'
        is an iterable of the same type as 'items'.
        If 'items' is a generator rather than a data structure, it should not be
        empty. Passing an empty generator for 'items' (zero yields before return)
        will cause topological_sort() to raise TopologicalSortFailure.
        An empty iterable (e.g. list, tuple, set, ...) produces no items but
        raises no exception.
        todo: replace with native sorting system


        variable generator

    function rotate_point(point, origin, rotation)
        
        Helper function for rotating an point around another one
        :param point: the point to rotate
        :param origin: the origin to rotate around
        :param rotation: the rotation angle
        :return: the rotated point
        todo: optimise!


        variable rx

        variable ry

        variable rz

        variable nx

        variable ny

        variable nx

        variable nz

        variable ny

        variable nz

    function product(iterable: typing.List[typing.SupportsFloat])
        
        Same as sum(), but will use * instead of +


    function vector_offset(
            vector: typing.Tuple[float, ...], base: typing.Tuple[float, ...]
            ) -> typing.Tuple[float, ...]:

    function vector_negate(vector: typing.Tuple[float, ...]) -> typing.Tuple[float, ...]

    function vector_distance(a, b)

    function sort_components(a: typing.Tuple[float, ...], b: typing.Tuple[float, ...])
        
        Util method for sorting two vectors
        :return: two tuples, one with the smallest x, y, z and one with the biggest x, y, z coordinate
        Example:
        sort_components((-1, 5, -7), (5, -10, 4)) == ((-1, -10, -7), (5, 5, 4))
        Useful when user inputs two coordinates and usage requires this special order (for example, for range()-ing over them)
