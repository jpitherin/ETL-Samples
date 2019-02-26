# ETL-Samples

## Finnish Adoptions: 
- Extract: Extracted and downloaded manually through data provider website UI
- Transform: Performed with Python code
- Load: Python code outputs a .csv file that can be easily loaded into a SQL table

### File Descriptions:
- **ETL_Example_FinnishAdoptions.py** - Python code that performs the data transformation
- **ETL_Example_FinnishAdoptions.ipynb** - Interactive Jupyter notebook 
- **Input_Data/FinlandAdoptions_2017.csv** - Sample file downloaded from data provider
- **Output_Data/ETL_2019-02-07_Finland_Adoptions.csv** - Transformed data

### Data Description:
**Data Provider:** Tilastokeskus, the Finnish public authority for national statistics. 

**Title of Dataset:** 001 -- Adoptions by country of birth, age group and sex of child and type of adoption in 1987 to 2017

**Link to Dataset:**
http://pxnet2.stat.fi/PXWeb/pxweb/en/StatFin/StatFin__vrm__adopt/statfin_adopt_pxt_001.px/?rxid=468082d6-a951-411f-8952-76c6a013bdcc

**Open Data License:** The Creative Commons Attribution 4.0 International licence is applied to Statistics Finland's open data materials:
http://tilastokeskus.fi/org/lainsaadanto/copyright_en.html

**Misc Notes:**
- File was downloaded (extracted) manually in the English version of the website 
- Download file format: "semicolon delimited with heading"
- Since files are updated anually, batching is done by year
