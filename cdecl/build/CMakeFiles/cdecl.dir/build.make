# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/yandong/projects/cdecl

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/yandong/projects/cdecl/build

# Include any dependencies generated for this target.
include CMakeFiles/cdecl.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/cdecl.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/cdecl.dir/flags.make

CMakeFiles/cdecl.dir/main.cpp.o: CMakeFiles/cdecl.dir/flags.make
CMakeFiles/cdecl.dir/main.cpp.o: ../main.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/yandong/projects/cdecl/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/cdecl.dir/main.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/cdecl.dir/main.cpp.o -c /home/yandong/projects/cdecl/main.cpp

CMakeFiles/cdecl.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/cdecl.dir/main.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/yandong/projects/cdecl/main.cpp > CMakeFiles/cdecl.dir/main.cpp.i

CMakeFiles/cdecl.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/cdecl.dir/main.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/yandong/projects/cdecl/main.cpp -o CMakeFiles/cdecl.dir/main.cpp.s

CMakeFiles/cdecl.dir/main.cpp.o.requires:
.PHONY : CMakeFiles/cdecl.dir/main.cpp.o.requires

CMakeFiles/cdecl.dir/main.cpp.o.provides: CMakeFiles/cdecl.dir/main.cpp.o.requires
	$(MAKE) -f CMakeFiles/cdecl.dir/build.make CMakeFiles/cdecl.dir/main.cpp.o.provides.build
.PHONY : CMakeFiles/cdecl.dir/main.cpp.o.provides

CMakeFiles/cdecl.dir/main.cpp.o.provides.build: CMakeFiles/cdecl.dir/main.cpp.o

# Object files for target cdecl
cdecl_OBJECTS = \
"CMakeFiles/cdecl.dir/main.cpp.o"

# External object files for target cdecl
cdecl_EXTERNAL_OBJECTS =

cdecl: CMakeFiles/cdecl.dir/main.cpp.o
cdecl: CMakeFiles/cdecl.dir/build.make
cdecl: CMakeFiles/cdecl.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable cdecl"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/cdecl.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/cdecl.dir/build: cdecl
.PHONY : CMakeFiles/cdecl.dir/build

CMakeFiles/cdecl.dir/requires: CMakeFiles/cdecl.dir/main.cpp.o.requires
.PHONY : CMakeFiles/cdecl.dir/requires

CMakeFiles/cdecl.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/cdecl.dir/cmake_clean.cmake
.PHONY : CMakeFiles/cdecl.dir/clean

CMakeFiles/cdecl.dir/depend:
	cd /home/yandong/projects/cdecl/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/yandong/projects/cdecl /home/yandong/projects/cdecl /home/yandong/projects/cdecl/build /home/yandong/projects/cdecl/build /home/yandong/projects/cdecl/build/CMakeFiles/cdecl.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/cdecl.dir/depend

