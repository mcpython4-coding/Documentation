***util.py - documentation - last updated on 28.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    function create_instruction(
            opname_or_code: str | int,
            arg_pt: int = 0,
            arg_val: typing.Any = None,
            offset=-1,
            start_line=None,
            is_jump_target=False,
            ):

            variable opname

            variable opcode

            variable opcode

            variable opname

    class PyOpcodes

        variable POP_TOP

        variable ROT_TWO

        variable ROT_THREE

        variable DUP_TOP

        variable DUP_TOP_TWO

        variable ROT_FOUR

        variable NOP

        variable UNARY_POSITIVE

        variable UNARY_NEGATIVE

        variable UNARY_NOT

        variable UNARY_INVERT

        variable BINARY_MATRIX_MULTIPLY

        variable INPLACE_MATRIX_MULTIPLY

        variable BINARY_POWER

        variable BINARY_MULTIPLY

        variable BINARY_MODULO

        variable BINARY_ADD

        variable BINARY_SUBTRACT

        variable BINARY_SUBSCR

        variable BINARY_FLOOR_DIVIDE

        variable BINARY_TRUE_DIVIDE

        variable INPLACE_FLOOR_DIVIDE

        variable INPLACE_TRUE_DIVIDE

        variable RERAISE

        variable WITH_EXCEPT_START

        variable GET_AITER

        variable GET_ANEXT

        variable BEFORE_ASYNC_WITH

        variable END_ASYNC_FOR

        variable INPLACE_ADD

        variable INPLACE_SUBTRACT

        variable INPLACE_MULTIPLY

        variable INPLACE_MODULO

        variable STORE_SUBSCR

        variable DELETE_SUBSCR

        variable BINARY_LSHIFT

        variable BINARY_RSHIFT

        variable BINARY_AND

        variable BINARY_XOR

        variable BINARY_OR

        variable INPLACE_POWER

        variable GET_ITER

        variable GET_YIELD_FROM_ITER

        variable PRINT_EXPR

        variable LOAD_BUILD_CLASS

        variable YIELD_FROM

        variable GET_AWAITABLE

        variable LOAD_ASSERTION_ERROR

        variable INPLACE_LSHIFT

        variable INPLACE_RSHIFT

        variable INPLACE_AND

        variable INPLACE_XOR

        variable INPLACE_OR

        variable LIST_TO_TUPLE

        variable RETURN_VALUE

        variable IMPORT_STAR

        variable SETUP_ANNOTATIONS

        variable YIELD_VALUE

        variable POP_BLOCK

        variable POP_EXCEPT

        variable HAVE_ARGUMENT - Opcodes from here have an argument:

        variable STORE_NAME - Index in name list

        variable DELETE_NAME - ""

        variable UNPACK_SEQUENCE - Number of tuple items

        variable FOR_ITER

        variable UNPACK_EX

        variable STORE_ATTR - Index in name list

        variable DELETE_ATTR - ""

        variable STORE_GLOBAL - ""

        variable DELETE_GLOBAL - ""

        variable LOAD_CONST - Index in const list

        variable LOAD_NAME - Index in name list

        variable BUILD_TUPLE - Number of tuple items

        variable BUILD_LIST - Number of list items

        variable BUILD_SET - Number of set items

        variable BUILD_MAP - Number of dict entries

        variable LOAD_ATTR - Index in name list

        variable COMPARE_OP - Comparison operator

        variable IMPORT_NAME - Index in name list

        variable IMPORT_FROM - Index in name list

        variable JUMP_FORWARD - Number of bytes to skip

        variable JUMP_IF_FALSE_OR_POP - Target byte offset from beginning of code

        variable JUMP_IF_TRUE_OR_POP - ""

        variable JUMP_ABSOLUTE - ""

        variable POP_JUMP_IF_FALSE - ""

        variable POP_JUMP_IF_TRUE - ""

        variable LOAD_GLOBAL - Index in name list

        variable IS_OP

        variable CONTAINS_OP

        variable JUMP_IF_NOT_EXC_MATCH

        variable SETUP_FINALLY - Distance to target address

        variable LOAD_FAST - Local variable number

        variable STORE_FAST - Local variable number

        variable DELETE_FAST - Local variable number

        variable RAISE_VARARGS - Number of raise arguments (1, 2, or 3)

        variable CALL_FUNCTION - #args

        variable MAKE_FUNCTION - Flags

        variable BUILD_SLICE - Number of items

        variable LOAD_CLOSURE

        variable LOAD_DEREF

        variable STORE_DEREF

        variable DELETE_DEREF

        variable CALL_FUNCTION_KW - #args + #kwargs

        variable CALL_FUNCTION_EX - Flags

        variable SETUP_WITH

        variable LIST_APPEND

        variable SET_ADD

        variable MAP_ADD

        variable LOAD_CLASSDEREF

        variable EXTENDED_ARG

        variable SETUP_ASYNC_WITH

        variable FORMAT_VALUE

        variable BUILD_CONST_KEY_MAP

        variable BUILD_STRING

        variable LOAD_METHOD

        variable CALL_METHOD

        variable LIST_EXTEND

        variable SET_UPDATE

        variable DICT_MERGE

        variable DICT_UPDATE