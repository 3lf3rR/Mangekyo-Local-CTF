from flask import Flask, render_template, render_template_string, request, redirect, url_for
from pathlib import Path
import re
import html

app = Flask(__name__)

BASE = Path(__file__).parent
FLAG_PATH = BASE / "flag.txt"

def get_flag():
    try:
        return FLAG_PATH.read_text().strip()
    except Exception:
        return "FLAG-MISSING"

# Expanded dataset: 50 articles with descriptive content
ARTICLES = [
    {
        "id": 1,
        "title": "Observations on Coastal Data",
        "author": "A. Researcher",
        "date": "2025-01-10",
        "content": """
        <p>Recent measurements show interesting tidal variations across the bay. Data collection methods were standardised across teams, enabling a robust comparison of seasonal changes.</p>
        <p>The dataset highlights subtle shifts in salinity correlated with rainfall patterns, suggesting a stronger freshwater influence during wet months. Future work should prioritise higher-frequency sampling during storm events.</p>
        """
    },
    {
        "id": 2,
        "title": "Design Patterns in Microservices",
        "author": "Dev Team",
        "date": "2024-11-02",
        "content": """
        <p>This article discusses common design patterns used in microservices and how they help decouple components.</p>
        <p>Examples include Circuit Breaker, Bulkhead, and Saga patterns; each pattern balances resilience and complexity in different scenarios.</p>
        """
    },
    {
        "id": 3,
        "title": "A Short Guide to Optimization",
        "author": "J. Optimizer",
        "date": "2023-08-19",
        "content": """
        <p>Optimization is iterative — start small, measure, and refine. Use profiling to find hotspots and address the highest-impact issues first.</p>
        <p>Always validate improvements under realistic load and document assumptions to avoid regressions later.</p>
        """
    },
    {
        "id": 4,
        "title": "Machine Learning for Environmental Monitoring",
        "author": "L. Data",
        "date": "2024-06-15",
        "content": """
        <p>ML techniques convert raw sensor streams into actionable insights. We outline a pipeline from data ingestion to deployment.</p>
        <p>Watch for distribution shift and maintain continuous evaluation to keep models reliable under changing conditions.</p>
        """
    },
    {
        "id": 5,
        "title": "Practical Observability: Traces, Metrics, Logs",
        "author": "Ops Lead",
        "date": "2024-09-20",
        "content": """
        <p>Traces, metrics and logs together provide a comprehensive view of system health.</p>
        <p>Design for correlated context and consider retention trade-offs for different observability signals.</p>
        """
    },
    {
        "id": 6,
        "title": "Caching Strategies That Work",
        "author": "Cache Team",
        "date": "2025-04-03",
        "content": """
        <p>Caching reduces latency and load when used appropriately. Choose patterns like cache-aside or write-through based on consistency needs.</p>
        <p>Plan invalidation and TTL policies based on data staleness tolerances rather than arbitrary durations.</p>
        """
    },
    {
        "id": 7,
        "title": "Building Inclusive Product Teams",
        "author": "People Ops",
        "date": "2023-12-01",
        "content": """
        <p>Inclusive teams build better products. Structured interviews and onboarding help reduce bias.</p>
        <p>Sponsorship and mentorship programs accelerate growth for underrepresented team members.</p>
        """
    },
    {
        "id": 8,
        "title": "Edge Computing: When It Makes Sense",
        "author": "R. Architect",
        "date": "2024-02-14",
        "content": """
        <p>Edge computing moves computation closer to data sources to reduce latency. Common use cases include IoT and AR/VR.</p>
        <p>Consider orchestration, security, and versioning when deploying at the edge.</p>
        """
    },
    {
        "id": 9,
        "title": "Data Contracts: Aligning Producers and Consumers",
        "author": "Schema Guild",
        "date": "2025-03-11",
        "content": """
        <p>Data contracts formalise expectations between services and prevent silent downstream failures.</p>
        <p>Automated compatibility checks and versioning in CI pipelines reduce incidents and maintain developer velocity.</p>
        """
    },
    {
        "id": 10,
        "title": "Sustainable Software Practices",
        "author": "Green Devs",
        "date": "2022-10-30",
        "content": """
        <p>Sustainability in software focuses on energy-efficient design and resource minimisation.</p>
        <p>Examples include reducing unnecessary polling and scheduling heavy workloads during off-peak energy windows.</p>
        """
    },
    {
        "id": 11,
        "title": "Human-Centered Debugging",
        "author": "Debug Collective",
        "date": "2024-12-05",
        "content": """
        <p>Debugging is a human activity that benefits from clear hypotheses and reproducible test cases.</p>
        <p>Pairing with the original author and documenting findings turns fixes into lasting improvements.</p>
        """
    },
    {
        "id": 12,
        "title": "Practical Security: Threat Modeling for Small Teams",
        "author": "Sec Team",
        "date": "2025-05-18",
        "content": """
        <p>Threat modeling is accessible to small teams. Start with simple data flow diagrams and list abuse cases.</p>
        <p>Prioritise mitigations that are fast to implement and provide high risk reduction.</p>
        """
    },
    {
        "id": 13,
        "title": "Event-Driven Architectures in Practice",
        "author": "Event Crew",
        "date": "2024-07-22",
        "content": """
        <p>Event-driven systems decouple producers and consumers with asynchronous messages. They scale well for many workloads.</p>
        <p>Design idempotent consumers and think about ordering guarantees when required.</p>
        """
    },
    {
        "id": 14,
        "title": "Observational Studies: Methods & Pitfalls",
        "author": "Research Unit",
        "date": "2021-05-12",
        "content": """
        <p>Observational studies can reveal correlations but must be careful around confounders and biases.</p>
        <p>Transparent methodology and sensitivity analyses strengthen findings.</p>
        """
    },
    {
        "id": 15,
        "title": "API Design: Balancing Simplicity and Flexibility",
        "author": "API Team",
        "date": "2023-03-30",
        "content": """
        <p>Good APIs are intuitive yet flexible. Use consistent naming, predictable errors, and sensible defaults.</p>
        <p>Documenting contract expectations prevents misunderstanding between teams and services.</p>
        """
    },
    {
        "id": 16,
        "title": "Operational Readiness Checklists",
        "author": "Ops Team",
        "date": "2022-08-21",
        "content": """
        <p>Readiness checklists help ensure services are prepared for production. Include monitoring, alerting, and runbook links.</p>
        <p>Periodic rehearsals of incident playbooks improve team response times and outcomes.</p>
        """
    },
    {
        "id": 17,
        "title": "Scaling Databases: Partitioning & Indexing",
        "author": "DB Experts",
        "date": "2024-10-11",
        "content": """
        <p>Scaling databases requires careful partitioning and sensible indexing strategies to maintain performance.</p>
        <p>Measure real query patterns and avoid premature sharding before clear needs arise.</p>
        """
    },
    {
        "id": 18,
        "title": "Cost-Aware Engineering",
        "author": "Finance Dev",
        "date": "2023-09-02",
        "content": """
        <p>Engineering decisions have cost implications. Track cloud spend, right-size resources, and build cost visibility into dashboards.</p>
        <p>Optimization efforts should balance developer time and operational savings for best ROI.</p>
        """
    },
    {
        "id": 19,
        "title": "Designing for Accessibility",
        "author": "UX Guild",
        "date": "2024-01-08",
        "content": """
        <p>Accessibility improves usability for everyone. Use semantic markup, keyboard navigability, and proper contrast ratios.</p>
        <p>Include assistive technology testing in release cycles to avoid regressions.</p>
        """
    },
    {
        "id": 20,
        "title": "Effective Incident Reviews",
        "author": "SRE Board",
        "date": "2025-02-01",
        "content": """
        <p>Post-incident reviews should focus on facts and systemic improvements rather than blame.</p>
        <p>Create clear action items and track them to closure to reduce repeat incidents.</p>
        """
    },
    {
        "id": 21,
        "title": "Progressive Delivery Techniques",
        "author": "Release Team",
        "date": "2024-04-18",
        "content": """
        <p>Progressive delivery reduces risk by gradually exposing changes to subsets of users via canary or feature flags.</p>
        <p>Combine with strong observability to detect regressions early during rollout.</p>
        """
    },
    {
        "id": 22,
        "title": "Maintaining Large Codebases",
        "author": "Arch Council",
        "date": "2023-06-07",
        "content": """
        <p>Large codebases require modularity and clear ownership boundaries. Automated tests and refactoring reduce technical debt.</p>
        <p>Encourage lightweight design docs to help onboard new contributors effectively.</p>
        """
    },
    {
        "id": 23,
        "title": "Serverless Trade-offs",
        "author": "Cloud Team",
        "date": "2022-11-14",
        "content": """
        <p>Serverless reduces operational burden but introduces cold starts and vendor lock-in considerations.</p>
        <p>Evaluate costs and performance trade-offs for each workload before a serverless adoption.</p>
        """
    },
    {
        "id": 24,
        "title": "Practical Experimentation in Product Teams",
        "author": "Product Insights",
        "date": "2024-05-05",
        "content": """
        <p>Experiments guide product decisions. Define success metrics and ensure statistical validity before shipping changes broadly.</p>
        <p>Small, rapid experiments reduce time-to-learning and inform higher confidence decisions.</p>
        """
    },
    {
        "id": 25,
        "title": "Secure Defaults: A Developer's Guide",
        "author": "SecOps",
        "date": "2025-01-28",
        "content": """
        <p>Secure defaults reduce the chance of misconfiguration. Use least privilege principles for services and storage.</p>
        <p>Automate policy checks to prevent insecure settings from reaching production.</p>
        """
    },
    {
        "id": 26,
        "title": "Efficient Frontend Architectures",
        "author": "UI Team",
        "date": "2023-10-09",
        "content": """
        <p>Frontend performance impacts conversions. Use code-splitting, image optimization, and caching to keep pages snappy.</p>
        <p>Measure real user metrics to prioritise frontend improvements with the most user impact.</p>
        """
    },
    {
        "id": 27,
        "title": "Message Queues: Patterns and Anti-patterns",
        "author": "Messaging Lab",
        "date": "2024-12-12",
        "content": """
        <p>Message queues enable asynchronous workflows but introduce complexity in delivery guarantees and ordering.</p>
        <p>Design idempotent consumers and consider dead-letter queues for robust error handling.</p>
        """
    },
    {
        "id": 28,
        "title": "Building Reliable Backups",
        "author": "Storage Team",
        "date": "2022-03-19",
        "content": """
        <p>Backups are vital. Verify restores regularly and test backup procedures under different failure scenarios.</p>
        <p>Consider retention policies and offsite copies to protect against regional failures.</p>
        """
    },
    {
        "id": 29,
        "title": "Designing Effective Onboarding",
        "author": "People Ops",
        "date": "2024-08-01",
        "content": """
        <p>A thoughtful onboarding process accelerates new hire productivity. Provide clear checklists, mentors, and small early wins.</p>
        <p>Gather feedback to continuously improve the onboarding experience for diverse backgrounds.</p>
        """
    },
    {
        "id": 30,
        "title": "Feature Flagging at Scale",
        "author": "Flags Team",
        "date": "2025-03-02",
        "content": """
        <p>Feature flags enable controlled rollouts and quick rollbacks. Maintain a lifecycle for flags to avoid accumulation.</p>
        <p>Use flagging to run experiments and reduce deployment risks while ensuring flags are removed when no longer needed.</p>
        """
    },
    {
        "id": 31,
        "title": "Hybrid Cloud Strategies",
        "author": "Cloud Architects",
        "date": "2023-04-22",
        "content": """
        <p>Hybrid cloud combines on-prem and public cloud resources to balance control and scalability.</p>
        <p>Network connectivity and consistent tooling are key to a successful hybrid strategy.</p>
        """
    },
    {
        "id": 32,
        "title": "Efficient Logging Practices",
        "author": "Observability Team",
        "date": "2024-09-28",
        "content": """
        <p>Log volume can grow rapidly; prioritise structured logs and appropriate levels to manage costs and signal quality.</p>
        <p>Enrich logs with context like request IDs to correlate with traces and metrics.</p>
        """
    },
    {
        "id": 33,
        "title": "Designing for Internationalisation",
        "author": "Global UX",
        "date": "2022-07-06",
        "content": """
        <p>Internationalisation requires planning for text expansion, date formats, and right-to-left scripts.</p>
        <p>Separate content from layout and test with representative locales early in the design process.</p>
        """
    },
    {
        "id": 34,
        "title": "Service Level Objectives: A Pragmatic Approach",
        "author": "SRE Council",
        "date": "2024-01-16",
        "content": """
        <p>SLOs focus teams on measurable service quality. Keep them simple, actionable, and tied to user experience.</p>
        <p>Use error budgets to balance innovation and reliability work.</p>
        """
    },
    {
        "id": 35,
        "title": "Practical API Versioning Strategies",
        "author": "API Team",
        "date": "2021-12-11",
        "content": """
        <p>API versioning protects consumers from breaking changes. Use semantic strategies and clear migration paths.</p>
        <p>Deprecate older versions with ample notice and tooling to help consumers migrate smoothly.</p>
        """
    },
    {
        "id": 36,
        "title": "Hybrid Testing: Unit, Integration, E2E",
        "author": "QA Collective",
        "date": "2023-02-27",
        "content": """
        <p>A balanced test pyramid uses unit tests for fast feedback, integration tests for subsystem correctness, and E2E tests for user flows.</p>
        <p>Automate tests in CI and prioritise flakiness reduction to maintain developer trust in the test suite.</p>
        """
    },
    {
        "id": 37,
        "title": "Practical Observability Case Studies",
        "author": "Ops Stories",
        "date": "2024-06-01",
        "content": """
        <p>Case studies demonstrate how observability prevented or shortened incidents. Combining traces and metrics yields fast root cause identification.</p>
        <p>Investments in dashboards and alerting paid off in measurable MTTR improvements.</p>
        """
    },
    {
        "id": 38,
        "title": "Modern Authentication Patterns",
        "author": "Identity Team",
        "date": "2024-10-05",
        "content": """
        <p>Authentication patterns such as OAuth2 and OIDC provide modern, standardised approaches for delegated identity.</p>
        <p>Implement refresh token rotations and secure storage to reduce token theft risks.</p>
        """
    },
    {
        "id": 39,
        "title": "Practical Machine Learning Pipelines",
        "author": "ML Ops",
        "date": "2025-05-04",
        "content": """
        <p>ML pipelines require robust data validation, feature stores, and model monitoring to remain reliable in production.</p>
        <p>Plan for retraining pipelines and drift detection to maintain prediction quality over time.</p>
        """
    },
    {
        "id": 40,
        "title": "GraphQL: When and When Not",
        "author": "API Guild",
        "date": "2022-05-17",
        "content": """
        <p>GraphQL offers flexible queries but can complicate caching and introspection. Evaluate based on client needs and team experience.</p>
        <p>Use persisted queries and schema governance to manage complexity at scale.</p>
        """
    },
    {
        "id": 41,
        "title": "Practical Feature Engineering",
        "author": "Data Eng",
        "date": "2023-11-08",
        "content": """
        <p>Feature engineering is often the most impactful step in ML workflows. Prioritise features that generalise and are easy to compute at inference time.</p>
        <p>Track lineage and transformations to ensure reproducibility of models in production.</p>
        """
    },
    {
        "id": 42,
        "title": "Maintaining Small Teams, Big Impact",
        "author": "People Ops",
        "date": "2024-03-12",
        "content": """
        <p>Small teams can move fast with strong autonomy and clear goals. Emphasise shared ownership and lightweight processes.</p>
        <p>Invest in synchronous communication channels when rapid decisions are needed and document to preserve knowledge.</p>
        """
    },
    {
        "id": 43,
        "title": "Reliable Feature Rollouts",
        "author": "Release Team",
        "date": "2024-08-29",
        "content": """
        <p>Feature rollouts should be observable and reversible. Combine metrics with user targeting to validate feature behavior.</p>
        <p>Keep rollback procedures rehearsed to avoid panic during regressions.</p>
        """
    },
    {
        "id": 44,
        "title": "Practical Data Pipelines: From Source to Sink",
        "author": "ETL Group",
        "date": "2025-02-20",
        "content": """
        <p>Data pipelines should be resilient to schema changes and intermittent upstream failures. Use idempotent processing where possible.</p>
        <p>Monitor data freshness and set alerts for delays to detect pipeline regressions quickly.</p>
        """
    },
    {
        "id": 45,
        "title": "Ethical Considerations in AI",
        "author": "Ethics Board",
        "date": "2023-01-15",
        "content": """
        <p>AI systems can have unintended social impacts. Prioritise fairness, accountability, and transparency when designing models.</p>
        <p>Human-in-the-loop review and clear documentation help identify and mitigate harmful outcomes.</p>
        """
    },
    {
        "id": 46,
        "title": "Practical Cost-Effective Caching",
        "author": "Cache Team",
        "date": "2024-11-30",
        "content": """
        <p>Cost-effective caching balances hit rate and storage costs. Use analytics to identify high-impact cache candidates.</p>
        <p>Combine edge caches with origin caching strategies for static and dynamic content.</p>
        """
    },
    {
        "id": 47,
        "title": "Performance Budgets for Reliable UX",
        "author": "UX Perf",
        "date": "2022-09-09",
        "content": """
        <p>Performance budgets set measurable goals for frontend performance to prevent regressions over time.</p>
        <p>Integrate budgets into CI pipelines and block merges that would violate them without justification.</p>
        """
    },
    {
        "id": 48,
        "title": "Service Mesh: Benefits and Costs",
        "author": "Infra Team",
        "date": "2024-06-30",
        "content": """
        <p>Service meshes offer observability and traffic control but add operational complexity and resource overhead.</p>
        <p>Evaluate needs for mTLS, traffic shaping, and telemetry before adopting a mesh across the platform.</p>
        """
    },
    {
        "id": 49,
        "title": "Design Systems: Consistency at Scale",
        "author": "Design Ops",
        "date": "2023-07-21",
        "content": """
        <p>Design systems create a shared language across products and teams. Maintain clear contribution patterns and versioning.</p>
        <p>Balance consistency with flexibility to avoid stifling product differentiation.</p>
        """
    },
    {
        "id": 50,
        "title": "Measuring Developer Productivity",
        "author": "Eng Leads",
        "date": "2025-05-01",
        "content": """
        <p>Developer productivity is multi-dimensional; focus on outcomes rather than raw metrics. Combine qualitative feedback with objective measures.</p>
        <p>Reduce friction in development workflows through tooling and clear documentation to improve long-term velocity.</p>
        """
    }
]

def strip_tags(text: str) -> str:
    # naive HTML tag stripper for excerpts
    return re.sub(r"<[^>]+>", "", text or "")

def excerpt_for(content: str, q: str, radius: int = 80) -> str:
    plain = strip_tags(content)
    if not q:
        return (plain[:240] + "...") if len(plain) > 240 else plain
    idx = plain.lower().find(q.lower())
    if idx == -1:
        return (plain[:240] + "...") if len(plain) > 240 else plain
    start = max(0, idx - radius)
    end = min(len(plain), idx + len(q) + radius)
    snippet = plain[start:end]
    if start > 0:
        snippet = "..." + snippet
    if end < len(plain):
        snippet = snippet + "..."
    return snippet

@app.route("/")
def index():
    return render_template("index.html", articles=ARTICLES)

@app.route("/article/<int:aid>")
def article(aid):
    article = next((a for a in ARTICLES if a["id"] == aid), None)
    if not article:
        return render_template("404.html"), 404
    return render_template("article.html", article=article)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        q = request.form.get("q", "")
        return redirect(url_for("results", q=q))
    return render_template("search.html")

@app.route("/results")
def results():
    # Keep SSTI vulnerability (rendering user-supplied template) while also performing a real search.
    q = request.args.get("q", "") or ""
    # produce vulnerable preview (intentional)
    try:
        rendered = render_template_string(q)
    except Exception as e:
        rendered = f"<pre>Render error: {html.escape(str(e))}</pre>"

    # perform simple case-insensitive search over title, author, content
    matches = []
    q_lower = q.lower()
    for a in ARTICLES:
        hay = " ".join([a.get("title", ""), a.get("author", ""), strip_tags(a.get("content", ""))]).lower()
        if not q or q_lower in hay:
            matches.append({
                "id": a["id"],
                "title": a["title"],
                "author": a["author"],
                "date": a["date"],
                "excerpt": excerpt_for(a.get("content", ""), q)
            })

    # sort matches by date descending (recent first) if date present
    try:
        matches.sort(key=lambda x: x.get("date", ""), reverse=True)
    except Exception:
        pass

    return render_template("results.html", q=q, rendered=rendered, matches=matches)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4002, debug=True)
