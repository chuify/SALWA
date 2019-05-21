from odoo import models, fields


class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    product_weight = fields.Float(default=1.0)


class MrpSubproduct(models.Model):
    _inherit = 'mrp.subproduct'

    product_weight = fields.Float(default=1.0)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    subproduct_ids = fields.One2many(comodel_name='mrp.subproduct', inverse_name='product_id')

    def action_bom_cost(self):
        if len(self.bom_ids) == 0:
           raise Warning('the product have no bom to compute the cost. If it is a byproduct, compute it from the main product')
        templates = self.filtered(lambda t: t.product_variant_count == 1)
        return templates.mapped('product_variant_id').action_bom_cost()

    def button_bom_cost(self):
        if len(self.bom_ids) == 0:
            raise Warning('the product have no bom to compute the cost. If it is a byproduct, compute it from the main product')
        templates = self.filtered(lambda t: t.product_variant_count == 1)
        return templates.mapped('product_variant_id').button_bom_cost()


class ProductProduct(models.Model):
    _inherit = 'product.product'

    # def _get_price_from_bom(self, boms_to_recompute=False):
    #     self.ensure_one()
    #     if self.bom_count > 0:
    #         bom = self.env['mrp.bom']._bom_find(product=self)
    #         return self._compute_bom_price(bom, boms_to_recompute=boms_to_recompute) * bom.product_weight
    #     elif len(self.subproduct_ids) > 0:
    #         subproduct = self.subproduct_ids[0]
    #         return self._compute_bom_price(subproduct.bom_id) * subproduct.product_weight

    def _compute_bom_price(self, bom, boms_to_recompute=False):

        bom_price = super(ProductProduct, self)._compute_bom_price(bom, boms_to_recompute)

        weight_total = bom.product_weight
        for byproduct in bom.sub_products:
                weight_total += byproduct.product_weight

        for byproduct in bom.sub_products:
                byproduct.product_id.standard_price = bom_price * byproduct.product_weight / weight_total

        if weight_total == 0:
            raise Warning('Byproducts and Main product must have a product_weight defined')

        return bom_price * bom.product_weight / weight_total
