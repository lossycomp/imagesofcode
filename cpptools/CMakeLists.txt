cmake_minimum_required(VERSION 3.5.1)

project(elfmanipulation)

set(CMAKE_CXX_STANDARD 11)

#Module directory.
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake/Modules/")

# Dependencies
find_package(Capstone)

#message("Modules: ${CMAKE_MODULE_PATH}")
#message("SRC DIR: ${CMAKE_SOURCE_DIR}")
#message("LIB PATH: ${CMAKE_LIBRARY_PATH}")

#find_package(PythonLibs)
include_directories(libs/elfio-3.2)
#include_directories(${PYTHON_INCLUDE_PATH})

# Just a little debug
message("DEPENDENCIES:")
message(" Capstone:")
message(" -- Library: ${CAPSTONE_LIBRARY}")
message(" -- Includes: ${CAPSTONE_INCLUDE_DIR}")
#message("Python Libs:")
#message(" - have the Python libs been found : ${PYTHONLIBS_FOUND}")
#message(" - path to the python library : ${PYTHON_LIBRARIES}")
#message(" - path to where Python.h is found (deprecated) : ${PYTHON_INCLUDE_PATH}")
#message(" - path to where Python.h is found : ${PYTHON_INCLUDE_DIRS}")
#message(" - version of the Python libs found : ${PYTHONLIBS_VERSION_STRING}")

# Add a subdir with the python bindings
# add_subdirectory(python_bindings)

#The ARM-To-Binary Program
set(TO_BIN_SOURCE elftobin.cpp)
add_executable(elfcodetobin ${TO_BIN_SOURCE})

# The ARM-To-Text Program
set(TO_TEXT_SOURCE elftotext.cpp)
add_executable(elfcodetotext ${TO_TEXT_SOURCE})
target_link_libraries(elfcodetotext ${CAPSTONE_LIBRARY})

# The ARM Modify Program
set(ELF_CODE_MODIFY_SOURCE elfmodifyinstructions.cpp)
add_executable(elfmodify ${ELF_CODE_MODIFY_SOURCE})

#ELFIO module for python
#set(ELFIO_WRAPPER_SOURCE elfiomodule.c)
#add_library(elfio SHARED ${ELFIO_WRAPPER_SOURCE} elfiomodule.h)
#target_link_libraries(elfio ${PYTHON_LIBRARIES})
# set_target_properties(elfio PROPERTIES RUNTIME_OUTPUT_DIRECTORY "python_bindings/elfio")
# Python follows some naming conventions that we must respect
# set_target_properties(elfiomdule PROPERTIES OUTPUT_NAME "elfiomdule")
# set_target_properties(elfiomdule PROPERTIES PREFIX "")
# set_target_properties(elfiomdule PROPERTIES SUFFIX ".pyd")



