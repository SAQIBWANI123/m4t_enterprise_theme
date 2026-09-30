# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    home_menu_background_image = fields.Binary(
        string="Home Menu Background Image",
        related='company_id.home_menu_background_image',
        readonly=False,
    )


class ResCompany(models.Model):
    _inherit = 'res.company'

    home_menu_background_image = fields.Binary(
        string="Home Menu Background Image",
        attachment=True,
    )
