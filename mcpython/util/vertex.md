***vertex.py - documentation - last updated on 5.2.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable CORNER_SIGNS
        This defines how cubes look; do not change!

    variable CUBE_MAP

    @try_optimise()
    function calculate_default(size: typing.Tuple[float, float, float])

        variable CORNERS

    @try_optimise()
    function offset_data(data, offset: typing.Tuple[float, float, float])

    @try_optimise()
    function rotate_data(
            data,
            origin: typing.Tuple[float, float, float],
            rotation: typing.Tuple[float, float, float],
            ):

    @try_optimise()
    function scale_data(data, scale: float)

    class VertexProvider
        
        Class doing some magic for vertices calculation
        Invoke create() for getting a shared one, otherwise it will not be made arrival to others
        All attributes are read-only and modification is not part of the public API
        Modification may get made un-arrival in the future
        Use invalidate_internal() to reduce cache load
        todo: can we use some optimised library like numpy here?


        variable SHARED
            Internal cache of instances, uses weak references in order to save memory when discarding instances
            in model system

        static
        function create(
                cls,
                offset: typing.Tuple[float, float, float],
                size: typing.Tuple[float, float, float],
                base_rotation_center: typing.Tuple[float, float, float] = None,
                base_rotation: typing.Tuple[float, float, float] = (0, 0, 0),
                ):

                variable base_rotation_center

            variable key
                This key defines the VertexProvider instance, so look up this key in the cache

        function __init__(
                self,
                offset: typing.Tuple[float, float, float],
                size: typing.Tuple[float, float, float],
                base_rotation_center: typing.Tuple[float, float, float],
                base_rotation: typing.Tuple[float, float, float],
                ):

            variable self.offset

            variable self.size

            variable self.base_rotation

            variable self.base_rotation_center

            variable self.default

            variable self.cache

        @try_optimise()
        function get_vertex_data(
                self,
                element_position: typing.Tuple[float, float, float],
                element_rotation: typing.Tuple[float, float, float] = (0, 0, 0),
                element_rotation_center: typing.Tuple[float, float, float] = None,
                scale: float = 1,
                ):

        @try_optimise()
        function ensure_prepared_rotation(
                self,
                rotation: typing.Tuple[float, float, float],
                center: typing.Tuple[float, float, float] = None,
                scale: float = 1,
                ):

                variable center

            variable key

        function invalidate_internal(self)