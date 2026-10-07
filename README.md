GENOMIC VARIANT ANALYZER
=========================

Overview
--------
This project is a small bioinformatics project developed as part of my learning journey in Python and computational biology.

The goal is to build a simple Genomic Variant Analyzer that reads variant information from a VCF (Variant Call Format) file, performs basic quality control and filtering, summarizes the variants, and creates visualizations.

This project demonstrates how Python can be used to perform common bioinformatics data-analysis tasks.


Project Objectives
------------------
The main objectives of this project are to:

- Read genomic variant data from a VCF file
- Explore and summarize variant data
- Calculate basic statistics
- Analyze variant quality scores
- Identify high-quality variants
- Categorize variants by nucleotide change
- Analyze variants by chromosome
- Create visualizations
- Export filtered variants for further analysis


Dataset
-------
For this learning project, a small practice VCF dataset was created.

The dataset contains:

- Chromosome
- Position
- Variant ID
- Reference allele (REF)
- Alternative allele (ALT)
- Quality score (QUAL)
- Filter status (FILTER)

Example:

CHROM  POS    ID    REF  ALT  QUAL  FILTER
chr1   10583  rs1   G    A    99    PASS
chr1   10611  rs2   C    T    85    PASS
chr1   10616  rs3   G    A    45    LowQual

The dataset contains 15 variants across chromosomes 1-4.


Technologies Used
-----------------
- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- VCF data format

Python Libraries:

    import pandas as pd
    import matplotlib.pyplot as plt


Project Workflow
----------------

VCF File
   |
   v
Load Variant Data
   |
   v
Explore Dataset
   |
   v
Calculate Summary Statistics
   |
   v
Analyze Quality Scores
   |
   v
Identify Variant Types
   |
   v
Filter High-Quality Variants
   |
   v
Create Visualizations
   |
   v
Export Results


Analysis Performed
------------------

1. Load the VCF File
--------------------
The VCF file is loaded into a Pandas DataFrame.

    variants = pd.read_csv(
        "variants.vcf",
        sep="\t",
        comment="#",
        names=[
            "CHROM",
            "POS",
            "ID",
            "REF",
            "ALT",
            "QUAL",
            "FILTER"
        ]
    )


2. Explore the Dataset
----------------------
The dataset was inspected using Pandas functions such as:

    variants.head()
    variants.shape
    variants.info()
    variants.describe()

The dataset contains 15 variants and 7 columns.


3. Analyze Variant Quality
--------------------------
The QUAL column was used to examine the quality of each variant.

Summary statistics:

- Mean quality score: 76.67
- Median quality score: 88
- Minimum quality score: 28
- Maximum quality score: 99

A histogram was created to visualize the distribution of variant quality scores.


4. Analyze Variants by Chromosome
---------------------------------
The number of variants on each chromosome was calculated.

    Chromosome    Number of Variants
    chr1          5
    chr2          4
    chr3          4
    chr4          2


5. Identify Variant Types
-------------------------
A new column was created to represent nucleotide changes.

Examples:

    G>A
    C>T
    T>C
    A>G

The variant type was generated using:

    variants["variant_type"] = (
        variants["REF"] + ">" + variants["ALT"]
    )

The most common variant types in this dataset were:

- G>A
- C>T
- T>C
- A>G


6. Filter High-Quality Variants
--------------------------------
High-quality variants were defined as:

- FILTER == "PASS"
- QUAL >= 70

The filtering was performed using:

    high_quality = variants[
        (variants["FILTER"] == "PASS") &
        (variants["QUAL"] >= 70)
    ].copy()

This produced 11 high-quality variants.


Results
-------
The analysis produced the following summary:

    Total variants:        15
    PASS variants:         12
    High-quality variants: 11

    Mean QUAL:             76.67
    Median QUAL:           88
    Minimum QUAL:          28
    Maximum QUAL:          99

The filtered high-quality variants were exported to:

    filtered_variants.csv


Visualizations
--------------
The project creates several plots.

1. Variant Distribution by Chromosome
-------------------------------------
Shows how many variants are present on each chromosome.

    variants_by_chromosome.png


2. Quality Score Distribution
-----------------------------
Shows the distribution of variant quality scores.

    quality_distribution.png


3. Variant Type Distribution
-----------------------------
Shows the frequency of different nucleotide substitutions.

    variant_types.png


Project Structure
-----------------

    01-variant-analysis/
    |
    +-- variants.vcf
    +-- day07_variant_analysis.ipynb
    +-- variant_analyzer.py
    +-- filtered_variants.csv
    +-- variants_by_chromosome.png
    +-- quality_distribution.png
    +-- variant_types.png
    +-- README.md


How to Run the Project
----------------------

1. Clone the repository

    git clone YOUR_GITHUB_REPOSITORY_URL

2. Navigate to the project

    cd 01-variant-analysis

3. Install the required libraries

    pip install pandas matplotlib

4. Run the Python script

    python variant_analyzer.py

Or open the Jupyter Notebook:

    day07_variant_analysis.ipynb

and run the cells sequentially.


Learning Outcomes
-----------------
Through this project, I practiced:

- Python programming for bioinformatics
- Reading biological data files
- Working with Pandas DataFrames
- Data cleaning and filtering
- Statistical summaries
- Variant quality analysis
- Basic genomic data interpretation
- Data visualization
- Exporting analysis results
- Structuring a bioinformatics project


Future Improvements
-------------------
This project can be expanded to perform more realistic genomic analysis.

Possible future improvements include:

- Use a real publicly available VCF dataset
- Parse VCF files using a specialized bioinformatics library
- Add genotype information
- Analyze SNPs and indels separately
- Annotate variants with gene information
- Identify coding and non-coding variants
- Add ClinVar annotations
- Predict potential functional effects
- Build an interactive dashboard using R Shiny
- Add automated quality-control reports


Skills Demonstrated
-------------------

Programming:
- Python
- Pandas
- Data visualization

Bioinformatics:
- VCF format
- Variant analysis
- Variant filtering
- Quality control
- SNP analysis

Data Science:
- Data exploration
- Statistical summaries
- Data filtering
- Visualization
- Reproducible analysis


Author
------
Maria Surahyo

Bioinformatics | Computational Biology | Genomics Data Science

This project is part of my hands-on bioinformatics learning and portfolio development.


Acknowledgements
----------------
This project was developed as a practical learning exercise while working through:

Bioinformatics with Python Cookbook, 4th Edition
by Shane Brubaker.
