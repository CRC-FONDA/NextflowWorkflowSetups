# Input data for atacseq

This information was provided by [Jonathan Bader](https://github.com/jonathanbader). For more information see [jonathanbader/atacseq](https://github.com/jonathanbader/atacseq).

## Download
The text files provided contain the locations of input data that can be used for the atacseq workflow. The input data can be obtained with tools like `wget`:

    wget -i inputs_atac_1.txt
    wget -i inputs_atac_2.txt
    wget -i inputs_atac_3.txt
    wget -i inputs_atac_4.txt
    wget -i inputs_atac_5.txt

## Usage
`csv` files of the required format are provided within the `example_inputs` directory. These can be used as input for the atacseq workflow.

    nextflow run nf-core/atacseq -profile test_full --input 1.csv
