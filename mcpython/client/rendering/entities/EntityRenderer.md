***EntityRenderer.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
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


            variable self.data

            variable reloaded

                variable box

                variable texture

                variable self.texture_size

                    variable group

                        variable group

                        variable group

                    variable uv

                    variable uv

                variable self.box_models[

                variable d

                variable self.states[state]

        function draw(self, entity_or_position, state, rotation=(0, 0, 0), part_rotation=None)
            
            Draws the EntityRenderer at the given position
            :param entity_or_position: the entity to render or the position to render at
            :param state: the state to render, as in the model of the entity
            :param rotation: the rotation to use; as (rx, ry, rz)
            :param part_rotation: the rotation of every part, as a dict of model part -> (rx, ry, rz), calculated onto
                the "other" rotations


        function draw_box(
                self,
                entity_or_position,
                box_name: str,
                position=(0, 0, 0),
                rotation=(0, 0, 0),
                rotation_center=(0, 0, 0),
                ):
            
            Renders a single box of the model
            :param entity_or_position: the position to render at or the entity to render
            :param box_name: the box name
            :param position: the offset
            :param rotation: the rotation
            :param rotation_center: the center to rotate around


            variable box

        function add_to_batch(
                self,
                batch: pyglet.graphics.Batch,
                entity_or_position,
                state,
                rotation=(0, 0, 0),
                part_rotation=None,
                ):
            
            Adds the entity to a batch. Useful mostly for static entities like static complex block elements
            WARNING: this is not-mutable
            WARNING: batch  M U S T  be rendered in an 3d environment with, if the texture needs it, alpha enabled
            :param batch: the batch to use
            :param entity_or_position: the entity to add
            :param state: the state to add
            :param rotation: the rotation to use
            :param part_rotation: the rotation of every part
            :return: an list of vertex-objects created with the batch


            variable data

                variable box

                variable rotation_2

                variable rotation_center