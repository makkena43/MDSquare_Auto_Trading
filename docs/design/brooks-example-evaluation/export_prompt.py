"""Export a single answer-free case; never reads the answer key."""
import json
import sys
from pathlib import Path

if len(sys.argv) != 2:
    raise SystemExit("Usage: python3 export_prompt.py CASE_ID")
records = [json.loads(line) for line in Path(__file__).with_name("cases.jsonl").read_text().splitlines()]
matches = [record for record in records if record["case_id"] == sys.argv[1]]
if len(matches) != 1:
    raise SystemExit("Unknown or non-unique case ID")
case = matches[0]
source = case.pop("source_locator")
case["instrument"] = source["instrument"]
case["timeframe"] = source["timeframe"]
print("Use only the evidence below. Do not retrieve the source chart, book commentary or future bars. "
      "Pilot enabled IDs: breakout_pullback_long, breakout_pullback_short, bull_high2, bear_low2, "
      "range_failed_breakout_long, range_failed_breakout_short. Other setups are observation only. "
      "Return JSON fields: decision (CANDIDATE/WAIT/SKIP/INSUFFICIENT_DATA), primary_setup_id, "
      "supporting_evidence, conflicting_evidence, conditional_trigger, invalidation, "
      "target_reference, missing_data, execution_ready. Do not invent exact prices, "
      "win probabilities or fills. CANDIDATE is a conditional qualitative idea; execution_ready must be false.")
print(json.dumps(case, indent=2))
