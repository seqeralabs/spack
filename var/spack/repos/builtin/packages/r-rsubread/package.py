# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsubread(RPackage):
    """Mapping, quantification and variant analysis of sequencing data"""

    homepage = "https://bioconductor.org/packages/3.16/bioc/html/Rsubread.html"
    url = "https://bioconductor.org/packages/release/bioc/src/contrib/Rsubread_2.14.2.tar.gz"

    bioc = "rsubread"

    depends_on("r-matrix")
    depends_on("zlib-api")

    version("2.14.2", sha256="ac8be0fad0eb2743443e3a60a9a94eec78c746638aaccca70e7166d034dcebb5")
    version("2.16.0", commit="62b92c9ed3fc2be89ed9f29e3db1809d1e115dbc")
