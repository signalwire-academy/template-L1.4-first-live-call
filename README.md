# Lab 1.4: First Live Call

**Duration:** 60 minutes
**Level:** 1

## Objectives

Complete this lab to demonstrate your understanding of the concepts covered.

## Prerequisites

- Completed previous labs
- Python 3.10+ with signalwire-agents installed
- Virtual environment activated

## Instructions

### 1. Set Up Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Implement Your Solution

Edit `solution/agent.py` according to the lab requirements:

1. Create an AgentBase instance with a name
2. Add at least one prompt section (e.g., "Role")
3. Configure a language with voice and fillers using `add_language()`
   - Use `speech_fillers` for what the agent says while thinking (e.g., "Um", "Uh")
   - Use `function_fillers` for what the agent says during tool calls (e.g., "One moment please")
   - **Note:** When both `speech_fillers` AND `function_fillers` are provided, they appear as separate fields in the SWML output

### 3. Test Locally

```bash
# List available functions
swaig-test solution/agent.py --list-tools

# Check SWML output
swaig-test solution/agent.py --dump-swml
```

### 4. Submit

```bash
git add solution/agent.py
git commit -m "Complete Lab 1.4: First Live Call"
git push
```

## Grading

| Check | Points |
|-------|--------|
| Agent Instantiation | 20 |
| SWML Generation | 20 |
| Prompt Configured | 20 |
| Language Configured | 20 |
| Speech Fillers | 20 |
| **Total** | **100** |

**Passing Score:** 60%

## Reference

See `reference/starter.py` for a boilerplate template.

---

## Next Assignment

Ready to continue? [**Start Lab 1.7: Build Lookup Function**](https://classroom.github.com/a/sf_Rpj3b)

---

*SignalWire AI Agents Certification*
