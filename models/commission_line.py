from odoo import fields, models


class CommissionLine(models.Model):
    _name = "commission.line"

    product_id = fields.Many2one('product.template', string="Product")
    product_category_id = fields.Many2one(related='product_id.categ_id', string="Product Category")
    rate_in_per = fields.Float(string="Rate in Percentage")
    max_price = fields.Float(string="maximum commission amount")

    commission_line_id = fields.Many2one("crm.commission.plan")


class RevenueWise(models.Model):
    _name = "revenue.wise"

    from_amount = fields.Float(string='Rate From')
    to_amount = fields.Float(string='To Rate')
    rev_wise_percentage = fields.Float(string="Percentage")
    sequence = fields.Integer(string="Sequence", default=10)

    revenue_id = fields.Many2one("crm.commission.plan")
