#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes para o módulo git_automation

Módulo: git_automation
Descrição: Automação Git
"""

import unittest
from pathlib import Path
import sys

# Adicionar diretório do módulo ao path
module_path = Path(__file__).parent
sys.path.insert(0, str(module_path))

from git_automation import GitautomationModule

class TestGitautomationModule(unittest.TestCase):
    """Testes para o módulo git_automation"""
    
    def setUp(self):
        """Configuração inicial dos testes"""
        self.module = GitautomationModule()
    
    def test_module_initialization(self):
        """Testa inicialização do módulo"""
        self.assertEqual(self.module.name, "git_automation")
        self.assertEqual(self.module.description, "Automação Git")
        self.assertEqual(self.module.version, "1.0.0")
    
    def test_module_execution(self):
        """Testa execução do módulo"""
        result = self.module.execute()
        self.assertIsInstance(result, bool)
    
    def test_module_validation(self):
        """Testa validação do módulo"""
        result = self.module.validate()
        self.assertIsInstance(result, bool)

if __name__ == "__main__":
    unittest.main()
