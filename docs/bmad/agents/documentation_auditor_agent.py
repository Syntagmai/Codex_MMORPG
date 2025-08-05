#!/usr/bin/env python3
"""
Documentation Auditor Agent
Audits documentation and wiki files for completeness, consistency, and quality.
"""

import os
import json
import re
import argparse
from datetime import datetime
from pathlib import Path

class DocumentationAuditor:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "project_root": str(self.project_root),
            "total_docs": 0,
            "total_wikis": 0,
            "broken_links": [],
            "outdated_content": [],
            "incomplete_docs": [],
            "missing_docs": [],
            "quality_issues": [],
            "general_problems": 0
        }
        
    def scan_documentation(self):
        """Scan all documentation and wiki files"""
        print("🔍 Scanning documentation and wiki files...")
        
        # Common documentation directories
        doc_dirs = [
            "docs/",
            "wiki/",
            "README.md",
            "CHANGELOG.md",
            "LICENSE",
            "*.md",
            "*.txt",
            "*.rst"
        ]
        
        total_files = 0
        doc_files = []
        
        # Scan for documentation files
        for pattern in doc_dirs:
            if pattern.endswith('/'):
                dir_path = self.project_root / pattern.rstrip('/')
                if dir_path.exists():
                    for file_path in dir_path.rglob('*'):
                        if file_path.is_file() and file_path.suffix.lower() in ['.md', '.txt', '.rst', '.html']:
                            doc_files.append(file_path)
                            total_files += 1
            else:
                for file_path in self.project_root.rglob(pattern):
                    if file_path.is_file():
                        doc_files.append(file_path)
                        total_files += 1
        
        self.results["total_docs"] = total_files
        
        # Analyze each documentation file
        for doc_file in doc_files:
            self.analyze_document(doc_file)
        
        # Check for missing critical documentation
        self.check_missing_documentation()
        
        # Check for outdated content
        self.check_outdated_content()
        
        # Check for broken links
        self.check_broken_links()
        
        # Check documentation quality
        self.check_documentation_quality()
        
        return self.results
    
    def analyze_document(self, file_path):
        """Analyze a single documentation file"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            relative_path = str(file_path.relative_to(self.project_root))
            
            # Check for incomplete sections
            incomplete_patterns = [
                r'TODO:',
                r'FIXME:',
                r'XXX:',
                r'\[ \]',
                r'INCOMPLETE',
                r'PENDING',
                r'TO BE DONE'
            ]
            
            for pattern in incomplete_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    self.results["incomplete_docs"].append({
                        "file": relative_path,
                        "issue": f"Contains incomplete marker: {pattern}",
                        "line": self.find_line_number(content, pattern)
                    })
            
            # Check for outdated content indicators
            outdated_patterns = [
                r'outdated',
                r'deprecated',
                r'old version',
                r'legacy',
                r'version \d+\.\d+',
                r'last updated.*\d{4}'
            ]
            
            for pattern in outdated_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    self.results["outdated_content"].append({
                        "file": relative_path,
                        "issue": f"Contains outdated indicator: {pattern}",
                        "line": self.find_line_number(content, pattern)
                    })
            
            # Check for broken markdown links
            if file_path.suffix.lower() == '.md':
                self.check_markdown_links(content, relative_path)
                
        except Exception as e:
            self.results["general_problems"] += 1
            print(f"Error analyzing {file_path}: {e}")
    
    def find_line_number(self, content, pattern):
        """Find line number where pattern occurs"""
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            if re.search(pattern, line, re.IGNORECASE):
                return i
        return 0
    
    def check_markdown_links(self, content, file_path):
        """Check for broken markdown links"""
        # Find all markdown links
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        matches = re.findall(link_pattern, content)
        
        for text, link in matches:
            if link.startswith('http'):
                # External link - could check if accessible
                continue
            elif link.startswith('#'):
                # Anchor link
                continue
            else:
                # Internal link
                link_path = Path(link)
                if not link_path.exists():
                    self.results["broken_links"].append({
                        "file": file_path,
                        "link": link,
                        "text": text
                    })
    
    def check_missing_documentation(self):
        """Check for missing critical documentation"""
        critical_docs = [
            "README.md",
            "docs/README.md",
            "wiki/README.md",
            "CHANGELOG.md",
            "LICENSE",
            "docs/installation.md",
            "docs/usage.md",
            "docs/api.md"
        ]
        
        for doc in critical_docs:
            doc_path = self.project_root / doc
            if not doc_path.exists():
                self.results["missing_docs"].append(doc)
    
    def check_outdated_content(self):
        """Check for potentially outdated content"""
        # Look for files with old timestamps or version numbers
        current_year = datetime.now().year
        
        for file_path in self.project_root.rglob('*.md'):
            try:
                stat = file_path.stat()
                # Check if file is older than 2 years
                if stat.st_mtime < (current_year - 2) * 365 * 24 * 3600:
                    self.results["outdated_content"].append({
                        "file": str(file_path.relative_to(self.project_root)),
                        "issue": f"File may be outdated (last modified: {datetime.fromtimestamp(stat.st_mtime)})",
                        "line": 0
                    })
            except:
                continue
    
    def check_broken_links(self):
        """Check for broken internal links"""
        # This is a simplified check - in a real implementation,
        # you might want to actually test the links
        pass
    
    def check_documentation_quality(self):
        """Check documentation quality metrics"""
        quality_issues = []
        
        for file_path in self.project_root.rglob('*.md'):
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                relative_path = str(file_path.relative_to(self.project_root))
                
                # Check for very short documentation
                if len(content.strip()) < 100:
                    quality_issues.append({
                        "file": relative_path,
                        "issue": "Very short documentation (less than 100 characters)",
                        "severity": "low"
                    })
                
                # Check for missing headers
                if not re.search(r'^#\s+', content, re.MULTILINE):
                    quality_issues.append({
                        "file": relative_path,
                        "issue": "Missing main header",
                        "severity": "medium"
                    })
                
                # Check for very long lines
                lines = content.split('\n')
                long_lines = [i+1 for i, line in enumerate(lines) if len(line) > 120]
                if long_lines:
                    quality_issues.append({
                        "file": relative_path,
                        "issue": f"Very long lines found at: {long_lines[:5]}",
                        "severity": "low"
                    })
                
            except Exception as e:
                self.results["general_problems"] += 1
        
        self.results["quality_issues"] = quality_issues

def main():
    parser = argparse.ArgumentParser(description='Documentation Auditor Agent')
    parser.add_argument('--scan', action='store_true', help='Scan documentation')
    parser.add_argument('--output', type=str, help='Output JSON file path')
    parser.add_argument('--project-root', type=str, default='.', help='Project root directory')
    
    args = parser.parse_args()
    
    if not args.scan:
        print("❌ Please use --scan to start the audit")
        return
    
    auditor = DocumentationAuditor(args.project_root)
    results = auditor.scan_documentation()
    
    # Save results
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"✅ Results saved to {args.output}")
    
    # Print summary
    print("\n📊 DOCUMENTATION AUDIT SUMMARY")
    print("=" * 50)
    print(f"📁 Total documentation files: {results['total_docs']}")
    print(f"🔗 Broken links found: {len(results['broken_links'])}")
    print(f"📅 Outdated content items: {len(results['outdated_content'])}")
    print(f"❌ Incomplete documents: {len(results['incomplete_docs'])}")
    print(f"📝 Missing critical docs: {len(results['missing_docs'])}")
    print(f"⚠️  Quality issues: {len(results['quality_issues'])}")
    print(f"🚨 General problems: {results['general_problems']}")
    
    if results['broken_links']:
        print(f"\n🔗 BROKEN LINKS (first 5):")
        for link in results['broken_links'][:5]:
            print(f"  - {link['file']}: {link['link']}")
    
    if results['missing_docs']:
        print(f"\n📝 MISSING CRITICAL DOCS:")
        for doc in results['missing_docs']:
            print(f"  - {doc}")
    
    if results['quality_issues']:
        print(f"\n⚠️  QUALITY ISSUES (first 5):")
        for issue in results['quality_issues'][:5]:
            print(f"  - {issue['file']}: {issue['issue']}")

if __name__ == "__main__":
    main() 