***EntityModelGenerator.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class EntityModelGenerator extends IDataGenerator
        
        Data generator for creating an entity model file


        function __init__(self, name)

            variable self.name

            variable self.boxes

            variable self.states

            variable self.y_inverted

        function setInvertedY(self, state=True)
            
            will set all y indexes to their other values
            :param state: the state to set to, default is True


        function add_box(
                self,
                name: str,
                texture: str,
                tex_size: tuple,
                position: tuple,
                rotation: tuple,
                size: tuple,
                center: tuple,
                uv=None,
                ):
            
            will add one new box to the entity model
            :param name: the name of the box
            :param texture: the texture of the box as an ResourceLocation-string
            :param tex_size: the size of the texture, needed for all subsequent calculations
            :param position: the position of the box relative to the entity origin
            :param rotation: the rotation of the box in degrees
            :param size: the size of the box, in 16 units = 1 block length
            :param center: the center of the rotation
            :param uv: the uv's to use


                variable uv

                variable uv

            variable self.boxes[name]

        function add_state(self, name: str, *boxes)
            
            adds an state for rendering the entity
            :param name: the name of the state
            :param boxes: the boxes to include


        function dump(self, generator: DataGeneratorInstance)

                        variable uv[i]

                variable data["boxes"][key]

                variable boxes

                        variable e

                            variable e["position"]

                            variable e["rotation"]

                            variable e["center"]

                        variable e

                variable data["states"][key]

        function get_default_location(self, generator: DataGeneratorInstance, name: str)