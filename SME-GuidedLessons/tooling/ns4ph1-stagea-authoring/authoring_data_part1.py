"""NS-4PH1 stage-A authoring data — the pilot note rn_k9wr3prcgSBg5vfw (Speed).

Written items only (the R3 authoring-parts law): kind order
[recall, recall, explain-why, application]; each item carries stem /
misconceptionClass / modelAnswer / keywords[] and an anchor.kp provenance index
(1-based into its lesson's keyPoints, stripped from emitted bytes).
Grounded in notes/1-forces-and-motion/1-1-movement-and-position/1-1-2-speed.md.
"""

PART1 = {
    "rn_k9wr3prcgSBg5vfw": {
        "lessons": [
            {
                "items": [
                    {
                        "kind": "recall",
                        "stem": "State, in words, the relationship used to work out how fast an object moves across a whole journey.",
                        "misconceptionClass": "average speed equation recall",
                        "modelAnswer": "average speed = total distance moved ÷ total time taken.",
                        "keywords": ["average", "speed", "distance", "time"],
                        "anchor": {"kp": 3},
                    },
                    {
                        "kind": "recall",
                        "stem": "A hiker covers a six-kilometre trail in ninety minutes. Name the single quantity that summarises how fast the hiker moved overall.",
                        "misconceptionClass": "average vs instantaneous recall",
                        "modelAnswer": "The hiker's average speed — the total distance moved divided by the total time taken.",
                        "keywords": ["average", "speed"],
                        "anchor": {"kp": 2},
                    },
                    {
                        "kind": "explain-why",
                        "stem": "Explain why a quantity that has a magnitude but no direction cannot be classed as a vector.",
                        "misconceptionClass": "scalar classification",
                        "modelAnswer": "Because a vector must carry both magnitude and direction; a quantity with magnitude alone is a scalar, and speed is exactly such a quantity.",
                        "keywords": ["scalar"],
                        "anchor": {"kp": 1},
                    },
                    {
                        "kind": "application",
                        "stem": "A car covers 120 kilometres in one and a half hours. Calculate how fast it moves.",
                        "misconceptionClass": "applying the average speed relationship",
                        "modelAnswer": "average speed = 120 km ÷ 1.5 h = 80 km/h.",
                        "keywords": ["80"],
                        "anchor": {"kp": 3},
                    },
                ]
            }
        ]
    }
}
