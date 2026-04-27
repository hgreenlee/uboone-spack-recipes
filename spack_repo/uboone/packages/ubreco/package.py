# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Ubreco(CMakePackage):
    """MicroBooNE reconstruction modules."""

    homepage = "https://github.com/uboone/ubreco"
    url = "https://github.com/uboone/ubreco/archive/refs/tags/v10_20_05.tar.gz"
    git = "https://github.com/uboone/ubreco.git"

    license("Apache-2.0")

    version("develop", branch="develop")
    version("10.20.05", sha256="b27408373a425582cae082ab43a1a66e343a8dc95ef188689935c002581e6366")

    depends_on("cmake@3.20:", type="build")
    depends_on("cxx", type="build")
    depends_on("cetmodules", type="build")
    depends_on("nufinder", type="build")
    depends_on("larfinder", type="build")

    depends_on("eigen", type=("build", "link", "run"))
    depends_on("larreco", type=("build", "link", "run"))
    depends_on("larpandora", type=("build", "link", "run"))
    depends_on("nugen", type=("build", "link", "run"))
    depends_on("nutools", type=("build", "link", "run"))
    depends_on("ubsim", type=("build", "link", "run"))

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    def patch(self):
        files = [ "ubreco/DetectorSystematics/WireModifier_module.cc",
                "ubreco/MichelReco/Algo/PhotonFinder.cxx",
                "ubreco/MichelReco/Fmwk/ClusterVectorCalculator.cxx",
                "ubreco/MichelReco/Algo/ConeHitFinder.cxx"
                ]
        filter_file("isnan", "std::isnan", *files)
        filter_file("cet_cmake_env\(\)",
                'cet_cmake_env()\nset(ubreco_FW_DIR, "scripts")',
                "CMakeLists.txt")
        cmakefiles = [ "ubreco/BlipReco/CMakeLists.txt",
                "ubreco/MicroBooNEPandora/scripts/CMakeLists.txt"]
        filter_file("install_fw\(LIST ${txt_file}\)",
                "install(FILES ${txt_file} DESTINATION ${ubreco_FW_DIR})",
                *cmakefiles)

    def cmake_args(self):
        args = [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            self.define("CMAKE_MODULE_PATH", "%s/Modules;%s/Modules" %
                       (self.spec['nufinder'].prefix, self.spec['larfinder'].prefix)),
        ] 
        return args


    def url_for_version(self, version):
        return f"https://github.com/uboone/ubreco/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"

    def cmake_args(self):
        args = []
        return args

