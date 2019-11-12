cmake_minimum_required(VERSION 3.5 FATAL_ERROR)
set(CMAKE_VERBOSE_MAKEFILE TRUE)

project(fft2d LANGUAGES C CXX)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Conan's auto-generated build info 
if(EXISTS "${CMAKE_BINARY_DIR}/conanbuildinfo.cmake")
    include("${CMAKE_BINARY_DIR}/conanbuildinfo.cmake")
else()
    include(conanbuildinfo.cmake)
endif()

# Perform basic stuff, as defined in the conan recipe (among other things)
conan_basic_setup()

set(SOURCE_FILES fftsg.c fftsg2d.c)

add_library(${PROJECT_NAME} STATIC ${SOURCE_FILES})

