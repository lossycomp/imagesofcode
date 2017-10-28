set(BASE_SOURCE_FILES pi.h round.h snipmath.h sniptype.h cubic.c isqrt.c rad2deg.c)
set(LARGE_SOURCE_FILES basicmath_large.c ${BASE_SOURCE_FILES})
set(SMALL_SOURCE_FILES basicmath_small.c ${BASE_SOURCE_FILES})
message(${LARGE_SOURCE_FILES})

add_executable(basicmath_large ${LARGE_SOURCE_FILES})
add_executable(basicmath_small ${SMALL_SOURCE_FILES})

target_link_libraries(basicmath_large m)
target_link_libraries(basicmath_small m)