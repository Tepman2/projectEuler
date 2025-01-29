qt_add_library(problem05 STATIC problem05.h problem05.cpp)

target_link_libraries(problem05 PRIVATE Qt6::Core)

target_include_directories(problem05 INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})
