#!/usr/bin/env python3
"""
Integration Auditor Agent - Epic 17 Task 17.5
Audits system integrations, dependencies, and integration points
"""

import os
import json
import ast
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict, deque

class IntegrationAuditor:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.report = {
            "timestamp": datetime.now().isoformat(),
            "project_root": str(self.project_root),
            "integration_points": [],
            "circular_dependencies": [],
            "broken_interfaces": [],
            "missing_dependencies": [],
            "integration_issues": [],
            "system_connections": [],
            "api_endpoints": [],
            "data_flows": [],
            "critical_integrations": [],
            "summary": {}
        }
        
    def scan_integration_points(self):
        """Scan for integration points between different systems"""
        print("🔍 Scanning integration points...")
        
        # Scan for common integration patterns
        integration_patterns = [
            r'import.*bmad',
            r'from.*bmad',
            r'require.*bmad',
            r'include.*bmad',
            r'integration.*point',
            r'api.*endpoint',
            r'interface.*',
            r'bridge.*',
            r'connector.*',
            r'adapter.*'
        ]
        
        for pattern in integration_patterns:
            for file_path in self.project_root.rglob('*'):
                if file_path.is_file() and file_path.suffix in ['.py', '.lua', '.cpp', '.hpp', '.js', '.json']:
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            matches = re.findall(pattern, content, re.IGNORECASE)
                            if matches:
                                self.report["integration_points"].append({
                                    "file": str(file_path.relative_to(self.project_root)),
                                    "pattern": pattern,
                                    "matches": len(matches),
                                    "type": file_path.suffix
                                })
                    except Exception as e:
                        continue
    
    def detect_circular_dependencies(self):
        """Detect circular dependencies in Python files"""
        print("🔄 Detecting circular dependencies...")
        
        import_graph = defaultdict(set)
        
        # Build import graph
        for py_file in self.project_root.rglob('*.py'):
            try:
                with open(py_file, 'r', encoding='utf-8', errors='ignore') as f:
                    tree = ast.parse(f.read())
                    
                module_name = str(py_file.relative_to(self.project_root)).replace('/', '.').replace('\\', '.')[:-3]
                
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for alias in node.names:
                            import_graph[module_name].add(alias.name)
                    elif isinstance(node, ast.ImportFrom):
                        if node.module:
                            import_graph[module_name].add(node.module)
                            
            except Exception as e:
                continue
        
        # Detect cycles using DFS
        def has_cycle(node, visited, rec_stack):
            visited.add(node)
            rec_stack.add(node)
            
            for neighbor in import_graph[node]:
                if neighbor not in visited:
                    if has_cycle(neighbor, visited, rec_stack):
                        return True
                elif neighbor in rec_stack:
                    return True
                    
            rec_stack.remove(node)
            return False
        
        # Check for cycles
        visited = set()
        for node in import_graph:
            if node not in visited:
                rec_stack = set()
                if has_cycle(node, visited, rec_stack):
                    self.report["circular_dependencies"].append({
                        "module": node,
                        "dependencies": list(import_graph[node])
                    })
    
    def check_broken_interfaces(self):
        """Check for broken interfaces and API endpoints"""
        print("🔌 Checking broken interfaces...")
        
        # Check for common interface issues
        interface_patterns = [
            r'def.*api.*',
            r'class.*API',
            r'@app\.route',
            r'@api\.',
            r'endpoint.*',
            r'interface.*',
            r'protocol.*'
        ]
        
        for pattern in interface_patterns:
            for file_path in self.project_root.rglob('*'):
                if file_path.is_file() and file_path.suffix in ['.py', '.lua', '.cpp', '.hpp']:
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            matches = re.findall(pattern, content, re.IGNORECASE)
                            if matches:
                                # Check if interface is properly implemented
                                if 'pass' in content or 'TODO' in content or 'FIXME' in content:
                                    self.report["broken_interfaces"].append({
                                        "file": str(file_path.relative_to(self.project_root)),
                                        "pattern": pattern,
                                        "issue": "Incomplete implementation",
                                        "type": file_path.suffix
                                    })
                    except Exception as e:
                        continue
    
    def scan_system_connections(self):
        """Scan for system connections and data flows"""
        print("🔗 Scanning system connections...")
        
        connection_patterns = [
            r'database.*connection',
            r'network.*connection',
            r'socket.*',
            r'http.*request',
            r'api.*call',
            r'data.*flow',
            r'pipeline.*',
            r'workflow.*'
        ]
        
        for pattern in connection_patterns:
            for file_path in self.project_root.rglob('*'):
                if file_path.is_file() and file_path.suffix in ['.py', '.lua', '.cpp', '.hpp', '.json', '.yml']:
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            matches = re.findall(pattern, content, re.IGNORECASE)
                            if matches:
                                self.report["system_connections"].append({
                                    "file": str(file_path.relative_to(self.project_root)),
                                    "pattern": pattern,
                                    "matches": len(matches),
                                    "type": file_path.suffix
                                })
                    except Exception as e:
                        continue
    
    def check_api_endpoints(self):
        """Check for API endpoints and their status"""
        print("🌐 Checking API endpoints...")
        
        api_patterns = [
            r'@app\.route\([\'"]([^\'"]+)[\'"]',
            r'@api\.route\([\'"]([^\'"]+)[\'"]',
            r'endpoint.*=.*[\'"]([^\'"]+)[\'"]',
            r'url.*=.*[\'"]([^\'"]+)[\'"]'
        ]
        
        for pattern in api_patterns:
            for file_path in self.project_root.rglob('*.py'):
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        matches = re.findall(pattern, content)
                        for match in matches:
                            self.report["api_endpoints"].append({
                                "file": str(file_path.relative_to(self.project_root)),
                                "endpoint": match,
                                "pattern": pattern
                            })
                except Exception as e:
                    continue
    
    def analyze_data_flows(self):
        """Analyze data flows between systems"""
        print("📊 Analyzing data flows...")
        
        data_flow_patterns = [
            r'data.*transfer',
            r'data.*flow',
            r'pipeline.*',
            r'stream.*',
            r'queue.*',
            r'buffer.*',
            r'cache.*'
        ]
        
        for pattern in data_flow_patterns:
            for file_path in self.project_root.rglob('*'):
                if file_path.is_file() and file_path.suffix in ['.py', '.lua', '.cpp', '.hpp']:
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            matches = re.findall(pattern, content, re.IGNORECASE)
                            if matches:
                                self.report["data_flows"].append({
                                    "file": str(file_path.relative_to(self.project_root)),
                                    "pattern": pattern,
                                    "matches": len(matches),
                                    "type": file_path.suffix
                                })
                    except Exception as e:
                        continue
    
    def identify_critical_integrations(self):
        """Identify critical integrations that need special attention"""
        print("⚠️ Identifying critical integrations...")
        
        critical_patterns = [
            r'critical.*integration',
            r'core.*system',
            r'main.*pipeline',
            r'essential.*',
            r'vital.*',
            r'primary.*'
        ]
        
        for pattern in critical_patterns:
            for file_path in self.project_root.rglob('*'):
                if file_path.is_file() and file_path.suffix in ['.py', '.lua', '.cpp', '.hpp', '.md']:
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            matches = re.findall(pattern, content, re.IGNORECASE)
                            if matches:
                                self.report["critical_integrations"].append({
                                    "file": str(file_path.relative_to(self.project_root)),
                                    "pattern": pattern,
                                    "matches": len(matches),
                                    "type": file_path.suffix
                                })
                    except Exception as e:
                        continue
    
    def generate_summary(self):
        """Generate summary statistics"""
        print("📋 Generating summary...")
        
        self.report["summary"] = {
            "total_integration_points": len(self.report["integration_points"]),
            "total_circular_dependencies": len(self.report["circular_dependencies"]),
            "total_broken_interfaces": len(self.report["broken_interfaces"]),
            "total_system_connections": len(self.report["system_connections"]),
            "total_api_endpoints": len(self.report["api_endpoints"]),
            "total_data_flows": len(self.report["data_flows"]),
            "total_critical_integrations": len(self.report["critical_integrations"]),
            "integration_issues_count": len(self.report["integration_issues"])
        }
    
    def run_audit(self):
        """Run the complete integration audit"""
        print("🚀 Starting Integration Audit...")
        
        self.scan_integration_points()
        self.detect_circular_dependencies()
        self.check_broken_interfaces()
        self.scan_system_connections()
        self.check_api_endpoints()
        self.analyze_data_flows()
        self.identify_critical_integrations()
        self.generate_summary()
        
        return self.report

def main():
    import sys
    
    if len(sys.argv) > 1:
        project_root = sys.argv[1]
    else:
        project_root = "."
    
    auditor = IntegrationAuditor(project_root)
    report = auditor.run_audit()
    
    # Save report
    output_dir = Path("wiki/docs/audit_reports")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = output_dir / "integration_audit_report.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    # Print summary
    print("\n" + "="*60)
    print("🔍 INTEGRATION AUDIT RESULTS")
    print("="*60)
    print(f"📁 Project Root: {report['project_root']}")
    print(f"⏰ Timestamp: {report['timestamp']}")
    print()
    print("📊 SUMMARY:")
    print(f"   🔗 Integration Points: {report['summary']['total_integration_points']}")
    print(f"   🔄 Circular Dependencies: {report['summary']['total_circular_dependencies']}")
    print(f"   🔌 Broken Interfaces: {report['summary']['total_broken_interfaces']}")
    print(f"   🌐 System Connections: {report['summary']['total_system_connections']}")
    print(f"   🚀 API Endpoints: {report['summary']['total_api_endpoints']}")
    print(f"   📊 Data Flows: {report['summary']['total_data_flows']}")
    print(f"   ⚠️ Critical Integrations: {report['summary']['total_critical_integrations']}")
    print()
    print(f"📄 Report saved to: {output_file}")
    print("="*60)

if __name__ == "__main__":
    main() 