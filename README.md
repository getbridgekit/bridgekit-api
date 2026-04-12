# Bridgekit API

A REST API wrapper around [Bridgekit](https://github.com/getbridgekit/bridgekit) — AI tools that make you a better data scientist.

## Base URL

```
https://bridgekit-api.onrender.com
```

## Authentication

All endpoints require your Anthropic API key passed in the request header:

```
X-Anthropic-Api-Key: your-anthropic-key
```

You can get an Anthropic API key at [console.anthropic.com](https://console.anthropic.com).

---

## Endpoints

### `POST /evaluate`

Review a data science write-up across four dimensions: clarity, statistical rigor, methodology, and business impact.

**Request:**
```json
{
  "text": "Your analysis write-up here."
}
```

**Example:**
```bash
curl -X POST https://bridgekit-api.onrender.com/evaluate \
  -H "Content-Type: application/json" \
  -H "X-Anthropic-Api-Key: $ANTHROPIC_API_KEY" \
  -d '{"text": "Users who used the reporting feature were 3x more likely to upgrade."}'
```

---

### `POST /plan`

Get a structured analytical plan before you start your analysis.

**Request:**
```json
{
  "question": "Did our new onboarding flow reduce churn?",
  "data_description": "A/B test with 1,000 users, tracking upgrade status and time to upgrade.",
  "goal": "causal inference"
}
```

`data_description` and `goal` are optional.

**Example:**
```bash
curl -X POST https://bridgekit-api.onrender.com/plan \
  -H "Content-Type: application/json" \
  -H "X-Anthropic-Api-Key: $ANTHROPIC_API_KEY" \
  -d '{"question": "Did our new onboarding flow reduce churn?"}'
```

---

### `POST /ask`

Ask a question against a block of text or your past reports.

**Request:**
```json
{
  "question": "What drove churn in Q3?",
  "text": "Optional raw text to search against."
}
```

**Example:**
```bash
curl -X POST https://bridgekit-api.onrender.com/ask \
  -H "Content-Type: application/json" \
  -H "X-Anthropic-Api-Key: $ANTHROPIC_API_KEY" \
  -d '{"question": "What drove churn in Q3?", "text": "Q3 churn rose to 4.5%, driven by a product outage in August."}'
```

---

## Interactive Docs

Visit [bridgekit-api.onrender.com/docs](https://bridgekit-api.onrender.com/docs) to explore and test all endpoints in the browser.

---

## Notes

- This API is hosted on Render's free tier and may take ~30 seconds to wake up after inactivity.
- Your Anthropic key is used only to process your request and is never stored.
- Built on [FastAPI](https://fastapi.tiangolo.com/).
