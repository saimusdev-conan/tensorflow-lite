#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: Conan is supported on a best-effort basis. Abseil doesn't use Conan
# internally, so we won't know if it stops working. We may ask community
# members to help us debug any problems that arise.

from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration
from conans.model.version import Version


class FFT2DConan(ConanFile):
    name = "fft2d"
    revision = "20161228"
    version = revision
    #url
    author = "ooura@kurims.kyoto-u.ac.jp"
    homepage = "http://www.kurims.kyoto-u.ac.jp/~ooura/fft.html"
    description = "General Purpose FFT (Fast Fourier/Cosine/Sine Transform)"
    license = "MIT"
    topics = ("conan", "abseil", "abseil-cpp", "google", "common-libraries")
    exports = ["LICENSE"]
    exports_sources = "*"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("LICENSE", dst="licenses")
        self.copy("*.a", dst="lib", src=".", keep_path=False)

