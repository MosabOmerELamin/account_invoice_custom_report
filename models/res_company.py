from odoo import models, fields

class ResCompany(models.Model):
    _inherit = 'res.company'

    company_arabic = fields.Char(string="Company Arabic Name")
