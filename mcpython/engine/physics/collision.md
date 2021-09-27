***collision.py - documentation - last updated on 27.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    function collide(position: tuple, height: int, previous=None)
        
        Checks to see if the player at the given `position` and `height`
        is colliding with any blocks in the world.
        :param position: The (x, y, z) position to check for collisions at.
        :param height: The height of the player.
        :param previous: the previous position the player was, for the block collision API, optional
        :return The new position of the player taking into account collisions.
        todo: make player based
        todo: make account player & block hit box


        variable dimension

        variable player

        variable previous_positions

        variable pad
            How much overlap with a dimension of a surrounding block you need to
            have to count as a collision. If 0, touching terrain at all counts as
            a collision. If .49, you sink into the ground, as if walking through
            tall grass. If >= .5, you'll fall through the ground.

        variable p

        variable np

                variable d
                    How much overlap you have with this dimension.

                    variable op

                    variable chunk

                    variable block

                    variable blockstate

                            variable blockstate

                            variable shared.window.dy

                        variable player.flying

                            variable dy

                            variable player.fallen_since_y

    function get_colliding_blocks(position: tuple, height: int) -> tuple
        
        Similar to collide(), but will simply return an list of block-positions the player collides with and an list of blocks the player is in, but should not collide
        :param position: the position to use as center
        :param height: the height of the player
        :return: a tuple of colliding full blocks and colliding no collision blocks


                variable d
                    How much overlap you have with this dimension.

                    variable op

                    variable chunk

                    variable block