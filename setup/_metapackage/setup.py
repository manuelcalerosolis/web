import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-web",
    description="Meta package for oca-web Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-web_advanced_search',
        'odoo12-addon-web_company_color',
        'odoo12-addon-web_decimal_numpad_dot',
        'odoo12-addon-web_dialog_size',
        'odoo12-addon-web_disable_export_group',
        'odoo12-addon-web_edit_user_filter',
        'odoo12-addon-web_environment_ribbon',
        'odoo12-addon-web_export_view',
        'odoo12-addon-web_favicon',
        'odoo12-addon-web_group_by_percentage',
        'odoo12-addon-web_ir_actions_act_multi',
        'odoo12-addon-web_ir_actions_act_view_reload',
        'odoo12-addon-web_listview_range_select',
        'odoo12-addon-web_m2x_options',
        'odoo12-addon-web_notify',
        'odoo12-addon-web_responsive',
        'odoo12-addon-web_searchbar_full_width',
        'odoo12-addon-web_timeline',
        'odoo12-addon-web_tree_duplicate',
        'odoo12-addon-web_tree_dynamic_colored_field',
        'odoo12-addon-web_tree_many2one_clickable',
        'odoo12-addon-web_tree_resize_column',
        'odoo12-addon-web_widget_color',
        'odoo12-addon-web_widget_domain_editor_dialog',
        'odoo12-addon-web_widget_image_download',
        'odoo12-addon-web_widget_many2many_tags_multi_selection',
        'odoo12-addon-web_widget_x2many_2d_matrix',
        'odoo12-addon-web_widget_x2many_2d_matrix_example',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
