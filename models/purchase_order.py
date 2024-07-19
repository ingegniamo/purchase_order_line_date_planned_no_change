
from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    def onchange_date_planned(self):
        return