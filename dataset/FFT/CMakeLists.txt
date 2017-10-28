set(SOURCE_FILES main.c fourier.h fourierf.c fftmisc.c ddc.h ddcmath.h)

add_executable(fft ${SOURCE_FILES})

target_link_libraries(fft m)