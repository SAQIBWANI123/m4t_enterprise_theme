# -*- coding: utf-8 -*-
{
    'name': 'M4T Enterprise Theme',
    'version': '19.0.2.0.0',
    'category': 'Hidden',
    'sequence': 1,
    'summary': 'Enterprise-style look and feel for Odoo 19 Community',
    'description': """
M4T Enterprise Theme
=====================
Transforms Odoo 19 Community Edition's backend UI to closely match
the Odoo Enterprise Edition design and responsiveness.

Features:
* Enterprise white navbar with dark text
* Enterprise color scheme (#714B67 brand, #017e84 teal accents)
* Enterprise-style home menu with background SVG
* Enterprise notebook tabs with top-border accent
* Enterprise-style inputs, buttons, and form controls
* Enterprise border-radius and shadow behavior
* Enterprise-style app switcher with drag-and-drop reordering
    """,
    'author': 'Mate4Tech',
    'website': 'https://www.mate4tech.com.au',
    'depends': ['web', 'base_setup'],
    'data': [
        'views/webclient_templates.xml',
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('after', 'web/static/src/scss/primary_variables.scss', 'm4t_enterprise_theme/static/src/**/*.variables.scss'),
            ('before', 'web/static/src/scss/primary_variables.scss', 'm4t_enterprise_theme/static/src/scss/primary_variables.scss'),
        ],
        'web._assets_secondary_variables': [
            ('before', 'web/static/src/scss/secondary_variables.scss', 'm4t_enterprise_theme/static/src/scss/secondary_variables.scss'),
        ],
        'web._assets_backend_helpers': [
            ('before', 'web/static/src/scss/bootstrap_overridden.scss', 'm4t_enterprise_theme/static/src/scss/bootstrap_overridden.scss'),
        ],
        'web.assets_frontend': [
            'm4t_enterprise_theme/static/src/scss/home_menu_background.scss',
            'm4t_enterprise_theme/static/src/scss/navbar.scss',
        ],
        'web.assets_backend': [
            'm4t_enterprise_theme/static/src/scss/home_menu_background.scss',
            'm4t_enterprise_theme/static/src/scss/home_menu.scss',
            'm4t_enterprise_theme/static/src/scss/navbar.scss',
            'm4t_enterprise_theme/static/src/scss/views.scss',
            'm4t_enterprise_theme/static/src/core/**/*.scss',
            'm4t_enterprise_theme/static/src/webclient/**/*.js',
            'm4t_enterprise_theme/static/src/webclient/**/*.xml',
        ],
        'web.assets_web': [
            ('replace', 'web/static/src/main.js', 'm4t_enterprise_theme/static/src/main.js'),
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
