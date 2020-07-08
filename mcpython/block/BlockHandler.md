***BlockHandler.py - documentation - last updated on 8.6.2020 by uuk***
___

    function register_block(registry, blockclass)

                variable blockclass.CONDUCTS_REDSTONE_POWER

                variable blockclass.CAN_MOBS_SPAWN_ON

                    variable blockclass.ENABLE_RANDOM_TICKS

    variable block_registry

    variable block_registry.full_table - an table of localized & un-localized block names

    function load()
        
        loads all blocks that should be loaded, only the ones for blocks may be loaded somewhere else
