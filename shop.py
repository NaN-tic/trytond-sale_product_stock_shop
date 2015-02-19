# This file is part of the sale_product_stock_shop module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields
from trytond.pyson import Eval

__all__ = ['SaleShop']
__metaclass__ = PoolMeta


class SaleShop:
    __name__ = 'sale.shop'
    enough_stock = fields.Boolean('Enough Stock',
        help='Check enough stock when convert a sale to quotation')
    enough_stock_qty = fields.Property(fields.Selection([
        ('quantity', 'Quantity'),
        ('forecast_quantity', 'Forecast Quantity'),
        ], 'Quantity Stock', states={
            'invisible': ~Eval('enough_stock', True),
        }, help='Manage Stock is Product Quantity or Product Forecast Quantity'))

    @staticmethod
    def default_enough_stock():
        return True

    @staticmethod
    def default_enough_stock_qty():
        return 'quantity'
