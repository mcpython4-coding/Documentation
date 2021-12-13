***TickHandler.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class TickHandler
        
        Main handler for ticks


        function __init__(self)

            variable self.tick_array

            variable self.active_tick

            variable self.next_ticket_id

            variable self.results

            variable self.lost_time

            variable self.enable_tick_skipping

            variable self.instant_ticks

            variable self.enable_random_ticks

            variable self.execute_array
                an array of (function, args, kwargs) for functions which should be executed in near future

        function schedule_tick(self, dt: float)
            
            Execute ticks
            :param dt: the time that came after the last event


                        variable result

                            variable self.results[ticket_id]

                        variable self.lost_time

                        variable result

        function schedule_once(self, function, *args, **kwargs)
            
            Will execute the function in near time. Helps when in an event and need to exchange stuff which might be
            affected when calling further down the event stack
            :param function: the function to call


        function bind(
                self, function, tick, is_delta=True, ticket_function=None, args=[], kwargs={}
                ):
            
            bind an function to an given tick
            :param function: the function to bind
            :param tick: the tick to add
            :param is_delta: if it is delta or not
            :param ticket_function: function which is called when the function is called with some informations
            :param args: the args to give
            :param kwargs: the kwargs to give


                variable self.tick_array[tick]

                variable ticket_id

                variable ticket_id

        function bind_redstone_tick(self, function, tick, *args, **kwargs)

            variable dimension

            variable random_tick_speed

            variable r

            variable blocks

                            variable x

                            variable z

                                    variable position

                                    variable instance

    variable handler