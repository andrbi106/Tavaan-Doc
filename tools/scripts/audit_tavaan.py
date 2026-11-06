#!/usr/bin/env python3
"""
audit_tavaan.py — ممیزی پروژه تَوان بر اساس skill tavaan-doc-writer
بررسی قوانین R1-R10 و اصول P1-P12
"""
import os, re, sys, json
from pathlib import Path

PROJECT = '/home/z/my-project/workspace/Tavaan-Demo'

def scan():
    report = {
        'project': 'Tavaan-Demo',
        'rules': {},
        'principles': {},
        'structure': {},
        'contradictions': [],
        'differences_with_reference': []
    }

    php_files = []
    for root, dirs, files in os.walk(PROJECT):
        if '/.git/' in root + '/' or '/vendor/' in root + '/': continue
        for f in files:
            if f.endswith('.php'):
                php_files.append(os.path.join(root, f))

    report['total_php_files'] = len(php_files)

    # R1: strict_types
    no_strict = []
    for f in php_files:
        try:
            content = open(f, encoding='utf-8').read()
            if 'declare(strict_types=1)' not in content:
                no_strict.append(os.path.relpath(f, PROJECT))
        except: pass
    report['rules']['R1_strict_types'] = {
        'violations': len(no_strict),
        'files': no_strict[:20]
    }

    # R3: ZeroDependency
    composer_jsons = []
    for root, dirs, files in os.walk(PROJECT):
        if '/.git/' in root + '/': continue
        for f in files:
            if f == 'composer.json':
                composer_jsons.append(os.path.relpath(os.path.join(root, f), PROJECT))

    psr_refs = []
    for f in php_files:
        try:
            content = open(f, encoding='utf-8').read()
            if re.search(r'use Psr\\|extends Psr\\', content):
                for m in re.finditer(r'use Psr\\[^\s;]+|extends Psr\\[^\s{]+', content):
                    psr_refs.append(f"{os.path.relpath(f, PROJECT)}: {m.group(0)}")
        except: pass

    psr4_keys = []
    for root, dirs, files in os.walk(PROJECT):
        if '/.git/' in root + '/': continue
        for fn in files:
            if fn.endswith('.php') or fn.endswith('.json'):
                fpath = os.path.join(root, fn)
                try:
                    content = open(fpath, encoding='utf-8').read()
                    if '"psr-4"' in content or "'psr-4'" in content:
                        psr4_keys.append(os.path.relpath(fpath, PROJECT))
                except: pass

    report['rules']['R3_zero_dependency'] = {
        'composer_json_files': composer_jsons,
        'psr_use_refs': psr_refs[:20],
        'psr4_keys': psr4_keys[:20]
    }

    # R8: error handling
    raw_exceptions = []
    for f in php_files:
        try:
            content = open(f, encoding='utf-8').read()
            for m in re.finditer(r'throw new \\\\?(Exception|RuntimeException|InvalidArgumentException|LogicException|Error)\(', content):
                raw_exceptions.append(f"{os.path.relpath(f, PROJECT)}: {m.group(0)}")
        except: pass
    report['rules']['R8_error_handling'] = {
        'raw_exceptions': len(raw_exceptions),
        'samples': raw_exceptions[:10]
    }

    # Engine count
    engines_dir = os.path.join(PROJECT, 'engines')
    engines = []
    if os.path.isdir(engines_dir):
        for d in os.listdir(engines_dir):
            if os.path.isdir(os.path.join(engines_dir, d)):
                engines.append(d)
    report['structure']['engines'] = {
        'count': len(engines),
        'list': sorted(engines)
    }

    # DOC-IDs in docs
    doc_ids = set()
    docs_dir = os.path.join(PROJECT, 'docs')
    if os.path.isdir(docs_dir):
        for root, dirs, files in os.walk(docs_dir):
            for f in files:
                if f.endswith('.md'):
                    fpath = os.path.join(root, f)
                    try:
                        content = open(fpath, encoding='utf-8').read()
                        for m in re.finditer(r'\bDOC-(\d{3})\b', content):
                            doc_ids.add(m.group(0))
                    except: pass
    report['structure']['doc_ids_found'] = sorted(doc_ids)

    # ADRs
    adr_dir = os.path.join(PROJECT, 'docs', 'adr') if os.path.isdir(os.path.join(PROJECT, 'docs')) else os.path.join(PROJECT, 'adr')
    adrs = []
    if os.path.isdir(adr_dir):
        for f in os.listdir(adr_dir):
            if f.startswith('ADR-') and f.endswith('.md'):
                adrs.append(f)
    report['structure']['adrs'] = sorted(adrs)

    # Differences with reference
    ref_engines = 53
    ref_adrs = 16
    report['differences_with_reference'] = [
        f"تعداد موتورها: مرجع={ref_engines}, دمو={len(engines)} (تفاوت: {ref_engines - len(engines)})",
        f"تعداد ADR: مرجع={ref_adrs}, دمو={len(adrs)} (تفاوت: {ref_adrs - len(adrs)})",
        f"مستندات موتور (17-بخشی): مرجع=53 سند کامل, دمو=فقط README/TROUBLESHOOTING",
        f"manifest.json ماشین‌خوان: مرجع=موجود, دمو=نبود",
        f"JSON Schemaها: مرجع=4 فایل, دمو=نبود",
        f"قالب‌ها (templates): مرجع=3 قالب, دمو=نبود",
        f"tools/scripts: مرجع=3 اسکریپت, دمو=نبود",
        f"docs/ با 10 بخش شماره‌گذاری‌شده: مرجع=موجود, دمو=نبود (فقط docs/skills/)",
        f"CLI 105 دستور: مرجع=کامل, دمو=فقط 5 دستور (info/version/engines/config/serve)",
        f"config-reference: مرجع=48 فایل config + 111 کلید ENV, دمو=.env.example با 11 کلید",
        f"roles-matrix + permission-catalog: مرجع=موجود, دمو=نبود",
        f"testing-strategy + definition-of-done: مرجع=موجود, دمو=نبود",
        f"roadmap M0-M9 + agent-backlog: مرجع=موجود, دمو=نبود",
        f"glossary فارسی↔لاتین: مرجع=موجود, دمو=نبود",
        f"applications (8 بلوپرینت): مرجع=موجود, دمو=نبود"
    ]

    # Contradictions
    contradictions = []
    if composer_jsons:
        contradictions.append(f"وجود composer.json ({len(composer_jsons)} فایل) در حالی که قانون ZeroDependency (R3) آن را ممنوع می‌کند")
    if psr_refs:
        contradictions.append(f"ارجاع به Psr\\ در کد ({len(psr_refs)} مورد) در حالی که ZeroDependency آن را ممنوع می‌کند")
    if psr4_keys:
        contradictions.append(f"کلید 'psr-4' در {len(psr4_keys)} فایل — تَوان از 'namespace-map' استفاده می‌کند")
    if no_strict:
        contradictions.append(f"{len(no_strict)} فایل PHP بدون declare(strict_types=1) — نقض R1")
    report['contradictions'] = contradictions

    return report

if __name__ == '__main__':
    r = scan()
    print(json.dumps(r, ensure_ascii=False, indent=2))
