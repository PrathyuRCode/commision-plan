from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    commission_percentage = fields.Float(compute="_compute_commission_percentage")

    @api.depends("price_unit")
    def _compute_commission_percentage(self):
        sale_to_commission = self.order_id.team_id.sale_commission_id
        if sale_to_commission.from_date <= self.order_id.date_order.date() < sale_to_commission.to_date:
            if sale_to_commission.plan == 'pro_wise':
                for rec in self:
                    for i in sale_to_commission.commission_ids:
                        if rec.commission_percentage == 0:
                            if i.product_id == rec.product_template_id:
                                percentage = i.rate_in_per
                                price = rec.price_unit
                                total = (percentage / 100) * price
                                if total >= i.max_price:
                                    rec.commission_percentage = i.max_price
                                else:
                                    rec.commission_percentage = total
                            else:
                                rec.commission_percentage = 0
            else:
                for rec in self:
                    if sale_to_commission.commission_type == 'straight':
                        for line in sale_to_commission.revenue_wise_ids:
                            if line.from_amount <= rec.price_unit < line.to_amount:
                                rec.commission_percentage = rec.price_unit * (line.rev_wise_percentage / 100)
                        return rec.commission_percentage

                    else:

                        for line in sale_to_commission.revenue_wise_ids:
                            if line.from_amount <= rec.price_unit < line.to_amount:
                                rec.commission_percentage = (rec.price_unit - line.from_amount) * (
                                            line.rev_wise_percentage / 100)
                            else:
                                val1 = line.to_amount*(line.rev_wise_percentage / 100)
                                for j in sale_to_commission.revenue_wise_ids:
                                    if j.from_amount <= rec.price_unit < j.to_amount:
                                        val2 = (rec.price_unit-j.from_amount)*(j.rev_wise_percentage/100)
                                        rec.commission_percentage = val2+val1

                            return rec.commission_percentage
