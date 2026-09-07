#!/usr/bin/env python3
"""Check localization integrity and report outstanding source-identical prose."""
import argparse
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STRING = re.compile(r'"(?:[^"\\]|\\.)*"', re.S)
PROTECTED = re.compile(r'\[(?:q|qb|d|s):[^\]]*\]|\{[^{}]*\}|<[^>]+>|\\[rnt]|\r\n|\r|\n|\t')
TEXT_KEYS = {
	'Name', 'HumanName', 'Description', 'Tooltip', 'Label', 'Title',
	'BuyMessage', 'SellMessage', 'MoveMessage', 'ButtonText',
	'ChangeDescriptionText', 'LevelDescriptionText', 'AvailableAt',
	'PluralName', 'VariableDescriptionText',
}


def editable(name, path, source, obj):
	key = path[-1]
	if key not in TEXT_KEYS:
		return False
	if key != 'Name':
		return True
	if name in {'events', 'qualities', 'areas', 'Tutorials', 'exchanges'}:
		return not source.startswith('_') and source != 'REUSE'
	if name == 'Associations':
		return 'LegacyUnlockQualities' in path
	if name == 'CombatItems':
		return 'AssociatedQualityId' in obj
	return False


def check(source, target, name, path=(), parent=None, stats=None):
	assert type(source) is type(target), (name, path, 'value type changed')
	if isinstance(source, dict):
		assert list(source) == list(target), (name, path, 'keys/order changed')
		for key in source:
			check(source[key], target[key], name, path + (key,), source, stats)
	elif isinstance(source, list):
		assert len(source) == len(target), (name, path, 'array length changed')
		for index, (a, b) in enumerate(zip(source, target)):
			check(a, b, name, path + (index,), parent, stats)
	elif isinstance(source, str):
		assert PROTECTED.findall(source) == PROTECTED.findall(target), (name, path, 'protected token/line break changed')
		can_edit = editable(name, path, source, parent)
		if source != target:
			assert can_edit, (name, path, 'internal identifier changed')
			stats['translated_values'] += 1
		if can_edit and source.strip() and source == target:
			stats['source_identical_candidates'] += 1
			stats['source_identical_words'] += len(source.split())
	else:
		assert source == target, (name, path, 'nontext value changed')


def main():
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument('--format-ref', default='1459376', help='Git revision defining the original root JSON layout')
	args = parser.parse_args()
	for path in sorted((ROOT / 'uae').glob('*.json')):
		name = path.name.split('-')[0]
		payload = json.loads(path.read_bytes())['0 TextAsset Base']['1 string m_Script']
		output = ROOT / path.name.replace('-uae', '-content')
		text = output.read_bytes().decode('utf-8')
		baseline = subprocess.check_output(['git', 'show', args.format_ref + ':' + output.name], cwd=ROOT).decode('utf-8')
		assert STRING.sub('""', baseline) == STRING.sub('""', text), (output.name, 'original root formatting changed')
		stats = Counter()
		check(json.loads(payload), json.loads(text), name, stats=stats)
		print(output.name + ': ' + json.dumps(stats, sort_keys=True))
	print('Integrity checks passed. Source-identical candidates include proper names and are NOT a language-detection or completeness check.')
	print('Translation remains incomplete: see TRANSLATION.md for reviewed scope and outstanding work.')


if __name__ == '__main__':
	main()
