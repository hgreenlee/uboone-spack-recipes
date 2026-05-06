# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *

from spack_repo.fnal_art.packages.fnal_github_package.package import *

class UboonedaqDatatypes(CMakePackage, FnalGithubPackage):
    """MicroBooNE DAQ data format structures and utility executables."""

    homepage = "https://github.com/uboone/uboonedaq_datatypes"
    url = "https://github.com/uboone/uboonedaq_datatypes/archive/refs/tags/v6_22_07.tar.gz"
    git = "https://github.com/uboone/uboonedaq_datatypes.git"

    license("UNKNOWN")

    version("master", branch="master")
    version("6.22.07", sha256="95a722920a24b96d7fcc46d6a542df19a064b206f543b4ed270879d025655e2d")

    depends_on("cmake", type="build")
    depends_on("cetmodules", type="build")
    depends_on("nufinder", type="build")
    depends_on("larfinder", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("boost", type=("build", "link", "run"))
    depends_on("openssl", type=("build", "link", "run"))

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )


    def patch(self):
        filter_file("find_package\(OpenMP REQUIRED\)"
                "find_package(OpenMP REQUIRED EXPORT)",
                "CMakeLists.txt"
                )


    def cmake_args(self):
        args = [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            self.define("CMAKE_MODULE_PATH", "%s/Modules;%s/Modules" %
                       (self.spec['nufinder'].prefix, self.spec['larfinder'].prefix)),
        ] 
        return args

    def setup_run_environment(self, env):
        env.set("UBOONEDAQ_DATATYPES_BASEDIR", self.prefix)
        env.set("UBOONEDAQ_DATATYPES_INCDIR", join_path(self.prefix, "include"))
        env.set("UBOONEDAQ_DATATYPES_LIBDIR", join_path(self.prefix, "lib"))


    def url_for_version(self, version):
        return f"https://github.com/uboone/uboonedaq_datatypes/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
