"""Plugin and marketplace are well formed, and every file the skill points to exists."""
import json, os, re
mk = json.load(open('.claude-plugin/marketplace.json'))
pl = json.load(open('plugin/.claude-plugin/plugin.json'))
entry = [p for p in mk['plugins'] if p['name'] == pl['name']]
assert mk.get('name') and mk.get('owner', {}).get('name'), 'marketplace needs name and owner'
assert len(entry) == 1 and entry[0]['source'] == './plugin', 'marketplace entry must match plugin name and point to ./plugin'
assert re.fullmatch(r'\d+\.\d+\.\d+', pl['version']), 'plugin version must be X.Y.Z'
skill = 'plugin/skills/landing-kit/SKILL.md'
s = open(skill, encoding='utf-8').read()
fm = re.match(r'---\n(.*?)\n---\n', s, re.S)
assert fm, 'SKILL.md needs YAML frontmatter'
meta = dict(re.findall(r'^(\w+):\s*(.*)$', fm.group(1), re.M))
assert meta.get('name') == 'landing-kit' and re.fullmatch(r'[a-z0-9-]{1,64}', meta['name'])
assert 0 < len(meta.get('description', '')) <= 1024, 'description must be 1-1024 characters'
assert '<' not in meta['description'] and '>' not in meta['description'], 'no angle brackets in description'
base = os.path.dirname(skill)
for ref in sorted(set(re.findall(r'`((?:scripts|references|assets)/[^`\s]*)`', s))):
    assert os.path.exists(os.path.join(base, ref.rstrip('/'))), 'SKILL.md points to a missing file: ' + ref
print('plugin: manifests, skill frontmatter and referenced files ok (version ' + pl['version'] + ')')
