# Medical Commonsense Reasoning and Diagnosis

## Description:
This task involves answering medical questions that require not only factual knowledge but also an understanding of everyday situations and human-like reasoning in a clinical context. It evaluates the model's ability to integrate medical knowledge with common sense to provide logical and practical responses to medical scenarios.

## Modality:
Text only

## Examples:

### Example 1:

Input:

```
A 28-year-old pregnant woman in her third trimester calls her obstetrician reporting that she hasn't felt her baby move in the last 24 hours. She mentions feeling fine otherwise and has had an uncomplicated pregnancy so far. What should the obstetrician advise as an immediate next step?
```

Output:

```
Given the presented information, the obstetrician should advise the patient to come to the hospital or clinic immediately for fetal monitoring. Here's the reasoning:

1. Patient profile:
   - 28-year-old pregnant woman
   - Third trimester of pregnancy
   - Previously uncomplicated pregnancy
   - No fetal movement felt in the last 24 hours
   - Patient feels fine otherwise

2. Analysis:
   a) Fetal movement is a key indicator of fetal well-being, especially in the third trimester.
   b) A sudden decrease or absence of fetal movement can signify fetal distress.
   c) The patient's well-being doesn't necessarily reflect the fetal condition.

3. Commonsense reasoning:
   a) While some variation in fetal movement is normal, 24 hours without perceived movement is concerning.
   b) Quick assessment is crucial as delayed intervention in cases of fetal distress can lead to serious complications.
   c) In-person evaluation allows for immediate intervention if needed.

4. Medical rationale for immediate in-person assessment:
   - Allows for prompt fetal heart rate monitoring (e.g., non-stress test)
   - Enables quick ultrasound evaluation if necessary
   - Facilitates immediate intervention if fetal distress is detected

5. Alternative steps considered:
   - Advising at-home kick counting
   - Scheduling a routine appointment
   - Recommending watchful waiting

6. Justification for chosen step:
   - Prioritizes fetal safety in a potentially critical situation
   - Aligns with standard obstetric care guidelines for reduced fetal movement
   - Provides reassurance to the patient through professional assessment

7. Next steps after arrival at hospital/clinic:
   - Perform non-stress test or biophysical profile
   - Conduct ultrasound if indicated
   - Assess maternal vital signs and overall health
   - Determine need for further monitoring or intervention based on findings

This approach demonstrates commonsense medical reasoning in obstetrics by recognizing the potential seriousness of reduced fetal movement, even in the absence of other symptoms, and prioritizing swift professional assessment to ensure both maternal and fetal well-being.
```

### Example 2:

Input:

```
A 10-year-old boy is brought to the pediatrician by his mother. She's concerned because he's been losing weight despite eating normally, and she noticed he's been drinking water excessively and urinating frequently. The boy mentions he's been feeling more tired than usual. What everyday objects or situations might the doctor ask about to help assess the likelihood of diabetes in this child?
```

Output:

```
To assess the likelihood of diabetes in this child, the doctor might ask about several everyday objects or situations that require commonsense reasoning combined with medical knowledge:

1. School water bottle:
   - How often does the child refill it?
   - Has the teacher noticed increased trips to the water fountain?

2. Bathroom habits:
   - Frequency of nighttime bathroom trips
   - Any bedwetting incidents (unusual for this age)

3. Clothing fit:
   - Are clothes becoming looser?
   - Has the child needed a new belt hole recently?

4. Sports or physical activities:
   - Any changes in endurance or performance?
   - Unusual fatigue during regular play?

5. Homework and attention:
   - Any difficulty concentrating on schoolwork?
   - Changes in grades or teacher feedback?

6. Lunchbox:
   - Any uneaten food returning home?
   - Requests for extra snacks or larger portions?

7. Garbage can:
   - Increase in empty juice or soda containers?

8. Fruit bowl:
   - Increased interest in sugary fruits?

9. Bathroom trash:
   - More tissues from frequent urination?

10. Laundry:
    - Increase in underwear changes due to accidents?

11. Family meals:
    - Finishing meals but still seeming hungry?

12. Video games or TV time:
    - Less interest or stamina for usual activities?

13. Cuts or bruises:
    - Taking longer to heal than usual?

14. Mood and behavior:
    - Any unusual irritability or mood swings?

Commonsense reasoning:
- These everyday items and situations can provide indirect evidence of diabetes symptoms.
- They offer a child-friendly way to gather information without relying solely on the child's self-reporting.
- Observations from daily life can reveal patterns that might not be apparent in a brief doctor's visit.

This approach demonstrates commonsense QA by connecting medical symptoms to tangible, everyday experiences that a child and parent can easily relate to and report on, potentially uncovering important diagnostic clues.
```

## Tags:
- Clinical Decision Making
- Symptom Interpretation
- Patient History Analysis
- Differential Diagnosis
- Everyday Life Medical Implications
- Pediatric Health Assessment
- Obstetric Risk Evaluation
- Fetal Well-being Monitoring
- Diabetes Screening in Children
- Growth and Development Evaluation
- Behavioral Health in Pediatrics
- Physical Activity and Health
- Nutritional Assessment
- Sleep Patterns in Disease
- Cognitive Function Evaluation
- Family Health Dynamics
- School Performance and Health
- Non-invasive Diagnostic Indicators
- Patient-Centered Care Approach
- Preventive Medicine Strategies

## Expert Verification
- Status: Pending
- Last Verified:  [YYYY-MM-DD]
- Verifying Expert: (see [EXPERTS.md](https://github.com/openlifescience-ai/Open-Medical-Reasoning-Tasks/blob/main/EXPERTS.md))
- Expert Notes: 
