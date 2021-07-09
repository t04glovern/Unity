from conans import ConanFile, CMake, tools
import os

class UnityConan(ConanFile):
    name = "Unity"
    version = "2.5.2"
    url = "https://github.com/t04glovern/Unity"
    description = "Simple Unit Testing for C"
    topics = ("testing")
    settings = "os", "compiler", "build_type", "arch"
    no_copy_source = False
    generators = "cmake"

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_TESTS"] = "OFF"
        cmake.configure(source_folder=self._source_subfolder)
        return 

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self._source_subfolder)
        cmake.build()

    def package(self):
        self.copy(pattern="*", dst=".", src=self._source_subfolder, keep_path=True, symlinks=True)

    def package_info(self):
        self.cpp_info.libs = ["Unity"]
