# Positive obedience margins prevent zero punishment

16 October2026. Author Nicholas Ham; root Codex proof, independently checked
by the separate Phase13 audit reviewer. This is a direct CE inequality corollary,
not a novelty claim or a full theory of boundedly rational agents.

Use the complete-information monotone contribution game in phase13-coalitions.md.
Write s for success probability, x_i for work probability, and p_i for the
probability i is pivotal. Pivotality implies p_i<=s. Suppose a recommendation
to i to work gives conditional expected gain at least eta>0 over abstaining.
The definition is the unconditional inequality

    B*p_i-c_i*x_i >= eta*x_i,

which remains meaningful when x_i=0. Then

    u_i = B*s-c_i*x_i >= B*eta*s/(c_i+eta).

Proof: the margin gives x_i<=B*p_i/(c_i+eta)<=B*s/(c_i+eta); substitute in
u_i. If successful singleton agents S exist, their always-work deviations give
u_j>=B-c_j, whereas u_j<=B*s, so s>=t0=1-min_(j in S)c_j/B. Therefore

    u_i >= B*eta*t0/(c_i+eta) > 0.

Thus P13-P2's zero-payoff continuations cannot have a positive work-obedience
margin for the punished agent. The margin need not hold for every agent or
every action, and does not assert robustness to coalitional deviations, noisy
signals or arbitrary learning dynamics. With no singleton, t0=0 provides no
positive bound. Security values alone and weak exact obedience are inadequate
for claiming a robust punishment implementation.

For the minimal-task family {s} or {i,j,k}, take B=2,c_s=1,c_i=3/2 and
eta=1/4. Mix {i,j,k} with probability1/2, failed{i} with probability1/14,
and empty with probability3/7. Agent i's work signal gives gain1/4, utility1/7,
meeting the bound exactly. Other selected agents have costs below2 and obey;
other abstainers cannot repair failure alone. The singleton's abstention gain
is zero. This witnesses sharpness for a specified agent's work margin, not
globally strict obedience.
