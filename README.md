# ⚽ Football Academy Analytics System

> Turning youth football academy data into smart decisions — automated dashboards, player performance PDFs and talent ranking algorithms.

**Built by [Willian Yudy Futema](www.linkedin.com/in/willian-yudy-futema) · IT Student · 2026**

---

## 🎯 What this project does

Most grassroots football academies run on intuition and spreadsheets. This system brings professional-grade data analytics to any academy — for **$0 in tooling costs**.

| Feature | Description |
|---|---|
| 📊 Live Dashboard | Real-time academy metrics via Looker Studio + Google Sheets |
| 📄 Player PDF Reports | Auto-generated, auto-emailed to parents at end of each term |
| 🏆 Talent Ranking | Algorithm scores player growth rate, not just current level |
| ⚠️ At-Risk Alerts | Automated email when student attendance drops below threshold |
| 📈 Lead Source Tracking | See which marketing channel brings paying students |

---

## 🖥️ Interactive Pitch Deck

A fully interactive HTML presentation that explains the system — no framework, no build step, just open in browser.

**→ [View live demo](https://github.com/Willian-Yudy-F)**

Features: keyboard navigation, expandable cards, animated KPIs, custom cursor, fullscreen mode.

---

## 🗂️ Project Structure

```
football-academy-analytics/
│
├── dashboard/
│   └── bfa_relatorio.py         # Main PDF generator + email sender
│
├── corinthians_demo/
│   └── dashboard_corinthians.py # Historical player analytics demo (Plotly)
│
├── pitch/
│   └── football_academy_analytics_demo.html  # This interactive presentation
│
├── sheets/
│   └── template_avaliacoes.csv  # Google Sheets template structure
│
└── README.md
```

---

## ⚙️ Tech Stack

| Layer | Tools |
|---|---|
| Data collection | Google Forms · JotForm |
| Data storage | Google Sheets (free database) |
| Data processing | Python · pandas · gspread |
| PDF generation | ReportLab |
| Email automation | smtplib · Gmail SMTP |
| Dashboard | Looker Studio (free) |
| Data visualisation | Plotly · Chart.js |
| Automation | Google Apps Script |
| Presentation | HTML · CSS · Vanilla JS |

---

## 🚀 Quick Start

### 1. Install dependencies
```bash
pip install gspread google-auth reportlab pandas plotly
```

### 2. Set up Google Sheets credentials
1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Create a project → Enable **Google Sheets API** + **Google Drive API**
3. Create a **Service Account** → download `credentials.json`
4. Share your Google Sheet with the service account email

### 3. Run with demo data (no credentials needed)
```bash
python dashboard/bfa_relatorio.py
# Generates PDFs in ./relatorios_pdf/ using built-in demo data
```

### 4. Run with your real Google Sheets
```bash
# Place credentials.json in project root
# Edit SPREADSHEET_NAME and TERMO_FILTRO in bfa_relatorio.py
python dashboard/bfa_relatorio.py
```

### 5. Enable email sending
```bash
python dashboard/bfa_relatorio.py --enviar
# Generates PDFs + emails each one to parents
```

---

## 📊 Google Sheets Structure

The system expects this column structure in the `Avaliacoes` tab:

| Column | Type | Example |
|---|---|---|
| Nome | text | James Silva |
| Programa | text | Elite |
| Localidade | text | Sydney |
| Termo | text | Term 2 · 2025 |
| Sessao | number | 1 |
| Data | date | 2025-04-15 |
| Controle_bola | 1–10 | 8.5 |
| Passe | 1–10 | 7.0 |
| Drible | 1–10 | 9.0 |
| Finalizacao | 1–10 | 7.5 |
| Posicionamento | 1–10 | 7.5 |
| Leitura_jogo | 1–10 | 7.0 |
| Velocidade | 1–10 | 8.5 |
| Resistencia | 1–10 | 8.0 |
| Atitude | 1–10 | 9.0 |
| Concentracao | 1–10 | 8.0 |
| Trabalho_equipe | 1–10 | 8.5 |
| Presenca | 0 or 1 | 1 |
| Comentario | text | Great session... |
| Email_pais | email | parent@email.com |

---

## 📄 Generated PDF Report

Each student receives a personalised PDF at the end of the term containing:

- ✅ Overall score, attendance %, sessions count
- ✅ Skill bars for 11 technical/tactical attributes
- ✅ Term-over-term delta (▲▼ indicators)
- ✅ Coach's written comment
- ✅ Academy branding and footer

**Example output:** `relatorios_pdf/bfa_james_silva_term_2_2025.pdf`

---

## 🧠 Talent Ranking Algorithm

The growth score is calculated as a weighted average:

```python
score = (technical_avg * 0.50) + (attendance_pct * 0.20) + (attitude_score * 0.30)
```

Key insight: the algorithm ranks **growth rate** between terms, not absolute skill level.  
A player who improved 1.5 points ranks above one who started higher but stagnated.

This is the same principle used by **Brentford FC** — who bought Ollie Watkins for £1.8M and sold for £28M by identifying trajectory over current ability.

---

## 🔔 At-Risk Alert (Apps Script)

Paste this in Google Sheets → Extensions → Apps Script and set a weekly trigger:

```javascript
function alertAtRisk() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet()
    .getSheetByName("Presencas");
  const data = sheet.getDataRange().getValues();

  const atRisk = data.filter(row => {
    const pct = row[/* presenca_col */] / row[/* total_col */];
    return pct < 0.70 && row[/* termo_col */] === "Term 2 · 2025";
  });

  if (atRisk.length === 0) return;

  const body = atRisk.map(r => `• ${r[0]} — ${Math.round(r[/*pct*/] * 100)}% attendance`).join("\n");
  GmailApp.sendEmail(
    "owner@academy.com",
    `⚠️ ${atRisk.length} students at risk of dropping out`,
    `Students with attendance below 70%:\n\n${body}\n\nConsider reaching out before the term ends.`
  );
}
```

---

## 📚 References & Inspiration

| Source | Link |
|---|---|
| Ian Graham — *How to Win the Premier League* (2024) | Book |
| TacticAI: DeepMind + Liverpool — *Nature Communications* (2024) | [Paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10951310/) |
| Brentford data revolution — DreamDataBall (2024) | [Article](https://dreamdataball.substack.com/p/brentford-fc-the-data-driven-revolution) |
| Data analytics in football — Lolli et al. (2024) | [PubMed](https://pubmed.ncbi.nlm.nih.gov/38745403/) |
| Michael Lewis — *Moneyball* (2003) | Book |

---

## 🤝 Contributing

Fork the repo, open a PR or just ⭐ it if you found it useful.  
Suggestions for new features (GPS wearable integration, video analysis connector) are welcome via Issues.

---

## 📝 License

MIT — free to use, adapt and deploy for any academy.

---

*"For David to beat Goliath, he needed to use a different weapon."*  
*— Rasmus Ankersen, Co-Director of Football, Brentford FC*
