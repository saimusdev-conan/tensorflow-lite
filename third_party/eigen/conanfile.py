from conans import ConanFile
import os

class EigenConan(ConanFile):
    name = "eigen"
    #version = "3.3.7"
    revision = "049af2f563313fab3ee56176995cf4bcfeaac626"
    version = revision[:7]
    #url
    #author = "Conan Community"
    homepage = "http://eigen.tuxfamily.org"
    description = "Eigen is a C++ template library for linear algebra: matrices, vectors, \
                   numerical solvers, and related algorithms."
    license = "MPL-2.0"
    topics = ("eigen", "algebra", "linear-algebra", "vector", "numerical")
    exports = "LICENSE"
    exports_sources = [ "CMakeLists.txt", "cmake", "eigen3.pc.in", "Eigen/*", "unsupported/*" ]
    generators = "cmake"
    build_subfolder = "build"
    source_subfolder = "."
    options = {"header_only": [True, False]}
    default_options = {"header_only": True}

    def package(self):
        unsupported_folder = os.path.join(self.package_folder, "include", "eigen3", "unsupported", "Eigen")
        eigen_folder = os.path.join(self.package_folder, "include", "eigen3", "Eigen")
        self.copy("COPYING.*", dst="licenses", src=self.source_subfolder)
        self.copy("*", dst=eigen_folder, src=os.path.join(self.source_subfolder, "Eigen"))
        self.copy("*", dst=unsupported_folder, src=os.path.join(self.source_subfolder, "unsupported", "Eigen"))
        self.copy("signature_of_eigen3_matrix_library", dst=os.path.join("include", "eigen3"), src=self.source_subfolder)

    def package_id(self):
        self.info.header_only()

    def package_info(self):
        self.cpp_info.name = "Eigen3"
        self.cpp_info.includedirs = ['include/eigen3', 'include/unsupported']

