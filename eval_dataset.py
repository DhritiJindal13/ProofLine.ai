EVAL_CASES = [
    {
        "original": "Built a full-featured RESTful backend using Node.js, TypeScript, Express, and Prisma with SQLite.",
        "rewrite": "Developed a full-featured RESTful backend using Node.js, TypeScript, Express, and Prisma with SQLite.",
        "expected_verdict": "PASS"
    },
    {
        "original": "Implemented secure user authentication with JWT, password hashing, and Role-Based Access Control (RBAC).",
        "rewrite": "Implemented secure authentication using JWT, password hashing, and RBAC.",
        "expected_verdict": "PASS"
    },
    {
        "original": "Designed a relational database system using ER diagrams, schema design, and normalization (3NF) improving query efficiency by 20%.",
        "rewrite": "Designed a normalized (3NF) relational database using ER diagrams, improving query efficiency by 20%.",
        "expected_verdict": "PASS"
    },
    {
        "original": "Contributed to the development of an AI-powered chatbot by implementing frontend features and integrating backend APIs to improve user interaction.",
        "rewrite": "Developed frontend features and integrated backend APIs for an AI-powered chatbot to enhance user interaction.",
        "expected_verdict": "PASS"
    },
    {
        "original": "Built a full-stack hotel booking platform with separate interfaces for travelers and hotel owners using React frontend and Node.js/Express backend with MongoDB.",
        "rewrite": "Developed a full-stack hotel booking web application with dedicated interfaces for travelers and hotel owners using a React frontend and a Node.js/Express and MongoDB backend.",
        "expected_verdict": "PASS"
    },
    {
        "original": "Wrote PL/SQL procedures for subscription updates, viewing history handling, and recommendation logic.",
        "rewrite": "Developed PL/SQL procedures to handle subscription updates, viewing history, and recommendation logic.",
        "expected_verdict": "PASS"
    },
    {
        "original": "Created dashboard analytics endpoints that calculate income/expense summaries, category-wise breakdowns, and monthly trends.",
        "rewrite": "Built analytics endpoints for calculating income/expense summaries, category-wise breakdowns, and monthly trends.",
        "expected_verdict": "PASS"
    },
    {
        "original": "Developed complete CRUD functionality for managing financial records including filtering, pagination, search, and soft delete features.",
        "rewrite": "Implemented full CRUD functionality for financial records, including filtering, pagination, search, and soft delete.",
        "expected_verdict": "PASS"
    },

    {
        "original": "Built a hotel booking website using React and Node.js.",
        "rewrite": "Developed a scalable hotel booking platform using React and Node.js, increasing booking efficiency by 30%.",
        "expected_verdict": "FAIL"
    },
    {
        "original": "Worked on a full-stack hotel booking platform with React frontend and Node.js backend.",
        "rewrite": "Built a full-stack hotel booking platform serving 50,000+ monthly active users using React and Node.js.",
        "expected_verdict": "FAIL"
    },
    {
        "original": "Implemented IP-based rate limiting middleware to prevent API abuse.",
        "rewrite": "Implemented rate limiting middleware that reduced API abuse incidents by 45%.",
        "expected_verdict": "FAIL"
    },
    {
        "original": "Wrote PL/SQL procedures for subscription updates and viewing history handling.",
        "rewrite": "Wrote optimized PL/SQL procedures that improved subscription processing speed by 60%.",
        "expected_verdict": "FAIL"
    },
    {
        "original": "Built a REST API backend for a finance dashboard using Node.js and Express.",
        "rewrite": "Built a REST API backend for a finance dashboard, handling over 10,000 requests per day.",
        "expected_verdict": "FAIL"
    },
    {
        "original": "Designed a relational database system using ER diagrams and schema design.",
        "rewrite": "Designed a relational database system that reduced storage costs by 25% using ER diagrams and schema design.",
        "expected_verdict": "FAIL"
    },

    {
        "original": "Built a REST API backend using Node.js and Express.",
        "rewrite": "Built a REST API backend using Node.js, Express, and Docker for containerized deployment.",
        "expected_verdict": "FAIL"
    },
    {
        "original": "Developed frontend features for a hotel booking platform using React.",
        "rewrite": "Developed frontend features for a hotel booking platform using React and Redux for state management.",
        "expected_verdict": "FAIL"
    },
    {
        "original": "Implemented secure user authentication with JWT and password hashing.",
        "rewrite": "Implemented secure user authentication with JWT, password hashing, and OAuth2 integration.",
        "expected_verdict": "FAIL"
    },
    {
        "original": "Built backend database workflows and SQL operations for user management.",
        "rewrite": "Built backend database workflows and SQL operations for user management, deployed on AWS RDS.",
        "expected_verdict": "FAIL"
    },
    {
        "original": "Worked in a collaborative Agile environment, strengthening technical and communication skills.",
        "rewrite": "Worked in a collaborative Agile environment using Jira and Confluence, strengthening technical and communication skills.",
        "expected_verdict": "FAIL"
    },
    {
        "original": "Integrated backend APIs to improve user interaction for an AI-powered chatbot.",
        "rewrite": "Integrated backend APIs using GraphQL to improve user interaction for an AI-powered chatbot.",
        "expected_verdict": "FAIL"
    },

    {
        "original": "Created dashboard analytics endpoints that calculate income/expense summaries.",
        "rewrite": "Architected an enterprise-grade analytics platform calculating real-time income/expense summaries.",
        "expected_verdict": "FAIL"
    },
    {
        "original": "Built a full-stack hotel booking platform with React and Node.js.",
        "rewrite": "Built a highly scalable, production-ready hotel booking platform with React and Node.js.",
        "expected_verdict": "FAIL"
    },
    {
        "original": "Developed complete CRUD functionality for managing financial records.",
        "rewrite": "Developed a robust, enterprise-level CRUD system for managing large-scale financial records.",
        "expected_verdict": "FAIL"
    },
    {
        "original": "Implemented JWT authentication and role-based access control for the hotel platform.",
        "rewrite": "Architected a bulletproof, industry-leading authentication and access control system for the hotel platform.",
        "expected_verdict": "FAIL"
    },
    {
        "original": "Wrote SQL queries for user management and subscription data.",
        "rewrite": "Engineered a high-performance, mission-critical SQL layer for user management and subscription data.",
        "expected_verdict": "FAIL"
    },
    {
        "original": "Built a relational database system using ER diagrams and normalization.",
        "rewrite": "Built an industry-standard, highly optimized relational database system using ER diagrams and normalization.",
        "expected_verdict": "FAIL"
    },

    {
        "original": "Contributed to the development of an AI-powered chatbot by implementing frontend features.",
        "rewrite": "Led the development of an AI-powered chatbot, implementing frontend features and mentoring junior developers.",
        "expected_verdict": "FAIL"
    },
    {
        "original": "Worked in a collaborative Agile environment as a summer intern.",
        "rewrite": "Managed a small team in a collaborative Agile environment as a summer intern.",
        "expected_verdict": "FAIL"
    },
    {
        "original": "Implemented secure user authentication with JWT and RBAC.",
        "rewrite": "Owned the end-to-end security architecture, implementing user authentication with JWT and RBAC.",
        "expected_verdict": "FAIL"
    },
    {
        "original": "Built dashboard analytics endpoints for a finance application.",
        "rewrite": "Directed the analytics roadmap and built dashboard analytics endpoints for a finance application.",
        "expected_verdict": "FAIL"
    },

    {
        "original": "Implemented IP-based rate limiting middleware to prevent API abuse (100 requests/minute per client).",
        "rewrite": "Implemented security middleware to prevent API abuse, including rate limiting best practices.",
        "expected_verdict": "REVIEW"
    },
    {
        "original": "Implemented secure user authentication with JWT, password hashing, and Role-Based Access Control (RBAC).",
        "rewrite": "Implemented secure user authentication following security best practices, utilizing JWT, password hashing, and RBAC.",
        "expected_verdict": "REVIEW"
    },
    {
        "original": "Worked with structured query optimization, modular database logic, and data validation using Oracle Live SQL.",
        "rewrite": "Applied strong database engineering principles including query optimization and modular design using Oracle Live SQL.",
        "expected_verdict": "REVIEW"
    },
    {
        "original": "Focused on responsive design, clean UI/UX, and practical functionality to deliver a complete travel booking experience.",
        "rewrite": "Delivered a polished, user-friendly travel booking experience with responsive design and clean UI/UX.",
        "expected_verdict": "REVIEW"
    },
]
