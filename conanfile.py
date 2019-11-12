from os import getcwd
from conans import ConanFile, tools, AutoToolsBuildEnvironment


class TFLiteConan(ConanFile):
    # Basic info
    name = "tensorflow-lite"
    revision = tools.load("revision")
    version = revision[:7]
    repo_url = "https://github.com/tensorflow/tensorflow.git"

    # Other package details
    description = "https://www.tensorflow.org/"
    url = "https://github.com/saimusdev/tflite-conan"
    homepage = "The core open source library to help you develop and train ML models"
    author = "saimusdev"
    license = "Apache-2.0"

    exports = [ "LICENSE.md", "revision" ]

    # Flags & other defines (INCLUDES; CXXFLAGS, LIBS,...)
    conan_makefile_defines = "conandefines.mak"
    exports_sources = [ conan_makefile_defines, "conanbuildinfo.mak" ]

    settings = "os", "arch", "compiler", "build_type"
    options = { "shared": [True, False], "fPIC": [True, False] }
    default_options = { "shared": True, "fPIC": True }
    source_subfolder = "tensorflow"
    build_subfolder = "tensorflow/tensorflow/lite/tools/make" # relative path
    generators = "make"

    def requirements(self):
        self.requires("abseil/43ef214@saimusdev-conan/testing")
        self.requires("eigen/049af2f@saimusdev-conan/testing")
        self.requires("farmhash/816a4ae@saimusdev-conan/testing")
        self.requires("fft2d/20161228@saimusdev-conan/testing")
        self.requires("flatbuffers/1.11.0@saimusdev-conan/testing")
        self.requires("gemmlowp/12fed0c@saimusdev-conan/testing")

    def config_options(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC

    def source(self):
        git = tools.Git(folder=self.source_subfolder)
        git.clone(self.repo_url)
        with tools.chdir(self.source_subfolder):
            self.run("git checkout %s" % (self.version))

    def build(self):
        build = AutoToolsBuildEnvironment(self)
        tools.replace_in_file("%s/Makefile" % self.build_subfolder, 
            "LIB_NAME := libtensorflow-lite.a\n",
            "LIB_NAME := libtensorflow-lite.a\n\n# Include Conan's flags\ninclude %s\n" % self.conan_makefile_defines)
        build_target = "micro"
        build.make(target="%s -f %s/Makefile -C %s" % (
            build_target, 
            self.build_subfolder,
            getcwd()))

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)
        self.copy(pattern="*.so*", dst="lib", src=self.source_subfolder, keep_path=False, symlinks=True)

    def package_info(self):
        self.cpp_info.libs = ["tensorflow"]
