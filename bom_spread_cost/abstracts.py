from odoo import models


class ReportBomStructure(models.AbstractModel):

    _inherit = 'report.mrp.report_bom_structure'

    def _get_bom(self, bom_id=False, product_id=False, line_qty=False, line_id=False, level=False):

        bom = self.env['mrp.bom'].browse(bom_id)
        bom_quantity = line_qty

        lines = super(ReportBomStructure, self)._get_bom(bom_id=bom_id, product_id=product_id, line_qty=line_qty, line_id=line_id, level=level)

        if len(bom.sub_products) == 1:
            byproduct = bom.sub_products[0].product_id
            lines['product_byproduct'] = byproduct
            lines['bom_prod_name_byproduct'] = byproduct.display_name
            lines['price_byproduct'] = byproduct.uom_id._compute_price(byproduct.standard_price, bom.product_uom_id) * bom_quantity

            unit_cost = bom.product_tmpl_id.standard_price
            for byproduct in bom.sub_products.mapped('product_id'):
                unit_cost += byproduct.standard_price
            for component in bom.bom_line_ids.mapped('product_id'):
                unit_cost += component.standard_price
            lines['unit_cost'] = unit_cost

        return lines
