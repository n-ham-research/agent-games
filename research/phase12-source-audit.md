# Real-algebraic source audit — Phase 12

16 October 2026. Original authors' book text was read through a [mirror](https://paperzz.com/doc/8144640/algorithms-in-real-algebraic-geometry), headed Basu–Pollack–Roy, 26 June 2016. This is an author-posted-version transcription, not an authenticated publisher PDF; author-hosted links failed.

Inspected: §12.4 pp499–500 defines real univariate output using a Thom-encoded root. Algorithm13.9 p551 bounds intermediate integer bits by (tau+bit(s))d^{O(k)}. Algorithm13.12 and Theorem13.13 pp553–554 give sampling in R^k, s^{k+1}d^{O(k)} arithmetic operations, and coefficient bits tau*d^{O(k)}. Numbering differs from published-edition Theorem13.11. Root read all these passages; the compact reviewer independently read output/sampling definitions and checked the bit conversion against root's retrieved intermediate bound.

Local application: polynomial-bit arithmetic converts these bounds to (sd)^{O(k)}poly(tau); clearing explicit rational denominators is polynomial in input length. Selecting a sample satisfying the Nash constraints yields exact algebraic output. The existing orbit construction and rational normalization repair then apply. No sampling solver was implemented. The missing theorem-text/bit/output check is resolved on this disclosed mirrored-text basis; publisher/author-copy authentication remains advisable before submission.
