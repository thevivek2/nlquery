<pre> ```json
{
  "run_id": "string",
  "timestamp_utc": "string",
  "source_type": "string",
  "tables": [
    {
      "name": "string",
      "source_id": "string",
      "row_count": 0,
      "description": "string",
      "columns": [
        {
          "name": "string",
          "raw_type": "string | null",
          "inferred_type": "string",
          "nullable": false,
          "null_count": 0,
          "null_pct": 0.0,
          "distinct_count": 0,
          "distinct_pct": 0.0,
          "examples": ["string"],
          "top_values": [
            {
              "value": "string | number | null",
              "count": 0
            }
          ],
          "pii": {
            "flag": false,
            "pii_type": "string | null",
            "confidence": 0.0,
            "evidence": ["string"]
          },
          "numeric_stats": {
            "min": null,
            "max": null,
            "mean": null,
            "p05": null,
            "p50": null,
            "p95": null
          },
          "string_stats": {
            "min_len": 0,
            "max_len": 0,
            "common_patterns": ["string"]
          },
          "description": "string"
        }
      ]
    }
  ],
  "relationships": [
    {
      "from_table": "string",
      "from_column": "string",
      "to_table": "string",
      "to_column": "string",
      "relationship_type": "string"
    }
  ],
  "warnings": ["string"]
}
 ``` </pre>