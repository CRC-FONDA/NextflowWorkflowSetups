# Input data for eager

This information was provided by [Jonathan Bader](https://github.com/jonathanbader). For more information see [jonathanbader/eager](https://github.com/jonathanbader/eager).

## Download
The text file provided contains the locations of input data that can be used for the eager workflow. The input data can be obtained with tools like `wget`:

    wget -i inputs_eager_1.txt

## Usage
`tsv` files of the required format are provided within the `example_inputs` directory. These can be used as input for the eager workflow.

    nextflow run nf-core/eager -profile test_full --input 1.tsv
