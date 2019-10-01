# TSH Test Data Conversion Assignment

## Description
This program parses through data files containing patients' information--name, age, gender, and thyroid stimulating hormone (TSH) level test results--and determines whether each patient has normal thyroid function, hypothyroidism, or hyperthyroidism. For each patient, the program outputs a unique data file named "FirstName-LastName.json" that includes all of their relevant information, including the diagnosis.

## Thyroid Function
Thyroid function is determined based on TSH levels; TSH is a hormone released by the pituitary gland to stimulate the thyroid gland to control thyroxine levels. The conditions are categorized as follows:

hyperthyroidism: any of their tests results is less than 1.0 <br/>
hypothyroidism: any of their test results is greater than 4.0 <br/>
normal thyroid function: all test results are b/w 1.0 and 4.0, inclusive <br/>
