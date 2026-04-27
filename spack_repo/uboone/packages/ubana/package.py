# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *

from spack_repo.fnal_art.packages.fnal_github_package.package import *

class Ubana(CMakePackage, FnalGithubPackage):
    """MicroBooNE analysis modules."""

    homepage = "https://github.com/uboone/ubana"
    url = "https://github.com/uboone/ubana/archive/refs/tags/v10_20_05.tar.gz"
    git = "https://github.com/uboone/ubana.git"

    license("Apache-2.0")

    version("develop", branch="develop")
    version("10.20.05", sha256="019e329075b3c8d5616cf3ce1d84ff663a4441ed42240066459612c2dd655e6e")

    depends_on("cmake@3.20:", type="build")
    depends_on("cxx", type="build")
    depends_on("cetmodules", type="build")
    depends_on("nufinder", type="build")
    depends_on("larfinder", type="build")

    depends_on("eigen", type=("build", "link", "run"))
    depends_on("larana", type=("build", "link", "run"))
    depends_on("larpandora", type=("build", "link", "run"))
    depends_on("ubcv", type=("build", "link", "run"))
    depends_on("ubraw", type=("build", "link", "run"))

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
            '--presets', 'default',
        ] 
        return args


    def url_for_version(self, version):
        return f"https://github.com/uboone/ubana/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
