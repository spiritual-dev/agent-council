# Org chart template

Prefer `org.json` as the live source. This markdown is for quick drafting.

## Vision
One paragraph.

## Values
- …

## Map

```mermaid
flowchart TB
  Chairman[Chairman]
  Master[Master agent]
  Council[Council]
  T1[Team: Domain A]
  T2[Team: Domain B]
  Chairman --> Master
  Master --> Council
  Master --> T1
  Master --> T2
```

## Seats

| Seat | Reports to | Purpose | Outcome |
|---|---|---|---|
| Master agent | Chairman | Interface | Clear reports and carried decisions |
| … | … | … | … |
