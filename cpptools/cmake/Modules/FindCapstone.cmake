# - Try to find CAPSTONE
# Once done, this will define
#
#  CAPSTONE_FOUND - system has CAPSTONE
#  CAPSTONE_INCLUDE_DIRS - the CAPSTONE include directories
#  CAPSTONE_LIBRARIES - link these to use CAPSTONE

# Try to use the Linux PKG Config tool to find the library
find_package(PkgConfig)
pkg_check_modules(PC_CAPSTONE QUIET libcapstone)
set(CAPSTONE_DEFINITIONS ${PC_LIBCAPSTONE_CFLAGS_OTHER})

# Include dir
find_path(CAPSTONE_INCLUDE_DIR
        NAMES capstone/capstone.h
        HINTS ${CAPSTONE_PKGCONF_INCLUDE_DIRS}
        )

# Finally the library itself
find_library(CAPSTONE_LIBRARY
        NAMES capstone libcapstone
        HINTS ${PC_LIBCAPSTONE_LIBDIR} ${PC_LIBCAPSTONE_LIBRARY_DIRS}
        )

# Set the include dir variables and the libraries and let libfind_process do the rest.
# NOTE: Singular variables for this library, plural for libraries this this lib depends on.
set(CAPSTONE_PROCESS_INCLUDES CAPSTONE_INCLUDE_DIR CAPSTONE_INCLUDE_DIRS)
set(CAPSTONE_PROCESS_LIBS CAPSTONE_LIBRARY CAPSTONE_LIBRARIES)

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(Capstone DEFAULT_MSG
        CAPSTONE_LIBRARY CAPSTONE_INCLUDE_DIR)