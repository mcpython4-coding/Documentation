***MatrixStack.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class MatrixStack
        
        class handling an configuration of transformations for applying
        todo: optimise
        todo: use pyglet.matrix instead [pyglet 2 needed]


        function __init__(self)

            variable self.operation_stack - operator stack for which stuff to apply

            variable self.template_stack - you can store an state and reset to it when needed

        function addTranslate3d(self, dx: float, dy: float, dz: float) -> int
            
            will add an glTranslated()-call
            :return: the operation id


        function addRotate3d(self, v: float, rx: float, ry: float, rz: float) -> int
            
            will add an glRotated()-call
            :return: the operation id


        function addScale3d(self, sx: float, sy: float, sz: float) -> int
            
            will add an glScaled()-call
            :return: the operation id


        function addViewport(self, *args)

        function addMatrixMode(self, mode)

        function addLoadIdentity(self)

        function addGluPerspective(self, *args)

        function modifyOperation(self, operation_id: int, *data)
            
            will modify data from an operation on the stack
            :param operation_id: the id of the operation
            :param data: the data to use


        function copy(self, include_template_stack=True)
            
            will copy the MatrixStack object
            :param include_template_stack: if the template stack should be copied or not
            :return: the copied one


        function store(self)
            
            will store the current status in the template stack


        function pop(self)
            
            will restore the latest stored status and remove it from the template stack


        function apply(self)
            
            will apply the configuration onto the system. Will reset all present transformations


    @onlyInClient() class LinkedMatrixStack extends MatrixStack
        
        Matrix stack for dynamically generated values


        function addTranslate3d(self, *args) -> int

        function addRotate3d(self, *args) -> int

        function addScale3d(self, *args) -> int

        function apply(self)
            
            will apply the configuration onto the system. Will reset all present transformations
