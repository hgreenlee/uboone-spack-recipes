# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *

from spack_repo.fnal_art.packages.fnal_github_package.package import *

class Ubsim(CMakePackage, FnalGithubPackage):
    """MicroBooNE detector simulation and event-weighting modules."""

    homepage = "https://github.com/uboone/ubsim"
    url = "https://github.com/uboone/ubsim/archive/refs/tags/v10_20_05.tar.gz"
    git = "https://github.com/uboone/ubsim.git"

    license("Apache-2.0")

    version("develop", branch="develop")
    version("10.20.05", sha256="07eed80f5e28b44decc30a402300a2f6af8d4328a36335ef2c89208dfc3201d3")

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
    depends_on("dk2nudata", type=("build", "link", "run"))
    depends_on("geant4reweight", type=("build", "link", "run"))
    depends_on("genie", type=("build", "link", "run"))
    depends_on("ifdh-art", type=("build", "link", "run"))
    depends_on("larcore", type=("build", "link", "run"))
    depends_on("larcorealg", type=("build", "link", "run"))
    depends_on("larsim", type=("build", "link", "run"))
    depends_on("larwirecell", type=("build", "link", "run"))
    depends_on("libxml2", type=("build", "link", "run"))
    depends_on("log4cpp", type=("build", "link", "run"))
    depends_on("messagefacility", type=("build", "link", "run"))
    depends_on("nugen", type=("build", "link", "run"))
    depends_on("nurandom", type=("build", "link", "run"))
    depends_on("nusimdata", type=("build", "link", "run"))
    depends_on("nutools", type=("build", "link", "run"))
    depends_on("ppfx", type=("build", "link", "run"))
    depends_on("root", type=("build", "link", "run"))
    depends_on("ubevt", type=("build", "link", "run"))

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
        return f"https://github.com/uboone/ubsim/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
