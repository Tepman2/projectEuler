qt_add_library(problem01 STATIC problem01.h problem01.cpp)

target_link_libraries(problem01 PRIVATE Qt::Core)

target_include_directories(problem01 INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})
