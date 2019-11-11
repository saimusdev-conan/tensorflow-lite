from conans import ConanFile, AutoToolsBuildEnvironment, tools
from conans.errors import ConanInvalidConfiguration
from conans.model.version import Version


class FarmHashConan(ConanFile):
    name = "farmhash"
    revision = "816a4ae622e964763ca0862d9dbd19324a1eaf45"
    version = revision[:7]
    #url
    author = "Abseil <abseil-io@googlegroups.com>"
    homepage = "https://github.com/google/farmhash"
    description = "FarmHash, a family of hash functions."
    license = "MIT"
    topics = ("conan", "farmhash", "hash", "google", "common-libraries")
    exports = ["COPYING"]
    exports_sources = "*" # Almost everything is needed
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"

    def build(self):
        autotools = AutoToolsBuildEnvironment(self)
        tools.replace_in_file("configure", "am__api_version='1.14'", "am__api_version='1.15'") # to avoid incompatibility issue
        autotools.configure()
        autotools.make(target="all check")
        autotools.install()

    def package(self):
        self.copy("COPYING", dst="licenses")

