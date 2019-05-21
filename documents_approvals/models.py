from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sales_manager_approval = fields.Many2one(comodel_name='res.users')
    finance_manager_approval = fields.Many2one(comodel_name='res.users')

    def action_sales_manager_approval(self):
        for rec in self:
            if self.env.user.has_group('sales_team.group_sale_manager'):
                rec.sales_manager_approval = self.env.user.id
            else:
                raise Warning('only Sales manager of Finance manager can approve this document')

    def action_finance_manager_approval(self):
        for rec in self:
            if self.env.user.has_group('account.group_account_manager'):
                rec.finance_manager_approval = self.env.user.id
            else:
                raise Warning('only Sales manager of Finance manager can approve this document')


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    purchase_manager_approval = fields.Many2one(comodel_name='res.users')
    finance_manager_approval = fields.Many2one(comodel_name='res.users')

    def action_purchase_manager_approval(self):
        for rec in self:
            if self.env.user.has_group('purchase.group_purchase_manager'):
                rec.purchase_manager_approval = self.env.user.id
            else:
                raise Warning('only Sales manager of Finance manager can approve this document')

    def action_finance_manager_approval(self):
        for rec in self:
            if self.env.user.has_group('account.group_account_manager'):
                rec.finance_manager_approval = self.env.user.id
            else:
                raise Warning('only Sales manager of Finance manager can approve this document')


class ResUsers(models.Model):
    _inherit = 'res.users'

    approval_signature = fields.Binary(groups="sales_team.group_sale_manager,account.group_account_manager")
