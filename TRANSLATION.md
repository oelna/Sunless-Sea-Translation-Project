# German translation: work in progress

This is **not a complete German localization**. The main narrative and quality collections still need substantial translation and editorial review. Do not infer completeness from the number of files processed.

## Reviewed scope

| Collection | Scope of this pass |
| --- | --- |
| Associations | Legacy titles, descriptions, and tooltips; jettison dialogue |
| CombatAttacks | All seven damage descriptions; attack identifiers retained |
| CombatItems | All eight player-facing item names and descriptions; function names retained |
| SpawnedEntities | All 50 display names; spawn and behavior identifiers retained |
| Tiles | All 341 nonempty display names, labels, and descriptions |
| Tutorials | All 34 titles and 34 descriptions |
| areas | All 213 nonempty names, descriptions, and movement messages |
| exchanges | All 170 nonempty shop names, headings, descriptions, and trade messages |
| personas | All 40 descriptive values reviewed; persona identifiers retained |
| Flavours, TileRules, TileSets, combatconstants, navigationconstants | Internal configuration inspected and retained unchanged |
| events | Opening passages and damaged passages revised; inherited token and paragraph-break defects repaired. Most prose remains English. |
| qualities | Untranslated; full review outstanding |

The nine supporting collections contain 933 reviewed values. Some properly remain identical, including names such as Irem, Anthe, and Thalatte, the label Sonar, and internal sentinel values. This is an editorial pass, not an in-game layout test.

At this checkpoint, `events` has 19,270 source-identical candidate text values, containing approximately 383,914 source words. `qualities` has 2,403 source-identical candidate values, containing approximately 28,655 source words. These counts include proper names and development text; they are not exact counts of untranslated player-visible English. The older translated event text also needs a complete literary review.

## Working voice and terminology

Use concise, idiomatic German, with restrained dread, dry humour, and room for ambiguity. Narration and tutorials address the player as `du`. Preserve a speaker's individual voice when working through the remaining dialogue. Do not explain mysteries or supply lore that the original withholds. Prefer a natural short sentence to an expanded paraphrase; never truncate essential meaning merely to meet a character count.

| English | Working German |
| --- | --- |
| Zee / Unterzee | Zee / Unterzee |
| zailor | Zeemann / Zeeleute |
| Neath | Unterwelt |
| Fallen London | Gefallenes London |
| Terror | Schrecken |
| Hearts / Iron / Pages / Mirrors / Veils | Herzen / Eisen / Seiten / Spiegel / Schleier |
| Echoes / Fragments / Secrets | Echos / Fragmente / Geheimnisse |
| Hull / Hold / Crew / Supplies / Fuel | Rumpf / Laderaum / Besatzung / Vorräte / Treibstoff |
| zubmarine | Zeeboot |
| firing solution | Feuerleitlösung |
| Drownies / Clay Men | Ertrunkene / Lehmmenschen |
| Salt | Salz |
| Dawn Machine | Morgenrötenmaschine |
| Lifeberg / Behemoustache | Lebberg / Behemobart |
| Bound-Shark / Jillyfleur | Fesselhai / Quallenblüte |
| Snuffer / Fluke | Snuffer / Fluke |

`Lebberg` and `Behemobart` are compact adaptations of the creature-name wordplay. `Ein eisernes Testament` echoes the iron/will imagery of `A Ironclad Will`. `Unklare Vorrichtung` retains the surface ambiguity of `Unclear Device`; its resemblance to “nuclear device” is not fully recoverable in this wording and merits later review. Proper names are not translated merely because they resemble ordinary words. The remaining events and qualities have not yet been brought into agreement with this terminology.

Setting references consulted before translation: [Failbetter's Sunless Sea and Zubmariner overview](https://www.failbettergames.com/games/sunless-sea) and [the developer's Steam description](https://store.steampowered.com/app/304650/SUNLESS_SEA/).

## Integrity and formatting

The originals remain in `uae`. The root `*-content.json` files retain their original four-space indentation and all structural whitespace. Only JSON string-value tokens were changed; no serializer was allowed to reformat the whole document. JSON keys, array order, IDs, numbers, booleans, nulls, asset references, code expressions, and function/variable names are retained.

The integrity check compares every root JSON file with the decoded `m_Script` source. It also checks embedded references such as `[q:Addressed as]`, `{x}` and `{y}`, markup, and paragraph/control-character sequences. The existing event translation had changed one quality-reference name and damaged line-break sequences in 88 other values; these have been repaired. An incorrectly translated `_REUSE` sentinel was also restored. The few passages with missing paragraphs were retranslated against the source.

Run:

```sh
python tools/validate_translation.py
```

The checker verifies structural integrity and reports source-identical candidates. It does **not** certify translation completeness, literary quality, or whether text fits inside the game's UI. Those remain editorial and in-game review tasks.
