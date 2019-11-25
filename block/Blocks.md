***block/Blocks.py - documentation***
___

This file is used for generating the simple block classes.
It uses factory.BlockFactory to generate the blocks.

1. def load_blocks

    will create the factory instances
    
    1. line 15 - 39: load stone-like blocks
    2. line 41 - 49: load colored blocks like concrete, concrete powder,
    wool & terracotta (only colored)
    3. line 51 - 64: load tree-type-specific blocks like logs, stripped
    logs, wood (log with log-side-texture on ALL sides), stripped wood,
    leaves, planks & slabs
    4. line 66 - 103: creates ores with their material blocks
    5. line 105 - 113: creates the special stone types with their 
    polished variants
    6. line 115 - 126: creates the stone-type-block-slabs

2. line 129: make (1) loaded by loading system