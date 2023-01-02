# gaussian-minimizer-density

This is associated with the manuscript "On minimizers and convolutional filters: a partial justification for the effectiveness of CNNs in categorical sequence analysis"
by Yun William Yu. https://arxiv.org/abs/2111.08452

In the manuscript, Figures 2 and 3 were experiments run comparing the density of minimizers generated via uniform random hash
functions vs random spherical Gaussian convolutions. These experiments can be rerun using the Gaussian_minimizer_density.ipynb colab.

For Figure 3, we used real data from the Telomere to Telomere project. https://github.com/marbl/CHM13
- To download those files, simply run download_t2t.sh.
- To extract the telomeres from the chromosomes into a JSON file, run extract_telomeres.py using Python 3.
- Currently, the Colab is set to download the extracted telomeres from this Github repo, but you can of course modify that to use your own extracted telomeres.
