from odoo import fields, models


class CommissionPlan(models.Model):
    _name = "crm.commission.plan"
    _description = "crm.commission.plan"
    _inherit = "mail.thread"

    name = fields.Char(string="Name", required="True")
    active = fields.Boolean(default='True')
    from_date = fields.Date(string='From Date')
    to_date = fields.Date(string='To Date')
    plan = fields.Selection(string="Commission Plan", selection=[('pro_wise', 'Product Wise'),
                                                                 ('rev_wise', 'Revenue Wise')],  default="pro_wise")
    commission_ids = fields.One2many("commission.line", "commission_line_id")
    commission_type = fields.Selection(string="Commission Type", selection=[('straight', 'Straight'),
                                                                            ('graduated', 'Graduated')])
    revenue_wise_ids = fields.One2many("revenue.wise", "revenue_id")
