import os
from conans import ConanFile


class GemmlowpConan(ConanFile):
    name = "gemmlowp"
    revision = "12fed0cd7cfcd9e169bf1925bc3a7a58725fdcc3"
    version = revision[:7]
    #url
    homepage = "https://github.com/google/gemmlowp"
    description = "gemmlowp: a small self-contained low-precision GEMM library"
    license = "Apache-2.0"
    topics = ("conan", "gemmlowp", "google", "common-libraries")
    exports = ["LICENSE"]
    exports_sources = ["public/*"]
    source_subfolder = "."
    options = {"header_only": [True, False]}
    default_options = {"header_only": True}

    def package(self):
        header_folder = os.path.join(self.package_folder, "include", "gemmlowp")
        self.copy("LICENSE", dst="licenses", src=self.source_subfolder)
        self.copy("*", dst=header_folder, src=os.path.join(self.source_subfolder, "public"))

    def package_id(self):
        self.info.header_only()

    def package_info(self):
        self.cpp_info.name = "Eigen3"
        self.cpp_info.includedirs = ['include/eigen3', 'include/unsupported']

