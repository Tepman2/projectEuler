qt_add_library(problem03 STATIC problem03.h problem03.cpp)

target_link_libraries(problem03 PRIVATE Qt6::Core)

target_include_directories(problem03 INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})
