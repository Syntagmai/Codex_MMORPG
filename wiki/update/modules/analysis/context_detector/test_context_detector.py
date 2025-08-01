#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes para o módulo context_detector

Módulo: context_detector
Descrição: Detecção de contexto
"""

import unittest
from pathlib import Path
import sys

# Adicionar diretório do módulo ao path
module_path = Path(__file__).parent
sys.path.insert(0, str(module_path))

from context_detector import ContextdetectorModule

class TestContextdetectorModule(unittest.TestCase):
    """Testes para o módulo context_detector"""
    
    def setUp(self):
        """Configuração inicial dos testes"""
        self.module = ContextdetectorModule()
    
    def test_module_initialization(self):
        """Testa inicialização do módulo"""
        self.assertEqual(self.module.name, "context_detector")
        self.assertEqual(self.module.description, "Detecção de contexto")
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
