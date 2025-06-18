# MotionOS JSON Schemas

This file documents the two main JSON payloads used by MotionOS:

---

## 1. `sim_output.json`
(origin: `/output/sim_output.json`)

```json
{
  "strain_timeline": [
    {
      "timestamp": <number>,
      "strained_joints": {
        "<joint_name>": <number>,
        "...": <...>
      }
    },
    ...
  ]
}
