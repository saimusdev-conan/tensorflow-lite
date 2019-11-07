import sys
from os import getcwd
from multiprocessing import cpu_count
from conans import ConanFile, tools, AutoToolsBuildEnvironment


class TFLiteConan(ConanFile):
    # Basic info
    name = "tensorflow-lite"
    version = "2.0.0"
    repo_url = "https://github.com/tensorflow/tensorflow.git"

    # Other package details
    description = "https://www.tensorflow.org/"
    url = "https://github.com/saimusdev/tflite-conan"
    homepage = "The core open source library to help you develop and train ML models"
    author = "saimusdev"
    license = "Apache-2.0"

    # Conan build process settings
    exports = ["LICENSE.md"]
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": True, "fPIC": True}
    source_subfolder = "tensorflow"
    build_subfolder = "lite/tools/make" # relative path
    generators = "make"

    def build_requirements(self):
        pass

    def config_options(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC

    def source(self):
        git = tools.Git()
        git.clone(self.repo_url)
        git.checkout(self.revision)

    def build(self):
        with tools.chdir(self.source_subfolder):
            #with tools.chdir(self.build_subfolder):
                #self.run("./download_dependencies.sh")
            env_build = AutoToolsBuildEnvironment(self)
            env_build.fpic = True
            #env_build.libs.append("pthread")
            env_build.defines.append("BUILD_WITH_NNAPI=false")
            env_build.defines.append("BUILD_WITH_MMAP=false")
            build_target = "all" # "micro"?
            env_build.make(target="%s -f %s/Makefile -C %s" % (
                build_target, 
                self.build_subfolder,
                getcwd()))

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)
        self.copy(pattern="*.so*", dst="lib", src=self.source_subfolder, keep_path=False, symlinks=True)

    def package_info(self):
        self.cpp_info.libs = ["tensorflow"]
