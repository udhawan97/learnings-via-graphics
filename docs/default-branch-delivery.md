# Default-branch delivery and failed-write recovery

This is the operational checklist for Elf and Mobster when maintaining this repository. Follow [editorial standards](editorial-standards.md) for content quality and safety. The objective is **a genuine, reviewed improvement reachable from `main`**, not an unreferenced Git object, an open PR, or a contribution square alone.

## Completion contract

An attempted write has four distinct states. Never collapse them into “committed”:

1. **Object prepared:** Git blob/tree/commit exists, but may be unreachable from any branch.
2. **Branch updated:** read back the exact feature branch ref and confirm it resolves to the new SHA.
3. **PR merged:** GitHub reports a successful merge, with no required review/check/protection bypass or deployment authorization gap.
4. **Default branch verified:** fetch `main` again, confirm the merge/accepted commit is reachable from it, inspect the final files, and verify the linked GitHub author and Chicago-local author/committer dates. A PR head is not sufficient proof. The visual graph is separately `VISUAL GRAPH NOT VERIFIED` unless inspected.

Only step 4 is a **verified default-branch landing**. Never label a commit eligible if ownership/fork/attribution/ancestry cannot be verified. No guarantee is made about when GitHub updates its contribution calendar.

## Start fast: finish existing work before starting another

- Confirm authenticated account `udhawan97`, public owned writable non-fork repository, `main` head, rulesets, currently open PRs and automation branches. Never guess fork status.
- Inspect open or stranded Elf/Mobster PRs and automation branches **first**. Resume independently valuable unmerged work rather than creating a competing edition or generic engineering log.
- Choose a bounded, meaningful deliverable with verifiable tests or source evidence. Respect the editorial pre-draft and final five-perspective checks.
- Capture exact base SHA and use a feature branch and PR; do not equate creating a branch with landing a contribution. Favor the **smallest verified path to a safe merge**; avoid broad speculative rewrites that cannot be completed during this invocation.

## Recover a stranded commit safely

1. **Read back:** fetch both `main` and the intended feature branch ref, plus the proposed commit. Compare `main...<commit SHA>` and inspect changed paths, parents, GitHub-linked author and diff. An unreferenced object may still be fetchable by SHA.
2. **Validate:** run or review reproducible tests/source checks and confirm the change remains useful, original and safe. Confirm no duplicate completed work already exists on `main`.
3. **Reconcile:** if the proposed commit is a fast-forward descendant of the *current* feature branch head, use one non-forced ref update with the **exact expected head SHA**. Read back the branch immediately. If the base moved, re-evaluate and create a new reviewed commit rather than forcing history.
4. **Classify failures:** `STALE_HEAD` -> refresh and rebuild against current base; `AUTH_OR_PERMISSION` -> stop and report; `REQUIRED_CHECK_OR_REVIEW` -> wait or stop; `DEPLOYMENT_UNKNOWN` -> hold PR; `PLATFORM_SAFETY_DENIAL` -> stop, do not bypass by switching API/repo; `TRANSIENT` -> at most one justified retry after state verification. Never retry an identical denied operation simply to push through a safety control.
5. **Finish:** open/reuse a scoped PR, inspect exact head and mergeability, required checks/reviews and deployment triggers, merge using expected head SHA only when genuinely allowed; re-fetch `main` and verify landing and attribution. If this cannot be done, report `BRANCH ONLY`, `PR PENDING`, or `NOT PERSISTED`, not success.

## Distinct legitimate fallback routes

In priority order: (1) merge a ready and reviewed nondeploying PR; (2) recover a useful stranded commit; (3) make a bounded tested defect/maintenance improvement; (4) publish **one substantive educational field guide** with original accessible diagrams, source ledger and exercise if all engineering routes are blocked or unproductive. Do not invent a fifth route made of filler, duplicate logs, rewritten dates or empty commits. A verified contribution today is permission to focus on quality, not to stop useful engineering work.

## Publishing firewall and read-only monitor

GitHub Pages and GitHub Actions are intentionally disabled. Do **not** enable them, create a release or tag, publish a website, or initiate deployment. Inspect both repository settings and push/PR/reusable-workflow/release triggers when available. If external hooks or an unknown deployment path cannot be verified, **hold the merge** and report the evidence gap. Never bypass branch protection, checks or human reviews. The 9 PM **GitHub Contribution Last Call** automation is **read-only**: it must never write to GitHub or edit any task. Elf and Mobster also must not mutate their own or other automation schedules from their scheduled runs.

## Incident: October 14–15, 2026

The Safe Saves lesson's authored commit object `4bf21e8f730a2729f5e393744936b592a3eed54a` existed but the October 14 recovery branch still pointed to `16365293013aacb142686baad8c827623324a7aa`; therefore nothing had landed on `main` on October 14. On October 15, the reviewed commit was recovered with a successful compare-and-swap non-forced ref update, its source reviewed and completed, and [PR #2](https://github.com/udhawan97/learnings-via-graphics/pull/2) was merged as `6e10bd36490460fdae16b819668e75849f07abd5`. Do not backdate or report that as an October 14 default-branch contribution.

The root process correction is to **verify every Git state transition** and to reserve enough of a scheduled run to finish a valid PR. Never claim a completed contribution from an orphan commit alone.
