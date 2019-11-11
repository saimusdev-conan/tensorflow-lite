from conans import ConanFile, tools
import os
from glob import glob


class EigenConan(ConanFile):
    name = "eigen"
    version = "3.3.7"
    repo_revision = "049af2f56331"
    homepage = "http://eigen.tuxfamily.org"
    description = "Eigen is a C++ template library for linear algebra: matrices, vectors, \
                   numerical solvers, and related algorithms."
    license = "MPL-2.0"
    author = "Conan Community"
    topics = ("eigen", "algebra", "linear-algebra", "vector", "numerical")
    exports = "LICENSE"
    exports_sources = [ "CMakeLists.txt", "cmake", "eigen3.pc.in", "Eigen/*", "unsupported/*" ]

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def package(self):
        unsupported_folder = os.path.join(self.package_folder, "include", "eigen3", "unsupported", "Eigen")
        eigen_folder = os.path.join(self.package_folder, "include", "eigen3", "Eigen")
        self.copy("COPYING.*", dst="licenses", src=self._source_subfolder)
        self.copy("*", dst=eigen_folder, src=os.path.join(self._source_subfolder, "Eigen"))
        self.copy("*", dst=unsupported_folder, src=os.path.join(self._source_subfolder, "unsupported", "Eigen"))
        self.copy("signature_of_eigen3_matrix_library", dst=os.path.join("include", "eigen3"), src=self._source_subfolder)
        self.copy("FindEigen3.cmake")
        os.remove(os.path.join(eigen_folder, "CMakeLists.txt"))
        os.remove(os.path.join(unsupported_folder, "CMakeLists.txt"))
        os.remove(os.path.join(unsupported_folder, "CXX11", "CMakeLists.txt"))
        os.remove(os.path.join(unsupported_folder, "CXX11", "src", "Tensor", "README.md"))
        os.remove(os.path.join(unsupported_folder, "src", "EulerAngles", "CMakeLists.txt"))
        os.rename(os.path.join(unsupported_folder, "src", "LevenbergMarquardt", "CopyrightMINPACK.txt"),
                               os.path.join(self.package_folder, "licenses", "CopyrightMINPACK.txt"))

    def package_id(self):
        self.info.header_only()

    def package_info(self):
        self.cpp_info.name = "Eigen3"
        self.cpp_info.includedirs = ['include/eigen3', 'include/unsupported']

