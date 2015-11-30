# This file is part of the sale_product_stock_shop module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class SaleProductStockShopTestCase(ModuleTestCase):
    'Test Sale Product Stock Shop module'
    module = 'sale_product_stock_shop'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleProductStockShopTestCase))
    return suite
