from odoo import fields, models


class CRMTeam(models.Model):
    _inherit = "crm.team"

    sale_commission_id = fields.Many2one("crm.commission.plan", string="Commission Plan")
