# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Gclib(Package):
    """Genomic C++ library of reusable code for bioinformatics projects

    This is an eclectic collection of basic C++ code (functions, classes,
    templates) which is shared between a few of my bioinformatics
    projects. The main idea was to provide a core collection of data
    structures, trying to avoid unnecessary code dependencies of other
    heavy libraries, while minimizing build time."""

    homepage = "https://github.com/gpertea/gclib"
    url = "https://github.com/gpertea/gclib/archive/refs/tags/v0.12.7.tar.gz"

    version("0.12.7", sha256="9c74db64c4ee1fb93a6c02fa227258baafc337303f26ce3ba0cf37dfc1ba687f")

    def install(self, spec, prefix):
        mkdirp(prefix.include)
        install("*.h", prefix.include)
        install("*.hh", prefix.include)
        install("*.cpp", prefix.include)
