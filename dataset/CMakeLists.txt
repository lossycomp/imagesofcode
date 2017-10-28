cmake_minimum_required(VERSION 3.5)
project(datasetprogramsv2)

set(CMAKE_CXX_STANDARD 99)

add_subdirectory(basicmath)
add_subdirectory(bitcount)
add_subdirectory(CRC32)
add_subdirectory(dijkstra)
add_subdirectory(FFT)
add_subdirectory(qsort)
add_subdirectory(sha)

message("[INFO]: Toolchain:" ${CMAKE_TOOLCHAIN_FILE})
message("[INFO]: Root folder:" ${CMAKE_FIND_ROOT_PATH})
message("[INFO]: C Compiler:" ${CMAKE_C_COMPILER})
message("[INFO]: CXX Compiler:" ${CMAKE_CXX_COMPILER})
message("[INFO]: Compiler Flags:" ${CMAKE_CXX_FLAGS})

#set(SOURCE_FILES main.cpp)
#add_executable(datasetprogramsv2 ${SOURCE_FILES})