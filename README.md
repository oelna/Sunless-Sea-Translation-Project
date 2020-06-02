# Sunless Sea Translation Project

## Premise

There probably is never going to be an official translated version of [Sunless Sea](https://store.steampowered.com/app/304650/SUNLESS_SEA/) by [Failbetter Games](https://www.failbettergames.com/). I get it, it's a lot of text (250,000 words), difficult to translate while preserving nuance and there is no money in it. The audience is small as it is, for any given translation probably close to zero. This is something I wanted to try for myself. Sunless Sea is one of my favorite games. I love it as it is. I would say my english is pretty good and I can pick up many of the small details hidden in the language. But I would like to be able to play this with my young daugther, when she is a little older. Her english is not going to be good enough for a long time. We'll see how far this goes.

## What this is

I looked into how to extract data from Unity games, found Unity Asset Extractor (I used v2.2) and opened up `resources.assets`. If there are text strings in any of the other asset or resource files, I did not see them. I tested the procedure by loading a modified text asset back into the catalog file and loaded up the game. It worked!

The original extracts that UAE made are in the [`uae`](./uae/) directory. In order to be readable I parsed them using a small PHP script I hacked together (don't email me):

```php
<?php
	$string = "<string to process>";
	
	$result = preg_replace('/\\r\\n/', "\n", $string);
	$result = preg_replace('/\\n/', "\n", $result);
	$result = preg_replace('/\\t/', "\t", $result);
	
	$result = json_decode($result);
	
	echo(json_encode($result, JSON_PRETTY_PRINT));
?>
```

## What I want to accomplish

Ideally, I'd like to translate all the player facing text in the game, in my case to german. I have identified the following files:

**contain text to translate**

- [events](./events-1143-content.json) (Name, Description)
- [Tiles](./Tiles-1151-content.json) (HumanName, Description)
- [qualities](./qualities-1147-content.json) (Name, Description)
- [exchanges](./exchanges-1149-content.json) (Name, Description)
- [SpawnedEntities](./SpawnedEntities-1156-content.json) (HumanName)
- [areas](./areas-1141-content.json) (Name, Description)
- [Tutorials](./Tutorials-1154-content.json) (Name, Description)
- [CombatItems](./CombatItems-1153-content.json) (Name, Description)

**not containing player facing text**

- Flavours
- personas
- CombatAttacks
- TileRules
- Associations
- navigationconstants
- TileSets
- combatconstants

> Note: all `\"`, `\n` or `\t` inside `Description` text strings need to be left intact or it will be impossible to convert these back and put them in the game!

I will create a branch for each language, probably only german for now. I somebody wants to contribute, they are very welcome. You should ask yourself whether you're really up for this. I'd like to preserve as much of the flavour as possible, even if it means finding totally different expressions in german. You should bring at least decent english and german skills to the table.

There will be text I'm not going to translate, such as some names that are characteristic. I have not made an official guide that defined what stays. Maybe I'll get to it at some point.

## Disclaimer

I don't own any of the content. It's all [Failbetter Games](https://www.failbettergames.com/)'. If there is a problem with me attempting this, let me know and I'll take this down. I don't know who this is hurting this late in the game's life cycle, but I don't mean to cause trouble. I have bought the game myself multiple times (Steam, iPad) and I suggest you do the same. It's perfect. I bought Sunless Skies as well but I could never bring myself to boot it up. I don't care much for the steampunk space setting. The <del>SUN</del> Zee hits home for me.
