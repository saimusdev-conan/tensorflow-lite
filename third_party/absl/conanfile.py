#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: Conan is supported on a best-effort basis. Abseil doesn't use Conan
# internally, so we won't know if it stops working. We may ask community
# members to help us debug any problems that arise.

from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration
from conans.model.version import Version


class AbseilConan(ConanFile):
    name = "abseil"
    revision = "43ef2148c0936ebf7cb4be6b19927a9d9d145b8f"
    version = revision[:7]
    #url
    author = "Abseil <abseil-io@googlegroups.com>"
    homepage = "https://github.com/abseil/abseil-cpp"
    description = "Abseil Common Libraries (C++) from Google"
    license = "Apache-2.0"
    topics = ("conan", "abseil", "abseil-cpp", "google", "common-libraries")
    exports = ["LICENSE"]
    exports_sources = ["CMakeLists.txt", "CMake/*", "absl/*"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"static": [True, False], "fPIC": [True, False]}
    default_options = {"static": True, "fPIC": True}

    def configure(self):
        if self.settings.os == "Windows" and \
           self.settings.compiler == "Visual Studio" and \
           Version(self.settings.compiler.version.value) < "14":
            raise ConanInvalidConfiguration("Abseil does not support MSVC < 14")

    def build(self):
        tools.replace_in_file("CMakeLists.txt", "project(absl CXX)", "project(absl CXX)\ninclude(conanbuildinfo.cmake)\nconan_basic_setup()")
        cmake = CMake(self)
        cmake.definitions["BUILD_TESTING"] = False
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("LICENSE", dst="licenses")
        self.copy("*.h", dst="include", src=".")
        self.copy("*.a", dst="lib", src=".", keep_path=False)

    def package_info(self):
        if self.settings.os == "Linux":
            self.cpp_info.libs = ["-Wl,--start-group"]
        self.cpp_info.libs.extend(tools.collect_libs(self))
        if self.settings.os == "Linux":
            self.cpp_info.libs.extend(["-Wl,--end-group", "pthread"])
