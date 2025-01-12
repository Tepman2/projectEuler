qt_add_library(problem02 STATIC problem02.h problem02.cpp)

target_link_libraries(problem02 PRIVATE Qt6::Core)

target_include_directories(problem02 INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})
