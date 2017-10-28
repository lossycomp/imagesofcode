add_executable(qsort_large qsort_large.c)
add_executable(qsort_small qsort_small.c)

target_link_libraries(qsort_large m)
target_link_libraries(qsort_small m)