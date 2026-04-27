# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *

from spack_repo.fnal_art.packages.fnal_github_package.package import *

class Ubevt(CMakePackage, FnalGithubPackage):
    """MicroBooNE event-level reconstruction and utility plugins."""

    homepage = "https://github.com/uboone/ubevt"
    url = "https://github.com/uboone/ubevt/archive/refs/tags/v10_20_02.tar.gz"
    git = "https://github.com/uboone/ubevt.git"

    license("Apache-2.0")

    version("develop", branch="develop")
    version("10.20.02", sha256="64b19bd32a34a0fd81ac0f62cd679333cd261d239a810f9d9ff59731c2c748fc")

    depends_on("cmake@3.20:", type="build")
    depends_on("cxx", type="build")
    depends_on("cetmodules", type="build")
    depends_on("nufinder", type="build")
    depends_on("larfinder", type="build")

    depends_on("art", type=("build", "link", "run"))
    depends_on("art-root-io", type=("build", "link", "run"))
    depends_on("canvas", type=("build", "link", "run"))
    depends_on("cetlib", type=("build", "link", "run"))
    depends_on("cetlib-except", type=("build", "link", "run"))
    depends_on("fhicl-cpp", type=("build", "link", "run"))
    depends_on("gallery", type=("build", "link", "run"))
    depends_on("gsl", type=("build", "link", "run"))
    depends_on("ifdh-art", type=("build", "link", "run"))
    depends_on("larcore", type=("build", "link", "run"))
    depends_on("larcorealg", type=("build", "link", "run"))
    depends_on("larcoreobj", type=("build", "link", "run"))
    depends_on("lardata", type=("build", "link", "run"))
    depends_on("lardataalg", type=("build", "link", "run"))
    depends_on("lardataobj", type=("build", "link", "run"))
    depends_on("larevt", type=("build", "link", "run"))
    depends_on("messagefacility", type=("build", "link", "run"))
    depends_on("nurandom", type=("build", "link", "run"))
    depends_on("root", type=("build", "link", "run"))
    depends_on("ubcore", type=("build", "link", "run"))

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


    def url_for_version(self, version):
        return f"https://github.com/uboone/ubevt/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
