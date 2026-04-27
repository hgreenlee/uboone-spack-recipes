# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Ubraw(CMakePackage):
    """MicroBooNE raw data handling and DAQ input modules."""

    homepage = "https://github.com/uboone/ubraw"
    url = "https://github.com/uboone/ubraw/archive/refs/tags/v10_20_02.tar.gz"
    git = "https://github.com/uboone/ubraw.git"

    license("Apache-2.0")

    version("develop", branch="develop")
    version("10.20.02", sha256="85647ddeedbe3ff444ca1477606d42f0823068312c05bb6126d2087202382a09")

    depends_on("cmake@3.20:", type="build")
    depends_on("cxx", type="build")
    depends_on("cetmodules", type="build")
    depends_on("nufinder", type="build")
    depends_on("larfinder", type="build")

    depends_on("art", type=("build", "link", "run"))
    depends_on("art-root-io", type=("build", "link", "run"))
    depends_on("boost", type=("build", "link", "run"))
    depends_on("curl", type=("build", "link", "run"))
    depends_on("fhicl-cpp", type=("build", "link", "run"))
    depends_on("ifdh-art", type=("build", "link", "run"))
    depends_on("lardata", type=("build", "link", "run"))
    depends_on("lardataobj", type=("build", "link", "run"))
    depends_on("larcore", type=("build", "link", "run"))
    depends_on("larcoreobj", type=("build", "link", "run"))
    depends_on("larevt", type=("build", "link", "run"))
    depends_on("libwda", type=("build", "link", "run"))
    depends_on("messagefacility", type=("build", "link", "run"))
    depends_on("postgresql", type=("build", "link", "run"))
    depends_on("root", type=("build", "link", "run"))
    depends_on("sqlite", type=("build", "link", "run"))
    depends_on("ubcore", type=("build", "link", "run"))
    depends_on("uboonedaq-datatypes", type=("build", "link", "run"))

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    def cmake_args(self):
        args = [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            self.define("CMAKE_MODULE_PATH", "%s/Modules;%s/Modules" %
                       (self.spec['nufinder'].prefix, self.spec['larfinder'].prefix)),
        ] 
        return args

    def url_for_version(self, version):
        return f"https://github.com/uboone/ubraw/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
