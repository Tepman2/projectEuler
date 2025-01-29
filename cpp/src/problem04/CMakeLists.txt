qt_add_library(problem04 STATIC problem04.h problem04.cpp)

target_link_libraries(problem04 PRIVATE Qt6::Core)

target_include_directories(problem04 INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})
