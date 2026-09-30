# -*- coding: utf-8 -*-
import base64
from odoo import http
from odoo.http import request


class HomeMenuBackgroundController(http.Controller):

    @http.route('/m4t_enterprise_theme/home_menu_background', type='http', auth='user')
    def home_menu_background(self):
        company = request.env.company
        if company.home_menu_background_image:
            image_data = base64.b64decode(company.home_menu_background_image)
            return request.make_response(image_data, headers=[
                ('Content-Type', 'image/png'),
                ('Cache-Control', 'no-cache, no-store, must-revalidate'),
            ])
        return request.not_found()
