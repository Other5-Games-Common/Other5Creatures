# Other5Creatures

Creature art (enemies today, any non-player creature tomorrow) for Other5 creations: skeletal meshes, animations, materials and the sounds each creature
makes. Content only, no C++. A creation makes its own enemy or NPC Blueprints from these (CubeEscape's `BP_CubeEnemy*` and
`BP_CubeBoss*` are examples), so behaviour, loot and tuning stay with the creation.

| Creature | Folder | Sounds |
|---|---|---|
| Barghest | `Content/Barghest` | `Barghest/Audio`: aggro, death |
| Griffon | `Content/Griffon` | (uses the shared attack sounds) |
| Kraken | `Content/Kraken` | `Kraken/Audio`: aggro, death |
| Stickman | `Content/Stickman` | (uses the shared attack sounds) |
| Whisper | `Content/Whisper` | `Whisper/Audio`: aggro, death |
| Shared | `Content/Shared/Audio` | Lyra melee whooshes and impacts for any creature's attacks |

## What's real here, and what's a stand-in
- **Other5's own:** the creature voices (`*/Audio/SW_*`, CC0, synthesised by CubeEscape's `Docs/Scripts/SetupSounds.py`)
  and `PAL_Creatures`.
- **Stand-ins** for what comes from Fab and Lyra (their licences don't let anyone share the source files):
  - the creatures from Fab: Barghest and Griffon (PROTOFACTOR's Quadruped Fantasy Creatures), Kraken, Whisper and
    Stickman (ROG Creatures). Each mesh is a small one-bone box with its own skeleton and physics asset; each
    animation holds still for a second; the textures and materials are plain;
  - Lyra's melee whooshes and impacts in `Shared/Audio`: a short soft tone of the same length.

  `StandIns.json` lists each one and where the real asset comes from.

To get the real look and sound, use **Tools > Other5 Setup** in the Other5 Creator. It walks you through getting the
Fab packs and Lyra Starter Game with your own Epic account, then puts the real assets in place of the stand-ins. Your
Creation's paks then ship them, cooked, under your own licence. The real files live in your **Other5 library** (by
default a folder `Other5Library` next to your project folder), never in this repository.

## Adding a creature
1. Make a folder `Content/<Name>` with `Meshes`, `Animations`, `Materials`, `Textures` and, if it has its own voice,
   `Audio`.
2. Set every animation's Bone and Curve Compression Settings to Other5Characters' `Other5AnimBoneCompressionSettings`
   and `Other5AnimCurveCompressionSettings` (the Other5 Tool refuses to cook others).
3. Make the enemy Blueprint in your creation (child of `Other5Enemy` or a CubeEscape enemy), pointing at the mesh,
   animations and sounds here.

Depends on Other5Characters.
