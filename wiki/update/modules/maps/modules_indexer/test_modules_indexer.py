#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes para o módulo modules_indexer

Módulo: modules_indexer
Descrição: Indexação de módulos Lua
"""

import unittest
from pathlib import Path
import sys

# Adicionar diretório do módulo ao path
module_path = Path(__file__).parent
sys.path.insert(0, str(module_path))

from modules_indexer import ModulesindexerModule

class TestModulesindexerModule(unittest.TestCase):
    """Testes para o módulo modules_indexer"""
    
    def setUp(self):
        """Configuração inicial dos testes"""
        self.module = ModulesindexerModule()
    
    def test_module_initialization(self):
        """Testa inicialização do módulo"""
        self.assertEqual(self.module.name, "modules_indexer")
        self.assertEqual(self.module.description, "Indexação de módulos Lua")
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
