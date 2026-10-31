$$
\node (two) at (0,0) {$2$};
\node (lp) at (0.3,0) {$($};
\node (a) at (0.6,0) {$a$};
\node (plus) at (1.0,0) {$+$};
\node (three) at (1.4,0) {$3$};
\node (rp) at (1.7,0) {$)$};
\node at (2.2,0) {$=$};
\node at (2.7,0) {$2a$};
\node at (3.1,0) {$+$};
\node at (3.5,0) {$6$};

\draw[->, bend left=40, color=black, thin]
(two.north) to (a.north);
\draw[->, bend left=40, color=black, thin]
(two.north) to (three.north);
$$