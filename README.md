## CS2 Developer Reference

Structured, navigatable HTML documentation for Counter-Strike 2 — entity
schemas, network message (Protobuf) references, ConVars, and UML inheritance
diagrams — auto-generated from [GameTracking-CS2](https://github.com/SteamDatabase/GameTracking-CS2)
and published to **GitHub Pages**.

### How it works

[GameTracking-CS2](https://github.com/SteamDatabase/GameTracking-CS2) is
included as a **read-only git submodule** at `data/`.  A scheduled GitHub
Actions workflow runs every **30 minutes**, advances the submodule to the latest
upstream HEAD, and regenerates documentation if anything has changed.  The
updated submodule pointer and generated Markdown are committed back to this
repo and deployed to GitHub Pages automatically.

```
SteamDatabase/GameTracking-CS2  (upstream, read-only)
    └── data/  ← git submodule (pointer committed here)
            │
            ▼
  this repo
    ├── docs/generate_docs.py   ← generator
    ├── docs/overlays/          ← community annotations
    └── docs/*.md               ← generated output (committed) → GitHub Pages
```

### Browse the docs

Visit the GitHub Pages site for this repository, or browse `docs/` directly.

### Protobuf Reference

Every Protobuf file has a page in [`docs/proto/`](docs/proto/) containing a
Mermaid class diagram, full field tables, enum value listings, and
overlay-based annotations.

### Contributing annotations

Community members can add descriptions, notes, and reverse-engineered details
to any entity or Protobuf message by placing a YAML file under `docs/overlays/`.
These annotations are merged into the generated HTML at build time.

See [`docs/overlays/README.md`](docs/overlays/README.md) for the full format and examples.

### Running the generator locally

```bash
# Clone with submodule
git clone --recurse-submodules https://github.com/sid2934/CS2-OpenDevDocs.git
cd CS2-OpenDevDocs

# Or initialise the submodule in an existing clone
git submodule update --init

pip install pyyaml

python3 docs/generate_docs.py \
  --repo-root . \
  --data-root ./data \
  --output docs
```

### Join our Discord

[![Join our Discord](https://discord.com/api/guilds/467730051622764565/embed.png?style=banner2)](https://steamdb.info/discord/)
