#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes para o módulo wiki_expander

Módulo: wiki_expander
Descrição: Expansão da wiki
"""

import unittest
from pathlib import Path
import sys

# Adicionar diretório do módulo ao path
module_path = Path(__file__).parent
sys.path.insert(0, str(module_path))

from wiki_expander import WikiexpanderModule

class TestWikiexpanderModule(unittest.TestCase):
    """Testes para o módulo wiki_expander"""
    
    def setUp(self):
        """Configuração inicial dos testes"""
        self.module = WikiexpanderModule()
    
    def test_module_initialization(self):
        """Testa inicialização do módulo"""
        self.assertEqual(self.module.name, "wiki_expander")
        self.assertEqual(self.module.description, "Expansão da wiki")
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
