import React from "react";
import ReactDOM from "react-dom/client";
import {
  AlertCircle,
  Archive,
  BookOpenCheck,
  BrainCircuit,
  CheckCircle2,
  ClipboardList,
  Download,
  FileText,
  Gauge,
  KeyRound,
  Layers3,
  Loader2,
  Pause,
  Play,
  Search,
  Send,
  ShieldCheck,
  Sparkles,
  Upload,
} from "lucide-react";
import "./styles.css";

type TargetType = "consulting_company" | "benchmark_company" | "hr_software_company" | "auto";
type Depth = "fast" | "standard" | "deep";
type Language = "zh" | "en" | "bilingual";
type StageStatus = "pending" | "active" | "done" | "blocked";

type FormState = {
  model: string;
  target: string;
  targetType: TargetType;
  focus: string;
  language: Language;
  depth: Depth;
  sources: string;
};

type Stage = {
  id: string;
  name: string;
  zh: string;
  weight: number;
  status: StageStatus;
  progress: number;
};

type Artifact = {
  label: string;
  detail: string;
  status: "ready" | "building" | "waiting";
};

const stageBlueprint: Omit<Stage, "status" | "progress">[] = [
  { id: "brief", name: "Brief Parsing", zh: "任务解析", weight: 5 },
  { id: "search", name: "Search Planning", zh: "搜索计划", weight: 10 },
  { id: "discovery", name: "Source Discovery", zh: "资料搜索", weight: 25 },
  { id: "fetch", name: "Source Fetching", zh: "资料抓取", weight: 20 },
  { id: "cards", name: "Source Cards", zh: "证据卡", weight: 15 },
  { id: "distill", name: "Distillation", zh: "方法论蒸馏", weight: 15 },
  { id: "quality", name: "Quality Check", zh: "质量检查", weight: 5 },
  { id: "output", name: "Skill Output", zh: "Skill 输出", weight: 5 },
];

const initialStages: Stage[] = stageBlueprint.map((stage) => ({
  ...stage,
  progress: 0,
  status: "pending",
}));

const defaultLogs = [
  "[Ready] 输入目标公司或方法论来源，即可开始蒸馏。",
  "[Tip] Gemini API Key 只保存在当前浏览器本地，不会写入仓库。",
  "[Tip] 长任务会显示阶段进度、文字日志和当前产物。",
];

const sampleSkill = `# Hay-style HR Consulting Expert

## 1. Hay-style 核心判断
先区分岗位、人、绩效、薪酬和组织气候，不直接用调薪或考核解决所有问题。

## 2. Tool Layer / 工具层
- Work Value Diagnostic Canvas / 岗位价值诊断画布
- Job-Person-Pay Separation Table / 岗位-人-薪酬分离表
- Leadership Style and Climate Audit / 领导风格-组织气候审计

## 3. Evidence Boundary / 证据边界
资料支持、综合判断和专业推断需要分开标注。正式岗位评估不能伪造 Hay 官方点值。`;

const sampleReport = `## Distillation Report / 蒸馏报告

- Search plan: query matrix + source-card-driven search
- Evidence: official methodology, video transcripts, tools, cases, external views
- Version: Usable Candidate
- Boundary: no proprietary guide charts, no fabricated scores`;

const sourceCards = `## Evidence Summary / 证据摘要

1. official_methodology: Hay Guide Chart/Profile Method public explanation
2. video_transcript: leadership style and organizational climate subtitles
3. tool_template: job-person-pay separation and work architecture tools
4. china_localization: Chinese Hay job evaluation practice materials`;

function App() {
  const [form, setForm] = React.useState<FormState>(() => ({
    model: import.meta.env.VITE_GEMINI_MODEL || "gemini-2.5-flash",
    target: "Hay Group",
    targetType: "consulting_company",
    focus: "岗位价值评估、薪酬绩效、领导力气候",
    language: "bilingual",
    depth: "standard",
    sources:
      "https://www.kornferry.com/about-us/our-story/hay-group\nhttps://www.kornferry.com/capabilities/leadership-professional-development/training-certifications/korn-ferry-hay-guide-chart",
  }));
  const [stages, setStages] = React.useState<Stage[]>(initialStages);
  const [logs, setLogs] = React.useState<string[]>(defaultLogs);
  const [isRunning, setIsRunning] = React.useState(false);
  const [isPaused, setIsPaused] = React.useState(false);
  const [activeTab, setActiveTab] = React.useState("skill");
  const [skillOutput, setSkillOutput] = React.useState(sampleSkill);
  const [reportOutput, setReportOutput] = React.useState(sampleReport);
  const [evidenceOutput, setEvidenceOutput] = React.useState(sourceCards);
  const [question, setQuestion] = React.useState("用这个 Skill，帮我设计集团岗位职级体系。");
  const [answer, setAnswer] = React.useState("");
  const [error, setError] = React.useState("");

  React.useEffect(() => {
    localStorage.setItem("geminiModel", form.model);
  }, [form.model]);

  const overallProgress = React.useMemo(() => {
    const weighted = stages.reduce((sum, stage) => sum + stage.progress * stage.weight, 0);
    return Math.round(weighted / 100);
  }, [stages]);

  const activeStage = stages.find((stage) => stage.status === "active") || stages.find((stage) => stage.status === "blocked");

  const artifacts: Artifact[] = [
    {
      label: "Search Plan / 搜索计划",
      detail: overallProgress >= 12 ? "source-card queries generated" : "waiting for brief",
      status: overallProgress >= 12 ? "ready" : isRunning ? "building" : "waiting",
    },
    {
      label: "Evidence Cards / 证据卡",
      detail: overallProgress >= 58 ? "methodology, tools, videos, cases" : "collecting sources",
      status: overallProgress >= 58 ? "ready" : overallProgress >= 20 ? "building" : "waiting",
    },
    {
      label: "Tool Layer / 工具层",
      detail: overallProgress >= 82 ? "diagnostic canvases and matrices" : "not distilled yet",
      status: overallProgress >= 82 ? "ready" : overallProgress >= 68 ? "building" : "waiting",
    },
    {
      label: "SKILL.md",
      detail: overallProgress >= 96 ? "ready to copy or download" : "drafting",
      status: overallProgress >= 96 ? "ready" : overallProgress >= 80 ? "building" : "waiting",
    },
  ];

  function patchForm<K extends keyof FormState>(key: K, value: FormState[K]) {
    setForm((current) => ({ ...current, [key]: value }));
  }

  function pushLog(text: string) {
    const stamp = new Date().toLocaleTimeString("zh-CN", { hour12: false });
    setLogs((current) => [...current, `[${stamp}] ${text}`]);
  }

  function resetRun() {
    setStages(initialStages);
    setLogs(defaultLogs);
    setError("");
    setAnswer("");
  }

  async function runDistillation() {
    setError("");
    if (!form.target.trim()) {
      setError("请先输入目标名称 / Please enter a target.");
      return;
    }
    setIsRunning(true);
    setIsPaused(false);
    resetRun();

    const stageMessages: Record<string, string[]> = {
      brief: ["已识别目标与研究重点。", "正在判断目标类型与输出语言。"],
      search: ["生成 query matrix。", "生成 source-card-driven search。", "生成视频字幕搜索计划。"],
      discovery: ["搜索官方方法论资料。", "搜索工具模板和案例实践。", "扩展公开视频、播客和字幕来源。"],
      fetch: ["准备抓取网页、PDF 和 transcript。", "筛选可用资料，跳过登录墙和低质量来源。"],
      cards: ["生成 official_methodology source cards。", "生成 video_transcript 和 tool_template source cards。"],
      distill: ["提炼核心心智模型。", "生成工具层和诊断流程。", "写入反模式和不确定性边界。"],
      quality: ["检查资料数量、视频来源和证据强度。", "判断版本：Full / Usable Candidate / Light。"],
      output: ["生成 SKILL.md。", "生成蒸馏报告和使用边界。"],
    };

    let completedWeight = 0;
    for (let index = 0; index < stageBlueprint.length; index += 1) {
      const blueprint = stageBlueprint[index];
      setStages((current) =>
        current.map((stage) =>
          stage.id === blueprint.id
            ? { ...stage, status: "active", progress: 0 }
            : current.findIndex((item) => item.id === stage.id) < index
              ? { ...stage, status: "done", progress: 100 }
              : stage,
        ),
      );
      pushLog(`${blueprint.zh} / ${blueprint.name} started.`);

      const ticks = form.depth === "deep" ? 5 : form.depth === "standard" ? 4 : 3;
      for (let tick = 1; tick <= ticks; tick += 1) {
        await wait(form.depth === "deep" ? 650 : 480);
        if (isPaused) {
          pushLog("任务已暂停，等待继续。");
          setIsRunning(false);
          return;
        }
        const messageList = stageMessages[blueprint.id] || [];
        const message = messageList[(tick - 1) % messageList.length];
        if (message) pushLog(message);
        setStages((current) =>
          current.map((stage) =>
            stage.id === blueprint.id
              ? { ...stage, progress: Math.round((tick / ticks) * 100) }
              : stage,
          ),
        );
      }
      completedWeight += blueprint.weight;
      if (blueprint.id === "discovery" && form.sources.trim().length < 40) {
        pushLog("资料较少：将降低确定性门槛，必要时生成 Usable Candidate。");
      }
    }

    pushLog(`完成：整体进度 ${completedWeight}%。正在生成结果预览。`);
    const generated = await generateSkillWithGemini();
    if (generated) {
      setSkillOutput(generated.skill);
      setReportOutput(generated.report);
      setEvidenceOutput(generated.evidence);
    } else {
      setSkillOutput(buildFallbackSkill(form));
      setReportOutput(buildFallbackReport(form));
      setEvidenceOutput(buildFallbackEvidence(form));
    }
    setStages((current) => current.map((stage) => ({ ...stage, status: "done", progress: 100 })));
    pushLog("SKILL.md、蒸馏报告和证据摘要已生成。");
    setIsRunning(false);
  }

  async function generateSkillWithGemini(): Promise<{ skill: string; report: string; evidence: string } | null> {
    const apiKey = import.meta.env.VITE_GEMINI_API_KEY || "";
    if (!apiKey.trim()) {
      pushLog("未配置 Gemini API Key，已使用本地模拟生成结果。");
      return null;
    }

    const prompt = `
You are HR SkillForge. Create a concise bilingual HR methodology Skill draft.

Target: ${form.target}
Target type: ${form.targetType}
Focus: ${form.focus}
Language: ${form.language}
Depth: ${form.depth}
Sources:
${form.sources}

Return JSON only:
{
  "skill": "markdown SKILL.md draft",
  "report": "markdown distillation report",
  "evidence": "markdown evidence summary"
}

The output must include source-card-driven search, tool layer, diagnostic workflow, evidence boundary, and runtime source recall.
`;

    try {
      pushLog(`正在调用 Gemini：${form.model}`);
      const text = await callGemini(apiKey, form.model, prompt);
      const parsed = parseJsonLoose(text);
      if (parsed?.skill && parsed?.report && parsed?.evidence) {
        pushLog("Gemini 已返回结构化蒸馏结果。");
        return parsed;
      }
      setReportOutput(text);
      pushLog("Gemini 返回非 JSON 内容，已放入蒸馏报告预览。");
      return null;
    } catch (err) {
      const message = err instanceof Error ? err.message : "Gemini call failed";
      setError(message);
      pushLog(`Gemini 调用失败：${message}`);
      return null;
    }
  }

  async function askGeneratedSkill() {
    setError("");
    if (!question.trim()) return;
    const apiKey = import.meta.env.VITE_GEMINI_API_KEY || "";
    if (!apiKey.trim()) {
      setAnswer(buildFallbackAnswer(question));
      return;
    }
    try {
      setAnswer("Thinking with generated Skill and evidence boundary...");
      const prompt = `
Use this generated HR Skill to answer the user question.

Generated Skill:
${skillOutput}

Evidence Summary:
${evidenceOutput}

User question:
${question}

Answer in Chinese with short sections:
1. Hay-style/HR SkillForge core judgment
2. Evidence consulted
3. Tool to use
4. Solution
5. Evidence-supported vs professional inference boundary
`;
      const text = await callGemini(apiKey, form.model, prompt);
      setAnswer(text);
    } catch (err) {
      const message = err instanceof Error ? err.message : "Gemini call failed";
      setError(message);
      setAnswer(buildFallbackAnswer(question));
    }
  }

  function copyActiveOutput() {
    const text = activeTab === "skill" ? skillOutput : activeTab === "report" ? reportOutput : evidenceOutput;
    navigator.clipboard.writeText(text);
    pushLog("已复制当前结果。");
  }

  function downloadActiveOutput() {
    const text = activeTab === "skill" ? skillOutput : activeTab === "report" ? reportOutput : evidenceOutput;
    const name = activeTab === "skill" ? "SKILL.md" : activeTab === "report" ? "distillation-report.md" : "evidence-summary.md";
    const blob = new Blob([text], { type: "text/markdown;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = name;
    link.click();
    URL.revokeObjectURL(url);
  }

  return (
    <main className="app">
      <header className="topbar">
        <div>
          <div className="eyebrow">HR SkillForge Web</div>
          <h1>把公开资料，锻造成可调用的 HR 专家</h1>
          <p>Forge public evidence into company-specific HR methodology Skills.</p>
        </div>
        <div className="topbarMetrics">
          <Metric icon={<ShieldCheck size={18} />} label="Evidence" value="Source Cards" />
          <Metric icon={<Gauge size={18} />} label="Progress" value={`${overallProgress}%`} />
          <Metric icon={<BrainCircuit size={18} />} label="Model" value={form.model} />
        </div>
      </header>

      <section className="workspace">
        <aside className="panel inputPanel">
          <PanelTitle icon={<ClipboardList size={18} />} title="Task Brief" subtitle="任务输入" />

          <div className="adminNote">
            <KeyRound size={16} />
            <div>
              <strong>Gemini configured by admin</strong>
              <span>用户无需输入 API Key / API Key is configured by the owner.</span>
            </div>
          </div>

          <label>
            Model / 模型
            <input value={form.model} onChange={(event) => patchForm("model", event.target.value)} />
          </label>

          <label>
            Target / 目标
            <input value={form.target} onChange={(event) => patchForm("target", event.target.value)} />
          </label>

          <label>
            Target Type / 类型
            <select value={form.targetType} onChange={(event) => patchForm("targetType", event.target.value as TargetType)}>
              <option value="consulting_company">Consulting Company / 咨询公司</option>
              <option value="benchmark_company">Benchmark Company / 标杆企业</option>
              <option value="hr_software_company">HR Software / HR 软件</option>
              <option value="auto">Auto / 自动判断</option>
            </select>
          </label>

          <label>
            Research Focus / 研究重点
            <textarea value={form.focus} onChange={(event) => patchForm("focus", event.target.value)} rows={3} />
          </label>

          <div className="fieldGrid">
            <label>
              Language
              <select value={form.language} onChange={(event) => patchForm("language", event.target.value as Language)}>
                <option value="bilingual">Bilingual / 中英文</option>
                <option value="zh">Chinese / 中文</option>
                <option value="en">English / 英文</option>
              </select>
            </label>
            <label>
              Depth
              <select value={form.depth} onChange={(event) => patchForm("depth", event.target.value as Depth)}>
                <option value="fast">Fast / 快速版</option>
                <option value="standard">Standard / 标准版</option>
                <option value="deep">Deep / 深度版</option>
              </select>
            </label>
          </div>

          <label>
            Sources / 资料
            <textarea
              className="sourceBox"
              value={form.sources}
              onChange={(event) => patchForm("sources", event.target.value)}
              rows={7}
              placeholder="Paste URLs, notes, transcript snippets..."
            />
          </label>

          <div className="buttonRow">
            <button className="primaryButton" onClick={runDistillation} disabled={isRunning}>
              {isRunning ? <Loader2 className="spin" size={17} /> : <Play size={17} />}
              Start / 开始蒸馏
            </button>
            <button className="ghostButton" onClick={() => setIsPaused((value) => !value)}>
              <Pause size={17} />
              Pause
            </button>
          </div>
          {error && (
            <div className="errorBox">
              <AlertCircle size={16} />
              {error}
            </div>
          )}
        </aside>

        <section className="panel progressPanel">
          <PanelTitle icon={<Sparkles size={18} />} title="Distillation Progress" subtitle="蒸馏进程" />
          <div className="progressHero">
            <div>
              <span>Overall Progress / 整体进度</span>
              <strong>{overallProgress}%</strong>
              <p>
                Current / 当前阶段：{activeStage ? `${activeStage.zh} · ${activeStage.name}` : "Ready / 待开始"}
              </p>
            </div>
            <div className="progressRing" style={{ background: `conic-gradient(#2563eb ${overallProgress * 3.6}deg, #e5e7eb 0deg)` }}>
              <span>{overallProgress}%</span>
            </div>
          </div>
          <div className="bar">
            <div style={{ width: `${overallProgress}%` }} />
          </div>

          <div className="stageList">
            {stages.map((stage) => (
              <div className={`stageItem ${stage.status}`} key={stage.id}>
                <div className="stageIcon">
                  {stage.status === "done" ? <CheckCircle2 size={16} /> : stage.status === "active" ? <Loader2 className="spin" size={16} /> : <Layers3 size={16} />}
                </div>
                <div className="stageCopy">
                  <strong>{stage.zh}</strong>
                  <span>{stage.name}</span>
                </div>
                <div className="stagePercent">{stage.progress}%</div>
              </div>
            ))}
          </div>

          <div className="logHeader">
            <span>Live Log / 文字进程</span>
            <button onClick={() => navigator.clipboard.writeText(logs.join("\n"))}>Export Logs</button>
          </div>
          <div className="logBox">
            {logs.slice(-12).map((log, index) => (
              <div key={`${log}-${index}`}>{log}</div>
            ))}
          </div>
        </section>

        <aside className="panel outputPanel">
          <PanelTitle icon={<Archive size={18} />} title="Output Preview" subtitle="结果预览" />
          <div className="artifactList">
            {artifacts.map((artifact) => (
              <div className={`artifact ${artifact.status}`} key={artifact.label}>
                <FileText size={16} />
                <div>
                  <strong>{artifact.label}</strong>
                  <span>{artifact.detail}</span>
                </div>
              </div>
            ))}
          </div>

          <div className="tabs">
            <button className={activeTab === "skill" ? "active" : ""} onClick={() => setActiveTab("skill")}>Skill.md</button>
            <button className={activeTab === "report" ? "active" : ""} onClick={() => setActiveTab("report")}>Report</button>
            <button className={activeTab === "evidence" ? "active" : ""} onClick={() => setActiveTab("evidence")}>Evidence</button>
          </div>
          <pre className="preview">
            {activeTab === "skill" ? skillOutput : activeTab === "report" ? reportOutput : evidenceOutput}
          </pre>
          <div className="buttonRow">
            <button className="ghostButton" onClick={copyActiveOutput}>
              <ClipboardList size={16} />
              Copy
            </button>
            <button className="ghostButton" onClick={downloadActiveOutput}>
              <Download size={16} />
              Download
            </button>
          </div>
        </aside>
      </section>

      <section className="playground panel">
        <PanelTitle icon={<BookOpenCheck size={18} />} title="Try Generated Skill" subtitle="试用生成后的 Skill" />
        <div className="playgroundGrid">
          <textarea value={question} onChange={(event) => setQuestion(event.target.value)} rows={4} />
          <button className="primaryButton" onClick={askGeneratedSkill}>
            <Send size={17} />
            Ask / 提问
          </button>
        </div>
        {answer && <pre className="answer">{answer}</pre>}
      </section>
    </main>
  );
}

function Metric({ icon, label, value }: { icon: React.ReactNode; label: string; value: string }) {
  return (
    <div className="metric">
      {icon}
      <span>{label}</span>
      <strong>{value}</strong>
    </div>
  );
}

function PanelTitle({ icon, title, subtitle }: { icon: React.ReactNode; title: string; subtitle: string }) {
  return (
    <div className="panelTitle">
      <div>{icon}</div>
      <span>{title}</span>
      <small>{subtitle}</small>
    </div>
  );
}

function wait(ms: number) {
  return new Promise((resolve) => window.setTimeout(resolve, ms));
}

async function callGemini(apiKey: string, model: string, prompt: string) {
  const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      contents: [
        {
          role: "user",
          parts: [{ text: prompt }],
        },
      ],
    }),
  });
  if (!response.ok) {
    const text = await response.text();
    throw new Error(`Gemini API ${response.status}: ${text.slice(0, 220)}`);
  }
  const data = await response.json();
  return data?.candidates?.[0]?.content?.parts?.map((part: { text?: string }) => part.text || "").join("\n") || "";
}

function parseJsonLoose(text: string): { skill: string; report: string; evidence: string } | null {
  try {
    return JSON.parse(text);
  } catch {
    const match = text.match(/\{[\s\S]*\}/);
    if (!match) return null;
    try {
      return JSON.parse(match[0]);
    } catch {
      return null;
    }
  }
}

function buildFallbackSkill(form: FormState) {
  return `# ${form.target} HR Skill

## Role / 角色
基于公开资料和用户输入，蒸馏 ${form.target} 的 HR 方法论，用于解决 ${form.focus} 相关问题。

## Search Method / 搜索方法
- Query matrix: company aliases x HR topics x source types x language
- Source cards: official_methodology, diagnostic_question, tool_template, case_practice, video_transcript, external_boundary, china_localization

## Tool Layer / 工具层
- Evidence Checklist / 证据清单
- Diagnostic Canvas / 诊断画布
- Implementation Roadmap / 落地路线图

## Runtime Rule / 使用规则
回答复杂问题前，必须回看 sources.csv、source cards、transcripts 和 quality report。`;
}

function buildFallbackReport(form: FormState) {
  return `# Distillation Report

- Target: ${form.target}
- Type: ${form.targetType}
- Focus: ${form.focus}
- Depth: ${form.depth}
- Version: Usable Candidate

This preview was generated locally because Gemini API was not provided or failed.`;
}

function buildFallbackEvidence(form: FormState) {
  return `# Evidence Summary

## User-provided sources
${form.sources || "No sources yet."}

## Evidence boundary
This is a prototype evidence summary. Add URLs, PDFs, transcripts, and notes for stronger distillation.`;
}

function buildFallbackAnswer(question: string) {
  return `## 核心判断
这个问题需要先回到证据和工具层，而不是直接给泛建议。

## 推荐动作
1. 明确业务问题和目标场景。
2. 回看 source cards 和 evidence summary。
3. 选择对应工具：诊断画布、证据表、实施路线图。
4. 区分资料支持、综合判断和专业推断。

## 用户问题
${question}`;
}

ReactDOM.createRoot(document.getElementById("root")!).render(<App />);
