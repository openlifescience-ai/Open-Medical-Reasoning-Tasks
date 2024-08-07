# Clinical Diagnosis Formulation

## Description:
This task involves analyzing patient symptoms, medical history, and test results to formulate accurate clinical diagnoses. It evaluates the model's ability to integrate diverse medical information, recognize patterns, and apply medical knowledge to identify potential diseases or conditions.

## Modality:
Text only

## Examples:

### Example 1:

Input:

```
A 45-year-old male presents with sudden onset of severe chest pain, shortness of breath, and sweating. He has a history of hypertension and smoking. Recent blood tests show elevated cholesterol levels. What is the most likely diagnosis?
```

Output:

```
Given the presented information, the most likely diagnosis is Acute Myocardial Infarction (Heart Attack). Here's the reasoning:

1. Patient profile:
   - 45-year-old male
   - History of hypertension and smoking
   - Elevated cholesterol levels

2. Symptoms:
   - Sudden onset of severe chest pain
   - Shortness of breath
   - Sweating

3. Analysis:
   a) The patient has several risk factors for cardiovascular disease:
      - Age (male over 45)
      - Hypertension
      - Smoking history
      - Elevated cholesterol

   b) The symptoms are classic for a heart attack:
      - Severe chest pain (often described as pressure or squeezing)
      - Shortness of breath
      - Sweating (diaphoresis)

   c) The sudden onset suggests an acute event rather than a chronic condition.

4. Differential diagnoses to consider:
   - Unstable Angina
   - Aortic Dissection
   - Pulmonary Embolism
   - Pneumothorax

5. Conclusion:
   While other conditions should be ruled out, the combination of risk factors and typical symptoms strongly suggests an Acute Myocardial Infarction as the most likely diagnosis.

6. Next steps:
   - Immediate ECG
   - Cardiac enzyme tests (Troponin)
   - Aspirin administration (if not contraindicated)
   - Preparation for potential cardiac catheterization

This diagnosis requires immediate medical attention and further tests for confirmation and treatment.
```

---

### Example 2:

Input:

```
A 28-year-old female presents with fatigue, unexplained weight loss, excessive thirst, and frequent urination over the past month. She has no significant medical history. What is the most likely diagnosis and what additional test would you recommend to confirm it?
```

Output:

```
Given the presented information, the most likely diagnosis is Type 1 Diabetes Mellitus. Here's the reasoning:

1. Patient profile:
   - 28-year-old female
   - No significant medical history

2. Symptoms:
   - Fatigue
   - Unexplained weight loss
   - Excessive thirst (polydipsia)
   - Frequent urination (polyuria)
   - Symptoms present for the past month

3. Analysis:
   a) The combination of symptoms is classic for diabetes:
      - Polyuria and polydipsia are hallmark symptoms
      - Unexplained weight loss suggests the body is not properly using glucose for energy
      - Fatigue can result from the body's inability to use glucose effectively

   b) The patient's age and lack of medical history suggest Type 1 rather than Type 2 Diabetes:
      - Type 1 often presents in younger individuals
      - Sudden onset of symptoms is more typical of Type 1

4. Differential diagnoses to consider:
   - Type 2 Diabetes Mellitus
   - Hyperthyroidism
   - Chronic kidney disease
   - Certain medications or recreational drugs

5. Conclusion:
   While other conditions should be ruled out, the combination of classic symptoms in a young, previously healthy individual strongly suggests Type 1 Diabetes Mellitus.

6. Recommended additional test:
   The most important test to confirm this diagnosis would be a fasting blood glucose test.

   Other tests to consider:
   - Glycated hemoglobin (A1C) test
   - Random blood glucose test
   - Oral glucose tolerance test
   - Tests for autoantibodies associated with Type 1 Diabetes

7. Next steps:
   - Conduct fasting blood glucose test
   - If elevated (≥126 mg/dL or 7.0 mmol/L), repeat the test on another day for confirmation
   - Check for ketones in urine to assess for diabetic ketoacidosis
   - Refer to an endocrinologist for further management if diagnosis is confirmed

This diagnosis requires prompt medical attention for proper management and to prevent complications.
```

## Tags:
- Medical Diagnosis
- Symptom Analysis
- Patient History Interpretation
- Clinical Reasoning
- Differential Diagnosis
- Data Integration
- Medical Knowledge Application
