# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class UboonedaqDatatypes(CMakePackage):
    """MicroBooNE DAQ data format structures and utility executables."""

    homepage = "https://github.com/uboone/uboonedaq_datatypes"
    url = "https://github.com/uboone/uboonedaq_datatypes/archive/refs/tags/v6_22_07.tar.gz"
    git = "https://github.com/uboone/uboonedaq_datatypes.git"

    license("UNKNOWN")

    version("master", branch="master")
    version("6.22.07", sha256="95a722920a24b96d7fcc46d6a542df19a064b206f543b4ed270879d025655e2d")

    depends_on("cmake", type="build")
    depends_on("cetmodules", type="build")
    depends_on("cxx", type="build")
    depends_on("boost", type=("build", "link", "run"))
    depends_on("openssl", type=("build", "link", "run"))

    def url_for_version(self, version):
        return f"https://github.com/uboone/uboonedaq_datatypes/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
