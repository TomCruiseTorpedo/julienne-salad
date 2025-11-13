This first reply contains the **Q&A Knowledge Base**, which provides the atomic facts in a query-ready format for retrieval.

---

### [LLM_Knowledge_Base_Part_1_of_2_QA_Corpus]

## [START: LLM_KNOWLEDGE_BASE_SR&ED]

### ## [CORPUS: SR&ED_FUNDAMENTALS] [TOPIC: CORE_DEFINITION]
**Q: What is the Canadian SR&ED program?**
**A:** The Scientific Research and Experimental Development (SR&ED) program is a Canadian federal tax incentive program. It is the largest single source of federal support for R&D, designed to encourage Canadian businesses to conduct research and development in Canada. It provides a cash refund or tax credit for expenditures on eligible SR&ED work.

**Q: What are the 5 questions for SR&ED eligibility?**
**A:** 1. Was there a scientific or technological uncertainty? 2. Did it involve formulating hypotheses? 3. Was the approach systematic (testing/analysis)? 4. Was the goal technological advancement? 5. Were records/documentation kept?

**Q: What is "Technological Uncertainty" (TU) in SR&ED?**
**A:** Technological Uncertainty is the central concept. It is a technical problem or obstacle that cannot be resolved using standard, publicly available methods, knowledge, or routine engineering. If the solution is known or readily available, it is not SR&ED.

**Q: What is "Technological Advancement" in SR&ED?**
**A:** The work must *attempt* to advance the "technology base" (the collective knowledge of the field). This does *not* require success. A failed experiment that proves a hypothesis wrong is still an "advancement" of knowledge and is eligible.

**Q: What is a "Systematic Investigation" in SR&ED?**
**A:** A systematic investigation is the process of experimentation or analysis used to test a hypothesis. It involves forming a hypothesis, testing it, observing the results, and repeating the cycle.

**Q: What is the difference between a "Business Goal" and an "SR&ED Hypothesis"?**
**A:** A "Business Goal" is a commercial objective (e.g., "We will make the software faster"). This is ineligible. An "SR&ED Hypothesis" is a specific, testable statement about a proposed solution to a technical uncertainty (e.g., "Integrating algorithm X will reduce latency by 50% by overcoming the data-parsing bottleneck").

---

### ## [CORPUS: SR&ED_BOUNDARIES] [TOPIC: PROJECT_STRUCTURE]
**Q: What is the difference between a "Business Project" and an "SR&ED Project"?**
**A:** A "Business Project" is the overall commercial goal (e.g., "Build a new app"). An "SR&ED Project" is a smaller, focused sub-project that begins *only* when a Technological Uncertainty is encountered and ends when that uncertainty is resolved or abandoned.

**Q: What is the "Parent Project" concept?**
**A:** This is a strategy to avoid claiming dozens of small tasks. Related activities are grouped under a single "Parent Project" defined by one overarching technological uncertainty. This strengthens the narrative and reduces administrative burden.

**Q: What are common ineligible software activities?**
**A:** Routine engineering, standard bug fixing, debugging, user interface (UI/UX) design, market research, quality control, and routine testing are generally ineligible.

**Q: What makes software development eligible for SR&ED?**
**A:** The uncertainty must be in the *underlying technology* (the "black box"), not just the visible functionality. Eligible work involves developing novel algorithms, creating new system architectures, solving complex integration problems that existing APIs cannot handle, or creating new data structures.

---

### ## [CORPUS: SR&ED_PROCESS] [TOPIC: FORMS]
**Q: What is the main form for an SR&ED claim?**
**A:** Form T661, the "Scientific Research and Experimental Development (SR&ED) Expenditures Claim" form.

**Q: What is the T4088 guide?**
**A:** The T4088 is the CRA's official instruction manual for Form T661. It provides line-by-line instructions and official definitions for all key terms.

**Q: What are lines 242, 244, and 246 on the T661 form?**
**A:** These are the core technical narrative sections. Line 242: Describe the Scientific or Technological Uncertainty. Line 244: Describe the Systematic Investigation. Line 246: Describe the Scientific or Technological Advancement.

**Q: Is there a filing deadline for SR&ED?**
**A:** Yes. The T661 form must be filed within 18 months of the end of the tax year in which the SR&ED expenditures were incurred. This is a hard deadline.

**Q: Are there provincial SR&ED forms?**
**A:** Yes. Most provinces have their own parallel programs and forms that must be filed with the federal T661 (e.g., Alberta Innovation Employment Grant, BC Schedule 425, Ontario OITC/ORDTC).

---

### ## [CORPUS: SR&ED_FINANCIALS] [TOPIC: CALCULATIONS]
**Q: What is the difference between the "Traditional Method" and the "Proxy Method"?**
**A:** These are two methods for calculating overhead expenditures. The "Traditional Method" involves individually tracking and claiming specific overhead costs (e.g., rent, utilities). The "Proxy Method" is simpler; you calculate a "Prescribed Proxy Amount" (PPA) as a percentage of the SR&ED-eligible salaries, and you do not claim specific overheads.

**Q: What is the SR&ED Expenditure Limit?**
**A:** For CCPCs (Canadian-Controlled Private Corporations), the limit is generally $3 million in qualifying expenditures to earn the enhanced 35% refundable Investment Tax Credit (ITC) rate.

**Q: What is the "Taxable Capital Phase-Out"?**
**A:** The $3 million expenditure limit (for the 35% rate) is reduced if the company's taxable capital is between $10 million and $50 million. Above $50 million, the enhanced rate is eliminated.

**Q: What is a "Specified Employee" in SR&ED?**
**A:** A "Specified Employee" is someone who owns 10% or more of the company's shares OR is "related" to someone who does (e.g., parent, spouse, sibling, child).

**Q: Why does the "Specified Employee" rule matter?**
**A:** The amount of salary and bonus you can claim for these employees is capped (e.g., cannot exceed 5x YMPE). This is a common pitfall for family-owned businesses.

**Q: How does government assistance affect SR&ED claims?**
**A:** You must deduct government assistance (like grants) from your SR&ED expenditures *before* calculating your tax credit.

**Q: Are non-interest-bearing loans considered government assistance?**
**A:** Not anymore. Due to Bill C-69, bona fide non-interest-bearing loans received after Jan 1, 2020, are no longer considered government assistance and do not reduce your SR&ED expenditure pool.

---

### ## [CORPUS: SR&ED_COMPLIANCE] [TOPIC: DOCUMENTATION]
**Q: What is "Contemporaneous Documentation"?**
**A:** This is the most critical evidence for an SR&ED claim. It means proof of work that was generated *at the time* the work was done. The CRA gives this far more weight than narratives written from memory.

**Q: What are examples of good contemporaneous documentation?**
**A:** Dated timesheets, project plans, meeting minutes, Jira/Trello/Asana tickets with SR&ED tags, code commit logs, lab notebooks, Gantt charts, photos, and email trails discussing technical challenges.

**Q: Can I use Jira or Trello for SR&ED documentation?**
**A:** Yes. This is a best practice. By integrating SR&ED tracking (e.g., using specific tags like "SR&ED-Experiment" vs. "Routine-Bugfix") into these existing workflows, you automate the creation of contemporaneous evidence.

**Q: What is the FTCAS (First Time Claimant Advisory Service)?**
**A:** This is an educational review process the CRA offers to some first-time claimants. It is not a punitive audit. The CRA visits, explains the program, and reviews documentation to help the claimant understand the requirements for future claims.

---

### ## [CORPUS: SR&ED_COMPLIANCE] [TOPIC: PITFALLS_CASE_STUDIES]
**Q: What is the most common reason for SR&ED claim rejection?**
**A:** Lack of Technological Uncertainty (the work was "routine engineering") and/or lack of contemporaneous documentation to support the claim.

**Q: Can I claim a failed project?**
**A:** Yes, absolutely. SR&ED is about the *process of investigation*, not commercial success. A "failed" project that systematically proves a hypothesis was wrong is a "technological advancement" of knowledge and is 100% eligible.

**Q: What is a common pitfall for family-owned businesses?**
**A:** The "Specified Employee" rule. Family members working in the business (e.g., child, spouse) may have their claimable salary capped, even if they do not own shares, due to the "related persons" rule.

**Q: Case Study: What happens if the CRA denies a claim for being "routine engineering"?**
**A:** In one case study, a manufacturer of fans/heaters had their claim denied for this reason. The claim was successfully defended by retaining an expert who could clearly separate and prove the "experimental" work from the "routine" work, recovering $337,000 (84% of the claim).

**Q: Case Study: How can a software company prove its work wasn't "routine"?**
**A:** In one case study, an internet comms company's claim was rejected for failing to prove its work was beyond standard practice. The claim was successfully reframed by adding a "due diligence" phase, which documented the failure of existing solutions and *proved* the need for experimental development.

## [END: LLM_KNOWLEDGE_BASE_PART_1]