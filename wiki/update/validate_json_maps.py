#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para validar mapas JSON atualizados
Task 19.7 - Validar todos os mapas JSON
"""

import os
import json
from datetime import datetime
from pathlib import Path

class JSONMapsValidator:
    def __init__(self):
        self.wiki_path = Path("wiki")
        self.maps_path = self.wiki_path / "maps"
        self.results = {
            "maps_validated": 0,
            "valid_maps": 0,
            "invalid_maps": 0,
            "validation_errors": [],
            "wiki_map_status": False,
            "tags_index_status": False,
            "search_index_status": False,
            "relationships_status": False
        }
        
    def validate_json_structure(self, data, required_fields, map_name):
        """Valida estrutura básica de um JSON."""
        errors = []
        
        # Verificar se é um dicionário
        if not isinstance(data, dict):
            errors.append(f"{map_name}: Dados não são um dicionário válido")
            return errors
        
        # Verificar campos obrigatórios
        for field in required_fields:
            if field not in data:
                errors.append(f"{map_name}: Campo obrigatório '{field}' não encontrado")
        
        return errors
    
    def validate_wiki_map(self):
        """Valida o wiki_map.json."""
        try:
            wiki_map_path = self.maps_path / "wiki_map.json"
            
            if not wiki_map_path.exists():
                self.results["validation_errors"].append("wiki_map.json não encontrado")
                return False
            
            with open(wiki_map_path, "r", encoding="utf-8") as f:
                wiki_map = json.load(f)
            
            # Campos obrigatórios
            required_fields = ["metadata", "categories", "files"]
            errors = self.validate_json_structure(wiki_map, required_fields, "wiki_map.json")
            
            if errors:
                self.results["validation_errors"].extend(errors)
                return False
            
            # Validar metadados
            metadata = wiki_map["metadata"]
            if "total_documents" not in metadata:
                self.results["validation_errors"].append("wiki_map.json: total_documents não encontrado")
                return False
            
            # Validar categorias
            categories = wiki_map["categories"]
            if not isinstance(categories, dict):
                self.results["validation_errors"].append("wiki_map.json: categories não é um dicionário")
                return False
            
            # Validar arquivos
            files = wiki_map["files"]
            if not isinstance(files, dict):
                self.results["validation_errors"].append("wiki_map.json: files não é um dicionário")
                return False
            
            # Verificar se total_documents corresponde ao número de arquivos
            if metadata["total_documents"] != len(files):
                self.results["validation_errors"].append(f"wiki_map.json: total_documents ({metadata['total_documents']}) não corresponde ao número de arquivos ({len(files)})")
                return False
            
            self.results["wiki_map_status"] = True
            return True
            
        except Exception as e:
            self.results["validation_errors"].append(f"Erro ao validar wiki_map.json: {e}")
            return False
    
    def validate_tags_index(self):
        """Valida o tags_index.json."""
        try:
            tags_index_path = self.maps_path / "tags_index.json"
            
            if not tags_index_path.exists():
                self.results["validation_errors"].append("tags_index.json não encontrado")
                return False
            
            with open(tags_index_path, "r", encoding="utf-8") as f:
                tags_index = json.load(f)
            
            # Campos obrigatórios
            required_fields = ["metadata", "files_by_tag", "tags_by_file"]
            errors = self.validate_json_structure(tags_index, required_fields, "tags_index.json")
            
            if errors:
                self.results["validation_errors"].extend(errors)
                return False
            
            # Validar metadados
            metadata = tags_index["metadata"]
            if "total_files" not in metadata or "total_tags" not in metadata:
                self.results["validation_errors"].append("tags_index.json: campos obrigatórios não encontrados em metadata")
                return False
            
            # Validar files_by_tag
            files_by_tag = tags_index["files_by_tag"]
            if not isinstance(files_by_tag, dict):
                self.results["validation_errors"].append("tags_index.json: files_by_tag não é um dicionário")
                return False
            
            # Validar tags_by_file
            tags_by_file = tags_index["tags_by_file"]
            if not isinstance(tags_by_file, dict):
                self.results["validation_errors"].append("tags_index.json: tags_by_file não é um dicionário")
                return False
            
            # Verificar consistência
            if metadata["total_tags"] != len(files_by_tag):
                self.results["validation_errors"].append(f"tags_index.json: total_tags ({metadata['total_tags']}) não corresponde ao número de tags ({len(files_by_tag)})")
                return False
            
            if metadata["total_files"] != len(tags_by_file):
                self.results["validation_errors"].append(f"tags_index.json: total_files ({metadata['total_files']}) não corresponde ao número de arquivos ({len(tags_by_file)})")
                return False
            
            self.results["tags_index_status"] = True
            return True
            
        except Exception as e:
            self.results["validation_errors"].append(f"Erro ao validar tags_index.json: {e}")
            return False
    
    def validate_search_index(self):
        """Valida o search_index.json."""
        try:
            search_index_path = self.maps_path / "search_index.json"
            
            if not search_index_path.exists():
                self.results["validation_errors"].append("search_index.json não encontrado")
                return False
            
            with open(search_index_path, "r", encoding="utf-8") as f:
                search_index = json.load(f)
            
            # Campos obrigatórios
            required_fields = ["metadata", "quick_search"]
            errors = self.validate_json_structure(search_index, required_fields, "search_index.json")
            
            if errors:
                self.results["validation_errors"].extend(errors)
                return False
            
            # Validar metadados
            metadata = search_index["metadata"]
            if "version" not in metadata:
                self.results["validation_errors"].append("search_index.json: version não encontrado em metadata")
                return False
            
            # Validar quick_search
            quick_search = search_index["quick_search"]
            if not isinstance(quick_search, dict):
                self.results["validation_errors"].append("search_index.json: quick_search não é um dicionário")
                return False
            
            # Validar estrutura de cada entrada de busca
            for term, data in quick_search.items():
                if not isinstance(data, dict):
                    self.results["validation_errors"].append(f"search_index.json: entrada '{term}' não é um dicionário")
                    return False
                
                if "files" not in data or "count" not in data:
                    self.results["validation_errors"].append(f"search_index.json: entrada '{term}' não tem campos obrigatórios")
                    return False
                
                if not isinstance(data["files"], list):
                    self.results["validation_errors"].append(f"search_index.json: entrada '{term}' files não é uma lista")
                    return False
                
                if data["count"] != len(data["files"]):
                    self.results["validation_errors"].append(f"search_index.json: entrada '{term}' count não corresponde ao número de arquivos")
                    return False
            
            self.results["search_index_status"] = True
            return True
            
        except Exception as e:
            self.results["validation_errors"].append(f"Erro ao validar search_index.json: {e}")
            return False
    
    def validate_relationships(self):
        """Valida o relationships.json."""
        try:
            relationships_path = self.maps_path / "relationships.json"
            
            if not relationships_path.exists():
                self.results["validation_errors"].append("relationships.json não encontrado")
                return False
            
            with open(relationships_path, "r", encoding="utf-8") as f:
                relationships = json.load(f)
            
            # Campos obrigatórios
            required_fields = ["metadata"]
            errors = self.validate_json_structure(relationships, required_fields, "relationships.json")
            
            if errors:
                self.results["validation_errors"].extend(errors)
                return False
            
            # Validar metadados
            metadata = relationships["metadata"]
            if "version" not in metadata:
                self.results["validation_errors"].append("relationships.json: version não encontrado em metadata")
                return False
            
            # Validar relacionamentos de arquivos
            for filename, rel_data in relationships.items():
                if filename == "metadata":
                    continue
                
                if not isinstance(rel_data, dict):
                    self.results["validation_errors"].append(f"relationships.json: relacionamento de '{filename}' não é um dicionário")
                    return False
                
                required_rel_fields = ["prerequisites", "next_steps", "related", "integration_links"]
                for field in required_rel_fields:
                    if field not in rel_data:
                        self.results["validation_errors"].append(f"relationships.json: '{filename}' não tem campo '{field}'")
                        return False
                    
                    if not isinstance(rel_data[field], list):
                        self.results["validation_errors"].append(f"relationships.json: '{filename}' campo '{field}' não é uma lista")
                        return False
            
            self.results["relationships_status"] = True
            return True
            
        except Exception as e:
            self.results["validation_errors"].append(f"Erro ao validar relationships.json: {e}")
            return False
    
    def run(self):
        """Executa o processo de validação."""
        print("🔍 Iniciando validação dos mapas JSON...")
        
        # Validar cada mapa
        maps_to_validate = [
            ("wiki_map.json", self.validate_wiki_map),
            ("tags_index.json", self.validate_tags_index),
            ("search_index.json", self.validate_search_index),
            ("relationships.json", self.validate_relationships)
        ]
        
        for map_name, validator_func in maps_to_validate:
            self.results["maps_validated"] += 1
            if validator_func():
                self.results["valid_maps"] += 1
                print(f"   ✅ {map_name}: Válido")
            else:
                self.results["invalid_maps"] += 1
                print(f"   ❌ {map_name}: Inválido")
        
        # Salvar relatório
        self.save_report()
        
        print(f"✅ Validação concluída!")
        print(f"   🔍 Mapas validados: {self.results['maps_validated']}")
        print(f"   ✅ Mapas válidos: {self.results['valid_maps']}")
        print(f"   ❌ Mapas inválidos: {self.results['invalid_maps']}")
        
        if self.results["validation_errors"]:
            print(f"   ⚠️ Erros encontrados: {len(self.results['validation_errors'])}")
            print("   📋 Primeiros 5 erros:")
            for error in self.results["validation_errors"][:5]:
                print(f"      - {error}")
    
    def save_report(self):
        """Salva o relatório de validação."""
        report = {
            "timestamp": datetime.now().isoformat(),
            "task": "19.7 - Validar Mapas JSON",
            "results": self.results
        }
        
        report_path = self.wiki_path / "log" / "json_maps_validation_report.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    validator = JSONMapsValidator()
    validator.run() 