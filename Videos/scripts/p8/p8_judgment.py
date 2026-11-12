#!/usr/bin/env python3
"""p8_judgment.py — agent judgment pass over the P8 physics-trio fill surface.

Surface: 240 strong-surface videos (distinctive-token candidates vs the trio's
empty SPEC_POINTs, pool-rarity gated) + 227 weak-surface videos (pre-pass
no-binding). Decision table below encodes the agent's per-video ruling.
Outputs: per-course video-map.draft.external-p8.json + owner-review-verdicts.p8.json.
"""
import json, os
from collections import defaultdict
from datetime import datetime, timezone

RES = '/home/z/my-project/repos/syllabai-resources'
HUB = '/home/z/my-project/repos/syllabai-v2-fresh'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
REVIEWER = ("delegated self-review (agent, per owner chat 2026-11-09: 'approve and review yourself'; "
            "lane authorized 2026-11-13: 'Proceed with remaining channel pools'; trio-fill follow-up "
            "anchored the same day: 'the ~50 specs still honest-empty on the physics trio')")
TASK = "T-VIDEOMAP-P8 (physics-trio honest-empty fill: re-adjudication of the pool remainder against the physics trio's empty spec points)"

AL25, IG23, IG19 = 'cie-a-level-physics-25', 'cie-igcse-physics-23', 'igcse-physics-19'
TRIO = [AL25, IG23, IG19]

# ---------------------------------------------------------------- keeps (8 rows)
KEEP = [
 dict(video='Y0xvoeiRTA0', course=AL25, specs=['1.3.2'], confidence='medium',
      title='A Level Practical Endorsement - Accuracy, Precision, Errors and Uncertainty', levelTag='a-level',
      evidence="title 'A Level Practical Endorsement - Accuracy, Precision, Errors and Uncertainty' -> 1.3.2 'understand the distinction between precision and accuracy' — the video's entire subject is the precision/accuracy/errors/uncertainty distinction; fresh adjudication (no prior entry)"),
 dict(video='4KTIxheE3bY', course=AL25, specs=['13.2.2'], confidence='medium',
      title='Big G and little g - Day 1 Answer in Detail', levelTag='a-level',
      evidence="title 'Big G and little g - Day 1 Answer in Detail' -> 13.2.2 'recall and use Newton's law of gravitation F = Gm m / r for the force between two point masses' — the title names G and g and the video's subject is exactly that distinction; 13.3.1 (g = GM/r^2) is already mapped; challenge-answer format disclosed"),
 dict(video='9HyKNkXW9W0', course=IG19, specs=['2.22P'], confidence='medium',
      title='Conductors, Insulators and Semi-Conductors - A Level Physics', levelTag='a-level',
      evidence="title 'Conductors, Insulators and Semi-Conductors - A Level Physics' -> 2.22P 'identify common materials that are electrical conductors or insulators, including metals and plastics' — the title names the spec's subject outright; boardMismatch (A-level video onto Edexcel IGCSE spec) disclosed; the prior AL25:p6 drop rejected only the AL25 I-V-characteristics candidate (generic 'conductor'), not this course"),
 dict(video='QMIcDNx36IQ', course=IG19, specs=['5.8P'], confidence='low',
      title='Changes of State - GCSE #Shorts', levelTag='gcse',
      evidence="title 'Changes of State - GCSE #Shorts' -> 5.8P 'explain why heating a system will change the energy stored within the system and raise its temperature or produce changes of state' — the title names changes of state; conceptual half only, the 5.11P practical is NOT bound; shorts format disclosed; low"),
 dict(video='4N6rPk9ucdI', course=IG23, specs=['3.2.4b'], confidence='medium',
      title='Real Images in a Converging Lens - A Level Physics', levelTag='a-level',
      evidence="title 'Real Images in a Converging Lens - A Level Physics' -> 3.2.4b 'Describe the characteristics of an image using the terms enlarged/same size/diminished, upright/inverted and real/virtual' — the title names real images in a converging lens; the P6 'no lens spec exists in CIE 9702' drop was a-level-only and did not adjudicate this course"),
 dict(video='L3jgUZ9l8kY', course=IG23, specs=['3.2.4b'], confidence='medium',
      title='Virtual Images in a Converging Lens  - A Level Physics', levelTag='a-level',
      evidence="title 'Virtual Images in a Converging Lens  - A Level Physics' -> 3.2.4b — the title names virtual images; same-course companion of the real-images video; the a-level-only P6 drop did not adjudicate this course"),
 dict(video='DkPLiQhDwms', course=IG23, specs=['3.2.4b'], confidence='low',
      title='Images in a Diverging Lens - A Level Physics', levelTag='a-level',
      evidence="title 'Images in a Diverging Lens - A Level Physics' -> 3.2.4b — diverging-lens images are always virtual+diminished, so the video teaches the virtual/diminished half of the characteristics vocabulary; low"),
 dict(video='2kHCvtTjOJs', course=IG23, specs=['1.1.7'], confidence='medium',
      title='Resolving Vectors - A Level Physics', levelTag='a-level',
      evidence="title 'Resolving Vectors - A Level Physics' -> 1.1.7 'Determine, by calculation or graphically, the resultant of two vectors at right angles, limited to forces or velocities only' — resolving into perpendicular components is the same right-angle vector skill in reverse; the prior AL25:p6 drop rejected only the AL25 4.2.3 equilibrium-triangle candidate (generic 'vector')"),
]

# ------------------------------------------------------- drop decision table
# video -> (class, reason) — one entry per strong-surface video (232 total)
CLS = {
 # DoodleScience (2)
 'OSsC3VnMC7g': ('adjacent', "eye-vs-camera GCSE physics video; the AL25 7.4.3 and IG23 3.3.4 binds matched 'eye' — neither spec's content is named (P7 dropped the same video's biology eye bind as cross-subject)"),
 'TfkZ_GtS5wk': ('adjacent', "'Life Cycle of Stars' bound to 23.2.4 'define half-life' on token 'life' — stellar evolution vs nuclear half-life, nonsense adjacency"),
 # Malmesbury (10) — sewage class
 'P4HZ5iQaF7I': ('sewage', "GCSE Maths angles lesson bound on 'angles' — non-science channel content"),
 'WE_ZxqUodqo': ('sewage', "Spanish language lesson bound on 'their'"),
 'Hro0jUuq2oQ': ('sewage', "English-Lit poem analysis bound on 'comparing' — the potentiometer spec is not the subject"),
 'H_fn2yLfP6w': ('sewage', "GCSE Maths corresponding-angles lesson bound on 'corresponding'/'angles' — antiparticles and CT scanning are not named"),
 'IIKhPL-9P9Q': ('sewage', "English-Lit poem analysis bound on 'exposure' — ionising-radiation exposure is not the subject"),
 '5auSJYKifeU': ('sewage', "KS3 science-skills video bound on 'relationships'"),
 'm1C023jvwX4': ('sewage', "French language lesson bound on 'present'"),
 '-6d78kXlYM8': ('sewage', "English-Lit poem analysis bound on 'remains' — Newton's first law is not the subject"),
 'fsEnQu6KG9M': ('sewage', "Spanish lesson bound on 'present' — the age-of-the-Universe estimate is not named"),
 '3D7EetDVWgU': ('sewage', "English-Lit poem analysis bound on 'tissue' — radiation dangers are not the subject"),
 # freesciencelessons (22)
 'cRC0-SxlUgQ': ('cross-subject', "A-level Biology ELISA-test revision bound to gravitational/electric potential definitions on token 'test'"),
 'NW1KGLvwQW8': ('cross-subject', "circulatory-system revision bound on 'human' — hearing range and visible wavelengths not the subject"),
 'FjY15FXbITM': ('cross-subject', "tissue-fluid revision bound on 'tissue' — radiation safety not the subject"),
 'OjLOzwfEKoU': ('cross-subject', "oestrogen/breast-cancer revision bound on 'cancer' — the EM-exposure spec's content is not named"),
 'XjGGVJ2gdeQ': ('adjacent', "synaptic transmission bound to Malus's law on token 'transmission'"),
 'q3L8xARUFZM': ('cross-subject', "VSEPR lone-pairs chemistry bound on 'shape'/'molecules' — piezo-electric crystals and particle forces not the subject"),
 'NTH9J_hlAVI': ('adjacent', "ionisation energy down a group bound to transformer terms on token 'down'"),
 '7TFldvLgII0': ('adjacent', "general formula chemistry bound on 'general' — sound-speed spec not named"),
 'QLhzsmx0EDs': ('cross-subject', "simple molecular substances chemistry bound to kinetic-theory gas pressure on 'molecular'"),
 '0ezyQMc4iqw': ('cross-subject', "simple molecular substances chemistry bound to kinetic-theory gas pressure on 'molecular'"),
 'fqnhRbuyy04': ('cross-subject', "group-2 reactivity bound to planetary comparison on 'elements'"),
 'ABYfB8r2BOg': ('cross-subject', "group-2 redox bound to planetary comparison on 'elements'"),
 'BLITE8uA4Tw': ('cross-subject', "GCSE Biology cancer bound on 'cancer' — the EM-wave detriment spec's content is not named"),
 'RXmpVboM040': ('content-mismatch', "GCSE Biology 'Mutations' covers DNA/gene mutations; the binds (5.2.1d, 7.16) are ionising-RADIATION mutation effects — radiation not the subject"),
 '3LeLccjpu0U': ('content-mismatch', "Biology order-of-magnitude cell sizes; 8.11P is absolute magnitude of stars"),
 '2MW6nwf80XM': ('cross-subject', "sampling organisms bound on 'organisms' — radiation dangers not named"),
 'iA4mk3CTkmI': ('cross-subject', "acids-reacting-with-metals chemistry bound to electrical conduction on 'metals'"),
 'rPbx_XrrKLQ': ('content-mismatch', "GCSE 'Electric Fields (Triple)' is the field-concept intro; 20.3.6 velocity selection and 5.2.5 gamma-fields not named (prior IG19:p7 drop consistent)"),
 'vJgBIvuLvgY': ('content-mismatch', "heating/cooling graphs = latent-heat curves; 16.2.2 first law of thermodynamics not named (prior IG23:p7 drop consistent)"),
 'lA8USjDkcXk': ('adjacent', "UK energy mix bound on 'mix' — density/float spec not named"),
 'nKbUbfadxRU': ('technique', "variables-skills video bound to photoelectric 'independent', potential-divider 'variable', control-rods 'control' — generic practical-skills vocabulary"),
 'beHZw0kH8js': ('technique', "'Precision' measurement-skills video; 1.3.2 is the precision/accuracy DISTINCTION and the title names only half — generic-skills class"),
 # Amoeba Sisters (33)
 'nnjmrrQ6xOs': ('cross-subject', "human body systems bound on 'human' — US-curriculum biology"),
 'gwcwSZIfKlM': ('adjacent', "mitosis bound to CT scanning / annihilation on token 'process'"),
 'GieZ3pk9YVo': ('content-mismatch', "DNA mutations != ionising-radiation mutations (5.2.1d, 7.16)"),
 'OT0jVsF3Yw8': ('promo', "subscriber celebration bound on '000'"),
 'PHJGNvDMn3U': ('promo', "edu-videos usage guide bound on 'our'"),
 'aO_kFKErl1k': ('promo', "Christmas carol bound on 'days'"),
 'yXuw_tKprqo': ('promo', "book promo bound on 'our'"),
 'RbA01iMBCK0': ('promo', "pet holiday special bound on 'pet' -> PET scanning / 'our'"),
 'e_ia8WbXeqQ': ('promo', "comment responses bound on 'other' -> quark charges"),
 '5j8j7BhCCEg': ('cross-subject', "body tissues bound on 'types'"),
 'P30QlwSsUic': ('cross-subject', "theory/law usage bound on 'theory' -> redshift"),
 'cQPVXrV0GNA': ('adjacent', "characteristics of life bound on 'life' -> half-life"),
 '6liTZpTeuu4': ('adjacent', "characteristics of life bound on 'life' -> half-life"),
 'Al7FueXTCKs': ('adjacent', "chromosome numbers bound on 'after' -> CMBR"),
 'rNjPI84sApQ': ('cross-subject', "ecological relationships bound on 'relationships' -> wave relationships"),
 'FGnS-Xk0ZqU': ('cross-subject', "endosymbiotic theory bound on 'theory' -> redshift"),
 'MEIXRLcC6RA': ('cross-subject', "lab safety bound on 'safety'/'general' -> radiation safety / sound speed"),
 '7S4WMwesMts': ('adjacent', "Hardy-Weinberg equilibrium bound on 'equilibrium' -> no-resultant-moment specs"),
 'gEUu-A2wfSE': ('cross-subject', "human body systems bound on 'human'"),
 '0JDCViWGn-0': ('cross-subject', "human body systems bound on 'human'"),
 'EIPmKuwhnRs': ('cross-subject', "human body systems bound on 'human'"),
 '-dbRterutHY': ('cross-subject', "cell signaling bound on 'signaling' -> digital signaling"),
 'C0zCCDOfXnM': ('promo', "Patreon bound on 'our'"),
 'f-ldPgEfAHI': ('adjacent', "mitosis bound to CT scanning / annihilation on token 'process'"),
 'vl6Vlf2thvI': ('content-mismatch', "DNA mutations != ionising-radiation mutations (5.2.1d, 7.16)"),
 'HL7i3H1FIaU': ('promo', "speed draw bound on 'once'"),
 'T_IHuzKt0lY': ('promo', "study-music video bound on 'flow' -> electron flow"),
 'EKxh4_l-BSI': ('promo', "study-music video bound on 'flow'"),
 'S4zFKkreu8A': ('promo', "study-music video bound on 'flow'"),
 'kpx-0CuXnc0': ('promo', "study-music video bound on 'flow'"),
 't6W3f8DfRqs': ('promo', "study tips bound on 'our'"),
 'NXkaTwEfAvQ': ('promo', "book preorder bound on 'second' -> Hubble constant"),
 'QVCjdNxJreE': ('cross-subject', "cell-cycle cancer bound on 'cancer' -> EM detriment"),
}

# PhysicsOnline drops (165) — part 1/2
CLS.update({
 'OA5QjL1nurQ': ('drill', "100 Day Challenge worked solutions — drill class, no spec content named"),
 'TwLwgpj3EiU': ('promo', "exam-dates announcement bound on 'released'"),
 'xiY3IBEVmSk': ('promo', "exams news bound on 'not'"),
 '-6WT6VBtHgY': ('promo', "equation-sheet commentary bound on 'problems' (prior IG23:p6)"),
 'ax3HYc1VXe4': ('promo', "book promo bound on 'things'"),
 'iZ0K-47ualg': ('promo', "half-term announcement bound on 'things'"),
 'LDZNqr_Jcsw': ('promo', "start-of-term announcement bound on 'things' (prior AL25:p6)"),
 'B8gdIDkRqlA': ('promo', "Easter advice bound on 'have'/'things'"),
 'BVPRdDhz5o8': ('promo', "engineering feature bound on 'buildings' -> radon sources (prior IG23:p6)"),
 'TjdyUZK8Nuk': ('promo', "equations list bound on 'they' -> PET scanning"),
 '5TjoqP79Wjk': ('promo', "unboxing bound on 'other' -> quark charges (prior IG19:p6)"),
 'O16dJE0SXoI': ('promo', "lessons-learned bound on 'things' (prior AL25:p6)"),
 'RUums27sUgQ': ('promo', "exam countdown bound on 'things'"),
 'JstnW51XA4s': ('promo', "book review bound on 'full' -> rectification"),
 'MwzDPhV6dlY': ('technique', "'Absolute Uncertainty' skills video; binds matched 'absolute' on zero-kelvin/particle-motion specs — measurement-skills class"),
 'hlpMRA_7SRo': ('technique', "vernier-scale skills bound on 'scale' -> thermodynamic-scale specs"),
 'YImQNPK3dK0': ('technique', "percentage-uncertainty skills bound on 'multiple' -> CT multi-angle"),
 'iFfx7olfzGU': ('technique', "single-reading uncertainty bound on 'single' -> age-of-universe"),
 '9_qxohScVbk': ('drill', "gradient maths bound on 'gradient' — maths-drill class"),
 'YF-XFae6PvA': ('technique', "zero-errors skills bound on 'zero' -> absolute-zero specs"),
 'OM1HbJQ1yKs': ('technique', "AQA data/formulae sheet walkthrough — board material, boardMismatch content (prior AL25:p6)"),
 'pIQeKsAClAc': ('promo', "paper-change news bound on 'have'"),
 'JNGyzmlFL9o': ('promo', "paper-2 revision hour bound on 'hour'"),
 'QDpxgMqisVc': ('promo', "resources promo bound on 'points' (prior AL25:p6)"),
 'sErfG5fMji0': ('adjacent', "gamma absorption in lead bound to 25.3.1 spectral absorption lines on 'absorption' — different phenomenon (prior AL25:p6)"),
 'Rgg5eOB0GnE': ('promo', "admissions interview bound on 'they'"),
 'RFD9Z4w3yKo': ('promo', "after-exams video bound on 'after' -> CMBR"),
 'pwp1NcfXu80': ('promo', "AQA measurements revision; IG23 5.2.5 'measurements' is background-radiation wording, not the subject (prior AL25:p6)"),
 'jhz29mQ6o_Q': ('adjacent', "cloud-chamber bound on 'cloud' -> planetary comparison (prior AL25:p6)"),
 'uZPi0aIKGaM': ('promo', "board comparison bound on 'these' -> damping terms (prior AL25:p6)"),
 'ste3iijdOh8': ('promo', "build suggestion bound on 'these' (prior AL25:p6)"),
 'PILsjybmVwI': ('drill', "unit-conversion maths bound on 'unit' (prior AL25:p6)"),
 '2944BURR06I': ('promo', "back-to-school news bound on 'about'"),
 'wXyAKFZ6AM0': ('adjacent', "botafumeiro pendulum demo bound to 1.1.3 small-interval measurement on 'pendulum' (prior AL25:p6)"),
 'AvrC0_W3mlw': ('adjacent', "Feynman-diagram LEGO bound to 8.12P HR diagram on 'diagram' — different diagram; no Feynman spec in the trio spines"),
 'rFou2q2-pNo': ('drill', "gradient maths bound on 'unit' (prior AL25:p6)"),
 'aXaAMqvmfmE': ('drill', "average-velocity worked example bound on 'average' -> kinetic-theory mean speed (prior IG23:p6)"),
 'BvLfbKRqYj8': ('drill', "gradient worked example bound on 'gradient' (prior IG19:p6)"),
 'g989q6Nc7AY': ('drill', "gradient worked example bound on 'gradient' (prior IG19:p6)"),
 'z925v3v9Va4': ('drill', "calculators sin/cos/tan bound on 'cos'/'sin' -> Malus/SHM/Snell equations — maths-drill class"),
 'YADOB7a-F7U': ('drill', "rearranging-lambda maths bound on 'these' (prior AL25:p6)"),
 'KlZwnpN_EZU': ('promo', "experiments list bound on 'these' (prior AL25:p6)"),
 'acNkshOYxio': ('adjacent', "'Colour Experiments' bound to star-colour specs on 'colour' — no stellar content named"),
 's9EA42kLNlM': ('drill', "combining equations bound on 'combining' -> CT (prior AL25:p6)"),
 'fqLqDOYT1Vc': ('technique', "control-variables skills bound on 'control' -> control rods (prior AL25:p6)"),
 'FnYD5Xp6jPo': ('technique', "graph relationships skills bound on 'common'/'relationships' (prior AL25:p6)"),
 's4MrVmWvIUw': ('adjacent', "conductance bound to 11.1.10 on 'anti' — anti-resistance wordplay, not antiparticles (prior AL25:p6)"),
 'rFnEXB7mOqI': ('promo', "solar-boat build bound on 'solar' -> universe/galaxies (prior IG19:p6)"),
 'Mv7oPnUgDF8': ('adjacent', "laser-diode construction bound to rectifier diode 21.2.2 on 'diode' — different device (prior AL25:p6)"),
 'xaUb1wDxlY8': ('technique', "fair-test skills bound on 'control' (prior AL25:p6)"),
 'KByPhYT-hYE': ('cross-subject', "coronavirus video bound on 'safe' -> radioactive-material storage"),
 'yfhEx669AFg': ('promo', "omicron update bound on 'could' -> exponential equations"),
 'PXQZMWStQNQ': ('promo', "challenge promo bound on 'could'/'complete'"),
 'shZ-3soLopE': ('promo', "book review bound on 'could'"),
 'jBSKFYOSmMo': ('promo', "book promo bound on 'could'/'complete'"),
 'XPlPH093z9M': ('promo', "grade-improvement bound on 'days' (prior AL25:p6)"),
 'sz2hfUQxlnQ': ('drill', "y-intercept maths bound on 'origin' -> Hall voltage/force origins (prior AL25:p6)"),
 'jchjZfdqtMs': ('promo', "do-not-buy bound on 'not'"),
 'AZ8IH1_YkD4': ('technique', "MC strategy bound on 'multiple' -> CT (prior AL25:p6)"),
 'Szxi6r8Z_po': ('promo', "starting-a-levels advice bound on 'these'"),
 'FGjNYIaYXGk': ('technique', "MC strategy bound on 'multiple'"),
 'KDG8NveLsaA': ('technique', "Edexcel formulae sheet — board material (prior AL25:p6)"),
 'gq9WWYQCGx4': ('technique', "Edexcel IGCSE formulae sheet (prior IG23:p6)"),
 'V1Julrf3l6o': ('drill', "elastic-PE worked example bound on 'stored' -> capacitor energy/internal energy (prior IG19:p6)"),
 'ydzrEUbvfT8': ('adjacent', "electron capture bound to 1.2.3 homogeneity on 'check' (prior AL25:p6)"),
 'XAVQDy-gQdA': ('adjacent', "energy-efficient buildings bound to radon background sources on 'buildings' — insulation is not radiation (prior IG23:p6)"),
 'B4TgGk8B5Nk': ('drill', "bullet energy worked example bound on 'transfers' (prior IG23:p6)"),
 'H2_uKX0Xcmg': ('drill', "escape-velocity equation maths bound on 'escape' -> evaporation (prior AL25:p6)"),
 'jPm_5eNy1MU': ('technique', "estimation skills bound on 'quantities' -> scalar/vector lists (prior AL25:p6)"),
 'vc4fHJl-N0M': ('content-mismatch', "fields overview compares the three field types; 20.3.6 velocity selection not named (prior IG19:p6)"),
 'IBDk8Opqn8E': ('adjacent', "inclined-plane bound to Malus's law on 'plane' (prior AL25:p6)"),
 'lDeyOXWZwsc': ('promo', "results-day news bound on 'does'"),
 'k7TzNcSyXb8': ('promo', "daily workout bound on 'far' -> galaxy brightness (prior AL25:p6)"),
 'nOmASKTL2ns': ('promo', "rules-changes bound on 'have' (prior AL25:p6)"),
 'cTKsXqzO4MQ': ('drill', "sledge worked example bound on 'could'/'fast' (prior IG23:p6)"),
 'wCmUOOxShxI': ('promo', "grade-awarding news bound on 'could'"),
 'cZp7-ofxr6s': ('drill', "significant figures bound on 'these' (prior AL25:p6)"),
 'Y2Qte2r66CM': ('promo', "paper-1 reaction bound on 'was'"),
 '9INUrQMVd70': ('promo', "paper-2 reaction bound on 'was'"),
 '4QjY2mmbHvc': ('promo', "motivation bound on 'determined'"),
 'Uh1yBPLfcIs': ('no-target', "LIGO gravitational waves — no trio spec names the content (prior IG19:p6 honest no-target)"),
 'rOIFGe3Nx7o': ('promo', "work-duration advice bound on 'long'"),
 'hcqWtCNNsiQ': ('technique', "MC answering bound on 'multiple' (prior AL25:p6)"),
 'N3_imYXsip0': ('promo', "grade-improvement bound on 'month' -> Moon orbit"),
 '_Tx_L0Mm_wg': ('technique', "circuit-problem technique bound on 'problems' -> radiation dangers (prior AL25:p6)"),
 'q0g9doFBVzQ': ('drill', "standard form bound on 'large' -> planets (prior AL25:p6)"),
 'xEQ7DfRydOk': ('promo', "assessment-materials pointer bound on 'find' (prior IG23:p6)"),
 'OXI31z6_xu4': ('promo', "oscilloscope build bound on 'too'/'far' (prior IG23:p6)"),
 'i6JFHiK8Jgs': ('promo', "revision advice bound on 'was'"),
 'DnMBkqfutsY': ('promo', "rota headlines bound on 'about'"),
 '0G6CA4Xs6xU': ('adjacent', "image processing bound to CT/PET specs on 'image'/'processing' — no CT/PET named (prior AL25:p6)"),
})

# PhysicsOnline drops (165) — part 2/2
CLS.update({
 'i9F6V3vWxWY': ('technique', "variables skills bound on 'independent' -> photoelectric (prior IG23:p6)"),
 'NuBs7CJVnk0': ('promo', "study-hours advice bound on 'too' -> neutron excess"),
 'TGKTnLRgi_4': ('promo', "product testimonial bound on 'big'/'played'"),
 'brU3avBGSmo': ('no-target', "Jeans-mass olympiad explainer — no trio empty spec names the content; bind was 'explains' -> solar-system mass"),
 'Ob8hu3EFTtc': ('promo', "reopening news bound on 'could'"),
 'Ghv7OnlQ_rk': ('promo', "grade-boundaries commentary bound on 'lowest'/'boundaries'"),
 '9M6sECHhoIM': ('promo', "interview question bound on 'people'/'happen'"),
 'Em4YDr749jA': ('drill', "MC questions bound on 'multiple' (prior IG23:p6)"),
 'U_aYZx2CTkY': ('adjacent', "muon-pendulum demo bound to 1.1.3 on 'pendulum' (prior AL25:p6)"),
 'F7j-64oN1-U': ('promo', "study plan bound on 'month' (prior AL25:p6)"),
 '5Wv8DZqS3uw': ('drill', "natural logs maths bound on 'natural' -> resonance/solar-system"),
 'j1zthPMilWA': ('drill', "natural logs worked example bound on 'natural'"),
 'pv5oer3ZEEU': ('drill', "natural logs worked example bound on 'natural'"),
 'bRsr7l0nbes': ('drill', "natural logs worked example bound on 'natural'"),
 'R-OSRUQEyfc': ('technique', "OCR formulae sheet — board material (prior AL25:p6)"),
 'EABJoapqIoE': ('promo', "pre-release commentary bound on 'release' -> stellar nuclear reactions (prior AL25:p6)"),
 '9Ej3X6RAz7U': ('drill', "specimen MC answers bound on 'multiple'"),
 '9Kpo6zAXk5A': ('promo', "grade boundaries bound on 'boundaries' -> light boundaries"),
 'qpemT9T1VpY': ('promo', "exam advice bound on 'show'"),
 '-f-rCBFx1dw': ('promo', "month recap bound on 'month'"),
 'eSRtcBkDbK8': ('promo', "question stats bound on 'correctly'/'over'"),
 'X0jF9V1rVP4': ('adjacent', "pendulum practical bound to 1.1.3 on 'pendulum' — the honest AL25 SHM-practical targets were already mapped (prior AL25:p6)"),
 'NzCDhVNWtiQ': ('promo', "aptitude-test prep bound on 'test' -> potential definitions (prior AL25:p6)"),
 'wdeOh4q_dfE': ('promo', "examiner Q&A bound on 'principal' -> focal-length spec"),
 'y42_IymUp0M': ('adjacent', "phone projector bound to CT on 'images'"),
 'iwWfoet4-zc': ('technique', "quantities/units skills bound on 'quantities' -> scalar/vector lists (prior AL25:p6)"),
 'LgOeZDUBXKo': ('technique', "quantities/symbols/units skills (prior IG19:p6)"),
 '-rWj9AoY_O8': ('adjacent', "RGB LED mixing bound to rectifier diode on 'diode' and star colour on 'colour' (prior IG23:p6)"),
 'Bg26bFr15Fk': ('drill', "charge-ratio maths bound on 'ratio' -> refractive index/Hubble (prior AL25:p6)"),
 'kN7j1PHoSKs': ('technique', "read-the-question bound on 'problems' (prior IG23:p6)"),
 'fV4_K77sAfk': ('adjacent', "Feynman-diagram car wrap bound to HR diagram on 'diagram' (prior AL25:p6)"),
 'AJ6MlcAi09Y': ('adjacent', "energy-losses insulation bound on 'losses'/'reducing' -> beam force/exposure time (prior IG23:p6)"),
 'EJOPslIfz_g': ('promo', "support programme bound on 'month' (prior IG23:p6)"),
 'BQJDKUSSAN0': ('drill', "scale drawing bound on 'scale' -> thermodynamic scale (prior IG23:p6)"),
 'pYZWVKI4zEk': ('drill', "scale drawing worked example bound on 'scale' (prior IG23:p6)"),
 'uvtAjwFd400': ('promo', "school-return news bound on 'but'"),
 '7FxIEm0YXbs': ('promo', "question stats bound on 'have'/'correctly'"),
 '_g4FM4-6HBE': ('promo', "solar boat bound on 'solar' (prior IG19:p6)"),
 'BnXpGHB8ULs': ('technique', "diagram technique bound on 'diagram'/'way' -> HR diagram (prior AL25:p6)"),
 'WSvCfzZn73g': ('promo', "start advice bound on 'minute' -> count rate/units"),
 'eD9H-2CQ2i0': ('adjacent', "Stokes' law laminar flow bound to 2.16 electron flow on 'flow' — different phenomenon; Stokes' law has no trio target (prior AL25:p6)"),
 'sUVTsd4ehf4': ('drill', "sphere maths bound on 'sphere' -> point-mass/spherical-conductor field specs — the geometry tool, not the field content (prior AL25:p6)"),
 'q9vc23F7YU8': ('drill', "sphere maths worked example bound on 'sphere'"),
 'D-RfpSkbQp4': ('drill', "sphere maths worked example bound on 'sphere'"),
 'td5w-u27N0E': ('drill', "sphere maths worked example bound on 'sphere'"),
 'fz8JL-mZHTw': ('adjacent', "earthquake-building tests bound to radon sources on 'buildings'"),
 'JIAW1xCR9GI': ('promo', "resource walkthrough bound on 'people'"),
 '4t2EVSYuP78': ('adjacent', "capacitor charging puzzle bound to friction charging on 'charging' (prior AL25:p6)"),
 'z1WUZ0QksWA': ('promo', "revision advice bound on 'about' (prior AL25:p6)"),
 'tcUpIDm1t10': ('adjacent', "particle model bound to attenuation specs on 'matter' — the honest IG23 2.1.x binds rest on the generic vocabulary matter/model/particle, per the prior IG23:p6 ruling"),
 'Wt7QaPb5Tko': ('adjacent', "rope-loop AC model bound to 6.1.5 on 'explains' — the honest AC/DC difference spec (2.6) is already mapped"),
 'O4OHAhi2XNQ': ('promo', "lockdown news bound on 'second' -> Hubble constant"),
 'uEBsklSKtc4': ('adjacent', "widmanstätten meteorite bound on 'earth'/'things' — no honest target names the content"),
 'LdAjhPosFzo': ('promo', "flight lecture bound on 'theory' -> redshift"),
 '3M92CVoyk7E': ('promo', "hard-questions teaser bound on 'but'"),
 'NTpw4k4BFzg': ('promo', "book critique bound on 'problems'"),
 'o7b7vKIRdQM': ('promo', "calculator review bound on 'not'"),
 'OhGei_hgIJw': ('promo', "question stats bound on 'too'/'their'"),
 'xbIPTFaZVl4': ('promo', "gcse-vs-a-level bound on 'differences' -> potentiometer (prior IG23:p6)"),
 '5e-OOtSH8iI': ('promo', "channel promo bound on 'things'/'about' (prior IG23:p6)"),
 'Gji7fOJJcp0': ('adjacent', "maltese-cross demo bound on 'cross' -> flux cross-section/wire resistance"),
 'j07lP00ZmMc': ('promo', "UCAS bound on 'process'"),
 '-cvXiGlzecM': ('technique', "variables skills bound on 'independent'/'control' (prior AL25:p6)"),
 'f42_Q8nLQQA': ('promo', "covid closure bound on 'due'"),
 'TFMRbx9mARU': ('adjacent', "wheatstone bridge bound to bridge RECTIFIER on 'bridge' — different circuit (prior AL25:p6)"),
 '-CaD3uN6dS0': ('promo', "calculator advice bound on 'which'"),
 'p_1iGvIU2Zo': ('promo', "circuit teaser bound on 'which'"),
 'A48kfQzsjts': ('promo', "video poll bound on 'which'"),
 'RNrzZc7T3oI': ('adjacent', "tail-rotor bound on 'which' -> absolute zero — junk token"),
 '6LARrjFbCmk': ('adjacent', "friction puzzle bound on 'fall' -> free-fall spec"),
 'Nn1Gwj1dea4': ('adjacent', "seven-days-in-a-week novelty; the Earth-orbit bind is word-adjacent (prior IG23:p6 ruling)"),
 'hRsT9IgWBrA': ('promo', "results-delay news bound on 'about'"),
 'LkUn9JSXrZs': ('promo', "safe-opening guidance bound on 'safe'"),
 'jdtAaX_qomE': ('drill', "daily workout solutions bound on 'solution'"),
})

def load():  # surfaces
    strong = json.load(open('/tmp/p8_judgment_rows.json'))  # pool-rarity-gated surface (240 videos / 369 rows)
    raw = json.load(open('/tmp/p8_candidate_rows.json'))    # full raw candidate surface (1,027 pairs / 467 videos)
    return strong, raw

def main():
    strong, raw = load()
    # kept-elsewhere junk binds: (video, course) -> reason for THIS course's reject ledger
    KEPT_ELSEWHERE = {
        ('4KTIxheE3bY', IG23): ("the video is kept for cie-a-level-physics-25 13.2.2; the IG23 6.2.4 redshift bind on token 'big' is word-adjacent nonsense"),
        ('9HyKNkXW9W0', AL25): ("the video is kept for igcse-physics-19 2.22P; the AL25 20.4.3 forces-between-conductors bind matched 'conductors' — magnetic forces between wires are not the subject (prior AL25:p6 drop consistent)"),
        ('4N6rPk9ucdI', AL25): ("the video is kept for cie-igcse-physics-23 3.2.4b; the AL25 24.2.4 CT-scanning bind matched 'images' — lens images are not CT (prior AL25:p6 drop: no lens spec exists in CIE 9702)"),
        ('L3jgUZ9l8kY', AL25): ("the video is kept for cie-igcse-physics-23 3.2.4b; the AL25 24.2.4 CT-scanning bind matched 'images' — lens images are not CT (prior AL25:p6 drop: no lens spec exists in CIE 9702)"),
        ('DkPLiQhDwms', AL25): ("the video is kept for cie-igcse-physics-23 3.2.4b; the AL25 24.2.4 CT-scanning bind matched 'images' — lens images are not CT (prior AL25:p6 drop: no lens spec exists in CIE 9702)"),
    }
    strong_by_course = defaultdict(set)   # course -> set(video)
    bind_codes = defaultdict(list)        # (course, video) -> [spec codes]
    for r in strong:
        strong_by_course[r['course']].add(r['video'])
        bind_codes[(r['course'], r['video'])].append(r['spec'])
    strong_vids = set(r['video'] for r in strong)
    keep_by_course = defaultdict(list)
    for k in KEEP:
        keep_by_course[k['course']].append(k)
    # weak surface: raw videos not in strong surface -> per-course no-binding rejects
    raw_by_course = defaultdict(set)
    for r in raw:  # flat rows: {video, course, spec, ...}
        if r['course'] in TRIO and r['video'] not in strong_vids:
            raw_by_course[r['course']].add((r['video'], r['spec']))
    missing = strong_vids - set(CLS.keys()) - set(k['video'] for k in KEEP)
    extra = set(CLS.keys()) - strong_vids
    assert not missing, f'CLS missing decisions for: {sorted(missing)}'
    assert not extra, f'CLS has non-surface videos: {sorted(extra)}'
    assert len(CLS) + len(KEEP) == len(strong_vids), f'{len(CLS)}+{len(KEEP)} != {len(strong_vids)}'
    print(f'strong surface: {len(strong_vids)} videos = {len(KEEP)} keeps + {len(CLS)} drops — decision table covers all')

    pool = {v['id']: v for v in json.load(open(f'{RES}/Videos/inventory/channels/physicsonline-uploads.json'))['videos']}
    authored = {}
    for v in pool.values():
        authored[v['id']] = v

    for course in TRIO:
        keeps = keep_by_course[course]
        kvids = {k['video'] for k in keeps}
        # per-course rejects: strong-surface videos not kept for this course
        rejects = []
        for vid in sorted(strong_by_course[course]):
            if vid in kvids:
                continue
            codes = ','.join(sorted(set(bind_codes[(course, vid)])))
            ke = KEPT_ELSEWHERE.get((vid, course))
            if ke is not None:
                rejects.append({'video': vid, 'reason': f'self-review drop (kept-elsewhere): {ke} [rejected bind(s): {codes}]'})
                continue
            cls, why = CLS[vid]
            rejects.append({'video': vid, 'reason': f'self-review drop ({cls}): {why} [rejected bind(s): {codes}]'})
        # no-binding rejects: weak-surface videos for this course (one entry per video)
        weak_pairs = raw_by_course[course]
        nobind_vids = sorted({v for v, _ in weak_pairs})
        for vid in nobind_vids:
            codes = ','.join(sorted({s for v, s in weak_pairs if v == vid}))
            rejects.append({'video': vid, 'reason': f'pre-pass no-binding: weak-token candidates for {codes} only (in-course df>3 or pool-common vocabulary) — no distinctive overlap'})
        applied = {'rowsKept': len(keeps), 'rowsDropped': len(strong_by_course[course]) - len(kvids),
                   'adjudicationNoBind': len(nobind_vids)}
        verdicts = {
            'schema': 'syllabai.owner-review/1', 'task': TASK, 'course': course,
            'ruledUtc': NOW,
            'source': ('agent judgment pass over the full P8 candidate surface: 240 strong-surface videos '
                       'adjudicated per video (classes: promo / drill / technique / adjacent / cross-subject / '
                       'sewage / content-mismatch / no-target) + weak-surface no-binding rejects; prior P6/P7 '
                       'rulings honored where they cover the same (video, course, spec) pair — lens-image drops '
                       'were a-level-only and the trio-empty IG23 3.2.4b target was never adjudicated before'),
            'default': 'approve', 'reviewer': REVIEWER,
            'evidenceBasis': ('Title-only posture, tightened binding rule, target = the trio EMPTY spec points '
                              'only (re-adjudication lane; mapped specs out of scope). Deterministic '
                              'distinctive-token pre-pass (df<=3 in-course + pool-rarity gate) then a full agent '
                              'judgment pass over every strong-surface video. Identity: oEmbed author '
                              "'Physics Online' verified 8/8 at adjudication time. Confidence never high. "
                              'Re-binds and keeps tabled with title assertions in the evidence strings.'),
            'rejects': rejects, 'applied': applied,
        }
        dd = f'{RES}/Videos/drafts/{course}'
        json.dump(verdicts, open(f'{dd}/owner-review-verdicts.p8.json', 'w'), indent=1, ensure_ascii=False)

        draft = {
            'schema': 'syllabai.video-map-draft/1', 'draftOf': f'hub.video-map/1 {course}',
            'task': TASK, 'course': course,
            'qual': 'A Level' if course == AL25 else 'IGCSE',
            'reviewState': 'owner-reviewed-external',
            'draftLaw': ('second-lane draft (P8): rows enter content/ only through owner-review-verdicts.p8.json '
                         '+ the apply step; a video may map into several courses; rejected videos stay out of the '
                         'shipped videos[] and live in the verdicts ledger (owner-review-verdicts.p8.json)'),
            'source': {'provider': 'PhysicsOnline',
                       'method': ('re-adjudication micro-lane: the pool remainder (PhysicsOnline 1,081 uploads '
                                  're-enumerated fresh 2026-11-13, 0 deltas; four P7 pools reused from the '
                                  '2026-11-12 enumeration) union-excluded against the mapped corpus, candidates '
                                  'generated ONLY against the trio empty spec points (distinctive-token pre-pass '
                                  '+ pool-rarity gate), full agent judgment pass; evidence is TITLE-ONLY'),
                       'enumeratedUtc': NOW},
            'videos': [{
                'id': k['video'], 'title': k['title'], 'provider': 'PhysicsOnline',
                'watchUrl': f'https://www.youtube.com/watch?v={k["video"]}',
                'lessonRef': None, 'lessonUrl': None, 'levelTag': k['levelTag'],
                'boardNote': ('PhysicsOnline (AQA/OCR/Edexcel-focused UK channel) bound onto CIE/Edexcel specs on '
                              'content match; boardMismatch disclosed per row; oEmbed identity verified '
                              "(author 'Physics Online')"),
                'durationS': authored[k['video']]['duration'], 'guestVisible': None,
                'subelementOfPrimary': False, 'oembedAuthor': 'Physics Online',
                'oembedVerifiedUtc': NOW,
            } for k in keeps],
            'mappings': [{
                'video': k['video'], 'lessonRef': None, 'lessonUrl': None, 'specs': k['specs'],
                'confidence': k['confidence'], 'evidence': k['evidence'],
                'method': 'llm-draft-external', 'reviewed': True, 'reviewer': REVIEWER,
                'reviewedUtc': NOW, 'boardMismatch': True,
            } for k in keeps],
            'coverage': {
                'specPointsTotal': len([n for n in json.load(open(f'{HUB}/apps/hub/content/{course}/curriculum.json'))['nodes'] if n.get('family') == 'SPEC_POINT']),
                'specPointsDraftedHere': len({s for k in keeps for s in k['specs']}),
                'rows': len(keeps),
                'byConfidence': {
                    'high': sum(1 for k in keeps if k['confidence'] == 'high'),
                    'medium': sum(1 for k in keeps if k['confidence'] == 'medium'),
                    'low': sum(1 for k in keeps if k['confidence'] == 'low'),
                },
            },
            'generatedUtc': NOW, 'reviewedUtc': NOW,
        }
        json.dump(draft, open(f'{dd}/video-map.draft.external-p8.json', 'w'), indent=1, ensure_ascii=False)
        total_rej = len(rejects)
        print(f'{course}: draft rows={len(keeps)} keeps={sorted(kvids)} verdicts: '
              f'rowsDropped={applied["rowsDropped"]} noBind={applied["adjudicationNoBind"]} ledger={total_rej}')

if __name__ == '__main__':
    main()
