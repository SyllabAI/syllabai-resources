#!/usr/bin/env python3
"""sme_speech_transpile_test.py — the pinned battery for the resources
speech->KaTeX transpiler (T-RULE-T3-SUBSTRATE-1).

Pinned expectations: the OF-RECORD v2 ladder itself (apps/hub/src/lib/
speech-math.ts + speech-extras.ts + apps/hub/scripts/cie/cie_math_extras.ts,
the T-RULE-T3-CORPUSGATE-ADJ-1 run-001/run-002 instrument, general variant)
was executed over real substrate specimens harvested at resources pin
54c0534 with katex throwOnError verification (speech_ladder_reference_r0.mjs,
lane receipt). The Python port must reproduce those outputs BYTE-EXACT —
a port-equivalence proof on live corpus data, not a re-derivation.

Legs:
  1. pinned pairs — byte-exact vs the of-record ladder;
  2. fail-closed negatives — plain-text alts stay untouched (None);
  3. guard unit cases — every _katex_approx_ok clause fires on its
     evidence class and passes its legitimate counter-example;
  4. idempotence — transpile_alt(output) does not reconvert ($..$ and
     `plain` outputs fail the trigger gate or stay stable);
  5. residual-grammar sweep — no $-output carries Chrome speech grammar.

Run: python3 scripts/sme_speech_transpile_test.py   (exit 0 = GREEN)
CI:  wired as a corpus-gates step in .github/workflows/scripts-tests.yml
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sme_speech_transpile import (  # noqa: E402
    transpile_alt,
    has_residual_grammar,
    _katex_approx_ok,
)

# (input alt, expected output or None, of-record via, fixture kind)
PINNED_PAIRS = [
    ('text PED\xa0=\xa0 end text fraction numerator percent sign space change space in space quantity space demanded over denominator percent sign space change space in space price end fraction space equals space fraction numerator percent sign triangle space in thin space QD over denominator percent sign triangle in space straight P end fraction\\n\\npercent sign triangle space in thin space QD space equals space 8 percent sign\\n\\npercent sign space increment P space equals space fraction numerator 90 minus 80 over denominator 80 end fraction space x space 100 space equals space 12.5 percent sign\\n\\ntext PED\xa0=\xa0 end text space fraction numerator 8 percent sign over denominator 12.5 percent sign end fraction space equals space 0.64', '$\\text{PED = } \\frac{\\% \\text{change} \\text{in} \\text{quantity} demanded}{\\% \\text{change} \\text{in} price} = \\frac{\\% \\Delta \\text{in} QD}{\\% \\Delta \\text{in} \\mathrm{P} } \\% \\Delta \\text{in} \\text{QD} = 8 \\% \\% \\Delta P = \\frac{90 - 80}{80} x 100 = 12.5 \\% \\text{PED = } \\frac{8 \\%}{12.5 \\%} = 0.64$', 'speechToTexSafe', 'md-span'),
    ('text PED\xa0=\xa0 end text fraction numerator percent sign space change space in space quantity space demanded over denominator percent sign space change space in space price end fraction space equals space fraction numerator percent sign triangle space in thin space QD over denominator percent sign triangle in space straight P end fraction\\n\\npercent sign space increment Q D space equals space fraction numerator 150 minus 200 over denominator 200 end fraction space x space 100 space equals space minus 25 percent sign\\n\\npercent sign space increment P space equals space fraction numerator 120 minus 80 over denominator 80 end fraction space x space 100 space equals space 50 percent sign\\n\\ntext PED\xa0=\xa0 end text space equals space fraction numerator 25 percent sign over denominator 50 percent sign end fraction space equals space 0.5', '$\\text{PED = } \\frac{\\% \\text{change} \\text{in} \\text{quantity} demanded}{\\% \\text{change} \\text{in} price} = \\frac{\\% \\Delta \\text{in} QD}{\\% \\Delta \\text{in} \\mathrm{P} } \\% \\Delta Q D = \\frac{150 - 200}{200} x 100 = - 25 \\% \\% \\Delta P = \\frac{120 - 80}{80} x 100 = 50 \\% \\text{PED} = \\frac{25 \\%}{50 \\%} = 0.5$', 'speechToTexSafe', 'md-span'),
    ('P E D space equals fraction numerator percent sign increment Q D over denominator percent sign increment P end fraction\\npercent sign increment Q D space equals fraction numerator 280 minus 200 over denominator 200 end fraction space x space 100 space equals space 40 percent sign\\npercent sign increment P space equals fraction numerator 40 space minus 50 over denominator 50 end fraction space x space 100 space equals space minus space 20 percent sign\\nP E D space equals fraction numerator 40 over denominator negative space 20 end fraction space minus space minus 2.0', '$P E D = \\frac{\\% \\Delta Q D}{\\% \\Delta P} \\% \\Delta Q D = \\frac{280 - 200}{200} x 100 = 40 \\% \\% \\Delta P = \\frac{40 - 50}{50} x 100 = - 20 \\% P E D = \\frac{40}{- 20} - - 2.0$', 'speechToTexSafe', 'md-span'),
    ('$ 60 space straight x space straight Q', '$\\$ 60 \\mathrm{x} \\mathrm{Q}$', 'speechToTexSafe', 'md-span'),
    ('equals fraction numerator Number space actively space seeking over denominator Total space labour space force end fraction space straight x space 100\\n\\nequals space fraction numerator 600 comma 000 over denominator 2 comma 400 comma 000 end fraction space straight x space 100\\n\\nequals space 25 percent sign', '$= \\frac{Number \\text{actively} seeking}{Total \\text{labour} force} \\mathrm{x} 100 = \\frac{600 , 000}{2 , 400 , 000} \\mathrm{x} 100 = 25 \\%$', 'speechToTexSafe', 'md-span'),
    ('Unemployment space rate space equals space fraction numerator 2.3 over denominator 30 end fraction space straight x space 100\\n\\nequals space 7.7 percent sign', '$\\text{Unemployment} \\text{rate} = \\frac{2.3}{30} \\mathrm{x} 100 = 7.7 \\%$', 'speechToTexSafe', 'md-span'),
    ('A equals πr squared equals straight pi open parentheses straight d over 2 close parentheses squared equals πd squared over 4', '`A = πr ^2 = pi ( d / 2 ) ^2 = πd ^2 / 4`', 'cie-plain', 'md-span'),
    ('increment rho equals open square brackets open parentheses fraction numerator 0.1 over denominator 10 end fraction close parentheses plus open parentheses fraction numerator 0.2 over denominator 15 end fraction close parentheses plus open parentheses fraction numerator 0.2 over denominator 30 end fraction close parentheses plus open parentheses fraction numerator 0.1 over denominator 30 end fraction close parentheses plus open parentheses fraction numerator 0.2 over denominator 15 end fraction close parentheses close square brackets cross times 10', '$\\Delta \\\\rho = [ ( \\frac{0.1}{10} ) + ( \\frac{0.2}{15} ) + ( \\frac{0.2}{30} ) + ( \\frac{0.1}{30} ) + ( \\frac{0.2}{15} ) ] \\times 10$', 'speechToTexSafe', 'md-span'),
    ('V subscript e m f end subscript cross times open parentheses fraction numerator R subscript 1 over denominator R subscript 1 plus R subscript 2 end fraction close parentheses', '$V_{e m f} \\times ( \\frac{R_{1} }{R_{1} + R_{2} } )$', 'speechToTexSafe', 'md-span'),
    ('R subscript T over R subscript M equals open parentheses 200 over 27 close parentheses divided by open parentheses 50 over 17 close parentheses equals open parentheses 5 over 2 close parentheses\\n  ', '`R _ T / R _ M = ( 200 / 27 ) / ( 50 / 17 ) = ( 5 / 2 )\\n`', 'cie-plain', 'md-span'),
    ('equals fraction numerator 4 open parentheses 1.7 cross times 10 to the power of negative 8 end exponent close parentheses L over denominator straight pi open parentheses 0.315 close parentheses squared end fraction', '$= \\frac{4 ( 1.7 \\times 10^{- 8} ) L}{ \\mathrm{\\pi } ( 0.315 )^{2}}$', 'speechToTexSafe', 'md-span'),
    ('A equals straight pi open parentheses straight d over 2 close parentheses squared', '`A = pi ( d / 2 ) ^2`', 'cie-plain', 'md-span'),
    ('A equals 1 half cross times 132 cross times 86 cross times sin open parentheses 28.15617... close parentheses\\nA equals 2678.37078...', '$A = 1 \\frac{1}{2} \\times 132 \\times 86 \\times \\sin ( 28.15617... ) A = 2678.37078...$', 'speechToTexSafe', 'md-span'),
    ('table row y equals cell fraction numerator 100 cross times 2 over denominator 8.4 cross times sin open parentheses 40 close parentheses end fraction end cell row blank equals cell 37.041043... end cell end table', '$\\begin{gathered} y = \\frac{100 \\times 2}{8.4 \\times \\sin ( 40 )} \\\\ = 37.041043... \\end{gathered}$', 'speechToTexSafe', 'md-span'),
    ('table row cell 5.03 end cell equals cell fraction numerator angle C O B over denominator 360 end fraction cross times 2 straight pi cross times 7 end cell row cell 5.03 cross times 360 end cell equals cell angle C O B cross times 2 straight pi cross times 7 end cell row cell fraction numerator 5.03 cross times 360 over denominator 2 straight pi cross times 7 end fraction end cell equals cell angle C O B end cell end table', '$\\begin{gathered} 5.03 & = \\frac{angle C O B}{360} \\times 2 \\mathrm{\\pi } \\times 7 \\\\ 5.03 \\times 360 & = \\text{angle} C O B \\times 2 \\mathrm{\\pi } \\times 7 \\\\ \\frac{5.03 \\times 360}{2 \\mathrm{\\pi } \\times 7} & = \\text{angle} C O B \\end{gathered}$', 'speechToTexSafe', 'md-span'),
    ('table row cell Area triangle end cell equals cell 1 half cross times 7.4 cross times 7.4 cross times sin 60 end cell end table', '$\\begin{gathered} \\text{Area} \\Delta & = 1 \\frac{1}{2} \\times 7.4 \\times 7.4 \\times \\sin 60 \\end{gathered}$', 'speechToTexSafe', 'md-span'),
    ('sin open parentheses theta degree close parentheses equals 3 over 5', '$\\sin ( \\\\theta ^{\\circ} ) = \\frac{3}{5}$', 'speechToTexSafe', 'md-span'),
    ('B equals cos to the power of negative 1 end exponent open parentheses 150 over 170 close parentheses equals 28.07248694...', '$B = \\cos ^{- 1} ( \\frac{150}{170} ) = 28.07248694...$', 'speechToTexSafe', 'md-span'),
    ('open square brackets B close square brackets subscript 3 over open square brackets B close square brackets subscript 1', '`[ B ] _ 3 / [ B ] _ 1`', 'cie-plain', 'md-span'),
    ('straight k equals fraction numerator rate over denominator left square bracket Br to the power of minus right square bracket left square bracket BrO subscript 3 superscript minus right square bracket left square bracket straight H to the power of plus right square bracket squared end fraction', '$\\mathrm{k} = \\frac{rate}{[ Br^{ - } ] [ BrO_{3}^{ - } ] [ \\mathrm{H} ^{ + } ] ^{2} }$', 'genericChain', 'md-span'),
    ('rate over open square brackets NO subscript 2 close square brackets squared', '$\\frac{rate}{open} \\text{square} \\text{brackets} NO_{2} ] ^{2}$', 'genericChain', 'md-span'),
    ('open square brackets C close square brackets subscript 4 over open square brackets C close square brackets subscript 3', '`[ C ] _ 4 / [ C ] _ 3`', 'cie-plain', 'md-span'),
    ('fraction numerator rate over denominator left square bracket NO right square bracket squared left square bracket straight O subscript 2 right square bracket end fraction', '`(rate)/(left square bracket NO right square bracket ^2 left square bracket O _ 2 right square bracket)`', 'cie-plain', 'md-span'),
    ('fraction numerator negative 2.2 minus open parentheses negative 0.9 close parentheses over denominator open parentheses 2.3 cross times 10 to the power of negative 3 end exponent close parentheses minus open parentheses 2.1 cross times 10 to the power of negative 3 end exponent close parentheses end fraction', '$\\frac{- 2.2 - ( - 0.9 )}{( 2.3 \\times 10^{- 3} ) - ( 2.1 \\times 10^{- 3} )}$', 'speechToTexSafe', 'md-span'),
    ('straight d equals space 1 minus open parentheses sum from blank to blank of open parentheses straight n over straight N close parentheses squared close parentheses', '`d = 1 - ( SUM_ _ to _ of ( n / N ) ^2 )`', 'cie-plain', 'md-span'),
    ('begin mathsize 14px style open parentheses n over N close parentheses squared end style', '$( \\frac{n}{N} )^{2}$', 'speechToTexSafe', 'md-span'),
    ('D equals 1 minus open parentheses straight capital sigma open parentheses straight n over straight N close parentheses squared close parentheses', '`D = 1 - ( capital sigma ( n / N ) ^2 )`', 'cie-plain', 'md-span'),
    ('RQ space equals space fraction numerator net space CO subscript 2 space produced over denominator straight O subscript 2 space consumed end fraction equals space fraction numerator 4 plus space open parentheses negative 0.72 close parentheses over denominator 4 end fraction equals fraction numerator 3.28 over denominator 4 end fraction equals 0.82', '$\\text{RQ} = \\frac{net CO_{2} produced}{ \\mathrm{O}_{2} consumed} = \\frac{4 + ( - 0.72 )}{4} = \\frac{3.28}{4} = 0.82$', 'speechToTexSafe', 'md-span'),
    ('bold italic t bold space equals space fraction numerator open vertical bar x with bar on top subscript 1 minus space x with bar on top subscript 2 close vertical bar over denominator square root of open parentheses fraction numerator s subscript 1 superscript 2 over denominator n subscript 1 end fraction plus fraction numerator s subscript 2 superscript 2 over denominator n subscript 2 end fraction close parentheses end root end fraction', '$t = \\frac{\\left| \\bar{x}_{1} - \\bar{x}_{2} \\right|}{\\sqrt{( \\frac{s_{1}^{2} }{n_{1} } + \\frac{s_{2}^{2} }{n_{2} } )}}$', 'speechToTexSafe', 'md-span'),
    ('straight S space equals space square root of fraction numerator 17.38 over denominator open parentheses 10 space minus space 1 close parentheses end fraction end root', '$\\mathrm{S} = \\sqrt{ \\frac{17.38}{( 10 - 1 )} }$', 'speechToTexSafe', 'md-span'),
    ('table row cell 3 e to the power of 3 x end exponent end cell equals cell 0 space space space space space space no space solutions end cell row cell open parentheses 2 x plus 3 close parentheses to the power of 5 end cell equals cell 0 space space space space space space x equals negative 3 over 2 end cell row cell open parentheses 2 x plus 7 close parentheses end cell equals cell 0 space space space space space space x equals negative 7 over 2 end cell end table', '$\\begin{gathered} 3 e^{3 x} & = 0 \\text{no} \\text{solutions} \\\\ ( 2 x + 3 )^{5} & = 0 x = - \\frac{3}{2} \\\\ ( 2 x + 7 ) & = 0 x = - \\frac{7}{2} \\end{gathered}$', 'speechToTexSafe', 'md-span'),
    ('table row cell fraction numerator straight d y over denominator straight d x end fraction end cell equals cell fraction numerator open parentheses 2 straight e cubed cross times 2 over 7 close parentheses minus open parentheses 6 straight e cubed cross times ln 7 close parentheses over denominator 4 straight e to the power of 6 end fraction end cell row blank equals cell negative 0.1382093041 end cell end table', '$\\begin{gathered} \\frac{ \\mathrm{d} y}{ \\mathrm{d} x} & = \\frac{( 2 \\mathrm{e}^{3} \\times \\frac{2}{7} ) - ( 6 \\mathrm{e}^{3} \\times \\ln 7 )}{4 \\mathrm{e}^{6} } \\\\ = - 0.1382093041 \\end{gathered}$', 'speechToTexSafe', 'md-span'),
    ('fraction numerator straight d y over denominator straight d x end fraction equals fraction numerator 6 open parentheses 2 close parentheses over denominator 3 open parentheses 2 close parentheses squared minus 4 end fraction minus open parentheses 2 close parentheses squared over 2\\nfraction numerator straight d y over denominator straight d x end fraction equals negative 1 half', '$\\frac{ \\mathrm{d} y}{ \\mathrm{d} x} = \\frac{6 ( 2 )}{3 ( 2 )^{2} - 4} - \\frac{( 2 )^{2}}{2} \\frac{ \\mathrm{d} y}{ \\mathrm{d} x} = - 1 \\frac{1}{2}$', 'speechToTexSafe', 'md-span'),
    ('fraction numerator d y over denominator d x end fraction space equals space minus 2 x space cross times space 3 over 2 open parentheses 16 space minus space x squared close parentheses to the power of 1 half end exponent', '$\\frac{d y}{d x} = - 2 x \\times \\frac{3}{2} ( 16 - x^{2} )^{1 \\frac{1}{2}}$', 'speechToTexSafe', 'md-span'),
    ('T equals 10 over 9 square root of 90 space 000 plus x squared end root plus fraction numerator 2 open parentheses 400 minus x close parentheses over denominator 3 end fraction', '$T = \\frac{10}{9} \\sqrt{90 000 + x^{2}} + \\frac{2 ( 400 - x )}{3}$', 'speechToTexSafe', 'md-span'),
    ('table row y equals cell fraction numerator 10 pi over denominator 1 third pi space x squared end fraction end cell row blank equals cell 30 over x squared end cell end table', '$\\begin{gathered} y = \\frac{10 \\pi }{1 \\frac{1}{3} \\pi x^{2}} \\\\ = \\frac{30}{x^{2}} \\end{gathered}$', 'speechToTexSafe', 'md-span'),
    ('y equals 4 open parentheses 2 over 3 close parentheses minus open parentheses 2 over 3 close parentheses squared minus 2 open parentheses 2 over 3 close parentheses cubed equals 44 over 27', '$y = 4 ( \\frac{2}{3} ) - ( \\frac{2}{3} )^{2} - 2 ( \\frac{2}{3} )^{3} = \\frac{44}{27}$', 'speechToTexSafe', 'md-span'),
    ('y equals 4 over x minus cube root of 27 over x end root', '$y = \\frac{4}{x} - \\sqrt[3]{\\frac{27}{x}}$', 'genericChain', 'md-span'),
    ('y equals open parentheses square root of x plus 3 minus fraction numerator 4 over denominator square root of x end fraction close parentheses squared', '$y = ( \\sqrt{x} + 3 - \\frac{4}{ \\sqrt{x} } )^{2}$', 'speechToTexSafe', 'md-span'),
    ('u subscript n equals a plus open parentheses n minus 1 close parentheses d', '$u_{n} = a + ( n - 1 ) d$', 'speechToTexSafe', 'md-span'),
    ('text f end text open parentheses 1 over k x close parentheses equals x', '$\\text{f} ( \\frac{1}{k} x ) = x$', 'speechToTexSafe', 'md-span'),
    ('text f end text open parentheses 1 over k x close parentheses', '$\\text{f} ( \\frac{1}{k} x )$', 'speechToTexSafe', 'md-span'),
    ('text power\xa0 end text open parentheses P close parentheses space equals space text current\xa0 end text open parentheses I close parentheses space cross times space text voltage\xa0 end text open parentheses V close parentheses', '$\\text{power } ( P ) = \\text{current } ( I ) \\times \\text{voltage } ( V )$', 'speechToTexSafe', 'md-span'),
    ('clockwise space momemts space equals space open parentheses 4.0 space straight N space cross times 1.0 space straight m close parentheses space plus space open parentheses 2.0 space straight N space cross times space 2.0 space straight m close parentheses space equals space 8.0 space straight N space straight m', '$\\text{clockwise} \\text{momemts} = ( 4.0 \\mathrm{N} \\times 1.0 \\mathrm{m} ) + ( 2.0 \\mathrm{N} \\times 2.0 \\mathrm{m} ) = 8.0 \\mathrm{N} \\mathrm{m}$', 'speechToTexSafe', 'md-span'),
    ('table row cell clockwise space moments space end cell equals cell space anticlockwise space moments end cell row blank blank blank row cell 180 space straight N space end cell equals cell space 20 space cm space cross times space straight F end cell row blank blank blank row cell fraction numerator 180 space straight N space cm over denominator 20 space cm end fraction space end cell equals cell space straight F end cell row blank blank blank row cell straight F space end cell equals cell space 9.0 space straight N end cell row blank blank blank end table', '$\\begin{gathered} \\text{clockwise} \\text{moments} & = \\text{anticlockwise} \\text{moments} \\\\ \\\\ 180 \\mathrm{N} & = 20 \\text{cm} \\times \\mathrm{F} \\\\ \\\\ \\frac{180 \\mathrm{N} cm}{20 cm} & = \\mathrm{F} \\\\ \\\\ \\mathrm{F} & = 9.0 \\mathrm{N} \\\\ \\end{gathered}$', 'speechToTexSafe', 'md-span'),
    ('fraction numerator T up diagonal strike L over denominator up diagonal strike 4 end fraction space equals space fraction numerator M g up diagonal strike L over denominator up diagonal strike 4 end fraction space plus space fraction numerator 3 m g up diagonal strike L over denominator up diagonal strike 4 end fraction', '$\\frac{T \\cancel{L} }{ \\cancel{4} } = \\frac{M g \\cancel{L} }{ \\cancel{4} } + \\frac{3 m g \\cancel{L} }{ \\cancel{4} }$', 'speechToTexSafe', 'md-span'),
    ('moment subscript ACW space equals space T space cross times space open parentheses L over 4 close parentheses', '$moment_{ACW} = T \\times ( \\frac{L}{4} )$', 'speechToTexSafe', 'md-span'),
    ('m subscript 2 d subscript 2 up diagonal strike g space equals space m subscript 1 up diagonal strike g square root of l subscript 1 squared space minus space h subscript 1 squared end root', '$m_{2} d_{2} \\cancel{g} = m_{1} \\cancel{g} \\sqrt{l_{1}^{2} - h_{1}^{2}}$', 'speechToTexSafe', 'md-span'),
    ('volume space of space hydrogen space open parentheses straight H subscript 2 close parentheses space equals space 5.0 space dm cubed', '`volume of hydrogen ( H _ 2 ) = 5.0 dm ^3`', 'cie-plain', 'md-span'),
    ('volume space of space hydrogen space open parentheses straight H subscript 2 close parentheses space equals space 0.2083 space mol space cross times space 24 space dm cubed mol to the power of negative 1 end exponent', '`volume of hydrogen ( H _ 2 ) = 0.2083 mol x 24 dm ^3 mol ^ - 1`', 'cie-plain', 'md-span'),
    ('volume space of space hydrogen space open parentheses straight H subscript 2 close parentheses space equals space moles space cross times space 24 space dm cubed mol to the power of negative 1 end exponent', '`volume of hydrogen ( H _ 2 ) = moles x 24 dm ^3 mol ^ - 1`', 'cie-plain', 'md-span'),
    ('fundamental space units space equals space 0.06757 space mol space cross times open parentheses 6.02 space cross times 10 to the power of 23 space mol to the power of negative 1 end exponent close parentheses', '$\\text{fundamental} \\text{units} = 0.06757 \\text{mol} \\times ( 6.02 \\times 10^{23} \\text{mol} ^{ - } 1 )$', 'genericChain', 'md-span'),
    ('2 cross times open parentheses 6.02 cross times 10 to the power of 23 close parentheses', '$2 \\times ( 6.02 \\times 10^{23} )$', 'speechToTexSafe', 'md-span'),
    ('CoCl subscript 2 bullet end subscript 6 straight H subscript 2 straight O space rightwards harpoon over leftwards harpoon CoCl subscript 2 space plus space 6 straight H subscript 2 straight O', '$CoCl_{2 bullet} 6 \\mathrm{H}_{2} \\mathrm{O} \\rightleftharpoons CoCl_{2} + 6 \\mathrm{H}_{2} \\mathrm{O}$', 'speechToTexSafe', 'md-span'),
    ('0.10 percent sign space space cross times space $ 12 straight m space equals space $ 12 comma 000', '$0.10 \\% \\times \\$ 12 \\mathrm{m} = \\$ 12 , 000$', 'speechToTexSafe', 'md-span'),
    ('0.25 percent sign space space cross times space $ 12 straight m space equals space $ 30 comma 000', '$0.25 \\% \\times \\$ 12 \\mathrm{m} = \\$ 30 , 000$', 'speechToTexSafe', 'md-span'),
    ('equals space $ 30 comma 000 space minus space $ 12 comma 000 space equals space $ 18 comma 000', '$= \\$ 30 , 000 - \\$ 12 , 000 = \\$ 18 , 000$', 'speechToTexSafe', 'md-span'),
    ('equals space 20 space cross times space 10 space equals space $ 200\\n\\nequals space $ 250 space plus space $ 25 space plus space $ 25 space equals space $ 300\\n\\nequals space $ 300 space plus space $ 200 space equals space $ 500\\n\\nequals space $ 500 space cross times space 1.5 space equals space $ 750', '$= 20 \\times 10 = \\$ 200 = \\$ 250 + \\$ 25 + \\$ 25 = \\$ 300 = \\$ 300 + \\$ 200 = \\$ 500 = \\$ 500 \\times 1.5 = \\$ 750$', 'speechToTexSafe', 'md-span'),
    ('equals space fraction numerator 1.05 over denominator 1.00 end fraction space cross times space 100 space equals space 105 percent sign', '$= \\frac{1.05}{1.00} \\times 100 = 105 \\%$', 'speechToTexSafe', 'md-span'),
    ('equals space fraction numerator 3 comma 900 over denominator 5 comma 000 end fraction space cross times space 100 space equals 78 percent sign', '$= \\frac{3 , 900}{5 , 000} \\times 100 = 78 \\%$', 'speechToTexSafe', 'md-span'),
    ('efficiency space equals space fraction numerator useful space power space or space energy space output over denominator total space power space or space energy space input end fraction space cross times space 100 space percent sign', '$\\text{efficiency} = \\frac{useful \\text{power} \\text{or} \\text{energy} output}{total \\text{power} \\text{or} \\text{energy} input} \\times 100 \\%$', 'speechToTexSafe', 'md-span'),
    ('E subscript K equals 1 half m open parentheses v over 2 close parentheses squared', '$E_{K} = 1 \\frac{1}{2} m ( \\frac{v}{2} )^{2}$', 'speechToTexSafe', 'md-span'),
    ('fraction numerator 0.5 over denominator 8.0 end fraction cross times 100 percent sign', '$\\frac{0.5}{8.0} \\times 100 \\%$', 'speechToTexSafe', 'md-span'),
    ('fraction numerator 7.5 over denominator 0.5 end fraction cross times 100 percent sign', '$\\frac{7.5}{0.5} \\times 100 \\%$', 'speechToTexSafe', 'md-span'),
    ('fraction numerator 600 space 000 over denominator open parentheses 4 cross times 60 close parentheses end fraction', '$\\frac{600 000}{( 4 \\times 60 )}$', 'speechToTexSafe', 'md-span'),
    ('fraction numerator 8.0 over denominator 0.5 end fraction cross times 100 percent sign', '$\\frac{8.0}{0.5} \\times 100 \\%$', 'speechToTexSafe', 'md-span'),
    ('straight k space equals space fraction numerator 1 over denominator open parentheses MPS space plus space MRT close parentheses end fraction<br>k space equals space fraction numerator 1 over denominator open parentheses 0.2 space plus space 0.15 close parentheses end fraction', '$\\mathrm{k} = \\frac{1}{( \\text{MPS} + \\text{MRT} )} \\\\ k = \\frac{1}{( 0.2 + 0.15 )}$', 'speechToTexSafe', 'md-span'),
    ('straight k space equals space fraction numerator 1 over denominator The space marginal space propensities space to space withdraw end fraction\\n\\nstraight k space equals space fraction numerator 1 over denominator open parentheses MPS space plus space MRT space plus space MPM close parentheses end fraction', '$\\mathrm{k} = \\frac{1}{The \\text{marginal} \\text{propensities} \\text{to} withdraw} \\mathrm{k} = \\frac{1}{( \\text{MPS} + \\text{MRT} + \\text{MPM} )}$', 'speechToTexSafe', 'md-span'),
    ('straight k space equals space fraction numerator 1 over denominator open parentheses MPS space plus space MPM close parentheses end fraction', '$\\mathrm{k} = \\frac{1}{( \\text{MPS} + \\text{MPM} )}$', 'speechToTexSafe', 'md-span'),
    ('straight k space equals space fraction numerator 1 over denominator open parentheses MPS space plus space MRT space plus space MPM close parentheses end fraction<br>straight k space equals space fraction numerator 1 over denominator open parentheses 0.2 space plus space 0.15 space equals space 0.15 close parentheses end fraction', '$\\mathrm{k} = \\frac{1}{( \\text{MPS} + \\text{MRT} + \\text{MPM} )} \\\\ \\mathrm{k} = \\frac{1}{( 0.2 + 0.15 = 0.15 )}$', 'speechToTexSafe', 'md-span'),
    ('straight k space equals space 1 over MPS space equals space fraction numerator 1 over denominator open parentheses 1 space minus space MPC close parentheses end fraction', '$\\mathrm{k} = \\frac{1}{MPS} = \\frac{1}{( 1 - \\text{MPC} )}$', 'speechToTexSafe', 'md-span'),
    ('straight k space equals space fraction numerator 1 over denominator open parentheses MPS space plus space MRT space plus space MPM close parentheses end fraction', '$\\mathrm{k} = \\frac{1}{( \\text{MPS} + \\text{MRT} + \\text{MPM} )}$', 'speechToTexSafe', 'md-span'),
    ('fraction numerator $ 7 space 000 space plus space $ 9 space 000 over denominator 2 end fraction equals $ 8 space 000', '$\\frac{\\$ 7 000 + \\$ 9 000}{2} = \\$ 8 000$', 'speechToTexSafe', 'md-span'),
    ('fraction numerator Profit space for space the space year space open parentheses after space interest close parentheses over denominator Revenue end fraction cross times 100', '`(Profit for the year ( after interest ))/(Revenue) x 100`', 'cie-plain', 'md-span'),
    ('fraction numerator $ 600 space 000 over denominator $ 1.50 end fraction equals 400 space 000', '$\\frac{\\$ 600 000}{\\$ 1.50} = 400 000$', 'speechToTexSafe', 'md-span'),
    ('$ 0.11 plus $ 0.10 equals $ 0.21 space per space share\\n$ 0.21 cross times 500 space 000 equals $ 105 space 000', '`$ 0.11 + $ 0.10 = $ 0.21 per share\\n$ 0.21 x 500 000 = $ 105 000`', 'cie-plain', 'md-span'),
    ('400 space 000 cross times $ 0.14 equals $ 56 space 000', '$400 000 \\times \\$ 0.14 = \\$ 56 000$', 'speechToTexSafe', 'md-span'),
    ('fraction numerator $ 80 space 000 over denominator 500 space 000 end fraction equals $ 0.16', '$\\frac{\\$ 80 000}{500 000} = \\$ 0.16$', 'speechToTexSafe', 'md-span'),
    ('equation', None, 'untouched', 'negative'),
    ('x', None, 'untouched', 'negative'),
    ('GDP graph', None, 'untouched', 'negative'),
    ('photo of a circuit diagram', None, 'untouched', 'negative'),
    ('See diagram', None, 'untouched', 'negative'),
    ('2023 paper 2 variant 1', None, 'untouched', 'negative'),
]

FAIL_CLOSED_NEGATIVES = [
    "equation",
    "x",
    "GDP graph",
    "photo of a circuit diagram",
    "See diagram",
    "2023 paper 2 variant 1",
]

GUARD_CASES = [
    (r"\frac{1}{2}", True),                        # valid
    (r"x_{1}^{2}", True),                          # sub then sup: legit
    (r"a ^{\frac{n}{b}}^{n}", False),              # double superscript (nested braces)
    (r"x_{1}_{2}", False),                         # double subscript
    (r"10^{8 )", False),                           # unclosed exponent brace
    (r"l_{1} & l_{2}", False),                     # & with no environment
    (r"\begin{gathered} a & b \\ c & d \end{gathered}", True),  # legit alignment
    (r"\begin{gathered} a & b \end{array}", False),             # env mismatch
    ("x \\n y", False),                            # bare \n artifact
    (r"x \neq 0", True),                           # \neq stays legal
    ("x \\bar{y}\u0305", False),                   # combining mark
    (r"y = \frac{4}{x} - \sqrt[3]{\frac{27}{x}}", True),        # valid nested
]


def main():
    fails = []

    # leg 1 + 2: pinned pairs byte-exact (negatives expect None)
    for inp, exp, via, kind in PINNED_PAIRS:
        got = transpile_alt(inp)
        if got != exp:
            fails.append("PINNED [%s/%s] in=%r exp=%r got=%r" % (kind, via, inp[:70], exp, got if got is None else got[:70]))

    # leg 3: guard unit cases
    for tex, want in GUARD_CASES:
        got = _katex_approx_ok(tex)
        if got != want:
            fails.append("GUARD %r -> %r (want %r)" % (tex[:60], got, want))

    # leg 4: idempotence — outputs must not reconvert
    for inp, exp, via, kind in PINNED_PAIRS:
        if exp is None:
            continue
        again = transpile_alt(exp)
        if again is not None:
            fails.append("IDEMPOTENCE [%s] %r reconverted -> %r" % (kind, exp[:60], again[:60]))

    # leg 5: residual-grammar sweep over $-outputs
    for inp, exp, via, kind in PINNED_PAIRS:
        if exp and exp.startswith("$"):
            core = exp[1:-1]
            if has_residual_grammar(core):
                fails.append("RESIDUAL-GRAMMAR [%s]: %r" % (kind, core[:80]))

    print("battery: %d pinned / %d negatives / %d guard cases"
          % (len(PINNED_PAIRS), len(FAIL_CLOSED_NEGATIVES), len(GUARD_CASES)))
    if fails:
        print("FAIL (%d):" % len(fails))
        for f in fails[:12]:
            print("  " + f)
        sys.exit(1)
    print("ALL GREEN")


if __name__ == "__main__":
    main()
