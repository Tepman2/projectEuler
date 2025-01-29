qt_add_library(problem06 STATIC problem06.h problem06.cpp)

target_link_libraries(problem06 PRIVATE Qt6::Core)

target_include_directories(problem06 INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})
