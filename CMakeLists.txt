cmake_minimum_required (VERSION 2.6)
project (chess-ai)
add_executable (chess-ai main.cpp)

include_directories("lib/googletest", "src", "include")
