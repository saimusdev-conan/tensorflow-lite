include conanbuildinfo.mak

#----------------------------------------
# Append Conan flags & defines
#----------------------------------------
CFLAGS          += $(CONAN_CFLAGS)
CXXFLAGS        += $(CONAN_CXXFLAGS)
INCLUDES        += $(addprefix -I, $(CONAN_INCLUDE_DIRS))
CPPFLAGS        += $(addprefix -D, $(CONAN_DEFINES))
LDFLAGS         += $(addprefix -L, $(CONAN_LIB_DIRS))
LIBS            += $(addprefix -l, $(CONAN_LIBS))

BUILD_WITH_MMAP=false
BUILD_WITH_NNAPI=false

