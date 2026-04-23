# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class UboonedaqDatatypes(CMakePackage):
    """MicroBooNE DAQ data format structures and utility executables."""

    homepage = "https://github.com/uboone/uboonedaq_datatypes"
    url = "https://github.com/uboone/uboonedaq_datatypes/archive/refs/tags/v09_78_03cm1.tar.gz"
    git = "https://github.com/uboone/uboonedaq_datatypes.git"

    license("UNKNOWN")

    version("master", branch="master")
    version("09.78.03cm1", sha256="f5789f0aee389a14823575cb0178d1a78fbadae6aa59bbc00408e7885f9923fa")

    depends_on("cmake", type="build")
    depends_on("cetmodules", type="build")
    depends_on("cxx", type="build")
    depends_on("boost", type=("build", "link", "run"))
    depends_on("openssl", type=("build", "link", "run"))

    def url_for_version(self, version):
        return f"https://github.com/uboone/uboonedaq_datatypes/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
