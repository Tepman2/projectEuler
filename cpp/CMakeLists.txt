cmake_minimum_required(VERSION 3.10.0)
project(projectEuler VERSION 0.1.0 LANGUAGES C CXX)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_PREFIX_PATH "C:/Qt/6.8.1/mingw_64")

find_package(Qt6 REQUIRED COMPONENTS Widgets)
qt_standard_project_setup()

add_subdirectory(src/app)
add_subdirectory(src/problem01)
add_subdirectory(src/problem02)
add_subdirectory(src/problem03)

include(CTest)
enable_testing()

