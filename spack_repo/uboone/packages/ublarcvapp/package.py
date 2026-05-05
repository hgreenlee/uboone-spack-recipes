# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Ublarcvapp(CMakePackage):
    """UB-specific LArCV applications and reconstruction utilities."""

    homepage = "https://github.com/LArbys/ublarcvapp"
    git = "https://github.com/LArbys/ublarcvapp.git"

    license("UNKNOWN")

    version("2.me.06.03.prod.01", commit="752dc2316cba79789e23420d9897d2ff5299073a")

    depends_on("cmake@3.10:", type="build")
    depends_on("gmake", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("root", type=("build", "link", "run"))
    depends_on("larcv", type=("build", "link", "run"))
    depends_on("larlite", type=("build", "link", "run"))
    depends_on("geo2d", type=("build", "link", "run"))
    depends_on("opencv", type=("build", "link", "run"))
    depends_on("eigen", type=("build", "link", "run"))
    depends_on("boost +graph +program_options", type=("build", "link", "run"))
    depends_on("cilantro", type=("build", "link", "run"))

    def setup_build_environment(self, env):
        larcv_prefix = self.spec["larcv"].prefix
        larlite_prefix = self.spec["larlite"].prefix
        geo2d_prefix = self.spec["geo2d"].prefix

        env.set("LARCV_BASEDIR", larcv_prefix)
        env.set("LARCV_LIBDIR", join_path(larcv_prefix, "build", "lib"))

        env.set("LARLITE_BASEDIR", larlite_prefix)
        env.set("LARLITE_LIBDIR", join_path(larlite_prefix, "lib"))
        env.set("LARLITE_INCDIR", join_path(larlite_prefix, "build", "installed", "include"))

        env.set("GEO2D_BASEDIR", geo2d_prefix)
        env.set("GEO2D_LIBDIR", join_path(geo2d_prefix, "lib"))
        env.set("GEO2D_INCDIR", geo2d_prefix)

        env.set("OPENCV_LIBDIR", self.spec["opencv"].prefix.lib)

        # LArOpenCV libraries are produced in larlite; ublarcvapp expects these names.
        env.set("LAROPENCV_BASEDIR", larlite_prefix)

        env.set("CILANTRO_LIB_DIR", join_path(self.spec["cilantro"].prefix, "lib", "cmake", "cilantro"))

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.set("UBLARCVAPP_BASEDIR", self.prefix)
        env.set("UBLARCVAPP_LIBDIR", join_path(self.prefix, "lib"))
        env.set("UBLARCVAPP_INCDIR", join_path(self.prefix, "include"))

    def setup_run_environment(self, env):
        env.set("UBLARCVAPP_BASEDIR", self.prefix)
        env.set("UBLARCVAPP_LIBDIR", join_path(self.prefix, "lib"))
        env.set("UBLARCVAPP_INCDIR", join_path(self.prefix, "include"))

        env.prepend_path("LD_LIBRARY_PATH", join_path(self.prefix, "lib"))
        env.prepend_path("PYTHONPATH", join_path(self.prefix, "python"))

    def cmake_args(self):
        args = [
            self.define("USE_OPENCV", True),
        ]
        return args