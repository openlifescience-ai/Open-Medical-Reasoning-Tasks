# Medical Coding and Billing Optimization

## Description:
The task of ICD-10 and CPT code classification involves interpreting clinical documentation to accurately identify and categorize diseases, disorders, and procedures using standardized codes. It assesses the ability to recognize clinical patterns, verify accuracy against medical records, facilitate billing processes, and support research through the analysis of coded health data. This involves understanding and applying medical terminology, diagnostic criteria, and procedural descriptions to ensure precise and consistent coding for various healthcare applications.

## Modality:
Text -> Coded Data (ICD-10, CPT)

## Examples:

### Example 1:

Input:
```
Schizoaffective disorder and developmental delay: Patient has become a behavioral problem in the home where she stays. Continue with Depakote extended release 750 mg nightly and gabapentin 400 mg twice daily. Increase Olanzapine to 10 mg BID. Continue with water restriction to 1200 cc daily. Repeat chemistry. Continue to encourage participation in group therapy and ward activities. Continue to monitor mental status.
```

Output:
```
ICD-10 Code(s):
- F25.0 - Schizoaffective disorder, bipolar type (Justification: "Schizoaffective disorder and developmental delay; the patient is exhibiting behavioral problems.")
- F70 - Mild intellectual disabilities (Justification: "Developmental delay mentioned in the context suggests an intellectual disability.")

CPT Code(s):
- 99213 - Established patient office or other outpatient visit, typically 15-29 minutes (Justification: "Ongoing management of schizoaffective disorder requires consistent follow-up and medication management.")
```

---

### Example 2:

Input:
```
Chronic depression and bipolar 2 disorder Restless leg syndrome - Continue with pramipexole 0.125 mg nightly. - Continue with lamotrigine 100 mg twice daily. - Continue with duloxetine 90 mg daily. - Increase quetiapine to 300 mg. - Discontinue trazodone 50 mg nightly. - Discontinue melatonin 5 mg nightly.
```

Output:
```
ICD-10 Codes:
- F31.81 - Bipolar disorder, current episode manic, unspecified (Justification: "Bipolar 2 disorder" typically indicates a current depressive episode, but here it's coded as a specific bipolar disorder since details suggest an ongoing management of the condition.)
- G25.81 - Restless legs syndrome (Justification: "Restless leg syndrome" is mentioned directly, thus requiring a code for accurate diagnosis.)

CPT Codes:
- 99214 - The provider sees an established patient for an office visit or other outpatient visit involving evaluation and management. The visit involves a moderate level of medical decision making, and/or the provider spends 30 minutes or more of total time on the encounter on a single date. (Justification: Considered due to the complexity of managing chronic depression, bipolar disorder, and additional psychiatric medications.)
```

## Tags:
- ICD-10
- CPT Codes
- Medical Coding
- Clinical Documentation
- Disease Classification
- Procedure Classification
- Medical Terminology
- Diagnostic Criteria
- Healthcare Billing
- Health Data Analysis
- Coding Accuracy
- Standardized Codes
- Medical Records Verification
- Research Support
