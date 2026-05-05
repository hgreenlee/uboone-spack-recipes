# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *

from spack_repo.fnal_art.packages.fnal_github_package.package import *

class Ubcv(CMakePackage, FnalGithubPackage):
    """MicroBooNE computer vision reconstruction modules."""

    homepage = "https://github.com/uboone/ubcv"
    url = "https://github.com/uboone/ubcv/archive/refs/tags/v10_20_05.tar.gz"
    git = "https://github.com/uboone/ubcv.git"

    license("Apache-2.0")

    version("develop", branch="develop")
    version("10.20.05", sha256="eed26a67ae6586f555d47ffad2710176c844c4532c1ef5af4ca4b98a2a3f2920")

    depends_on("cmake@3.20:", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cetmodules", type="build")
    depends_on("nufinder", type="build")
    depends_on("larfinder", type="build")

    depends_on("larevt", type=("build", "link", "run"))
    depends_on("larlite", type=("build", "link", "run"))
    depends_on("larcv", type=("build", "link", "run"))
    depends_on("ublarcvapp", type=("build", "link", "run"))
    depends_on("nusimdata", type=("build", "link", "run"))
    depends_on("ubevt", type=("build", "link", "run"))
    depends_on("ubreco", type=("build", "link", "run"))
    depends_on("ubsim", type=("build", "link", "run"))

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    @cmake_preset
    def cmake_args(self):
        args = [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            self.define("CMAKE_MODULE_PATH", "%s/Modules;%s/Modules" %
                       (self.spec['nufinder'].prefix, self.spec['larfinder'].prefix)),
        ] 
        return args

    def setup_build_environment(self, env):
        env.set("LARCV_LIBDIR", join_path(self.spec['larcv'].prefix, "build", "installed", "lib"))
        env.set("LARLITE_LIBDIR", join_path(self.spec['larlite'].prefix, "build", "installed", "lib"))

    def url_for_version(self, version):
        return f"https://github.com/uboone/ubcv/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
