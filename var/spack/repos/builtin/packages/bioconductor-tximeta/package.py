# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class BioconductorTximeta(RPackage):
    """Transcript Quantification Import with Automatic Metadata

    Transcript quantification import from Salmon and alevin with automatic
    attachment of transcript ranges and release information, and other associated
    metadata. De novo transcriptomes can be linked to the appropriate sources with
    linkedTxomes and shared for computational reproducibility."""

    homepage = "https://bioconductor.org/packages/release/bioc/html/tximeta.html"
    url = "https://bioconductor.org/packages/release/bioc/src/contrib/tximeta_1.18.0.tar.gz"

    bioc = "tximeta"

    version("1.18.0", sha256="e12f809029b99b2b9e0836fa3adc64849a546241e9e10480612848e7dcb5b50d")

    depends_on("r",type=("build", "run"))
    depends_on("r-annotationdbi")
    depends_on("r-annotationhub")
    depends_on("r-biocfilecache")
    depends_on("r-biostrings")
    depends_on("r-ensembldb")
    depends_on("r-genomeinfodb")
    depends_on("r-genomicfeatures")
    depends_on("r-genomicranges")
    depends_on("r-iranges")
    depends_on("r-s4vectors")
    depends_on("r-summarizedexperiment")
    depends_on("r-tximport")
    depends_on("r-jsonlite")
    depends_on("r-matrix")
    depends_on("r-tibble")
