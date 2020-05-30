***enums.py - documentation - last updated on 30.5.2020 by uuk***
___

    class EnumSide extends enum.Enum

        variable TOP

        variable BOTTOM

        variable NORTH

        variable EAST

        variable SOUTH

        variable WEST

        static
        function iterate(cls)

        function __init__(self, dx, dy, dz, normal_name)

            variable self.relative

            variable self.normal_name

        function invert(self)

        function __eq__(self, other)

        function __hash__(self)

        function rotate(self, rotation)

        function rotate_reverse(self, rotation)

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