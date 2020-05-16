***WorldGenerationHandler.py - documentation - last updated on 16.5.2020 by uuk***
___

    class WorldGenerationTaskHandler
        
        handler for generating tasks off-call


        function __init__(self)

            variable self.chunks

            variable self.data_maps - invoke, world_changes, shown_updates

        function get_task_count_for_chunk(self, chunk: world.Chunk.Chunk) -> int
            
            gets the total count of tasks for an given chunk as an int
            :param chunk:
            :return:


        function schedule_invoke(self, chunk: world.Chunk.Chunk, method, *args, **kwargs)
            
            schedules an callable-invoke for the future
            :param chunk: the chunk to link to
            :param method: the method to call
            :param args: the args to call with
            :param kwargs: the kwargs to call with


        function schedule_block_add(self, chunk: world.Chunk.Chunk, position: tuple, name: str, *args, on_add=None, **kwargs)
            
            schedules an addition of an block
            :param chunk: the chunk the block is linked to
            :param position: the position of the block
            :param name: the name of the block
            :param args: the args to send to the add_block-method
            :param on_add: an callable called together with the block instance when the block is added
            :param kwargs: the kwargs send to the add_block-method


        function schedule_block_remove(self, chunk: world.Chunk.Chunk, position: tuple, *args, on_remove=None, **kwargs)
            
            schedules an removal of an block
            :param chunk: the chunk the block is linked to
            :param position: the position of the block
            :param args: the args to call the remove_block-function with
            :param on_remove: an callable to call when the block gets removed, with None as an parameter
            :param kwargs: the kwargs to call the remove_block-function with


        function schedule_block_show(self, chunk: world.Chunk.Chunk, position: tuple)
            
            schedules an show of an block
            :param chunk: the chunk
            :param position: the position of the block


        function schedule_block_hide(self, chunk: world.Chunk.Chunk, position: tuple)
            
            schedules an hide of an block
            :param chunk: the chunk
            :param position: the position of the block


        function schedule_visual_update(self, chunk: world.Chunk.Chunk, position: tuple)
            
            schedules an visual update of an block (-> show/hide as needed)
            :param chunk: the chunk
            :param position: the position of the block


        function process_one_task(self, chunk=None, reorder=True, log_msg=False) -> int
            
            processes one task from an semi-random chunk or an given one
            :param chunk: the chunk or None to select one
            :param reorder: unused; only for backwards-compatibility todo: remove
            :param log_msg: if messages for extra info should be logged


        function process_tasks(self, chunks=None, timer=None)
            
            process tasks
            :param chunks: if given, an iterable of chunks to generate
            :param timer: if given, an float in seconds to determine how far to generate


        function _process_0_array(self, chunk: world.Chunk.Chunk) -> bool

        function _process_1_array(self, chunk: world.Chunk.Chunk) -> bool

        function _process_2_array(self, chunk: world.Chunk.Chunk) -> bool

        function get_block(self, position: tuple, chunk=None, dimension=None)
            
            gets an generated block from the array
            :param position: the position of the block
            :param chunk: if the chunk is known
            :param dimension: if the dimension is known


        function clear_chunk(self, chunk: world.Chunk.Chunk)
            
            will remove all scheduled tasks from an given chunk
            :param chunk: the chunk


        function clear(self)
            
            will remove all scheduled tasks [chunk-wise]


    class WorldGenerationTaskHandlerReference
        
        reference class to an WorldGenerationTaskHandler for setting the chunk globally
        all scheduling functions are the same of WorldGenerationTaskHandler exept the chunk-parameter is missing.
        It is set on construction


        function __init__(self, handler: WorldGenerationTaskHandler, chunk: world.Chunk.Chunk)

            variable self.handler

            variable self.chunk

        function schedule_invoke(self, method, *args, **kwargs)

        function schedule_block_add(self, position, name, *args, on_add=None, **kwargs)

        function schedule_block_remove(self, position, *args, on_remove=None, **kwargs)

        function schedule_block_show(self, position)

        function schedule_block_hide(self, position)

        function schedule_visual_update(self, position)

        function process_one_task(self, chunk=None, reorder=True, log_msg=True)

        function get_block(self, position, chunk=None, dimension=None)

    class WorldGenerationHandler

        function __init__(self)

            variable self.layers

            variable self.features

            variable self.configs

            variable self.enable_generation - if world gen should be enabled

            variable self.enable_auto_gen - if chunks around the player should be generated when needed

            variable self.task_handler
            
            adds chunk schedule to the system
            will set the loaded-flag of the chunk during the process
            will schedule the internal _add_chunk function
            :param chunk: the chunk
            :param dimension: optional: if chunk is tuple, if another dim than active should be used
            :param prior: not used anymore, only for backward compatibility todo: remove
            :param force_generate: if generation should take place also when auto-gen is disabled
            :param generate_add: not used anymore, only for backward compatibility todo: remove
            :param immediate: if _add_chunk should be called immediate or not [can help in cases where TaskHandler stops
                running tasks when in-generation progress]


        function _add_chunk(self, chunk: world.Chunk.Chunk)
            
            internal implementation of the chunk generation code
            :param chunk: the chunk to schedule


        function process_one_generation_task(self, **kwargs):  # todo

        function setup_dimension(self, dimension, config=None)

        function generate_chunk(self, chunk: world.Chunk.Chunk, dimension=None, check_chunk=True)

        function register_layer(self, layer: world.gen.layer.Layer.Layer)

        function register_feature(self, decorator)

        function register_world_gen_config(self, name: str, layerconfig: dict)

        function __call__(self, data: str or world.gen.layer.Layer, config=None)

    variable G.worldgenerationhandler

    function load_layers()

    function load_modes()