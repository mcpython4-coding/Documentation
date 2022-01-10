***AxisAlignedBoundingBox.py - documentation - last updated on 28.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractBoundingBox extends ABC
        
        Abstract base class for bounding-box like classes to use in the corresponding systems
        todo: add ray hit system


        function test_point_hit(
                self,
                point: typing.Tuple[float, float, float],
                box_position: typing.Tuple[float, float, float],
                ):
            
            Tests for a collision with a single point
            :param point: the point
            :param box_position: the offset of the box


        function draw_outline(self, position: typing.Tuple[float, float, float])
            
            Draws an outline of the box
            :param position: the offset of the box


        function get_collision_motion_vector(
                self,
                this_position: typing.Tuple[float, float, float],
                collision_with: "AbstractBoundingBox",
                that_position: typing.Tuple[float, float, float],
                ) -> typing.Tuple[float, float, float]:
            
            Optional method implementing an algorithm for collision, where self is the moving body, and
            the parameter is the stationary body
            Returns a motion vector for self to move to not collide with the body


    class AxisAlignedBoundingBox extends AbstractBoundingBox
        
        The basic bounding box - an axis aligned cube


        function __init__(
                self,
                size: typing.Tuple[float, float, float],
                relative_position: typing.Tuple[float, float, float] = (0, 0, 0),
                ):

            variable self.size

            variable self.relative_position

            variable self.vertex_provider

        function recalculate_vertices(self)

        function test_point_hit(
                self,
                point: typing.Tuple[float, float, float],
                box_position: typing.Tuple[float, float, float],
                ):

        function draw_outline(self, position: typing.Tuple[float, float, float])

        function get_collision_motion_vector(
                self,
                this_position: typing.Tuple[float, float, float],
                collision_with: "AbstractBoundingBox",
                that_position: typing.Tuple[float, float, float],
                ):

        static
        function get_collision_vector_component(
                cls, x: float, sx: float, y: float, sy: float
                ) -> float:

        function test_collision_with(
                self, this_position, that_position, box: "AxisAlignedBoundingBox"
                ) -> int:

            variable v

        function collides_in_dimension(
                self,
                this_position: int,
                that_position: int,
                dim: int,
                box: "AxisAlignedBoundingBox",
                ) -> int:

            variable mx

            variable msx

            variable tx

            variable mtx

    class BoundingArea extends AbstractBoundingBox
        
        More options for hit-test by using a list of BoundBoxes


        function __init__(self)

            variable self.bounding_boxes

        function add_box(
                self,
                size: typing.Tuple[float, float, float],
                relative_position=(0, 0, 0),
                ):

        function test_point_hit(
                self,
                point: typing.Tuple[float, float, float],
                box_position: typing.Tuple[float, float, float],
                ):

        function draw_outline(self, position: typing.Tuple[float, float, float])

    variable FULL_BLOCK_BOUNDING_BOX

    variable EMPTY_BOUNDING_BOX