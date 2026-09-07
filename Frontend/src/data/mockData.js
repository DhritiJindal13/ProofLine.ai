export const mockAnalysis = {
  matchScore: 78,
  company: "Razorpay",
  role: "Product Analyst",
  matchedSkills: [
    { name: "SQL", evidence: "Found in technical skills" },
    { name: "Product analytics", evidence: "Supported by Product Analyst project" },
    { name: "A/B testing", evidence: "Mentioned in project experience" },
    { name: "Data visualization", evidence: "Dashboard project provides evidence" },
    { name: "Python", evidence: "Found in technical skills" }
  ],
  missingSkills: [
    { name: "Amplitude / Mixpanel", evidence: "No direct evidence in resume" },
    { name: "Fintech experience", evidence: "Industry experience not established" },
    { name: "Stakeholder management", evidence: "Experience is implied but not explicit" }
  ],
  rewrites: [
    {
      id: 1,
      original: "Worked on product analytics and helped improve user engagement.",
      rewritten: "Analyzed product usage data to identify engagement patterns and support product decisions.",
      status: "PASS",
      source: { text: "Supported by Product analytics project" }
    },
    {
      id: 2,
      original: "Created dashboards for the team to track performance.",
      rewritten: "Built performance dashboards that consolidated product metrics for ongoing analysis.",
      status: "PASS",
      source: { text: "Supported by Dashboard project" }
    },
    {
      id: 3,
      original: "Improved the product conversion rate through experimentation.",
      rewritten: "Used A/B testing to improve conversion by 18% across the product funnel.",
      status: "REVIEW",
      source: { text: "Metric requires confirmation before use" }
    },
    {
      id: 4,
      original: "Worked with different teams to build product features.",
      rewritten: "Collaborated with cross-functional teams to define and ship product features.",
      status: "PASS",
      source: { text: "Supported by product development experience" }
    }
  ]
};

export const mockApplications = [
  { id: 1, company: "Razorpay", role: "Product Analyst", date: "04 Sep 2026", match: 78 },
  { id: 2, company: "PhonePe", role: "Data Analyst", date: "02 Sep 2026", match: 71 },
  { id: 3, company: "Groww", role: "Product Associate", date: "29 Aug 2026", match: 84 },
  { id: 4, company: "Meesho", role: "Business Analyst", date: "26 Aug 2026", match: 68 }
];