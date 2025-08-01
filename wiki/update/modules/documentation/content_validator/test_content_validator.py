#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes para o módulo content_validator

Módulo: content_validator
Descrição: Validação de conteúdo
"""

import unittest
from pathlib import Path
import sys

# Adicionar diretório do módulo ao path
module_path = Path(__file__).parent
sys.path.insert(0, str(module_path))

from content_validator import ContentvalidatorModule

class TestContentvalidatorModule(unittest.TestCase):
    """Testes para o módulo content_validator"""
    
    def setUp(self):
        """Configuração inicial dos testes"""
        self.module = ContentvalidatorModule()
    
    def test_module_initialization(self):
        """Testa inicialização do módulo"""
        self.assertEqual(self.module.name, "content_validator")
        self.assertEqual(self.module.description, "Validação de conteúdo")
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
