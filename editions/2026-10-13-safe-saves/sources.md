# Sources & claim ledger — reviewed source edition

- **Primary category / track:** Engineering / The Builder's Workbench
- **Topic:** Files & reliability
- **Reading layers:** [Visual brief](brief.md) · [Full guide](index.html)

- **Edition:** Safe Saves: why a renamed file is not the same as a durable transaction
- **Track:** The Builder's Workbench
- **Reporting date:** 2026-10-13 (America/Chicago)
- **Primary-source consultation:** 2026-10-13; rechecked 2026-10-14
- **Publication scope:** Educational source files only. No GitHub Pages website, installer, package release or deployment; only a merged, reviewed PR is indexed as a completed archive edition.

| Claim / panel | Evidence level | Primary source | Publication/update date | Consulted | Qualification |
| --- | --- | --- | --- | --- | --- |
| [P1] `os.replace(src, dst)` overwrites an existing destination file, is atomic on success under POSIX, and may fail across filesystems. Panels 1–3. | FOUNDATION / documented API contract | https://docs.python.org/3/library/os.html#os.replace | Python 3.15.0 documentation; page footer updated **2026-10-13** | 2026-10-13 | Atomicity describes visibility of a rename on a supporting local filesystem, not guaranteed survival of a crash. Windows and unusual/network filesystems have additional limits. |
| [P2] Buffered file objects need `flush()` before `os.fsync()`; `fsync` invokes the OS sync primitive. Panel 2 and lab. | FOUNDATION / documented API contract | https://docs.python.org/3/library/os.html#os.fsync | Python 3.15.0 documentation; page footer updated **2026-10-13** | 2026-10-13 | OS/storage hardware can break durability assumptions. This is a best-effort request, not a certification of power-loss resistance. |
| [P3] `NamedTemporaryFile` securely creates a named temporary file; `delete=False` requires deliberate cleanup. Panel 2 and lab. | FOUNDATION / documented API contract | https://docs.python.org/3/library/tempfile.html#tempfile.NamedTemporaryFile | Python 3.15.0 documentation; page footer updated **2026-10-13** | 2026-10-13 | The lab uses the parent directory for same-filesystem replacement and deletes leftover temp files. This does not establish a defense against malicious path races in an untrusted directory. |
| [L1] Linux `rename` atomically replaces existing file pathname; rename on NFS may report failure after actually completing. Panels 2, 3, 5. | FOUNDATION / system behavior | https://man7.org/linux/man-pages/man2/rename.2.html | Linux man-pages 6.19, **2026-02-08** | 2026-10-13 | Linux-specific explanation; avoid extrapolation to cloud sync, arbitrary Windows handles, and remote mounts. |
| [S1] SQLite uses rollback-journal or WAL mechanisms to make multi-page commits atomic; sync order and storage assumptions matter. Panels 3, 5. | FOUNDATION / upstream technical documentation | https://www.sqlite.org/atomiccommit.html | Page **undated** | 2026-10-13 | Its detailed model assumes particular hardware properties and settings; this edition does not claim SQLite guarantees on broken media. |
| [S2] SQLite WAL permits readers during a writer and one writer at a time; WAL is inappropriate across network filesystems. Panel 5. | FOUNDATION / upstream technical documentation | https://www.sqlite.org/wal.html | WAL introduced in SQLite **3.7.0 on 2010-07-21**; page update date undated | 2026-10-13 | This is about SQLite WAL, not the `os.replace` teaching lab, which has **no** concurrency protocol. |
| [S3] Disk, journaling and application misuse can corrupt SQLite databases; choose recovery tests, not blanket durability assurances. Panel 5. | FOUNDATION / upstream technical documentation | https://www.sqlite.org/howtocorrupt.html | Page **undated** | 2026-10-13 | Not evidence that this small lab withstands actual power failure. |

## Editorial boundaries

**No simulated crash is a hardware power-off test.** The included test suite runs controlled ordinary Python exceptions and inspects local filesystem states. The diagram is conceptual with no empirical axes or measured reliability percentages. `sync_directory()` returns an attempted local `fsync` result, not proof that all device caches persisted data. The lab intentionally uses a single writer and trusted temporary folder; it is not an audited replacement for production application save pipelines. For untrusted input, shared drives, multi-writer state, coordinated metadata, encryption and backups, use vetted platform APIs / transactional storage and a tailored threat model.

**Review:** Sequential fact-check, domain analysis, education design, visual/accessibility, and safety/minimalism perspectives; no independent external editorial participants. Final test/render outcomes must be recorded separately, not inferred here.


## Visual brief and reusable diagrams

The brief added on October 20, 2026 summarizes this edition; the SVGs in `assets/` reproduce its original inline diagrams. Existing claim mappings and limitations apply to both reading layers. This navigation update does not redate the original source review or assert a new product release.
