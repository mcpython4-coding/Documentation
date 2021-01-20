***EntityRenderer.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    variable RENDERERS

    variable TEXTURES

    @onlyInClient() class EntityRenderer

        function __init__(self, name)

            variable self.name

            variable self.path

            variable self.data

            variable self.box_models

            variable self.states

            variable self.texture_size

        function reload(self)
            
            reloads from file
            concept: every entity has an state which can be rendered (similar to blockstates). Every state contains multiple
                boxes, which can be shared across multiple states. You can select from every level the rendering position
                and rotation, but only on the lowest level (the level of the boxes) you can select the parameters of the box
                itself
            file format:
            {
                "boxes": {
                    <name>: {
                        "texture": <texturepath>,
                        "texture_size": <how big the texture is normally>,
                        "position": <relative position to center>,
                        "rotation": <relative rotation to center>,
                        "size": <size of the box>,
                        "center": <center of rotation>
                    }
                },
                "states": {
                    <name>: {
                        "boxes": [
                            {
                                "box": <box name>,
                                "rotation": <rotation relative to center>,
                                "center": <center of rotation>,
                                "position": <position relative to center>
                            }
                        ]
                    }
                }
            }


        function draw(self, entity, state, rotation=(0, 0, 0), part_rotation=None)
            
            draws the EntityRenderer
            :param entity: the entity to render
            :param state: the state to render
            :param rotation: the rotation to use
            :param part_rotation: the rotation of every part


        function draw_box(
                self,
                entity,
                boxname,
                position=(0, 0, 0),
                rotation=(0, 0, 0),
                rotation_center=(0, 0, 0),
                ):

            variable box

        function add_to_batch(
                self, batch, entity, state, rotation=(0, 0, 0), part_rotation=None
                ):
            
            adds the entity to an batch. Useful mostly for static entities like static complex block elements
            :param batch: the batch to use
            :param entity: the entity to add
            :param state: the state to add
            :param rotation: the rotation to use
            :param part_rotation: the rotation of every part
            :return: an list of vertex-objects created with the batch
            WARNING: batch  M U S T  be rendered in an 3d environment with, if the texture needs it, alpha enabled


            variable data

                variable box

                variable rotation_2

                variable rotation_center