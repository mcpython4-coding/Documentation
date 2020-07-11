***enums.py - documentation - last updated on 11.7.2020 by uuk***
___

    variable COLORS

    class EnumSide extends enum.Enum
        
        Enum holding the 6 different sides of an Block.
        Also used for defining axis where it points in the direction


        variable TOP

        variable BOTTOM

        variable NORTH

        variable EAST

        variable SOUTH

        variable WEST

        static
        function iterate(cls)
            
            Iterator for the faces


        function __init__(self, dx: int, dy: int, dz: int, normal_name: str)
            
            Constructs an new enum instance
            :param dx: the delta in x
            :param dy: the delta in y
            :param dz: the delta in z
            :param normal_name: the normal name of the face


            variable self.relative

            variable self.normal_name

        function invert(self)
            
            Will invert the face to its opposite
            :return: the opposite face


        function __eq__(self, other)

        function __hash__(self)

        function rotate(self, rotation: tuple)

        function rotate_reverse(self, rotation: tuple)

    variable FACE_ORDER

    variable ROTATE
        How to rotate the different faces?

    class LogAxis extends enum.Enum

        variable X

        variable Y

        variable Z

    class ToolType extends enum.Enum

        variable HAND

        variable PICKAXE

        variable AXE

        variable SHOVEL

        variable SHEAR

        variable SWORD - not real an tool, but internally handled as one of it

        variable HOE - not real an tool, but internally handled as one of it

    class SlabModes extends enum.Enum

        variable TOP

        variable BOTTOM

        variable DOUBLE

    class LoadingStageStatus extends enum.Enum

        variable WORKING

        variable MOD_CHANGED

        variable EVENT_CHANGED

        variable FINISHED

    class ButtonMode extends enum.Enum

        variable DISABLED

        variable ENABLED

        variable HOVERING