# This file is part of the sale_product_stock_shop module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction

__all__ = ['Sale']
__metaclass__ = PoolMeta


class Sale:
    __name__ = 'sale.sale'

    @classmethod
    def check_enough_stock(cls):
        '''Check enough stock from user preferences'''
        Shop = Pool().get('sale.shop')

        if Transaction().context.get('without_warning'):
            return False

        shop = Transaction().context.get('shop')
        if shop:
            shop = Shop(shop)
            if not shop.enough_stock:
                return False
            return True
        return super(Sale, cls).check_enough_stock()

    @classmethod
    def get_enough_stock_qty(cls):
        '''Check enough stock qty from user preferences'''
        Shop = Pool().get('sale.shop')

        shop = Transaction().context.get('shop')
        if shop:
            shop = Shop(shop)
            if shop.enough_stock_qty:
                return shop.enough_stock_qty
        return super(Sale, cls).get_enough_stock_qty()
