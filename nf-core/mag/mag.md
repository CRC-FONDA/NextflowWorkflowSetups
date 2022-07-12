# Input data for mag

This information was provided by [Jonathan Bader](https://github.com/jonathanbader). For more information see [jonathanbader/mag](https://github.com/jonathanbader/mag).

## Download
The text file provided contains the locations of input data that can be used for the mag workflow. The input data can be obtained with tools like `wget`:

    wget -i input_mag.txt

## Usage
`csv` files of the required format are provided within the `example_inputs` directory. These can be used as input for the mag workflow.

    nextflow run nf-core/mag -profile test_full --input design_1.csv
