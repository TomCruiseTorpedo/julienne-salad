This is the **Process-Entity Model**. It provides the LLM with the chronological workflow and the relationships between all the key concepts. When combined with Part 1 (the Q&A Corpus), this gives the LLM both the facts and the context to understand the *entire* SR&ED process from start to finish.

---

### [LLM_Knowledge_Base_Part_2_of_2_Process_Entity_Model]

## [START: LLM_PROCESS_ENTITY_MODEL_SR&ED]

### 1.0 Chronological Workflow (The User Journey)

This model defines the end-to-end lifecycle of an SR&ED claim.

* **[PHASE: 1] [NAME: Pre-Claim / R&D Year]**
    * **[TRIGGER]:** A `Business_Project` encounters a technical problem that standard practice or routine engineering cannot solve.
    * **[ACTION: 1.1]:** Identify `Technological_Uncertainty`. Must prove that the solution is not publicly known or easily discoverable.
    * **[ACTION: 1.2]:** Formulate a testable `SR&ED_Hypothesis`. This must be a specific, testable technical statement, *not* a "Business Goal".
    * **[ACTION: 1.3]:** Establish `Contemporaneous_Documentation`. This is the most critical step for surviving a `CRA_Review`.
        * **[BEST_PRACTICE]:** Integrate tracking into existing tools (Jira, Trello, Asana) with tags for "SR&ED-Experiment" vs. "Routine-Work".
        * **[EVIDENCE_TYPES]:** Dated timesheets, code commits, lab notebooks, meeting minutes, photos, email trails.

* **[PHASE: 2] [NAME: Claim Preparation / Post-Year-End]**
    * **[ACTION: 2.1]:** Gather all `Contemporaneous_Documentation` from Phase 1.
    * **[ACTION: 2.2]:** Define Project Boundaries. Separate the `Business_Project` from the specific `SR&ED_Project`. Use the "Parent Project" strategy to group related tasks under one overarching `Technological_Uncertainty`.
    * **[ACTION: 2.3]:** Calculate `Expenditure` Pool.
        * **[DECISION]:** Choose overhead method: `Traditional_Method` (track all specific overheads) or `Proxy_Method` (simpler, based on salaries).
        * **[PITFALL]:** Identify all `Specified_Employee` salaries (owners >10% or their relatives) and apply the `Expenditure_Cap`.
        * **[ADJUSTMENT]:** Deduct any `Government_Assistance` from the cost pool. *Exception*: Do *not* deduct bona fide non-interest-bearing loans.
    * **[ACTION: 2.4]:** Write the Technical Narratives. This is **Form T661, Part 2** (Lines 242, 244, 246), where you use your documentation to describe the Uncertainty, Investigation, and Advancement.

* **[PHASE: 3] [NAME: Filing & Review / CRA Phase]**
    * **[ACTION: 3.1]:** File the forms. Submit **Form T661** (Federal) and the required **Provincial_Form** (e.g., OITC, BC Schedule 425).
    * **[ACTION: 3.2]:** Await Review. The CRA will either accept the claim, select it for a `CRA_Review` (technical/financial), or, for first-timers, select it for the **FTCAS (First Time Claimant Advisory Service)**.
    * **[ACTION: 3.3]:** Defend the Claim (if reviewed). Use your `Contemporaneous_Documentation` to prove the "what, when, and why" of your claim.
    * **[ACTION: 3.4]:** Receive Credit. Once approved, the claim results in a cash refund (for CCPCs) or a non-refundable tax credit.

---

### 2.0 Core Entity-Relationship Model (The "Object Map")

This map defines the "nouns" of the SR&ED program and the "verbs" that connect them, providing deep contextual understanding.

* **[ENTITY: `Project`]**
    * **[IS_DEFINED_BY]:** `Technological_Uncertainty`
    * **[IS_TESTED_VIA]:** `SR&ED_Hypothesis`
    * **[IS_DESCRIBED_IN]:** `T661_Form` (Part 2)
    * **[IS_PROVEN_BY]:** `Contemporaneous_Documentation`
    * **[IS_SEPARATE_FROM]:** `Business_Project`
    * **[CAN_BE_ELIGIBLE_IF]:** "Failed" (proves a hypothesis wrong).

* **[ENTITY: `Employee`]**
    * **[GENERATES]:** `Expenditure` (Salary)
    * **[GENERATES]:** `Contemporaneous_Documentation` (e.g., `Timesheet`, `Jira_Ticket`, `Code_Commit`)
    * **[CAN_BE_A]:** `Specified_Employee`

* **[ENTITY: `Specified_Employee`]**
    * **[IS_A]:** `Employee`
    * **[IS_DEFINED_AS]:** Owner (>10% shares) OR "Related Person" (spouse, child, sibling, parent).
    * **[IS_SUBJECT_TO]:** `Expenditure_Cap`
    * **[IS_A_PITFALL_FOR]:** `Family_Owned_Business`.

* **[ENTITY: `Expenditure` (The Cost Pool)]**
    * **[IS_CALCULATED_BY]:** `Proxy_Method` OR `Traditional_Method`.
    * **[IS_REDUCED_BY]:** `Government_Assistance`.
    * **[IS_NOT_REDUCED_BY]:** Bona-fide non-interest loans (post-Jan 1, 2020).
    * **[IS_CAPPED_FOR]:** `Specified_Employee`.
    * **[IS_SUBJECT_TO]:** `Expenditure_Limit` ($3M for 35% rate) and `Capital_Phase_Out` ($10M-$50M).

* **[ENTITY: `Contemporaneous_Documentation` (The Proof)]**
    * **[INCLUDES]:** `Timesheet`, `Jira_Ticket`, `Gantt_Chart`, `Code_Commit`, `Lab_Notebook`, `Email_Trail`.
    * **[IS_REQUIRED_FOR]:** `CRA_Review`.
    * **[BEST_PRACTICE_VIA]:** `Jira` / `Trello` integration.

* **[ENTITY: `CRA_Review` (The Audit)]**
    * **[IS_DEFENDED_BY]:** `Contemporaneous_Documentation`.
    * **[CAN_BE_A]:** `FTCAS_Review` (for first-timers, this is an educational service).
    * **[COMMON_REJECTION_REASON]:** "Routine Engineering" (Lack of `Technological_Uncertainty`) or Lack of Evidence.

* **[ENTITY: `T661_Form` (The Application)]**
    * **[IS_THE]:** Primary federal application form.
    * **[IS_EXPLAINED_BY]:** `T4088_Guide`.
Type
    * **[HAS_DEADLINE]:** 18 months post-tax-year-end.
    * **[IS_FILED_WITH]:** `Provincial_Form`.

## [END: LLM_PROCESS_ENTITY_MODEL_SR&ED]