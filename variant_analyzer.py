# ==========================================
# GENOMIC VARIANT ANALYZER
# ==========================================


# ------------------------------------------
# 1. IMPORT LIBRARIES
# ------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt


# ------------------------------------------
# 2. LOAD THE VCF FILE
# ------------------------------------------

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

print("VCF loaded successfully!")
print(variants.head())


# ------------------------------------------
# 3. BASIC DATASET INFORMATION
# ------------------------------------------

print("\nDataset information:")
print("Total variants:", len(variants))

print("\nVariants by chromosome:")
print(variants["CHROM"].value_counts().sort_index())

print("\nFilter status:")
print(variants["FILTER"].value_counts())


# ------------------------------------------
# 4. CREATE VARIANT TYPE
# ------------------------------------------

variants["variant_type"] = (
    variants["REF"] + ">" + variants["ALT"]
)

print("\nVariant types:")
print(variants["variant_type"].value_counts())


# ------------------------------------------
# 5. QUALITY STATISTICS
# ------------------------------------------

print("\nQuality statistics:")
print(variants["QUAL"].describe())


# ------------------------------------------
# 6. FILTER HIGH-QUALITY VARIANTS
# ------------------------------------------

high_quality = variants[
    (variants["FILTER"] == "PASS") &
    (variants["QUAL"] >= 70)
].copy()

print("\nFiltering results:")
print("Total variants:", len(variants))
print("PASS variants:", len(
    variants[variants["FILTER"] == "PASS"]
))
print("High-quality variants:", len(high_quality))


# ------------------------------------------
# 7. SAVE FILTERED VARIANTS
# ------------------------------------------

high_quality.to_csv(
    "filtered_variants.csv",
    index=False
)

print("\nFiltered variants saved as:")
print("filtered_variants.csv")


# ------------------------------------------
# 8. PLOT VARIANTS BY CHROMOSOME
# ------------------------------------------

chrom_counts = (
    variants["CHROM"]
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(8, 5))

chrom_counts.plot(kind="bar")

plt.xlabel("Chromosome")
plt.ylabel("Number of variants")
plt.title("Number of Variants by Chromosome")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    "variants_by_chromosome.png",
    dpi=300
)

plt.show()


# ------------------------------------------
# 9. PLOT QUALITY DISTRIBUTION
# ------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    variants["QUAL"],
    bins=5
)

plt.xlabel("Variant quality (QUAL)")
plt.ylabel("Number of variants")
plt.title("Distribution of Variant Quality Scores")

plt.tight_layout()

plt.savefig(
    "quality_distribution.png",
    dpi=300
)

plt.show()


# ------------------------------------------
# 10. PLOT VARIANT TYPES
# ------------------------------------------

variant_counts = (
    variants["variant_type"]
    .value_counts()
)

plt.figure(figsize=(8, 5))

variant_counts.plot(kind="bar")

plt.xlabel("Variant type")
plt.ylabel("Number of variants")
plt.title("Distribution of Variant Types")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "variant_types.png",
    dpi=300
)

plt.show()


# ------------------------------------------
# 11. FINAL SUMMARY
# ------------------------------------------

print("\n================================")
print("FINAL PROJECT SUMMARY")
print("================================")

print("Total variants:", len(variants))

print(
    "PASS variants:",
    len(variants[variants["FILTER"] == "PASS"])
)

print(
    "High-quality variants:",
    len(high_quality)
)

print(
    "Mean QUAL:",
    round(variants["QUAL"].mean(), 2)
)

print(
    "Median QUAL:",
    variants["QUAL"].median()
)

print(
    "Minimum QUAL:",
    variants["QUAL"].min()
)

print(
    "Maximum QUAL:",
    variants["QUAL"].max()
)