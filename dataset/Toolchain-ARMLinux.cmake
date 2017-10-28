# this one is important
set(CMAKE_SYSTEM_NAME Linux)
# this one not so much
set(CMAKE_SYSTEM_VERSION 1)

# Create an option to generate ARM, THUMB instructions or both. Both by default
set(INSTRUCTION_ENCODING "both" CACHE STRING "Define if we allow the compier to use THUMB instructions")
set_property(CACHE INSTRUCTION_ENCODING PROPERTY STRINGS arm_only thumb_only both)

# Add compiler flags depending on the instruction set that the user wants to generate
if ( ${INSTRUCTION_ENCODING} STREQUAL "arm_only"  )
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -marm" )
    message("ARM ONLY ISA")
elseif( ${INSTRUCTION_ENCODING} STREQUAL "thumb_only" )
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -mthumb" )
    message("THUMB ONLY ISA")
else()
    # Quick and dirty
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -marm" )
    message("FIXED TO BE: ARM ISA")
endif()

# Let the user know the instrucion encoding used
if (NOT ${INSTRUCTION_ENCODING} STREQUAL "both")
    message("[INFO]: Instruction encoding:" ${INSTRUCTION_ENCODING})
    message("[INFO]: CXX Options:" ${CMAKE_CXX_FLAGS})
endif()

# where is the target environment
# In order to run this configuration from CLion, you must modify the
# CMake options of CLion settings (File -> Settings -> CMake) setting the value of this variable
set(CMAKE_TOOLCHAIN_ROOT_PATH "" CACHE PATH "Path to the toolchain root path")

#By default, we will be using the Crosstool-ng toolchain builder, therefore
#the compilers will be located in a fixed location withing the CMAKE_FIND_ROOT_PATH
set(CMAKE_C_COMPILER   ${CMAKE_TOOLCHAIN_ROOT_PATH}/bin/arm-unknown-linux-gnueabi-gcc)
set(CMAKE_CXX_COMPILER ${CMAKE_TOOLCHAIN_ROOT_PATH}/bin/arm-unknown-linux-gnueabi-g++)

# search for programs in the build host directories
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
# for libraries and headers in the target directories
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)