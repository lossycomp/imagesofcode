set(SOURCE_FILES
        bitops.h sniptype.h extkword.h conio.h
        bstr_i.c bitstrng.c bitfiles.c bitcnts.c
        bitcnt_1.c bitcnt_2.c bitcnt_3.c bitcnt_4.c)

add_executable(bitcount ${SOURCE_FILES})
#target_link_libraries(basicmath_large m)
#target_link_libraries(basicmath_small m)